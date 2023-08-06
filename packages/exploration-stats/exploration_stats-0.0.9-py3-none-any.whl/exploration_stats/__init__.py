
import pandas as pd
import numpy as np
from IPython.display import display
import missingno as msno
import colorama
from colorama import Fore


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




   
  