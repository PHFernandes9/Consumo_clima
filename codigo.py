import requests
from collections import defaultdict
import pandas as pd

df = pd.read_csv(r"C:\Projetos\Consumo_e_Temperatura\CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.csv")
df2 = pd.DataFrame(df)

resultados_totais = []

# Definição dos anos e meses
meses = list(range(1, 13))
anos = [2022, 2023, 2024]

# Dicionário com as regiões e coordenadas
regioes = {
    "Norte": {
        "Rio Branco": (-9.97, -67.81),
        "Macapá": (0.03, -51.07),
        "Manaus": (-3.10, -60.02),
        "Belém": (-1.46, -48.50),
        "Porto Velho": (-8.76, -63.90),
        "Boa Vista": (2.82, -60.67),
        "Palmas": (-10.24, -48.35),
    },
    "Nordeste": {
        "Sao Luis": (-2.53, -44.3),
        "Teresina": (-5.08, -42.8),
        "Fortaleza": (-3.71, -38.54),
        "Natal": (-5.79, -35.21),
        "Joao Pessoa": (-7.11, -34.84),
        "Recife": (-8.04, -34.87),
        "Maceió": (-9.66, -35.73),
        "Aracaju": (-10.94, -37.07),
        "Salvador": (-12.97, -38.50),
    },
    "Sudeste": {
        "Belo Horizonte": (-19.92, -43.94),
        "São Paulo": (-23.54, -46.63),
        "Rio de Janeiro": (-22.90, -43.20),
        "Vitória": (-22.32, -40.33),
    },
    "Sul": {
        "Curitiba": (-25.43, -49.27),
        "Florianópolis": (-27.60, -48.55),
        "Porto Alegre": (-30.03, -51.23),
    },
    "Centro-Oeste": {
        "Brasília": (-15.78, -47.93),
        "Goiânia": (-16.68, -49.25),
        "Campo Grande": (-20.45, -54.62),
        "Cuiabá": (-15.60, -56.10),
    },
}

# Loop para coletar as temperaturas por mês e ano
for ano in anos:
    for mes in meses:
        temperaturas_por_mes = defaultdict(list)  # Reinicializa a cada mês para evitar acúmulo indevido

        # Definição do primeiro e último dia do mês
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            ultimo_dia = 31
        elif mes == 2:
            ultimo_dia = 28
        else:
            ultimo_dia = 30

        primeiro_dia = f"{ano}-{mes:02d}-01"
        ultimo_dia = f"{ano}-{mes:02d}-{ultimo_dia}"

        print(f"\n🔍 Coletando dados para {ano}-{mes:02d}...")

        # Percorre todas as regiões
        for regiao, cidades in regioes.items():
            for cidade, (lat, lon) in cidades.items():
                url = "https://archive-api.open-meteo.com/v1/archive"
                params = {
                    "latitude": lat,
                    "longitude": lon,
                    "start_date": primeiro_dia,
                    "end_date": ultimo_dia,
                    "daily": "temperature_2m_max,temperature_2m_min",
                    "timezone": "America/Sao_Paulo",
                }

                response = requests.get(url, params=params)

                if response.status_code == 200:
                    data = response.json()
                else:
                    print(f"❌ Erro ao obter dados para {cidade} ({ano}-{mes:02d}): {response.status_code}")
                    continue  # Pula essa cidade se houver erro na requisição

                if "daily" in data and "temperature_2m_max" in data["daily"] and "temperature_2m_min" in data["daily"]:
                    temp_max = data["daily"]["temperature_2m_max"]
                    temp_min = data["daily"]["temperature_2m_min"]

                    if temp_max and temp_min:
                        # Cálculo da média de temperatura do mês
                        media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))
                        temperaturas_por_mes[regiao].append(media_temp)
                        print(f"✅ {cidade}: {round(media_temp, 2)}°C")
                    else:
                        print(f"⚠️ {cidade}: Dados vazios.")
                else:
                    print(f"⚠️ {cidade}: Dados ausentes no JSON.")

            # Calcula a média final da região para o mês e ano
            if temperaturas_por_mes[regiao]:  # Garante que existam dados antes de calcular
                media_geral = sum(temperaturas_por_mes[regiao]) / len(temperaturas_por_mes[regiao])
                resultados_totais.append({
                    'Data': f"{ano}-{mes}",
                    'Temperatura': round(media_geral, 2),
                    'Regiao': regiao
                })
                print(f"📊 Média mensal para {regiao}: {round(media_geral, 2)}°C")

# Salvar os resultados em um arquivo CSV
if resultados_totais:
    df_resultados = pd.DataFrame(resultados_totais)
    caminho_arquivo = r'C:\Projetos\Consumo_e_Temperatura\Temperatura_API.csv'
    df_resultados.to_csv(caminho_arquivo, index=False)
    print(f'\n📂 Dados exportados para o arquivo: {caminho_arquivo}')
else:
    print("\n⚠️ Nenhum dado coletado! Verifique os logs acima.")
