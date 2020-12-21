import pandas as pd

formatura_banco_completo = pd.read_csv('/home/fernandoluismc/Documents/Formatura/Formatura FGA 2_2019.csv/Formatura FGA 2/2019.csv')
#print(formatura_banco_completo.columns)
#pd.set_option('display.max_rows', formatura_banco_completo.shape[0]+1)
Formatura_Aero = formatura_banco_completo[formatura_banco_completo['Curso'].isin(['Engenharia Aeroespacial'])]#fremont_weather[fremont_weather['month'].isin(['Jun','Jul','Aug'])])
#print(Formatura_Aero.columns)
print(len(Formatura_Aero))
print(Formatura_Aero[['Nome Completo','Curso','Telefone ','Username']])
Formatura_Aero.to_csv('/home/fernandoluismc/Documents/Formatura/Formatura FGA 2_2019.csv/Formatura FGA 2/2019_Aero.csv')