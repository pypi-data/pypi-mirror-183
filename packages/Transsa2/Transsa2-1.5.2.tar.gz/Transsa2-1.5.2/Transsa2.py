#################################### Paquetes ##############################################
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.model_selection import cross_val_score, cross_val_predict
import joblib
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import sys
import xgboost as xgb

#################################### Funciones ##############################################


# Función para agregar columnas con indices (ufm2, etc) y cambiar el tipo de
# dato de ciertas columnas
def InsertColumns(D): #(D es la tabla) 
    D=D.astype({'antiguedad':'float64','supCSII':'float64','supTSII':'float64','valor':'float64'})
    D.insert(D.shape[1],'ufm2(supCSII)',D.loc[:,'valor']/D.loc[:,'supCSII'], True) 
    D.insert(D.shape[1],'ufm2(supTSII)',D.loc[:,'valor']/D.loc[:,'supTSII'], True)
    D.insert(D.shape[1],'supTSII/supCSII',D.loc[:,'supTSII']/D.loc[:,'supCSII'], True) 
    return D

# Concatenación de tablas de ventas y tasaciones
def tabla_auxiliar(df1,df2,method): #(df1 es la tabla de ventas, df2 es la tabla de tasaciones, 
                                     #method: el proposito para el cual se genera la tabla: ML o AVM) 
    while (method!="ML" and method!="AVM"):
        print("El método seleccionado no es válido")
        method=input("Ingrese correctamente el método a utilizar (ML o AVM): ")
    if method=="ML":
        df1_aux=df1[['antiguedad','longitud',
           'latitud','supCSII','supTSII','valor','cve_comuna',
           'ufm2(supCSII)','ufm2(supTSII)','supTSII/supCSII']]
        df2_aux=df2[['antiguedad','longitud',
           'latitud','supCSII','supTSII','valor','cve_comuna',
           'ufm2(supCSII)','ufm2(supTSII)','supTSII/supCSII']]
    else:
        df1_aux=df1[['num_','cve_propiedad','rol','cve_comuna','cve_region','ah','ah_hom','zona_eod',
             'zona_jjvv','materialidad','antiguedad','longitud',
             'latitud','supCSII','supTSII','valor']]
        df2_aux=df2[['num_','cve_propiedad','rol','cve_comuna','cve_region','ah','ah_hom','zona_eod',
             'zona_jjvv','materialidad','antiguedad','longitud',
             'latitud','supCSII','supTSII','valor']]
    df1_df2_aux=pd.concat([df1_aux,df2_aux], ignore_index=True, sort=False)
    df1_df2_aux=df1_df2_aux.dropna()
    return df1_df2_aux

# Selección de comuna
def Selec_Comuna(D1,cve): #(D1 es la tabla, cve: es el codigo de la comuna)
    comunas=[19,21,22,52]
    while cve not in comunas:
        print('Ingrese alguna de las siguientes comunas: La Reina (19), Las Condes (21), Lo Barnechea (22) o Vitacura (52):')
        cve=int(input())
    if cve==52:
        tol=5000
    else:
        tol=1000
    D_comuna=D1.loc[(D1.loc[:,'cve_comuna']==cve) & (D1.loc[:,'valor']>=tol)]
    return D_comuna

# Eliminación de datos duplicados
def datosduplicados(tabla,T): #(tabla es la tabla, T es True entonces se muestra la cantidad de datos eliminados)
    n_inicial = tabla.shape[0];
    tabla2 = tabla.drop_duplicates(subset=['longitud','latitud',
                                          'supCSII','supTSII','valor'])
    
    if T==True:
        print(f'Hay {n_inicial-tabla2.shape[0]} datos duplicados')
        print(f'Al eliminarlos quedan {tabla2.shape[0]} datos')
    return tabla2

