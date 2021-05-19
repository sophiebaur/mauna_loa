##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    df=pd.read_csv(filename)
    first_date=(df['decimal_date'][0])
    df['years_since_first']=df['decimal_date']-first_date
    df=df[['years_since_first','C02']]
    return df
   

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    plt.plot(df['years_since_first'],df['C02'])
    plt.xlabel('Years since 1958')
    plt.ylabel('CO2 levels')
    
    ax=plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    
    
    
    