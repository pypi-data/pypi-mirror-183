
import pandas as pd
import numpy as np
from IPython.display import display


def eda(df):
    display(df.head())
    print ("\n") 
    print("Description of the DataFrame ")
    print ("\n")  
    display(df.describe())
    print ("\n")  
    print('Shape of the Data')
    print ("\n")  
    display(df.shape)
    print ("\n")  
    numeric_features = df.select_dtypes(include=[np.number])
    print('numeric_features of the Data')
    print ("\n")  

    display(numeric_features.columns)



   
  