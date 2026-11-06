# Mobilidade em Foco — parte individual

**Estudante:** Gabriel Maya Aguilar Assis  
**Tema:** Transporte público e deslocamento para o trabalho  
**Fonte:** IBGE, Censo Demográfico 2022 — Deslocamentos para trabalho e para estudo.

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

O painel tem três áreas: visão geral, exploração dos meios e método/interpretação. A base está em `data/transporte_trabalho_ibge_2022.csv`.

## O que foi calculado

Média, mediana, moda, quartis, intervalo interquartil (IQR), amplitude, desvio padrão e outliers dos percentuais dos meios de transporte. O painel também soma, de forma exploratória, os meios classificados como transporte público.

## Observação metodológica

O dado representa o meio que ocupava mais tempo no trajeto até o trabalho principal. Os percentuais são nacionais e vêm dos resultados preliminares da amostra do Censo 2022. A classificação de transporte público usada no painel é uma organização didática das categorias divulgadas pelo IBGE.
