# Projeto Integrador — Mobilidade em Foco

**Estudante:** Gabriel Maya Aguilar Assis  
**Disciplina:** Python e Matemática  
**Indicador:** Meios de transporte usados no deslocamento para o trabalho  
**Recorte:** Brasil  
**Ano dos dados:** 2022

## 1. Objetivo

Analisar como as pessoas ocupadas chegam ao trabalho, destacando a participação do transporte público. A análise usa estatística descritiva para comparar os percentuais dos meios de transporte e observar a dispersão entre eles.

## 2. Fonte e cuidado na leitura

A base foi construída a partir da publicação do **IBGE — Censo Demográfico 2022: Deslocamentos para trabalho e para estudo**. O indicador considera o meio de transporte que ocupava mais tempo no trajeto até o trabalho principal. A pesquisa apresenta percentuais nacionais para automóvel, ônibus, caminhada, motocicleta, bicicleta, trem ou metrô e outros meios.

## 3. Resultados

O **automóvel** foi o meio mais utilizado, com **32,3%**. O **ônibus** foi o transporte público mais usado, com **21,4%**. Também aparecem trem ou metrô, van, mototáxi, táxi, BRT e embarcações.

Somando os modos classificados no painel como transporte público, chega-se a aproximadamente **26,3%** dos deslocamentos analisados. Esse resultado deve ser entendido como uma soma exploratória das categorias publicadas pelo IBGE, e não como um indicador separado criado pelo instituto.

Foram analisados 14 meios de transporte. A média dos percentuais foi de aproximadamente **7,14%** e a mediana foi **1,05%**. A diferença entre média e mediana acontece porque automóvel, ônibus, caminhada e motocicleta apresentam percentuais muito maiores que os demais meios.

O primeiro quartil foi **0,375%**, a mediana foi **1,05%** e o terceiro quartil foi **13,85%**. O intervalo interquartil foi **13,475 pontos percentuais**. A amplitude foi **32,2 pontos percentuais** e o desvio padrão amostral foi aproximadamente **10,45 pontos percentuais**.

## 4. Interpretação para apresentar

> “O automóvel é o meio de transporte mais usado para chegar ao trabalho, com 32,3%. Entre os meios coletivos, o ônibus é o principal, com 21,4%. Quando somamos os modos classificados no painel como transporte público, eles representam aproximadamente 26,3%. A média dos percentuais é maior que a mediana porque poucos meios concentram grande parte dos deslocamentos, enquanto vários outros têm participação pequena.”

## 5. Como o Python foi usado

O programa foi desenvolvido em **Python** com `pandas`, `numpy`, `plotly` e `streamlit`. O `pandas` organiza a base. O `numpy` apoia os cálculos estatísticos. O `plotly` cria gráficos interativos de barras e setores. O `streamlit` transforma a análise em um dashboard.

Os outliers foram calculados com a regra:

```text
IQR = Q3 - Q1
limite inferior = Q1 - 1,5 × IQR
limite superior = Q3 + 1,5 × IQR
```

## 6. Referências

[1]: https://agenciadenoticias.ibge.gov.br/media/com_mediaibge/arquivos/eb6833eb8d1aa7d4f77b9b38cd20fbdb.pdf "IBGE — Censo 2022: Deslocamentos para trabalho e para estudo"

[2]: https://educa.ibge.gov.br/jovens/materias-especiais/23064-censo-2022-como-a-populacao-se-desloca-para-estudar-e-trabalhar.html "IBGE Educa — Como a população se desloca para estudar e trabalhar"
