# import numpy as np
# import pandas as pd
# df = pd.read_csv("CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.csv")
# df2= pd.DataFrame(df)
# print(df)
from itertools import count

import requests
from pyparsing import countedArray
from scipy.cluster.hierarchy import average

Dias_com_31=[1,2,3,4,5,6,7,8,9,10,11,12,13,
14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

Dias_com_30=[1,2,3,4,5,6,7,8,9,10,11,12,13,
14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

Dias_com_28=[1,2,3,4,5,6,7,8,9,10,11,12,13,
14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

Meses = [1,2,3,4,5,6,7,8,9,10,11,12]

Ano = [2022,2023,2024]

inicio='2022-12-01'
fim='2022-12-31'


url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": -19.92,  # Latitude de Belo Horizonte
    "longitude": -43.94, # Longitude de Belo Horizonte
    "start_date": f'{inicio}',
    "end_date": f'{fim}',
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)
data = response.json()

media=(sum(data["daily"]["temperature_2m_max"]) + sum(data["daily"]["temperature_2m_min"]))/(2*len(data["daily"]["temperature_2m_max"]))

print(media)
