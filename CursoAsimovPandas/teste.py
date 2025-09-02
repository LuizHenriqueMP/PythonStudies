import pandas as pd

caminho_dados = "C:/Users/usuario/Documents/Programas/csv/2023_Viagem.csv"

df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";")
pd.set_option('display.max_columns', None)

df_viagens['Valor diárias'] == df_viagens["Valor diárias"].str.replace(",", ".").astype(float)
df_viagens['Valor passagens'] == df_viagens["Valor passagens"].str.replace(",", ".").astype(float)
df_viagens['Valor devolução'] == df_viagens["Valor devolução"].str.replace(",", ".").astype(float)
df_viagens['Valor outros gastos'] == df_viagens["Valor outros gastos"].str.replace(",", ".").astype(float)

print(df_viagens["Valor diárias"]+ df_viagens["Valor passagens"])