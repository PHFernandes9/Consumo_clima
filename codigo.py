
# import numpy as np
# import pandas as pd
# df = pd.read_csv("CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.csv")
# df2= pd.DataFrame(df)
# print(df)

#Bibliotecas------------------------------------------------------------------------

from itertools import count
import requests
from pyparsing import countedArray
from scipy.cluster.hierarchy import average

from collections import defaultdict

#-------------------------------------------------------------------------------

Dias_com_28 = list(range(1, 29))
Dias_com_30 = list(range(1, 31))
Dias_com_31 = list(range(1, 32))

Meses = list(range(1, 13))
Ano = [2022, 2023, 2024]

# Dicionário para armazenar o primeiro e o último dia de cada mês/ano
primeiro_ultimo_dia = defaultdict(tuple)

for k in Ano:
    for j in Meses:
        if j in [1, 3, 5, 7, 8, 10, 12]:
            dias = Dias_com_31
        elif j == 2:
            dias = Dias_com_28
        else:
            dias = Dias_com_30

        primeiro_ultimo_dia[(j, k)] = (f"{k}-{j:02d}-01", f"{k}-{j:02d}-{dias[-1]}")

# Exibindo os primeiros e últimos dias de cada mês
for (mes, ano), (primeiro, ultimo) in primeiro_ultimo_dia.items():

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": -19.92,  # Latitude de Belo Horizonte
        "longitude": -43.94, # Longitude de Belo Horizonte
        "start_date": f'{primeiro}',
        "end_date": f'{ultimo}',
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "America/Sao_Paulo"
    }

    response = requests.get(url, params=params)
    data = response.json()


    media=(sum(data["daily"]["temperature_2m_max"]) + sum(data["daily"]["temperature_2m_min"]))/(2*len(data["daily"]["temperature_2m_max"]))
    Vetor_temperatura=[]

    print(mes,'-',ano,round(media,2))
