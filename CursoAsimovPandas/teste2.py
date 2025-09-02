import pandas as pd

caminho_dados = "C:/Users/usuario/Documents/Programas/csv/2023_Viagem.csv"
pd.set_option('display.max_columns', None)
df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";", decimal=",")

df_viagens['Despesas'] = df_viagens['Valor diárias'] + df_viagens['Valor passagens'] + df_viagens['Valor outros gastos']

print( (df_viagens['Cargo'].value_counts(normalize=True) * 100).rename("Proporção de viagens").reset_index())