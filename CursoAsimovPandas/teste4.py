import pandas as pd

caminho_dados = "C:/Users/usuario/Documents/Programas/csv/2023_Viagem.csv"
pd.set_option('display.max_columns', None)
df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";", decimal=",")

df_viagens['Despesas'] = df_viagens['Valor diárias'] + df_viagens['Valor passagens'] + df_viagens['Valor outros gastos']

viagens_por_cargo = (df_viagens['Cargo'].value_counts(normalize=True) * 100).rename("Proporção de viagens").reset_index()

filtro_1pct = viagens_por_cargo['Proporção de viagens'] > 1
filtro_tec = viagens_por_cargo['Cargo'].str.startswith('TECNICO')

print(viagens_por_cargo[filtro_tec | filtro_1pct])