import requests
from collections import defaultdict
import pandas as pd
import numpy as np
df = pd.read_csv("C:\Projetos\Consumo_e_Temperatura\CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.csv")
df2= pd.DataFrame(df)


resultados_totais=[]

# Definição dos anos e meses
meses = list(range(1, 13))
anos = [2022, 2023, 2024]

# Dicionário para armazenar as temperaturas agrupadas por (mês, ano)

# Definição das capitais das 5 regioes (latitude, longitude)
sudeste = {
            "Belo Horizonte": (-19.92, -43.94),
            "São Paulo": (-23.54, -46.63),
            "Rio de Janeiro": (-22.90, -43.20),
            "Vitória": (-22.32, -40.33)
}

Nordeste = {"Sao Luis": (-2.53, -44.3),
            "Teresina ":(-5.08, -42.8),
            "Fortaleza": (-3.71,-38.54),
            "Natal" :(-5.79,-35.21),
            "Joao Pessoa": (-7.11,-34.84),
            "Recife": (-8.04,-34.87),
            "Maceió": (-9.66,-35.73),
            "Aracaju": (-10.94,-37.07),
            "Salvador":(-12.97, -38.50)
}

Norte = {
            "Rio Branco": (-9.97, -67.81),
            "Macapá": (0.03, -51.07),
            "Manaus": (-3.10, -60.02),
            "Belém": (-1.46, -48.50),
            "Porto Velho": (-8.76, -63.90),
            "Boa Vista": (2.82, -60.67),
            "Palmas": (-10.24, -48.35)
}

Sul = {
            "Curitiba": (-25.43, -49.27),
            "Florianópolis": (-27.60, -48.55),
            "Porto Alegre": (-30.03, -51.23)
}

Centro_Oeste = {
            "Brasília": (-15.78, -47.93),
            "Goiânia": (-16.68, -49.25),
            "Campo Grande": (-20.45, -54.62),
            "Cuiabá": (-15.60, -56.10)
}
# Loop para coletar as temperaturas por mês e ano
for ano in anos:
    for mes in meses:
        temperaturas_por_mes = defaultdict(list)  # Reinicia o dicionário para evitar acumulação
        # Definição do primeiro e último dia do mês
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            ultimo_dia = 31
        elif mes == 2:
            ultimo_dia = 28
        else:
            ultimo_dia = 30

        primeiro_dia = f"{ano}-{mes:02d}-01"
        ultimo_dia = f"{ano}-{mes:02d}-{ultimo_dia}"

        for cidade, (lat, lon) in Norte.items():
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))

                # Armazena no dicionário
                temperaturas_por_mes[(mes, ano)].append(media_temp)
        # Calcula a média final por mês e ano
        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao': 'Norte'
            })

        for cidade, (lat, lon) in Nordeste.items():
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))

                # Armazena no dicionário
                temperaturas_por_mes[(mes, ano)].append(media_temp)

        # Calcula a média final por mês e ano
        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao': 'Nordeste'
            })

        for cidade, (lat, lon) in sudeste.items():
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))

                # Armazena no dicionário
                temperaturas_por_mes[(mes, ano)].append(media_temp)

        # Calcula a média final por mês e ano
        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao': 'Sudeste'
            })

        for cidade, (lat, lon) in Sul.items():
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))

                # Armazena no dicionário
                temperaturas_por_mes[(mes, ano)].append(media_temp)

        # Calcula a média final por mês e ano
        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao': 'Sul'
        })

        for cidade, (lat, lon) in Centro_Oeste.items():
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

            response = requests.get(url, params=params)
            data = response.json()

            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))

                # Armazena no dicionário
                temperaturas_por_mes[(mes, ano)].append(media_temp)

            # Calcula a média final por mês e ano
        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao':'Centro-Oeste'
            })
        print(f"Aqui - Centro-Oeste")

if resultados_totais:
    df_resultados = pd.DataFrame(resultados_totais)
    caminho_arquivo = r'C:\Projetos\Consumo_e_Temperatura\Novo_Temperatura_API.csv'
    df_resultados.to_csv(caminho_arquivo, index=False)
    print(f'\n📂 Dados exportados para o arquivo: {caminho_arquivo}')
else:
    print("\n⚠️ Nenhum dado coletado! Verifique os logs acima.")
