import requests
from collections import defaultdict

# Definição dos anos e meses
meses = list(range(1, 13))
anos = [2022, 2023, 2024]

# Dicionário para armazenar as temperaturas agrupadas por (mês, ano)
temperaturas_por_mes = defaultdict(list)

# Definição das cidades do Sudeste (latitude, longitude)
sudeste = {
    "Belo Horizonte": (-19.92, -43.94),
    "São Paulo": (-23.54, -46.63),
    "Rio de Janeiro": (-22.90, -43.20),
    "Vitória": (-22.32, -40.33)
}

# Loop para coletar as temperaturas por mês e ano
for ano in anos:
    for mes in meses:
        # Definição do primeiro e último dia do mês
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            ultimo_dia = 31
        elif mes == 2:
            ultimo_dia = 28
        else:
            ultimo_dia = 30

        primeiro_dia = f"{ano}-{mes:02d}-01"
        ultimo_dia = f"{ano}-{mes:02d}-{ultimo_dia}"

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
        print(f"{mes}-{ano}: {round(media_geral, 2)}°C, Sudeste")
