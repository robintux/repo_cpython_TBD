# data_cleaning.py - Limpieza basica de los datos con feature flag
import pandas as pd 
def clean_data(use_clean: bool = False):
  df = pd.read_csv("data/dataset.csv")
  if use_clean:
    df = df.dropna()
  return df 
