
import pandas as pd
import numpy as np
from IPython.display import display
import missingno as msno
from colorama import Fore
import seaborn as sns


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
    print(Fore.GREEN +"Visualising missing values of the Dataframe")
    print ("\n")  
    msno.matrix(df)
    print ("\n")  

    print(Fore.GREEN + "Heatmap \n The missingno correlation heatmap measures nullity correlation: how strongly the presence or absence of one variable affects the presence of another")
    msno.heatmap(df)
    print ("\n")  

    print(Fore.GREEN +"Estimate Skewness")
    print ("\n") 
    display(df.skew())
    display(sns.distplot(df.skew(),color='blue',axlabel ='Skewness'))





    print ("\n")  

    print(Fore.GREEN +"Estimate Kurtosis")
    
    print ("\n")  
    display(df.kurt())
    display(sns.distplot(df.kurt(),color='blue',axlabel ='Skewness'))


    




   
  