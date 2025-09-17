import pandas as pd

caminho_dados = "C:/Users/usuario/Documents/Programas/csv/2023_Viagem.csv"
pd.set_option('display.max_columns', None)
df_viagens = pd.read_csv(caminho_dados, encoding="Windows-1252", sep=";", decimal=",")

df_viagens['Despesas'] = df_viagens['Valor diárias'] + df_viagens['Valor passagens'] + df_viagens['Valor outros gastos']

viagens_por_cargo = (df_viagens['Cargo'].value_counts(normalize=True) * 100).rename("Proporção de viagens").reset_index()
filtro_1pct = viagens_por_cargo['Proporção de viagens'] > 1
filtro_tec = viagens_por_cargo['Cargo'].str.startswith('TECNICO')
filtro_1m = df_viagens['Despesas'] > 100000
df_viagens['Cargo'] = df_viagens['Cargo'].fillna("NÃO IDENTIFICADO")

df_viagens['Período - Data de início'] = pd.to_datetime(df_viagens['Período - Data de início'], format = '%d/%m/%Y')
df_viagens['Período - Data de fim'] = pd.to_datetime(df_viagens['Período - Data de fim'], format = '%d/%m/%Y')

df_viagens['Mês da viagem'] = df_viagens['Período - Data de início'].dt.month_name()
df_viagens['Dias da viagem'] = (df_viagens['Período - Data de fim'] - df_viagens['Período - Data de início']).dt.days

gastos_totais_cargo = df_viagens.groupby('Cargo')['Despesas'].mean().reset_index()

df_viagens_consolidado = (df_viagens.groupby('Cargo').agg(
            despesa_media=('Despesas', 'mean') , 
            duracao_media=("Dias da viagem", "mean"),
            despesas_totais=('Despesas', 'sum'),
            destino_mais_frequente=('Destinos', pd.Series.mode),
            n_viagens=('Nome', 'count')
            ).reset_index())

df_cargos = df_viagens['Cargo'].value_counts(normalize=True).reset_index()
print(df_cargos.loc[df_cargos['proportion'] > 0.01])

cargos_relevantes = df_cargos.loc[df_cargos['proportion'] > 0.01, 'Cargo']

filtro = df_viagens_consolidado['Cargo'].isin(cargos_relevantes)

print(df_viagens_consolidado[filtro])