import pandas as pd

igm_df = pd.read_csv("Módulo 2/igm_modificado.csv")

ind_des = igm_df['indice_governanca']

print(igm_df.describe())