# REPOSITÓRIO DE ANÁLISE DE DADOS DE PAULO HENRIQUE


# 1 Introdução



Segundos dados da ONS, em Janeiro e Fevereiro de 2025, bateram recorde de consumo de
energia elétrica. No dia 12/02 atingiu-se a marca 103.785 MW. Este é o terceiro recorde do ano, superando as 
marcas anteriores de 11/02 (103.335 MW) e 22/01 (102.810 MW). Esse aumento se deve pricinpalmente
as altas temperaturas registradas no país. 

Mas qual é a relação entre a temperatura e o consumo de energia elétrica ? 

O gráfico da Figura 1 possível ver  os aparelhos e dispositivos que mais consomem 
energia elétrica.



![Imagem](https://raw.githubusercontent.com/PHFernandes9/Consumo_clima/refs/heads/main/consumo.png)
                            Figura 1


Durante a época de calor, aumenta o uso  de apartelhos como ventiladores 
e ares condicionados, esse último conforme mostrado no gráfico é principal 
vilão para o consumo tão alto de energia elétrica. Por causa da sua estrutura
de funcionamento o ar-condiconado consome mais energia que qualquer outro aparelho.
Em decorrência das altas temperaturas principais no comercio o uso se torna bem maior.


# 2 Metodologia 
## 2.1 Database

Primeriramente será utiliados os dados de consumo de energia elétrica, 
esses dadsos são disponibilizados no site da EPE (Empresa de Pesquisa Energética),
disponível nesse  [link](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/consumo-de-energia-eletrica).
O consumo de energia é dividido por regiões do Brasil e será analsados do período de Janeiro de
2022 até Dezembro de 2024. Totalizando 36 meses de análise.

| Regiao       | Consumo(Kw) | Data |
|--------------|-------------|--|
| Norte        | 3033623     | 2022-01 |
| Nordeste     |7269935| 2022-01 |
| Sudeste      |20526803| 2022-01  |
| Sul          |8495715|  2022-01 |
| Centro-Oeste |3254143|  2022-01 |


## 2.2 API 
Para a temperatura será utilizada uma API(Aplication Programing Interface) chamada de 
Open Meteo, que é uma API gratuita com dados históricos. Que fará a coleta das médias das temperaturas de cada mês. Como existem mais de 5 mil municípios
no Brasil fica inviavél fazer a coleta da média de temperatura de cada um deles, dessa forma
será obitida apenas a média de temperatura das capitais das regiões. 

## 2.3 Obtenção das temperaturas
Primeiramente para se usar a Open Meteo, irá se precisar dos dados de longitude e
latidude de cada capital, Conforme mostrado na Tabela 1.

| Cidade          | Latitude  | Longitude  |
|--------------- |----------|------------|
| Belo Horizonte | -19.92   | -43.94     |
| São Paulo      | -23.54   | -46.63     |
| Rio de Janeiro | -22.90   | -43.20     |
| Vitória        | -22.32   | -40.33     |
| São Luís       | -2.53    | -44.30     |
| Teresina       | -5.08    | -42.80     |
| Fortaleza      | -3.71    | -38.54     |
| Natal          | -5.79    | -35.21     |
| João Pessoa    | -7.11    | -34.84     |
| Recife        | -8.04    | -34.87     |
| Maceió         | -9.66    | -35.73     |
| Aracaju        | -10.94   | -37.07     |
| Salvador       | -12.97   | -38.50     |
| Rio Branco     | -9.97    | -67.81     |
| Macapá         | 0.03     | -51.07     |
| Manaus         | -3.10    | -60.02     |
| Belém          | -1.46    | -48.50     |
| Porto Velho    | -8.76    | -63.90     |
| Boa Vista      | 2.82     | -60.67     |
| Palmas         | -10.24   | -48.35     |
    | Curitiba       | -25.43   | -49.27     |
    | Florianópolis  | -27.60   | -48.55     |
    | Porto Alegre   | -30.03   | -51.23     |
    | Goiânia        | -16.68   | -49.25     |
    | Campo Grande   | -20.45   | -54.62     |
    | Cuiabá         | -15.60   | -56.10     |

Primeiro foi preciso criar um __for__ que irá interar para pegar o primeiro e o último
dia do mês

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

Após isso será passados os valores de primeiro e ultimo dia nos parâmetros da url.

        for cidade, (lat, lon) in sudeste.items():
                params = {
                "latitude": lat,
                "longitude": lon,
                "start_date": primeiro_dia,
                "end_date": ultimo_dia,
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "America/Sao_Paulo"
            }

  Será pego os valores de temperatura máxima e mínima de cada cidade e armazenados
nas variaveis de temp_max e temp_min.
   
            if "daily" in data:
                temp_max = data["daily"]["temperature_2m_max"]
                temp_min = data["daily"]["temperature_2m_min"]

                # Cálculo da média de temperatura do mês
                media_temp = (sum(temp_max) + sum(temp_min)) / (2 * len(temp_max))


                temperaturas_por_mes[(mes, ano)].append(media_temp)

Após isso será agregado as temperaturas por mês. (Exemplo 2022-01,2022-02 ....) 

        for (mes, ano), temperaturas in temperaturas_por_mes.items():
            media_geral = sum(temperaturas) / len(temperaturas)
            resultados_totais.append({
                'Data': f"{ano}-{mes}",
                'Temperatura': round(media_geral, 2),
                'Regiao':'Centro-Oeste'
            })
Apos isso é feito para cada região posteriormente. Por útlimo os dados serão exportados 
em formato CSV. 
    
        if resultados_totais:
        df_resultados = pd.DataFrame(resultados_totais)
        caminho_arquivo = r'C:\Projetos\Consumo_e_Temperatura\Novo_Temperatura_API.csv'
        df_resultados.to_csv(caminho_arquivo, index=False)
        print(f'\n📂 Dados exportados para o arquivo: {caminho_arquivo}')
    else:
        print("\n⚠️ Nenhum dado coletado! Verifique os logs acima.")

# Resultados