#Identificación de atípicos dada una columna
def outliers_col(df,columna,n,a,T,n_i,limit):  #(df:tabla, columna, n: cantidad de datos inicial,
                                               # a: zscore o IQR, T es True entonces se muestran los resultados
                                               # n_i: cantidad de datos inicial, limit: limite del zscore)
    tabla= pd.DataFrame.from_dict({
    'Variable': [],'Cantidad de Atípicos': [],
    'Type': []});
    col = ['Variable','Cantidad de Atípicos','Type'];
    k=0;
    if (a=='zscore'):
        n_outliers = len(df[np.abs(stats.zscore(df[columna])) > limit])
        k=k+n_outliers;
        tablaux = pd.DataFrame([[df[columna].name,n_outliers,df[columna].dtype]],
                                    columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
        
    if (a=='IQR'):
        Q1,Q3 = np.percentile(df[columna], [25,75])
        iqr = Q3 - Q1
        ul = Q3+1.5*iqr
        ll = Q1-1.5*iqr
        n_outliers = len(df[(df[columna] > ul) | (df[columna] < ll)])
        k=k+n_outliers;
        tablaux = pd.DataFrame([[df[columna].name,n_outliers,df[columna].dtype]],
                                    columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    if T==True:
        print(tabulate(tabla, headers=col, tablefmt="fancy_grid"))  
        print('\nSe eliminarán:',k,'datos, y quedarán al menos:',n-k)
        print('en porcentaje con respecto a la cantidad inicial:',(n-k)*100/n_i,'%.\n')     
    return k,tabla

#Eliminación de atípicos dada una columna
def outliers_col_eliminacion(df,columna,a,limit):  #(df:tabla, columna, a: zscore o IQR, limit: limite del zscore)
    if a=='zscore':
        l=df[np.abs(stats.zscore(df[columna])) > limit].index;
        for x in l.values:
            df.loc[x,columna] = np.nan;
                
    if a=='IQR':
        Q1,Q3 = np.percentile(df[columna], [25,75])
        iqr = Q3 - Q1
        ul = Q3+1.5*iqr
        ll = Q1-1.5*iqr
        l=df[(df[columna] > ul) | (df[columna] < ll)].index;
        for x in l.values:
            df.loc[x,columna] = np.nan;
    
    df=df.dropna(axis = 0);
    return df

# Gráficas
def grafico_histograma_sns(df,columna,option1,option2):   #(df:tabla, columna, option1: kde True or False
                                                          #,option2: discrete True or False)
    plt.figure(figsize = (9,4))
    sns.set_style("whitegrid")
    sns.histplot(data=df[columna],color="#008080",
                 kde=option1,discrete=option2,bins=100);
    plt.xlabel(None)
    plt.title(columna);
    plt.ylabel('Cantidad')
    plt.show() 
    
    
def grafico_hyb_sns(df,columna,option1,option2,binss,col):   #(df:tabla, columna, option1: kde True or False
                                                             #,option2: discrete True or False, binss: numero de bins,
                                                             # col: color)
    #plt.rcParams['figure.figsize'] = (6,4)
    f, (ax_box, ax_hist) = plt.subplots(2,sharex=True,gridspec_kw={"height_ratios": (.25, .95)})
    red_cir = dict(markerfacecolor='r',marker='o',markersize=6)
    sns.set_style("whitegrid")
    sns.boxplot(x=df[columna],ax=ax_box,color=col,
                flierprops=red_cir).set_title(columna)
    sns.stripplot(x=df[columna],ax=ax_box,color="orange",jitter=0.15, size=2.5)
    sns.histplot(data=df[columna],color=col,ax=ax_hist,
                 kde=option1,discrete=option2,bins=binss)   
    ax_box.set(xlabel='')
    ax_hist.set(xlabel='')
    ax_hist.set(ylabel='Cantidad')
    plt.show()    
    
def grafico_boxplot_jitted(df,columna,jit):              #(df:tabla, columna, jit: si o no)
    plt.rcParams['figure.figsize'] = (9,12)
    red_cir = dict(markerfacecolor='r',marker='o',markersize=6)
    sns.set_style("whitegrid")
    if(jit=='no'):
         sns.boxplot(y=df[columna],color="#008080",
                     flierprops=red_cir).set_title(columna);  
    else:
        ax=sns.boxplot(x=df[columna],data=df,color="#008080",
                flierprops=red_cir).set_title(columna); 
        ax=sns.stripplot(x=df[columna], data=df, color="orange", jitter=0.15, size=2.5)
        
    plt.xlabel(None)    
    plt.show()

######## Función de gráficos y eliminación iterada de atípicos #######   
#atypicals_be_gone(ven_tas_comuna1,['valor','ufm2(supCSII)','ufm2(supTSII)','],False,'zscore',2.5)

def atypicals_be_gone(df,pars,T,metodo,limit):
    ## Gráficos antes de la eliminación
    # Histogramas 1
    print('Histogramas (con atípicos)')
    colors=['#008080','red','blue','orange']
    for j in range(0,len(pars)):
        grafico_hyb_sns(df,pars[j],True,False,100,colors[j])
        plt.show()
    ## Eliminación de atípicos  
    n_i=df.shape[0]
    for j in range(0,len(pars)):
        w=1
        if T==True:
            print(f'Eliminación de atípicos considerando: {pars[j]}')
        while (w!=0):
            [w,resum]=outliers_col(df,pars[j],df.shape[0],metodo,T,n_i,limit);
            df=outliers_col_eliminacion(df,pars[j],metodo,limit);
    ## Gráficos después de la eliminación
    # Histogramas 2
    print('Histogramas (sin atípicos)')
    colors=['#008080','red','blue','orange']
    for j in range(0,len(pars)):
        grafico_hyb_sns(df,pars[j],True,False,100,colors[j])
        plt.show()
   
    return df

# Matriz de correlación
def matriz_correlacion(df):
    matriz = df.corr(method='kendall')
    plt.rcParams['figure.figsize'] = (7,7);
    plt.matshow(matriz, cmap='BrBG', vmin=-1, vmax=1)
    plt.xticks(range(df.shape[1]), df.columns, rotation=90)
    plt.yticks(range(df.shape[1]), df.columns)

    for i in range(len(matriz.columns)):
          for j in range(len(matriz.columns)):
                 plt.text(i, j, round(matriz.iloc[i, j], 2),
                 ha="center", va="center")

    plt.colorbar()
    plt.grid(False)
    plt.show()

# Cálcular el tamaño de la muestra
def tam_muestra(ven_tas_comuna1,confianza):
    alpha=1-confianza # Confianza del 90%=0.9
    N=ven_tas_comuna1.shape[0]
    er=10/ven_tas_comuna1['valor'].mean()
    Z=stats.norm.ppf(1-alpha/2)
    COV=ven_tas_comuna1['valor'].std()/ven_tas_comuna1['valor'].mean()
    nmuestra=(N*(COV**2)*(Z**2))/((er**2)*(N-1)+(COV**2)*(Z**2))
    n_muestra=int(nmuestra)
    return n_muestra

def Muestra(df1,df2,cve):
    nn=tam_muestra(df1,0.9)
    n1=int(nn/10)
    N=df1.shape[0]
    n2=int(N/10)
    df3=df1.sort_values(by="valor", ascending= True)
    Muestras=[]
    for i in range(0,2):
        a1=df3.iloc[0:n2,:]
        b1=df3.iloc[n2:2*n2,:]
        c1=df3.iloc[2*n2:3*n2,:]
        d1=df3.iloc[3*n2:4*n2,:]
        e1=df3.iloc[4*n2:5*n2,:]
        f1=df3.iloc[5*n2:6*n2,:]
        g1=df3.iloc[6*n2:7*n2,:]
        h1=df3.iloc[7*n2:8*n2,:]
        i1=df3.iloc[8*n2:9*n2,:]
        j1=df3.iloc[9*n2:N+1,:]
        if n1==n2:
            A1=a1.sample(n=n1)
            B1=b1.sample(n=n1)
            C1=c1.sample(n=n1)
            D1=d1.sample(n=n1)
            E1=e1.sample(n=n1)
            F1=f1.sample(n=n1)
            G1=g1.sample(n=n1)
            H1=h1.sample(n=n1)
            I1=i1.sample(n=n1)
            J1=j1.sample(n=nn-9*n1)
        else:
            k,n3=0,n1
            while 10*n1+k<nn:
                k=k+1
                n3=n3+1
                A1=a1.sample(n=n3)
                if 10*n1+k==nn:
                    B1=b1.sample(n=n1)
                    C1=c1.sample(n=n1)
                    D1=d1.sample(n=n1)
                    E1=e1.sample(n=n1)
                    F1=f1.sample(n=n1)
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break   
                k=k+1
                B1=b1.sample(n=n3)
                if 10*n1+k==nn:
                    C1=c1.sample(n=n1)
                    D1=d1.sample(n=n1)
                    E1=e1.sample(n=n1)
                    F1=f1.sample(n=n1)
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break
                k=k+1
                C1=c1.sample(n=n3)
                if 10*n1+k==nn:
                    D1=d1.sample(n=n1)
                    E1=e1.sample(n=n1)
                    F1=f1.sample(n=n1)
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break  
                k=k+1
                D1=d1.sample(n=n3)
                if 10*n1+k==nn:
                    E1=e1.sample(n=n1)
                    F1=f1.sample(n=n1)
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break 
                k=k+1
                E1=e1.sample(n=n3)
                if 10*n1+k==nn:
                    F1=f1.sample(n=n1)
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break 
                k=k+1
                F1=f1.sample(n=n3)
                if 10*n1+k==nn:
                    G1=g1.sample(n=n1)
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break
                k=k+1
                G1=g1.sample(n=n3)
                if 10*n1+k==nn:
                    H1=h1.sample(n=n1)
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break 
                k=k+1
                H1=h1.sample(n=n3)
                if 10*n1+k==nn:
                    I1=i1.sample(n=n1)
                    J1=j1.sample(n=n1)
                    break 
                k=k+1
                I1=i1.sample(n=n3)
                if 10*n1+k==nn:
                    J1=j1.sample(n=n1)
                    break 
                k=k+1
                J1=j1.sample(n=n3)
        MuestraML=pd.concat([A1,B1,C1,D1,E1,F1,G1,H1,I1,J1],sort=False)
        MuestraML=datosduplicados(MuestraML,False)
        Muestras.append(MuestraML)
    MuestraML=Muestras[0]
    MuestraAVM=pd.merge(df2,Muestras[1], how="right", 
                        on=["cve_comuna","antiguedad","longitud","latitud","supCSII","supTSII","valor"])
    MuestraAVM=datosduplicados(MuestraAVM,False)
    nombre1='MuestraML'+str(cve)+'.xlsx'
    nombre2='MuestraAVM'+str(cve)+'.xlsx'
    MuestraML.to_excel(nombre1)
    MuestraAVM.to_excel(nombre2)
    return MuestraML,MuestraAVM,nn


def Muestra_Total(A):
    if A=="ML":
        LR = pd.read_excel('MuestraLRML.xlsx');
        LC = pd.read_excel('MuestraLCML.xlsx');
        LB = pd.read_excel('MuestraLBML.xlsx');
        V = pd.read_excel('MuestraVML.xlsx');
        MuestraZOML = pd.concat([LR,LC,LB,V], ignore_index=True, sort=False)
        MuestraZOML.to_excel('MuestraZOML.xlsx')
    elif A=="AVM":
        LR = pd.read_excel('MuestraLRAVM.xlsx');
        LC = pd.read_excel('MuestraLCAVM.xlsx');
        LB = pd.read_excel('MuestraLBAVM.xlsx');
        V = pd.read_excel('MuestraVAVM.xlsx');
        MuestraZOML = pd.concat([LR,LC,LB,V], ignore_index=True, sort=False)
        MuestraZOML.to_excel('MuestraZOAVM.xlsx')
    return MuestraZOML



# Función que hace la indexacion de 10 y 5, además de asignar valores booleanos de acuerdo a dicha indexación
def indexacion(df,mini,maxi):
    years1=[]
    years2=[]
    for i in range(mini,maxi,10):
        years1.append(i)
    for j in range(mini,maxi,5):
        years2.append(j)
    if maxi not in years1:
        years1.append(maxi)
    if maxi not in years2:
        years2.append(maxi)
    conditionlist1=[]
    conditionlist2=[]
    for k in range(0,(len(years1))-2): 
        c=(df['antiguedad'] >=years1[k]) & (df['antiguedad'] <years1[k+1])
        conditionlist1.append(c)
    c=(df['antiguedad'] >=years1[(len(years1))-2]) & (df['antiguedad'] <=years1[(len(years1))-1])
    conditionlist1.append(c)
    L=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
    vectorS1=[]
    vectorS2=[]
    for i in range(0,len(years1)-2):
        vectorS1.append(L[i]+str(years1[i])+"/"+str(years1[i+1]-1))
    vectorS1.append(L[len(years1)-2]+str(years1[len(years1)-2])+"/"+str(years1[len(years1)-1]))
    choicelist1=[]
    for i in range(0,len(vectorS1)):
        choicelist1.append(vectorS1[i][0]+vectorS1[i][3:6]+vectorS1[i][8:10])
    
    for k in range(0,(len(years2))-2): 
        c2=(df['antiguedad'] >=years2[k]) & (df['antiguedad'] <years2[k+1])
        conditionlist2.append(c2)
    c2=(df['antiguedad'] >=years2[(len(years2))-2]) & (df['antiguedad'] <=years2[(len(years2))-1])
    conditionlist2.append(c2)
    for i in range(0,len(years2)-2):
        vectorS2.append(L[i]+str(years2[i])+"/"+str(years2[i+1]-1))
    vectorS2.append(L[len(years2)-2]+str(years2[len(years2)-2])+"/"+str(years2[len(years2)-1]))    
    choicelist2=[]
    for i in range(0,len(vectorS2)):
        choicelist2.append(vectorS2[i][0]+vectorS2[i][3:6]+vectorS2[i][8:10])
    df_=df.copy()
    df_=df_.astype({'antiguedad':'float64','supCSII':'float64','supTSII':'float64','valor':'float64'})
    df.insert(df.shape[1],'Index_antiguedad_10',np.select(conditionlist1, choicelist1, default=0))
    df.insert(df.shape[1],'Index_antiguedad_5',np.select(conditionlist2, choicelist2, default=0))
    df2=df.astype({'antiguedad':'float64','supCSII':'float64','supTSII':'float64','valor':'float64'})
    df3=pd.concat([df_,pd.get_dummies(df2[['Index_antiguedad_10','Index_antiguedad_5']])], axis=1)
    return df2,df3
  
# Gráfica de boxplots
def grafico_boxplot_rcParams(interval,df2):
    if interval==10:
        plt.rcParams['figure.figsize'] = (9,6);
        sns.boxplot(data=df2.sort_values(by=['Index_antiguedad_10'],
                  ascending=True, inplace=False), 
                  x="Index_antiguedad_10", y="valor",
                  showfliers=False,palette="Set2");
        sns.stripplot(data=df2.sort_values(by=['Index_antiguedad_10'], 
                  ascending=True, inplace=False), 
                  x="Index_antiguedad_10", y="valor",
                  linewidth=1.0,palette="Set2");
        plt.xlabel('Década')
        plt.ylabel('Valor UF')
        plt.title('Distribución valor UF por década')
        plt.grid(True, color='lightgrey',linestyle='--')
        plt.show()
    elif interval==5:
        plt.rcParams['figure.figsize'] = (9,5);
        sns.boxplot(
                  data=df2.sort_values(by=['Index_antiguedad_5'], 
                  ascending=True, inplace=False), 
                  x="Index_antiguedad_5", y="valor",
                  showfliers=False,palette="Set2");
        sns.stripplot(data=df2.sort_values(by=['Index_antiguedad_5'], 
                  ascending=True, inplace=False), 
                  x="Index_antiguedad_5", y="valor",
                  linewidth=1.0,palette="Set2");

        plt.xlabel('Periodo 5 años')
        plt.ylabel('Valor UF')
        plt.title('Distribución valor UF cada 5 años')
        plt.grid(True, color='lightgrey',linestyle='--')
        plt.show()

# indexación de las columnas
def indexs(inter,df2):
    col=['antiguedad','longitud','latitud','supCSII','supTSII']
    index=[]
    nombre='Index_antiguedad_'+str(inter)
    if inter==10 or inter==5:
        a=np.array(df2[nombre].unique())
        a.sort()
        for i in range(0,len(a)):
            string=nombre+'_'+a[i]
            index.append(string)
        for k in range(1,len(col)):
            index.append(col[k])
    elif inter==1:
        index=col
    return index

# Entrenamiento y escalamiento de datos para los modelos
def Entrenamiento(inter, df2, df3, t_s):
    Xrlinter = np.array(df3[indexs(inter,df2)])
    yrlinter = np.array(df3.valor)
    
    Xrlinter_train, Xrlinter_test, yrlinter_train, yrlinter_test = train_test_split(Xrlinter, yrlinter, test_size=t_s)
    return Xrlinter_train, Xrlinter_test, yrlinter_train, yrlinter_test, Xrlinter
    
def Escalas(cve, Xrlinter_train, Xrlinter_test,df2,inter):
    if inter==1:
        scl = StandardScaler().fit(Xrlinter_train)
        Xrlinter_train = scl.transform(Xrlinter_train)  
        Xrlinter_test = scl.transform(Xrlinter_test)
    elif inter==10 or inter==5:
        index=indexs(inter,df2)
        leni=len(index)
        scl= StandardScaler().fit(Xrlinter_train[:,leni-4:leni]) 
        Xrlinter_train[:,leni-4:leni]= scl.transform(Xrlinter_train[:,leni-4:leni])   
        Xrlinter_test[:,leni-4:leni]= scl.transform(Xrlinter_test[:,leni-4:leni])  
    
    return Xrlinter_train, Xrlinter_test,scl


# Regresion lineal para una indexacion
def Regresion(Xtrain,Xtest,ytrain,ytest,k):
    multi_regr= linear_model.LinearRegression()
    multi_regr.fit(Xtrain, ytrain)
    y_pred13 =cross_val_predict(multi_regr, Xtest, ytest, cv=k)
    return multi_regr,y_pred13


#### SELECCIÓN MODELO REGRESIÓN ####
def indexs_maximos(mini,maxi): #mini: 1970, maxi: 2022
    years1=[]
    years2=[]
    for i in range(mini,maxi,10):
        years1.append(i)
    for j in range(mini,maxi,5):
        years2.append(j)
    if maxi not in years1:
        years1.append(maxi)
    if maxi not in years2:
        years2.append(maxi)

    L=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
    vectorS1=[]
    vectorS2=[]
    for i in range(0,len(years1)-2):
        vectorS1.append(L[i]+str(years1[i])+"/"+str(years1[i+1]-1))
    vectorS1.append(L[len(years1)-2]+str(years1[len(years1)-2])+"/"+str(years1[len(years1)-1]))
    choicelist1=[]
    for i in range(0,len(vectorS1)):
        choicelist1.append(vectorS1[i][0]+vectorS1[i][3:6]+vectorS1[i][8:10])
    for i in range(0,len(years2)-2):
        vectorS2.append(L[i]+str(years2[i])+"/"+str(years2[i+1]-1))
    vectorS2.append(L[len(years2)-2]+str(years2[len(years2)-2])+"/"+str(years2[len(years2)-1]))    
    choicelist2=[]
    for i in range(0,len(vectorS2)):
        choicelist2.append(vectorS2[i][0]+vectorS2[i][3:6]+vectorS2[i][8:10])
    indexs_maximos=[choicelist1,choicelist2]
    return indexs_maximos
    
def RegresionEleccion(df2,df3,cve,k,indexs_maximos): 
    L1,L1_test,L1_pred,L1_er,L1_reg=[],[],[],[],[]
    L2,L2_test,L2_pred,L2_er,L2_reg=[],[],[],[],[]
    L3,L3_test,L3_pred,L3_er,L3_reg=[],[],[],[],[]
    SCL1,SCL5,SCL10=[],[],[]
    L_10=list(df2['Index_antiguedad_10'].unique())
    L_10.sort()
    L_5=list(df2['Index_antiguedad_5'].unique())
    L_5.sort()
    if L_5==indexs_maximos[1]: 
        for i in range(0,30):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
            Xrl5_train, Xrl5_test, yrl5_train, yrl5_test,Xrl5=Entrenamiento(5,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
            Xrl5_train, Xrl5_test,scl5=Escalas(cve, Xrl5_train, Xrl5_test,df2,5)
            # Regresiones            
            regr1,y_pred13=Regresion(Xtodos_train, Xtodos_test,ytodos_train,ytodos_test,k)
            regr2,y_pred16=Regresion(Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,k)
            regr3,y_pred19=Regresion(Xrl5_train, Xrl5_test, yrl5_train, yrl5_test,k)
            
            E=porcentajeerror(ytodos_test,y_pred13,yrl10_test,y_pred16,yrl5_test,y_pred19)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            b=sum(E["Cantidad_Index_10_Relativa"][0:3])
            c=sum(E["Cantidad_Index_5_Relativa"][0:3])
            er1=abs(ytodos_test-y_pred13)
            er2=abs(yrl10_test-y_pred16)
            er3=abs(yrl5_test-y_pred19)
            r1,r2,r3=max(er1),max(er2),max(er3)
            mini_r=min(r1,r2,r3)
            if mini_r==r1:
                L1.append(a) # Lista con las cantidades de errores menores que +-15%
                L1_test.append(ytodos_test)
                L1_pred.append(y_pred13)
                L1_er.append(ytodos_test-y_pred13)
                L1_reg.append(regr1)
                SCL1.append(scl1)
            if mini_r==r2:
                L2.append(b)
                L2_test.append(yrl10_test)
                L2_pred.append(y_pred16)
                L2_er.append(yrl10_test-y_pred16)
                L2_reg.append(regr2)
                SCL10.append(scl10)
            if mini_r==r3:
                L3.append(c)
                L3_test.append(yrl5_test)
                L3_pred.append(y_pred19)
                L3_er.append(yrl5_test-y_pred19)
                L3_reg.append(regr3)
                SCL5.append(scl5)
        A,B,C=0,0,0
        if len(L1)>0:
            L1_T=L1_test[0]
            L1_P=L1_pred[0]
            L1_R=L1_reg[0]
            L1_E=L1_er[0]
            L1_F=L1[0]
            SCL1_F=SCL1[0]
            for k in range(0,len(L1)):
                if L1[k]>L1_F:
                    L1_T=L1_test[k]
                    L1_P=L1_pred[k]
                    L1_R=L1_reg[k]
                    L1_E=L1_er[k]
                    L1_F=L1[k]
                    SCL1_F=SCL1[k]
            A=L1_E.std()

        if len(L2)>0:
            L2_T=L2_test[0]
            L2_P=L2_pred[0]
            L2_R=L2_reg[0]
            L2_E=L2_er[0]
            L2_F=L2[0]
            SCL10_F=SCL10[0]
            for k in range(0,len(L2)):
                if L2[k]>L2_F:
                    L2_T=L2_test[k]
                    L2_P=L2_pred[k]
                    L2_R=L2_reg[k]
                    L2_E=L2_er[k]
                    L2_F=L2[k]
                    SCL10_F=SCL10[k]
            B=L2_E.std()
        if len(L3)>0:
            L3_T=L3_test[0]
            L3_P=L3_pred[0]
            L3_R=L3_reg[0]
            L3_E=L3_er[0]
            L3_F=L3[0]
            SCL5_F=SCL5[0]
            for k in range(0,len(L3)):
                if L3[k]>L3_F:
                    L3_T=L3_test[k]
                    L3_P=L3_pred[k]
                    L3_R=L3_reg[k]
                    L3_E=L3_er[k]
                    L3_F=L3[k]
                    SCL5_F=SCL5[k]
            C=L3_E.std()
        P1,P2=[A,B,C],[]
        for k in range(0,3):
            if P1[k]!=0:
                P2.append(P1[k])
        p=min(P2)
        if p==B:
            yrl10_test,y_pred16,regr2,scl10=L2_T,L2_P,L2_R,SCL10_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaRL_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file) 
            print("El método de regresión lineal escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(regr2,"Rlineal_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred16,regr2,inter
        elif p==C:
            yrl5_test,y_pred19,regr3,scl5=L3_T,L3_P,L3_R,SCL5_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler5_file = "escalaRL_"+str(cve)+".save"
            joblib.dump(scl5, scaler5_file) 
            print("El método de regresión lineal escogido será con indexación 5. Se procederá a guardarlo")
            joblib.dump(regr3,"Rlineal_"+str(cve)+".joblib")
            inter=5
            return scl5,yrl5_test,y_pred19,regr3,inter
        elif p==A:
            ytodos_test,y_pred13,regr1,scl1=L1_T,L1_P,L1_R,SCL1_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler1_file = "escalaRL_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de regresión lineal escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(regr1,"Rlineal_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred13,regr1,inter
        
    elif L_10==indexs_maximos[0]: 
        for i in range(0,30):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
            # Regresiones            
            regr1,y_pred13=Regresion(Xtodos_train, Xtodos_test,ytodos_train,ytodos_test,k)
            regr2,y_pred16=Regresion(Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,k)
            
            E=porcentajeerror(ytodos_test,y_pred13,yrl10_test,y_pred16,yrl10_test,y_pred16)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            b=sum(E["Cantidad_Index_10_Relativa"][0:3])
            er1=abs(ytodos_test-y_pred13)
            er2=abs(yrl10_test-y_pred16)
            r1,r2=max(er1),max(er2)
            mini_r=min(r1,r2)
            if mini_r==r1:
                L1.append(a) # Lista con las cantidades de errores menores que +-15%
                L1_test.append(ytodos_test)
                L1_pred.append(y_pred13)
                L1_er.append(ytodos_test-y_pred13)
                L1_reg.append(regr1)
                SCL1.append(scl1)
            if mini_r==r2:
                L2.append(b)
                L2_test.append(yrl10_test)
                L2_pred.append(y_pred16)
                L2_er.append(yrl10_test-y_pred16)
                L2_reg.append(regr2)
                SCL10.append(scl10)
        A,B=0,0
        if len(L1)>0:
            L1_T=L1_test[0]
            L1_P=L1_pred[0]
            L1_R=L1_reg[0]
            L1_E=L1_er[0]
            L1_F=L1[0]
            SCL1_F=SCL1[0]
            for k in range(0,len(L1)):
                if L1[k]>L1_F:
                    L1_T=L1_test[k]
                    L1_P=L1_pred[k]
                    L1_R=L1_reg[k]
                    L1_E=L1_er[k]
                    L1_F=L1[k]
                    SCL1_F=SCL1[k]
            A=L1_E.std()

        if len(L2)>0:
            L2_T=L2_test[0]
            L2_P=L2_pred[0]
            L2_R=L2_reg[0]
            L2_E=L2_er[0]
            L2_F=L2[0]
            SCL10_F=SCL10[0]
            for k in range(0,len(L2)):
                if L2[k]>L2_F:
                    L2_T=L2_test[k]
                    L2_P=L2_pred[k]
                    L2_R=L2_reg[k]
                    L2_E=L2_er[k]
                    L2_F=L2[k]
                    SCL10_F=SCL10[k]
            B=L2_E.std()
        P1,P2=[A,B],[]
        for k in range(0,2):
            if P1[k]!=0:
                P2.append(P1[k])
        p=min(P2)
        if p==B:
            yrl10_test,y_pred16,regr2,scl10=L2_T,L2_P,L2_R,SCL10_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaRL_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file) 
            print("El método de regresión lineal escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(regr2,"Rlineal_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred16,regr2,inter
        elif p==A:
            ytodos_test,y_pred13,regr1,scl1=L1_T,L1_P,L1_R,SCL1_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler1_file = "escalaRL_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de regresión lineal escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(regr1,"Rlineal_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred13,regr1,inter
    else:
        for i in range(0,30):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            # Regresiones            
            regr1,y_pred13=Regresion(Xtodos_train, Xtodos_test,ytodos_train,ytodos_test,k)
            
            E=porcentajeerror(ytodos_test,y_pred13,ytodos_test,y_pred13,ytodos_test,y_pred13)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            L1.append(a) # Lista con las cantidades de errores menores que +-15%
            L1_test.append(ytodos_test)
            L1_pred.append(y_pred13)
            L1_er.append(ytodos_test-y_pred13)
            L1_reg.append(regr1)
            SCL1.append(scl1)
            
        L1_T=L1_test[0]
        L1_P=L1_pred[0]
        L1_R=L1_reg[0]
        L1_E=L1_er[0]
        L1_F=L1[0]
        SCL1_F=SCL1[0]
        for k in range(0,len(L1)):
            if L1[k]>L1_F:
                L1_T=L1_test[k]
                L1_P=L1_pred[k]
                L1_R=L1_reg[k]
                L1_E=L1_er[k]
                L1_F=L1[k]
                SCL1_F=SCL1[k]
        ytodos_test,y_pred13,regr1,scl1=L1_T,L1_P,L1_R,SCL1_F
        # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
        scaler1_file = "escalaRL_"+str(cve)+".save"
        joblib.dump(scl1, scaler1_file)
        print("El método de regresión lineal escogido será sin indexación. Se procederá a guardarlo")
        joblib.dump(regr1,"Rlineal_"+str(cve)+".joblib")
        inter=1
        return scl1,ytodos_test,y_pred13,regr1,inter
    

def GraEstModels(a,b,c,d,e,f,g,h):
    xvec=list(a)
    xvec2=list(c)
    xvec3=list(e)
    xvec4=list(g)
    for k in range(0,len(xvec2)):
        xvec.append(xvec2[k])
    for k in range(0,len(xvec3)):
        xvec.append(xvec3[k])
    for k in range(0,len(xvec4)):
        xvec.append(xvec4[k])   
    xmin,xmax=min(xvec)-250,max(xvec)+250
    yvec=list(b)
    yvec2=list(d)
    yvec3=list(f)
    yvec4=list(h)
    for k in range(0,len(yvec2)):
        yvec.append(yvec2[k])
    for k in range(0,len(yvec3)):
        yvec.append(yvec4[k])
    for k in range(0,len(yvec4)):
        yvec.append(yvec4[k])
    ymin,ymax=min(yvec)-250,max(yvec)+250
    red=[xmin,xmax]
    
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14,10))
    axs[0,0].scatter(a,b,color="#008080");
    axs[0,0].plot(red,red,color="red")
    axs[0,0].set_xlabel('Valor Observado',size=12)
    axs[0,0].set_ylabel('Valor Estimado',size=12)
    axs[0,0].grid(True)
    axs[0,0].set_xlim(xmin,xmax)
    axs[0,0].set_ylim(ymin,ymax)
    axs[0,0].set_title('Regresión Lineal', size= 16)

    axs[0,1].scatter(c,d,color="#008080");
    axs[0,1].plot(red,red,color="red")
    axs[0,1].set_xlabel('Valor Observado',size=12)
    axs[0,1].set_ylabel('Valor Estimado',size=12)
    axs[0,1].grid(True)
    axs[0,1].set_xlim(xmin,xmax)
    axs[0,1].set_ylim(ymin,ymax)
    axs[0,1].set_title('ElasticNet', size= 16)
    
    axs[1,0].scatter(e,f,color="#008080");
    axs[1,0].plot(red,red,color="red")
    axs[1,0].set_xlabel('Valor Observado',size=12)
    axs[1,0].set_ylabel('Valor Estimado',size=12)
    axs[1,0].grid(True)
    axs[1,0].set_xlim(xmin,xmax)
    axs[1,0].set_ylim(ymin,ymax)
    axs[1,0].set_title('Random Forest', size= 16)
    
    axs[1,1].scatter(g,h,color="#008080");
    axs[1,1].plot(red,red,color="red")
    axs[1,1].set_xlabel('Valor Observado',size=12)
    axs[1,1].set_ylabel('Valor Estimado',size=12)
    axs[1,1].grid(True)
    axs[1,1].set_xlim(xmin,xmax)
    axs[1,1].set_ylim(ymin,ymax)
    axs[1,1].set_title('Extreme Gradient Boosting', size= 16)

    plt.show()

    ##### Error1 ####

def porcentajeerror(a,b,c,d,e,f):
    r1=100*(b-a)/a;
    rr1=r1.tolist();
    r2=100*(d-c)/c;
    rr2=r2.tolist();
    r3=100*(f-e)/e;
    rr3=r3.tolist();

    tabla= pd.DataFrame.from_dict({'Intervalo':[],
                                '%_Est_Acumulado': [],'Cantidad_Est_Relativa': [],
                                '%_Index_10_Acumulado': [],'Cantidad_Index_10_Relativa': [],
                                '%_Index_5_Acumulado': [],'Cantidad_Index_5_Relativa': []});
    col = ['Intervalo','%_Est_Acumulado','Cantidad_Est_Relativa','%_Index_10_Acumulado','Cantidad_Index_10_Relativa',
        '%_Index_5_Acumulado','Cantidad_Index_5_Relativa'];
    cant=[0,0,0]
    k=[5,10,15,20,25,50]
    for lim in range(0,len(k)):
        if k[lim]==5:
            inter=f"|Error|<={k[lim]} %"
        else: 
            inter=f"{k[lim-1]}% <|Error|<={k[lim]}%"
        porcentaje1=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))/len(rr1)
        cantidad1=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))-cant[0]
        porcentaje2=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))/len(rr2)
        cantidad2=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))-cant[1]
        porcentaje3=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))/len(rr3)
        cantidad3=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))-cant[2]
        cant=[cant[0]+cantidad1,cant[1]+cantidad2,cant[2]+cantidad3]

        tablaux = pd.DataFrame([[inter,porcentaje1,cantidad1,porcentaje2,cantidad2,porcentaje3,cantidad3]],
                              columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    return tabla

# ElasticNet para uno
def ELasticNet(Xlrinter_train, Xlrinter_test,yrlinter_train,yrlinter_test,CV):
    ENet_models = {}
    training_scores = []
    test_scores = []
    L1_ratio=[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]
    for l1_ratio in L1_ratio:
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        ENet = ElasticNet(alpha=1,l1_ratio=l1_ratio,max_iter=8000).fit(Xlrinter_train, yrlinter_train)
        training_scores.append(ENet.score(Xlrinter_train, yrlinter_train))
        test_scores.append(ENet.score(Xlrinter_test, yrlinter_test))
        ENet_models[l1_ratio] = ENet
    a_aux,a=0,0
    for k in range(0,len(L1_ratio)):
        if test_scores[k]>test_scores[a_aux]:
            a_aux=k
            a=L1_ratio[k]
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
    ENet=ENet_models[a]
    ENet.fit(Xlrinter_train, yrlinter_train)
    y_pred23 = cross_val_predict(ENet, Xlrinter_test, np.ravel(yrlinter_test), cv=CV)
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
    return ENet,y_pred23


# Para elegir 
def ELasticNetEleccion(df2,df3,cve,indexs_maximos):
    L1,L1_test,L1_pred,L1_er,L1_ENet=[],[],[],[],[]
    L2,L2_test,L2_pred,L2_er,L2_ENet=[],[],[],[],[]
    L3,L3_test,L3_pred,L3_er,L3_ENet=[],[],[],[],[]
    SCL1,SCL5,SCL10=[],[],[]
    L_10=list(df2['Index_antiguedad_10'].unique())
    L_10.sort()
    L_5=list(df2['Index_antiguedad_5'].unique())
    L_5.sort()
    if L_5==indexs_maximos[1]: 
        for i in range(0,20):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
            Xrl5_train, Xrl5_test, yrl5_train, yrl5_test,Xrl5=Entrenamiento(5,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
            Xrl5_train, Xrl5_test,scl5=Escalas(cve, Xrl5_train, Xrl5_test,df2,5)
            # ElasticNets
            ENet1,y_pred23=ELasticNet(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,10)
            ENet2,y_pred26=ELasticNet(Xrl10_train,Xrl10_test, yrl10_train,yrl10_test,10)
            ENet3,y_pred29=ELasticNet(Xrl5_train,Xrl5_test, yrl5_train,yrl5_test,10)
        
            E=porcentajeerror(ytodos_test,y_pred23,yrl10_test,y_pred26,yrl5_test,y_pred29)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            b=sum(E["Cantidad_Index_10_Relativa"][0:3])
            c=sum(E["Cantidad_Index_5_Relativa"][0:3])
            er1=abs(ytodos_test-y_pred23)
            er2=abs(yrl10_test-y_pred26)
            er3=abs(yrl5_test-y_pred29)
            r1,r2,r3=max(er1),max(er2),max(er3)
            mini_r=min(r1,r2,r3)
            if mini_r==r1:
                L1.append(a) # Lista con las cantidades de errores menores que +-15%
                L1_test.append(ytodos_test)
                L1_pred.append(y_pred23)
                L1_er.append(ytodos_test-y_pred23)
                L1_ENet.append(ENet1)
                SCL1.append(scl1)
            if mini_r==r2:
                L2.append(b)
                L2_test.append(yrl10_test)
                L2_pred.append(y_pred26)
                L2_er.append(yrl10_test-y_pred26)
                L2_ENet.append(ENet2)
                SCL10.append(scl10)
            if mini_r==r3:
                L3.append(c)
                L3_test.append(yrl5_test)
                L3_pred.append(y_pred29)
                L3_er.append(yrl5_test-y_pred29)
                L3_ENet.append(ENet3)
                SCL5.append(scl5)
        A,B,C=0,0,0
        if len(L1)>0:
            L1_T=L1_test[0]
            L1_P=L1_pred[0]
            L1_R=L1_ENet[0]
            L1_E=L1_er[0]
            L1_F=L1[0]
            SCL1_F=SCL1[0]
            for k in range(0,len(L1)):
                if L1[k]>L1_F:
                    L1_T=L1_test[k]
                    L1_P=L1_pred[k]
                    L1_R=L1_ENet[k]
                    L1_E=L1_er[k]
                    L1_F=L1[k]
                    SCL1_F=SCL1[k]
            A=L1_E.std()
        if len(L2)>0:
            L2_T=L2_test[0]
            L2_P=L2_pred[0]
            L2_R=L2_ENet[0]
            L2_E=L2_er[0]
            L2_F=L2[0]
            SCL10_F=SCL10[0]
            for k in range(0,len(L2)):
                if L2[k]>L2_F:
                    L2_T=L2_test[k]
                    L2_P=L2_pred[k]
                    L2_R=L2_ENet[k]
                    L2_E=L2_er[k]
                    L2_F=L2[k]
                    SCL10_F=SCL10[k]
            B=L2_E.std()
        if len(L3)>0:
            L3_T=L3_test[0]
            L3_P=L3_pred[0]
            L3_R=L3_ENet[0]
            L3_E=L3_er[0]
            L3_F=L3[0]
            SCL5_F=SCL5[0]
            for k in range(0,len(L3)):
                if L3[k]>L3_F:
                    L3_T=L3_test[k]
                    L3_P=L3_pred[k]
                    L3_R=L3_ENet[k]
                    L3_E=L3_er[k]
                    L3_F=L3[k]
                    SCL5_F=SCL5[k]
            C=L3_E.std()
        P1,P2=[A,B,C],[]
        for k in range(0,3):
            if P1[k]!=0:
                P2.append(P1[k])
        p=min(P2)
        if p==B:
            yrl10_test,y_pred26,ENet2,scl10=L2_T,L2_P,L2_R,SCL10_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaEN_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de ElasticNet  escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(ENet2,"ElasticNet_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred26,ENet2,inter
        elif p==C:
            yrl5_test,y_pred29,ENet3,scl5=L3_T,L3_P,L3_R,SCL5_F 
            scaler5_file = "escalaEN_"+str(cve)+".save"
            joblib.dump(scl5, scaler5_file) 
            print("El método de ElasticNet escogido será con indexación 5. Se procederá a guardarlo")
            joblib.dump(ENet3,"ElasticNet_"+str(cve)+".joblib")
            inter=5
            return scl5,yrl5_test,y_pred29,ENet3,inter
        elif p==A:
            ytodos_test,y_pred23,ENet1,scl1=L1_T,L1_P,L1_R,SCL1_F
            scaler1_file = "escalaEN_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de ElasticNet escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(ENet1,"ElasticNet_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred23,ENet1, inter
    if L_10==indexs_maximos[0]:
        for i in range(0,20):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
            # ElasticNets
            ENet1,y_pred23=ELasticNet(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,10)
            ENet2,y_pred26=ELasticNet(Xrl10_train,Xrl10_test, yrl10_train,yrl10_test,10)
        
            E=porcentajeerror(ytodos_test,y_pred23,yrl10_test,y_pred26,yrl10_test,y_pred26)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            b=sum(E["Cantidad_Index_10_Relativa"][0:3])
            er1=abs(ytodos_test-y_pred23)
            er2=abs(yrl10_test-y_pred26)
            r1,r2=max(er1),max(er2)
            mini_r=min(r1,r2)
            if mini_r==r1:
                L1.append(a) # Lista con las cantidades de errores menores que +-15%
                L1_test.append(ytodos_test)
                L1_pred.append(y_pred23)
                L1_er.append(ytodos_test-y_pred23)
                L1_ENet.append(ENet1)
                SCL1.append(scl1)
            if mini_r==r2:
                L2.append(b)
                L2_test.append(yrl10_test)
                L2_pred.append(y_pred26)
                L2_er.append(yrl10_test-y_pred26)
                L2_ENet.append(ENet2)
                SCL10.append(scl10)
        A,B=0,0
        if len(L1)>0:
            L1_T=L1_test[0]
            L1_P=L1_pred[0]
            L1_R=L1_ENet[0]
            L1_E=L1_er[0]
            L1_F=L1[0]
            SCL1_F=SCL1[0]
            for k in range(0,len(L1)):
                if L1[k]>L1_F:
                    L1_T=L1_test[k]
                    L1_P=L1_pred[k]
                    L1_R=L1_ENet[k]
                    L1_E=L1_er[k]
                    L1_F=L1[k]
                    SCL1_F=SCL1[k]
            A=L1_E.std()
        if len(L2)>0:
            L2_T=L2_test[0]
            L2_P=L2_pred[0]
            L2_R=L2_ENet[0]
            L2_E=L2_er[0]
            L2_F=L2[0]
            SCL10_F=SCL10[0]
            for k in range(0,len(L2)):
                if L2[k]>L2_F:
                    L2_T=L2_test[k]
                    L2_P=L2_pred[k]
                    L2_R=L2_ENet[k]
                    L2_E=L2_er[k]
                    L2_F=L2[k]
                    SCL10_F=SCL10[k]
            B=L2_E.std()
        P1,P2=[A,B],[]
        for k in range(0,2):
            if P1[k]!=0:
                P2.append(P1[k])
        p=min(P2)
        if p==B:
            yrl10_test,y_pred26,ENet2,scl10=L2_T,L2_P,L2_R,SCL10_F
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaEN_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de ElasticNet  escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(ENet2,"ElasticNet_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred26,ENet2,inter
        elif p==A:
            ytodos_test,y_pred23,ENet1,scl1=L1_T,L1_P,L1_R,SCL1_F
            scaler1_file = "escalaEN_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de ElasticNet escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(ENet1,"ElasticNet_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred23,ENet1, inter
    else:
        for i in range(0,20):
            # Entrenamientos
            Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
            # Escalas
            Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
            # ElasticNets
            ENet1,y_pred23=ELasticNet(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,10)
        
            E=porcentajeerror(ytodos_test,y_pred23,ytodos_test,y_pred23,ytodos_test,y_pred23)
            a=sum(E["Cantidad_Est_Relativa"][0:3])
            L1.append(a) # Lista con las cantidades de errores menores que +-15%
            L1_test.append(ytodos_test)
            L1_pred.append(y_pred23)
            L1_er.append(ytodos_test-y_pred23)
            L1_ENet.append(ENet1)
            SCL1.append(scl1)
           
        L1_T=L1_test[0]
        L1_P=L1_pred[0]
        L1_R=L1_ENet[0]
        L1_E=L1_er[0]
        L1_F=L1[0]
        SCL1_F=SCL1[0]
        for k in range(0,len(L1)):
            if L1[k]>L1_F:
                L1_T=L1_test[k]
                L1_P=L1_pred[k]
                L1_R=L1_ENet[k]
                L1_E=L1_er[k]
                L1_F=L1[k]
                SCL1_F=SCL1[k]
        ytodos_test,y_pred23,ENet1,scl1=L1_T,L1_P,L1_R,SCL1_F
        scaler1_file = "escalaEN_"+str(cve)+".save"
        joblib.dump(scl1, scaler1_file)
        print("El método de ElasticNet escogido será sin indexación. Se procederá a guardarlo")
        joblib.dump(ENet1,"ElasticNet_"+str(cve)+".joblib")
        inter=1
        return scl1,ytodos_test,y_pred23,ENet1, inter

## Random Forest para un par de datos
def RForest(Xtrain,Xtest,ytrain,ytest,k,df2,inter):
    long=len(indexs(inter,df2))
    rforest = RandomForestRegressor(max_features=long,random_state=42) #n_estimators=600, 
    params={'n_estimators':[300,500,800],
           'max_depth':[30,50,80]}  
    Search=GridSearchCV(estimator=rforest,
                       param_grid=params,
                       n_jobs=-1)
    rforest1=Search.fit(Xtrain,ytrain)
    rforest1.best_estimator_
    y_pred43 = cross_val_predict(rforest1, Xtest, np.ravel(ytest), cv=k)
    return rforest1,y_pred43

## ELECCION RANDOM FOREST ##
def RForestEleccion(df2,df3,cve,k,indexs_maximos): 
    L_10=list(df2['Index_antiguedad_10'].unique())
    L_10.sort()
    L_5=list(df2['Index_antiguedad_5'].unique())
    L_5.sort()
    if L_5==indexs_maximos[1]: 
        # Entrenamientos
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
        Xrl5_train, Xrl5_test, yrl5_train, yrl5_test,Xrl5=Entrenamiento(5,df2,df3,0.2)
        # Escalas
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
        Xrl5_train, Xrl5_test,scl5=Escalas(cve, Xrl5_train, Xrl5_test,df2,5)
        # Randoms Forests
        rforest1,y_pred43=RForest(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k,df2,1)
        rforest2,y_pred46=RForest(Xrl10_train,Xrl10_test,yrl10_train,yrl10_test,k,df2,10)
        rforest3,y_pred49=RForest(Xrl5_train,Xrl5_test,yrl5_train,yrl5_test,k,df2,5)
        
        E=porcentajeerror(ytodos_test,y_pred43,yrl10_test,y_pred46,yrl5_test,y_pred49)
        a=sum(E["Cantidad_Est_Relativa"][0:3])
        b=sum(E["Cantidad_Index_10_Relativa"][0:3])
        c=sum(E["Cantidad_Index_5_Relativa"][0:3])
        maxi=max(a,b,c)
        if maxi==b:
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaRF_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de Random Forest escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(rforest2,"RForest_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred46,rforest2,inter
        elif maxi==c:
            scaler5_file = "escalaRF_"+str(cve)+".save"
            joblib.dump(scl5, scaler5_file)  
            print("El método de Random Forest escogido será con indexación 5. Se procederá a guardarlo")
            joblib.dump(rforest3,"RForest_"+str(cve)+".joblib")
            inter=5
            return scl5,yrl5_test,y_pred49,rforest3,inter
        elif maxi==a:
            scaler1_file = "escalaRF_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de Random Forest escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(rforest1,"RForest_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred43,rforest1,inter
    elif L_10==indexs_maximos[0]:
        # Entrenamientos
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
        # Escalas
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
        # Randoms Forests
        rforest1,y_pred43=RForest(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k,df2,1)
        rforest2,y_pred46=RForest(Xrl10_train,Xrl10_test,yrl10_train,yrl10_test,k,df2,10)
        
        E=porcentajeerror(ytodos_test,y_pred43,yrl10_test,y_pred46,yrl10_test,y_pred46)
        a=sum(E["Cantidad_Est_Relativa"][0:3])
        b=sum(E["Cantidad_Index_10_Relativa"][0:3])
        maxi=max(a,b)
        if maxi==b:
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaRF_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de Random Forest escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(rforest2,"RForest_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred46,rforest2,inter
        elif maxi==a:
            scaler1_file = "escalaRF_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de Random Forest escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(rforest1,"RForest_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred43,rforest1,inter
    else:
        # Entrenamiento
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        # Escala
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        # Random Forest
        rforest1,y_pred43=RForest(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k,df2,1)
        
        scaler1_file = "escalaRF_"+str(cve)+".save"
        joblib.dump(scl1, scaler1_file)
        print("El método de Random Forest escogido será sin indexación. Se procederá a guardarlo")
        joblib.dump(rforest1,"RForest_"+str(cve)+".joblib")
        inter=1
        return scl1,ytodos_test,y_pred43,rforest1,inter
        

# XGB para un par de datos
def XGB(Xtrain,Xtest,ytrain,ytest,k):
    xg=xgb.XGBRegressor(objective="reg:squarederror",alpha=1)
    colsample= [0.3,0.5,0.7]
    lr=[0.05,0.2,0.5]
    max_d=[30,50,80]
    n_est=[300,500,800]
    params={"colsample_bytree":colsample,"learning_rate":lr,"max_depth":max_d,"n_estimators":n_est}
    search=GridSearchCV(estimator=xg,param_grid=params,n_jobs=-1)
    search_model=search.fit(Xtrain,ytrain)
    search_model.best_params_                    
    y_pred63 = cross_val_predict(search_model, Xtest, np.ravel(ytest), cv=k)
    return search_model,y_pred63


### ELECCIÓN DE XGB ###
def XGB_Eleccion(df2,df3,cve,k,indexs_maximos):
    L_10=list(df2['Index_antiguedad_10'].unique())
    L_10.sort()
    L_5=list(df2['Index_antiguedad_5'].unique())
    L_5.sort()
    if L_5==indexs_maximos[1]: 
        # Entrenamientos
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
        Xrl5_train, Xrl5_test, yrl5_train, yrl5_test,Xrl5=Entrenamiento(5,df2,df3,0.2)
        # Escalas
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
        Xrl5_train, Xrl5_test,scl5=Escalas(cve, Xrl5_train, Xrl5_test,df2,5)
        # XGBs
        xgb1,y_pred43=XGB(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k)
        xgb2,y_pred46=XGB(Xrl10_train,Xrl10_test,yrl10_train,yrl10_test,k)
        xgb3,y_pred49=XGB(Xrl5_train,Xrl5_test,yrl5_train,yrl5_test,k)
        
        E=porcentajeerror(ytodos_test,y_pred43,yrl10_test,y_pred46,yrl5_test,y_pred49)
    
        a=sum(E["Cantidad_Est_Relativa"][0:3])
        b=sum(E["Cantidad_Index_10_Relativa"][0:3])
        c=sum(E["Cantidad_Index_5_Relativa"][0:3])
        maxi=max(a,b,c)
 
        if maxi==b:
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaXGB_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de Extreme Gradient Boosting escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(xgb2,"XGB_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred46,xgb2,inter
        elif maxi==c:
            scaler5_file = "escalaXGB_"+str(cve)+".save"
            joblib.dump(scl5, scaler5_file)  
            print("El método de Extreme Gradient Boosting escogido será con indexación 5. Se procederá a guardarlo")
            joblib.dump(xgb3,"XGB_"+str(cve)+".joblib")
            inter=5
            return scl5,yrl5_test,y_pred49,xgb3,inter
        elif maxi==a:
            scaler1_file = "escalaXGB_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de Extreme Gradient Boosting escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(xgb1,"XGB_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred43,xgb1,inter
    elif L_10==indexs_maximos[0]: 
        # Entrenamientos
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        Xrl10_train, Xrl10_test, yrl10_train, yrl10_test,Xrl10=Entrenamiento(10,df2,df3,0.2)
        # Escalas
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        Xrl10_train, Xrl10_test,scl10 =Escalas(cve, Xrl10_train, Xrl10_test,df2,10)
        # XGBs
        xgb1,y_pred43=XGB(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k)
        xgb2,y_pred46=XGB(Xrl10_train,Xrl10_test,yrl10_train,yrl10_test,k)
        
        E=porcentajeerror(ytodos_test,y_pred43,yrl10_test,y_pred46,yrl10_test,y_pred46)
    
        a=sum(E["Cantidad_Est_Relativa"][0:3])
        b=sum(E["Cantidad_Index_10_Relativa"][0:3])
        maxi=max(a,b)
 
        if maxi==b:
            # Se guarda el escalamiento para cada forma con la que se trabajan los datos de entrada
            scaler10_file = "escalaXGB_"+str(cve)+".save"
            joblib.dump(scl10, scaler10_file)
            print("El método de Extreme Gradient Boosting escogido será con indexación 10. Se procederá a guardarlo")
            joblib.dump(xgb2,"XGB_"+str(cve)+".joblib")
            inter=10
            return scl10,yrl10_test,y_pred46,xgb2,inter
        elif maxi==a:
            scaler1_file = "escalaXGB_"+str(cve)+".save"
            joblib.dump(scl1, scaler1_file)
            print("El método de Extreme Gradient Boosting escogido será sin indexación. Se procederá a guardarlo")
            joblib.dump(xgb1,"XGB_"+str(cve)+".joblib")
            inter=1
            return scl1,ytodos_test,y_pred43,xgb1,inter
    else:
        # Entrenamientos
        Xtodos_train, Xtodos_test, ytodos_train, ytodos_test,Xtodos=Entrenamiento(1,df2,df3,0.2)
        # Escalas
        Xtodos_train, Xtodos_test,scl1 =Escalas(cve, Xtodos_train, Xtodos_test,df2,1)
        # XGBs
        xgb1,y_pred43=XGB(Xtodos_train,Xtodos_test,ytodos_train,ytodos_test,k)
        
        scaler1_file = "escalaXGB_"+str(cve)+".save"
        joblib.dump(scl1, scaler1_file)
        print("El método de Extreme Gradient Boosting escogido será sin indexación. Se procederá a guardarlo")
        joblib.dump(xgb1,"XGB_"+str(cve)+".joblib")
        inter=1
        return scl1,ytodos_test,y_pred43,xgb1,inter

# Error para los 4 modelos
def porcentajeerror2(a,b,c,d,e,f,g,h):
    r1=100*(b-a)/a;
    rr1=r1.tolist();
    r2=100*(d-c)/c;
    rr2=r2.tolist();
    r3=100*(f-e)/e;
    rr3=r3.tolist();
    r4=100*(h-g)/g;
    rr4=r4.tolist();
    
    tabla= pd.DataFrame.from_dict({'Intervalo':[],
                                '%_Est_Regresión': [],'Cantidad_Est_Regresión': [],
                                '%_Est_ElasticNet': [],'Cantidad_Est_ElasticNet': [],
                                '%_Est_RandomForest': [],'Cantidad_Est_RandomForest': [],
                                 '%_Est_XGboosting': [],'Cantidad_Est_XGboosting':[]});
    col = ['Intervalo','%_Est_Regresión','Cantidad_Est_Regresión','%_Est_ElasticNet','Cantidad_Est_ElasticNet',
        '%_Est_RandomForest','Cantidad_Est_RandomForest', '%_Est_XGboosting','Cantidad_Est_XGboosting'];
    cant=[0,0,0,0]
    k=[5,10,15,20,25,50]
    for lim in range(0,len(k)):
        if k[lim]==5:
            inter=f"|Error|<={k[lim]} %"
        else: 
            inter=f"{k[lim-1]}% <|Error|<={k[lim]}%"
        porcentaje1=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))/len(rr1)
        cantidad1=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))-cant[0]
        porcentaje2=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))/len(rr2)
        cantidad2=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))-cant[1]
        porcentaje3=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))/len(rr3)
        cantidad3=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))-cant[2]
        porcentaje4=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr4))/len(rr4)
        cantidad4=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr4))-cant[3]
        cant=[cant[0]+cantidad1,cant[1]+cantidad2,cant[2]+cantidad3,cant[3]+cantidad4]
      
        tablaux = pd.DataFrame([[inter,porcentaje1,cantidad1,porcentaje2,cantidad2,porcentaje3,cantidad3,porcentaje4,cantidad4]],
                              columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    return tabla

def Tabla_Estadistica_Error(y11,y12,y21,y22,y31,y32,y41,y42):
    E_regr=[]
    E_ElasticNet=[]
    E_RForest=[]
    E_XGB=[]
    Sobreestimados1=0
    Sobreestimados2=0
    Sobreestimados3=0
    Sobreestimados4=0
    Subestimados1=0
    Subestimados2=0
    Subestimados3=0
    Subestimados4=0
    Estimados1=0
    Estimados2=0
    Estimados3=0
    Estimados4=0
    for i in range(0,len(y11)):
        E_regr.append(y11[i]-y12[i])
        if y11[i]-y12[i]<0:
            Sobreestimados1+=1
        elif y11[i]-y12[i]>0:
            Subestimados1+=1
        Estimados1+=1
    for i in range(0,len(y21)):
        E_ElasticNet.append(y21[i]-y22[i])
        if y21[i]-y22[i]<0:
            Sobreestimados2+=1
        elif y21[i]-y22[i]>0:
            Subestimados2+=1
        Estimados2+=1
    for i in range(0,len(y31)):
        E_RForest.append(y31[i]-y32[i])
        if y31[i]-y32[i]<0:
            Sobreestimados3+=1
        elif y31[i]-y32[i]>0:
            Subestimados3+=1
        Estimados3+=1
    for i in range(0,len(y41)):
        E_XGB.append(y41[i]-y42[i])
        if y41[i]-y42[i]<0:
            Sobreestimados4+=1
        elif y41[i]-y42[i]>0:
            Subestimados4+=1
        Estimados4+=1
    Sobreestimados=[Sobreestimados1,Sobreestimados2,Sobreestimados3,Sobreestimados4]
    Subestimados=[Subestimados1,Subestimados2,Subestimados3,Subestimados4]
    Estimados=[Estimados1,Estimados2,Estimados3,Estimados4]
    tabla= pd.DataFrame.from_dict({'Método':[],
                                'Media': [],'Desviación estándar': [],"Rango":[],
                                'Mediana': [],"Cuartil 1": [],
                                "Cuartil 3": [],"Datos sobreestimados":[], "Datos subestimados":[],"Datos Estimados":[]});
    col = ['Método','Media','Desviación estándar',"Rango",'Mediana','Cuartil 1',"Cuartil 3","Datos sobreestimados",
        "Datos subestimados","Datos Estimados"];
    inter=["Regresión lineal","Elastic Net","Random Forest", "Xtreme Gradient Boosting"]
    media=[np.mean(E_regr),np.mean(E_ElasticNet),np.mean(E_RForest),np.mean(E_XGB)]
    ds=[np.std(E_regr),np.std(E_ElasticNet),np.std(E_RForest),np.std(E_XGB)] 
    med=[np.percentile(E_regr,50),np.percentile(E_ElasticNet,50),np.percentile(E_RForest,50),np.percentile(E_XGB,50)]
    Cuart1=[np.percentile(E_regr,25),np.percentile(E_ElasticNet,25),np.percentile(E_RForest,25),np.percentile(E_XGB,25)]
    Cuart3=[np.percentile(E_regr,75),np.percentile(E_ElasticNet,75),np.percentile(E_RForest,75),np.percentile(E_XGB,75)]
    Rango=[max(E_regr)-min(E_regr),max(E_ElasticNet)-min(E_ElasticNet),max(E_RForest)-min(E_RForest),max(E_XGB)-min(E_XGB)]
    for i in range(0,4):
        tablaux = pd.DataFrame([[inter[i],media[i],ds[i],Rango[i],med[i],Cuart1[i],Cuart3[i],Sobreestimados[i],Subestimados[i],Estimados[i]]],
                                  columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    return tabla


##################### PARTE 3 #########################

def InsertColumnasAVM(reavm):
    reavm.insert(reavm.shape[1],'% de error',
             100*(reavm.loc[:,'Estimación AVM']-reavm.loc[:,'valor'])/reavm.loc[:,'valor'],
             True)
    reavm.insert(reavm.shape[1],'error',reavm['Estimación AVM']-reavm['valor'],True)
    return reavm

def Is_estimated_by_AVM(reavm):
    reavm1=reavm.loc[reavm.loc[:,'Estimación AVM']==0]
    print(f"La cantidad de datos no estimados por AVM es de: {len(reavm[reavm['Estimación AVM']==0])}")
    print(f"Cuyo porcentaje equivale a: {(len(reavm[reavm['Estimación AVM']==0])*100)/reavm.shape[0]: .2f}%")
    reavm2=reavm.loc[reavm.loc[:,'Estimación AVM']>0]
    print(f"La cantidad de datos estimados por AVM es de: {len(reavm[reavm['Estimación AVM']>0])}")
    print(f"Cuyo porcentaje equivale a: {(len(reavm[reavm['Estimación AVM']>0])*100)/reavm.shape[0]: .2f}%")
    return reavm1,reavm2

def add_index_AVM(reml,reml2,index_maximos):
    L_5=list(reml['Index_antiguedad_5'].unique())
    L_5.sort()
    L_10=list(reml["Index_antiguedad_10"].unique())
    L_10.sort()
    nombre1="Index_antiguedad_5"
    nombre2="Index_antiguedad_10" 
    for i in range(0,len(index_maximos[0])): 
        if index_maximos[0][i] not in L_10:
            string=nombre2+"_"+index_maximos[0][i]
            reml.insert(i+25, string, 0, allow_duplicates=False)
        elif index_maximos[0][i] in L_10:
            string=nombre2+"_"+index_maximos[0][i]
            reml.insert(i+25,string,np.array(reml2[[string]]))
    for j in range(0,len(index_maximos[1])):
        if index_maximos[1][j] not in L_5:
            string=nombre1+"_"+index_maximos[1][j]
            reml.insert(j+25+len(index_maximos[0]), string, 0, allow_duplicates=False)
        elif index_maximos[1][j] in L_5:
            string=nombre1+"_"+index_maximos[1][j]
            reml.insert(j+25+len(index_maximos[0]),string,np.array(reml2[[string]]))
    return reml

def Rend_Est_AVM(reavm2):
    plt.rcParams['figure.figsize'] = (9,5);
    sns.scatterplot(data=reavm2,x='valor',y='Estimación AVM',color="#008080")
    plt.plot(reavm2['valor'],reavm2['valor'],color="red")
    plt.plot(reavm2['valor'],reavm2['valor']*(1.05),color="blue")
    plt.plot(reavm2['valor'],reavm2['valor']*(0.95),color="blue")
    plt.plot(reavm2['valor'],reavm2['valor']*(1.2),color="orange")
    plt.plot(reavm2['valor'],reavm2['valor']*(0.8),color="orange")
    plt.legend(["Datos","Recta ajustada a los datos","Error del +5%","Error del -5%","Error del +20%","Error del -20%"])
    plt.title("Datos estimados por el AVM",size=16)
    plt.xlabel('Valor Observado');
    plt.ylabel('Valor Estimado AVM');
    plt.grid(True)
    plt.show()
    
    
def Xrl_inter(reml,reml2,inter):
    Xrlinter = np.array(reml2[indexs(inter,reml)])
    long=len(indexs(inter,reml))
    return Xrlinter,long


def SCL_model(scl,inter,Xtodos,Xrl10,long2,Xrl5,long3):
    if inter==1:
        Xtodos=scl.transform(Xtodos)
        return Xtodos
    elif inter==10:
        Xrl10[:,long2-4:long2]= scl.transform(Xrl10[:,long2-4:long2]) 
        return Xrl10
    elif inter==5:
        Xrl5[:,long3-4:long3]= scl.transform(Xrl5[:,long3-4:long3])
        return Xrl5

def Prediccion(modelo,Xrlinter): #modelo=regr,rforest,Enet y xgb
    ValEst_mod=modelo.predict(Xrlinter)
    return ValEst_mod

def InsertColumnsML(reml2,ValEst_RL,ValEst_EN,ValEst_RF,ValEst_XGB):
    reml2.insert(reml2.shape[1],'ValEst_RL',ValEst_RL,True)
    reml2.insert(reml2.shape[1],'ValEst_EN',ValEst_EN,True)
    reml2.insert(reml2.shape[1],'ValEst_RF',ValEst_RF,True)
    reml2.insert(reml2.shape[1],'ValEst_XGB',ValEst_XGB,True)
    reml2.insert(reml2.shape[1],'% de error RL',100*(reml2['ValEst_RL']-reml2['valor'])/reml2['valor'],True)
    reml2.insert(reml2.shape[1],'error RL',reml2['ValEst_RL']-reml2['valor'],True)

    reml2.insert(reml2.shape[1],'% de error EN',100*(reml2['ValEst_EN']-reml2['valor'])/reml2['valor'],True)
    reml2.insert(reml2.shape[1],'error EN',reml2['ValEst_EN']-reml2['valor'],True)

    reml2.insert(reml2.shape[1],'% de error RF',100*(reml2['ValEst_RF']-reml2['valor'])/reml2['valor'],True)
    reml2.insert(reml2.shape[1],'error RF',reml2['ValEst_RF']-reml2['valor'],True)

    reml2.insert(reml2.shape[1],'% de error XGB',100*(reml2['ValEst_XGB']-reml2['valor'])/reml2['valor'],True)
    reml2.insert(reml2.shape[1],'error XGB',reml2['ValEst_XGB']-reml2['valor'],True)
    return reml2

def Rend_Est_ML(reml2):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

    axs[0,0].scatter(reml2['valor'],reml2['ValEst_RL'],color="#008080");
    axs[0,0].plot(reml2['valor'],reml2['valor']*(1.05),color="blue")
    axs[0,0].plot(reml2['valor'],reml2['valor']*(0.95),color="blue")
    axs[0,0].plot(reml2['valor'],reml2['valor']*(1.2),color="orange")
    axs[0,0].plot(reml2['valor'],reml2['valor']*(0.8),color="orange")
    axs[0,0].plot(reml2['valor'],reml2['valor'],color="red")
    axs[0,0].set_xlabel('Valor Observado')
    axs[0,0].set_ylabel('Valor Estimado')
    axs[0,0].set_title('Regresión Lineal')
    axs[0,0].grid(True)

    axs[0,1].scatter(reml2['valor'],reml2['ValEst_EN'],color="#008080");
    axs[0,1].plot(reml2['valor'],reml2['valor']*(1.05),color="blue")
    axs[0,1].plot(reml2['valor'],reml2['valor']*(0.95),color="blue")
    axs[0,1].plot(reml2['valor'],reml2['valor']*(1.2),color="orange")
    axs[0,1].plot(reml2['valor'],reml2['valor']*(0.8),color="orange")
    axs[0,1].plot(reml2['valor'],reml2['valor'],color="red")
    axs[0,1].set_xlabel('Valor Observado')
    axs[0,1].set_ylabel('Valor Estimado')
    axs[0,1].set_title('ElasticNet')
    axs[0,1].grid(True)

    axs[1,0].scatter(reml2['valor'],reml2['ValEst_RF'],color="#008080");
    axs[1,0].plot(reml2['valor'],reml2['valor'],color="red")
    axs[1,0].plot(reml2['valor'],reml2['valor']*(1.05),color="blue")
    axs[1,0].plot(reml2['valor'],reml2['valor']*(0.95),color="blue")
    axs[1,0].plot(reml2['valor'],reml2['valor']*(1.2),color="orange")
    axs[1,0].plot(reml2['valor'],reml2['valor']*(0.8),color="orange")
    axs[1,0].set_xlabel('Valor Observado')
    axs[1,0].set_ylabel('Valor Estimado')
    axs[1,0].set_title('Random Forest')
    axs[1,0].grid(True)

    axs[1,1].scatter(reml2['valor'],reml2['ValEst_XGB'],color="#008080");
    axs[1,1].plot(reml2['valor'],reml2['valor'],color="red")
    axs[1,1].plot(reml2['valor'],reml2['valor']*(1.05),color="blue")
    axs[1,1].plot(reml2['valor'],reml2['valor']*(0.95),color="blue")
    axs[1,1].plot(reml2['valor'],reml2['valor']*(1.2),color="orange")
    axs[1,1].plot(reml2['valor'],reml2['valor']*(0.8),color="orange")
    axs[1,1].set_xlabel('Valor Observado')
    axs[1,1].set_ylabel('Valor Estimado')
    axs[1,1].set_title('Extreme Gradient Boosting')
    axs[1,1].grid(True)

    plt.show()
    
def Error_AVM_vs_ML(reml2):
    real=reml2['valor']
    estimadoavm=reml2['Estimación AVM']
    estimado1=reml2['ValEst_RL']
    estimado2=reml2['ValEst_EN']
    estimado3=reml2['ValEst_RF']
    estimado4=reml2['ValEst_XGB']
    r=100*(estimadoavm-real)/real 
    rr=r.tolist();
    r1=100*(estimado1-real)/real;
    rr1=r1.tolist();
    r2=100*(estimado2-real)/real;
    rr2=r2.tolist();
    r3=100*(estimado3-real)/real;
    rr3=r3.tolist();
    r4=100*(estimado4-real)/real;
    rr4=r4.tolist();

    tabla= pd.DataFrame.from_dict({'Intervalo':[],
                                   '%_AVM_Acumulado': [],'Cantidad_AVM': [],
                                   '%_RL_Acumulado': [],'Cantidad_RL': [],
                                   '%_EN_Acumulado': [],'Cantidad_EN': [],
                                   '%_RF_Acumulado': [],'Cantidad_RF': [],
                                   '%_XGB_Acumulado': [],'Cantidad_XGB': []});

    col = ['Intervalo','%_AVM_Acumulado','Cantidad_AVM','%_RL_Acumulado','Cantidad_RL', '%_EN_Acumulado','Cantidad_EN',
                                   '%_RF_Acumulado','Cantidad_RF', "%_XGB_Acumulado",'Cantidad_XGB'];
    cant=[0,0,0,0,0]
    k=[5,10,15,20,25,50]
    for lim in range(0,len(k)):
        if k[lim]==5:
            inter=f"|Error|<={k[lim]} %"
        else: 
            inter=f"{k[lim-1]}% <|Error|<={k[lim]}%"
        porcentajeavm=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr))/len(rr)
        cantidadavm=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr))-cant[0]
        porcentaje1=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))/len(rr1)
        cantidad1=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr1))-cant[1]
        porcentaje2=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))/len(rr2)
        cantidad2=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr2))-cant[2]
        porcentaje3=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))/len(rr3)
        cantidad3=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr3))-cant[3]
        porcentaje4=100*sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr4))/len(rr4)
        cantidad4=sum(map(lambda x : (x>=-k[lim]) & (x<=k[lim]), rr4))-cant[4]
        cant=[cant[0]+cantidadavm,cant[1]+cantidad1,cant[2]+cantidad2,cant[3]+cantidad3,cant[4]+cantidad4]


        tablaux = pd.DataFrame([[inter,porcentajeavm,cantidadavm,
                                 porcentaje1,cantidad1,porcentaje2,cantidad2,
                                 porcentaje3,cantidad3,porcentaje4,cantidad4]],
                                columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    return tabla

def Tabla_Estadistica_Error2(df):
    E_AVM=df.loc[:,"error"]
    E_regr=df.loc[:,"error RL"]
    E_ElasticNet=df.loc[:,"error EN"]
    E_RForest=df.loc[:,"error RF"]
    E_XGB=df.loc[:,"error XGB"]
    Sobreestimados1=len(E_AVM[E_AVM>0])
    Sobreestimados2=len(E_regr[E_regr>0])
    Sobreestimados3=len(E_ElasticNet[E_ElasticNet>0])
    Sobreestimados4=len(E_RForest[E_RForest>0])
    Sobreestimados5=len(E_XGB[E_XGB>0])
    Subestimados1=len(E_AVM[E_AVM<0])
    Subestimados2=len(E_regr[E_regr<0])
    Subestimados3=len(E_ElasticNet[E_ElasticNet<0])
    Subestimados4=len(E_RForest[E_RForest<0])
    Subestimados5=len(E_XGB[E_XGB<0])
    #EstimadosTotales1=len(E_AVM)
    #EstimadosTotales2=len(E_regr)
    #EstimadosTotales3=len(E_ElasticNet)
    
    Sobreestimados=[Sobreestimados1,Sobreestimados2,Sobreestimados3,Sobreestimados4,Sobreestimados5]
    Subestimados=[Subestimados1,Subestimados2,Subestimados3,Subestimados4,Subestimados5]
    
    tabla= pd.DataFrame.from_dict({'Método':[],
                                'Media': [],'Desviación estándar': [],"Rango":[],
                                'Mediana': [],"Cuartil 1": [],
                                "Cuartil 3": [],"Datos sobreestimados":[], "Datos subestimados":[],"Datos estimados":[]});
    col = ['Método','Media','Desviación estándar',"Rango",'Mediana','Cuartil 1',"Cuartil 3","Datos sobreestimados",
        "Datos subestimados"];
    inter=["AVM","Regresión lineal","Elastic Net","Random Forest", "Xtreme Gradient Boosting"]
    media=[E_AVM.mean(),np.mean(E_regr),np.mean(E_ElasticNet),np.mean(E_RForest),np.mean(E_XGB)]
    ds=[E_AVM.std(),np.std(E_regr),np.std(E_ElasticNet),np.std(E_RForest),np.std(E_XGB)] 
    med=[E_AVM.median(),np.percentile(E_regr,50),np.percentile(E_ElasticNet,50),np.percentile(E_RForest,50),np.percentile(E_XGB,50)]
    Cuart1=[np.percentile(E_AVM,25),np.percentile(E_regr,25),np.percentile(E_ElasticNet,25),np.percentile(E_RForest,25),np.percentile(E_XGB,25)]
    Cuart3=[np.percentile(E_AVM,75),np.percentile(E_regr,75),np.percentile(E_ElasticNet,75),np.percentile(E_RForest,75),np.percentile(E_XGB,75)]
    Rango=[max(E_AVM)-min(E_AVM),max(E_regr)-min(E_regr),max(E_ElasticNet)-min(E_ElasticNet),max(E_RForest)-min(E_RForest),max(E_XGB)-min(E_XGB)]
    for i in range(0,5):
        tablaux = pd.DataFrame([[inter[i],media[i],ds[i],Rango[i],med[i],Cuart1[i],Cuart3[i],Sobreestimados[i],Subestimados[i]]],
                                  columns=col);
        tabla=pd.concat([tabla, tablaux],ignore_index=True);
    return tabla

def ModeloFinal(reml2,scls,models,cve):
    Menor50=[] # Lista para guardar los 2 modelos con menor cantidad de datos sobre el 50% de error
    indice=[]
    RL_er=np.array(list(map(abs, reml2['% de error RL'].tolist())))
    EN_er=np.array(list(map(abs, reml2['% de error EN'].tolist())))
    RF_er=np.array(list(map(abs, reml2['% de error RF'].tolist())))
    XGB_er=np.array(list(map(abs, reml2['% de error XGB'].tolist())))
    L=[RL_er,EN_er,RF_er,XGB_er] #Lista 
    a1=len(RL_er[RL_er>15])
    a2=len(EN_er[EN_er>15])
    a3=len(RF_er[RF_er>15])
    a4=len(XGB_er[XGB_er>15])
    a,A=[a1,a2,a3,a4],[a1,a2,a3,a4]
    A.sort()
    for i in range(0,4):
        if a[i]==A[0] or a[i]==A[1]:
            Menor50.append(L[i])
            indice.append(i)
        if len(Menor50)==2:
            break
    M0,M1=Menor50[0],Menor50[1]
    b0=len(M0[M0<10])
    b1=len(M1[M1<10])
    B=[b0,b1]
    for i in range(0,2):
        if B[i]==max(B):
            Model_F=Menor50[i]
            k=indice[i]
    if k==0:
        print("El método escogido de manera definitiva será el de regresión lineal. Se procede a guardarlo")
        scaler_file = "escalaF_RL_"+str(cve)+".save"
        joblib.dump(scls[0], scaler_file)
        joblib.dump(models[0],"Rlineal_F_"+str(cve)+".joblib")
        return models[0],scls[0]
    elif k==1:
        print("El método escogido de manera definitiva será el de Elastic Net. Se procede a guardarlo")
        scaler_file = "escalaF_EN_"+str(cve)+".save"
        joblib.dump(scls[1], scaler_file)
        joblib.dump(models[1],"ENet_F_"+str(cve)+".joblib")
        return models[1],scls[1]
    elif k==2:
        print("El método escogido de manera definitiva será el de Random Forest. Se procede a guardarlo")
        scaler_file = "escalaF_RF_"+str(cve)+".save"
        joblib.dump(scls[2], scaler_file)
        joblib.dump(models[2],"RF_F_"+str(cve)+".joblib")
        return models[2],scls[2]
    elif k==3:
        print("El método escogido de manera definitiva será el Extreme Gradient Boosting. Se procede a guardarlo")
        scaler_file = "escalaF_XGB_"+str(cve)+".save"
        joblib.dump(scls[3], scaler_file)
        joblib.dump(models[3],"XGB_F_"+str(cve)+".joblib")
        return models[3],scls[3]
