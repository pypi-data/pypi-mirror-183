
import pandas as pd
import numpy as np
from IPython.display import display
import missingno as msno
from colorama import Fore
import seaborn as sns
import matplotlib.pyplot as plt 

def eda(df):
    display(df.head())
    print ("\n") 
    print(Fore.GREEN +"Description of the DataFrame ")
    print ("\n")  
    display(df.describe())
    print ("\n")  
    print(Fore.GREEN +'Shape of the Data')
    print ("\n")  
    display(df.shape)
    print ("\n")  
    numeric_features = df.select_dtypes(include=[np.number])
    print(Fore.GREEN +'numeric_features of the Data')
    print ("\n")  

    display(numeric_features.columns)
    print ("\n")  
    print(Fore.GREEN +'categorical_features of the Data')

    
    categorical_features = df.select_dtypes(include=[np.object])

    display(categorical_features.columns)
    print ("\n")  
    

    print(Fore.GREEN +"Estimate Skewness")
    print ("\n") 
    display(df.skew())






    print ("\n")  

    print(Fore.GREEN +"Estimate Kurtosis")
    
    print ("\n")  
    display(df.kurt())


    print(Fore.GREEN +"Pairplot")
    print ("\n")  
    pp = sns.pairplot(df, height=3.5)
    pp.fig.suptitle("My Pairplot")
    plt.show()



    print ("\n")  
    print(Fore.GREEN +"No of Missing Values")
    display(df.isnull().sum())


    

   
    
   
    print ("\n") 
    

    plt.title(" Countplot on categorical feathures")
    print ("\n")  
    list1=list(categorical_features.columns)
    for i in list1:
        plt.figure()
        plt.title(f'countplot of {i}')
        sns.countplot(x=df[i])
    
    print ("\n")      

    plt.title(" Distplot on Numerical feathures")
    print ("\n")  
    list2=list(numeric_features)
    for i in list2:
        plt.figure()
        plt.title(f'Distribution plot of {i}')
        sns.distplot(df[i])
        plt.show()    

    plt.title("Visualising missing values of the Dataframe")
    print ("\n")  
    msno.matrix(df)
    print ("\n")  



    plt.title("Heatmap \n The missingno correlation heatmap measures nullity correlation: how strongly the presence or absence of one variable affects the presence of another")
    msno.heatmap(df)
 
    print ("\n")  
  