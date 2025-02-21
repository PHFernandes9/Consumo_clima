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


# 2 Database

Primeriramente será utiliados os dados de consumo de energia elétrica, 
esses dadsos são disponibilizados no site da EPE (Empresa de Pesquisa Energética),
disponível nesse  [link](https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/consumo-de-energia-eletrica).
O consumo de energia é dividido por regiões do Brasil e será analsados do período de Janeiro de
2022 até Dezembro de 2024. Totalizando 36 meses de análise.

Para a temperatura será utilizada uma API(Aplication Programing Interface) chamada de 
Open Meteo. Que fará a coleta das médias das temperaturas de cada mês. Como existem mais de 5 mil municípios
no Brasil fica inviavél fazer a coleta da média de temperatura de cada um deles, dessa forma
será obitida apenas a média de temperatura das capitais das regiões. 


