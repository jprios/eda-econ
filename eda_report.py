import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os
import sys
from pathlib import Path

def load_data():
    # Obter diretório atual
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])
    else:
        # Caminho padrão
        data_path = current_dir / "data.csv"

    if not data_path.exists():
        st.error(f"Arquivo não encontrado em: {data_path}")
        st.stop()

    df = pd.read_csv(data_path,on_bad_lines= 'skip')
    return df

def treat_data(df):
  df = df.iloc[:-2]
  df.drop(['Time Code','Country Code'],axis = 1,inplace = True)
  df.columns = ['time','country','gdp_growth','inflation','real_interest_rate','reer']
  df = df.replace({'..':np.nan})
  cols = ['gdp_growth','inflation','real_interest_rate','reer']
  for col in cols:
    df[col] = df[col].astype('float')
  df = df.dropna()
  df.loc[:,'time'] = df.loc[:,'time'].astype(int)
  countries = df.groupby('country')['time'].count().reset_index().rename({'time':'freq'},axis = 1)
  country_list = countries[countries['freq']==20]['country'].tolist()
  df_final = df[df['country'].isin(country_list)]
  return df

def load_continent_data():
    # Obter diretório atual
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])
    else:
        # Caminho padrão
        data_path = current_dir / "continents.csv"

    if not data_path.exists():
        st.error(f"Arquivo não encontrado em: {data_path}")
        st.stop()

    df = pd.read_csv(data_path,on_bad_lines= 'skip')
    df.columns = ['continent','country']
    return df

def merge_datasets(df1,df2):
  df_merge = df1.merge(df2, on = ['country'], how = 'inner')
  df_merge = df_merge[['time','country','continent','gdp_growth','inflation','real_interest_rate','reer']]
  return df_merge

def select_year(df,year):
  return df.query(f"time == {year}")


def cat_box_plot(df,y_var,cat,color_cat = None):
  fig = px.box(df, x=cat, y=y_var,color = color_cat)
  fig.update_traces(quartilemethod="exclusive")
  return fig.show()

def cat_scatter_plot(df,y_var,x_var,color_cat = None):
  fig = px.scatter(df, x=x_var, y=y_var, color=color_cat,
                 range_x = [np.min(df[x_var]),np.max(df[x_var])],
                 range_y = [np.min(df[y_var]),np.max(df[y_var])])
  return fig.show()