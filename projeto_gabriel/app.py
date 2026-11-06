from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Mobilidade em Foco | Gabriel Maya Aguilar Assis", page_icon="🚌", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--ink:#12233f;--muted:#65738b;--cyan:#17c3b2;--orange:#ff9f43;}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}.stApp{background:linear-gradient(135deg,#f7f9fc,#eef4f7);color:var(--ink)}
h1,h2,h3{font-family:'Space Grotesk',sans-serif!important;color:var(--ink)!important}.hero{background:linear-gradient(120deg,#12233f,#1c3f5b 60%,#087f8c);padding:2.2rem 2.5rem;border-radius:24px;color:white;margin-bottom:1.2rem;box-shadow:0 14px 30px rgba(18,35,63,.16)}
.hero h1{color:white!important;font-size:2.6rem;margin:0 0 .3rem;letter-spacing:-.05em}.hero p{color:#d9edf0;font-size:1rem;margin:0}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:#85eee2;margin-bottom:.6rem}
.card{background:rgba(255,255,255,.9);border:1px solid #e2e9f0;border-radius:18px;padding:1rem 1.1rem;min-height:112px;box-shadow:0 5px 18px rgba(18,35,63,.05)}.card-label{color:var(--muted);font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em}.card-value{color:var(--ink);font-family:'Space Grotesk';font-size:1.75rem;font-weight:700;margin-top:.4rem}.card-note{color:#7e8b9e;font-size:.76rem;margin-top:.25rem}.section-note{color:var(--muted);font-size:.92rem;margin:-.5rem 0 1rem}.insight{background:#fff8ed;border-left:5px solid var(--orange);padding:1rem 1.1rem;border-radius:12px;color:#684a27;line-height:1.5}.source{color:#77869c;font-size:.78rem;margin-top:.7rem}[data-testid="stSidebar"]{background:#12233f}[data-testid="stSidebar"] *{color:#edf7f7!important}
</style>
""", unsafe_allow_html=True)

DATA_PATH = Path(__file__).parent / "data" / "transporte_trabalho_ibge_2022.csv"

@st.cache_data
def carregar_dados():
    return pd.read_csv(DATA_PATH)

def pct(v): return f"{v:.1f}%".replace('.', ',')

def calcular_estatisticas(serie):
    x = serie.astype(float).dropna(); q1=x.quantile(.25); q2=x.quantile(.5); q3=x.quantile(.75); iqr=q3-q1
    return {'n':len(x),'media':x.mean(),'mediana':x.median(),'moda':x.mode().iloc[0],'q1':q1,'q2':q2,'q3':q3,'iqr':iqr,'amplitude':x.max()-x.min(),'desvio_padrao':x.std(ddof=1),'limite_inf':q1-1.5*iqr,'limite_sup':q3+1.5*iqr}

df=carregar_dados(); stats=calcular_estatisticas(df['percentual'])
coletivo=df[df['categoria']=='Transporte público']; coletivo_total=coletivo['percentual'].sum()

st.markdown("""<div class="hero"><div class="eyebrow">Projeto Integrador · Python + Matemática</div><h1>Mobilidade em Foco</h1><p>Como os brasileiros chegam ao trabalho? Um olhar sobre o transporte público no Censo 2022.</p></div>""", unsafe_allow_html=True)
st.sidebar.markdown("## Navegação")
aba=st.sidebar.radio("Ir para", ["Visão geral", "Explorar meios", "Método e interpretação"])
st.sidebar.markdown("---")
st.sidebar.markdown("**Estudante**  \nGabriel Maya Aguilar Assis")
st.sidebar.markdown("**Fonte**  \nIBGE · Censo 2022")

if aba == "Visão geral":
    st.markdown("### Um retrato da mobilidade brasileira")
    st.markdown("<p class='section-note'>Indicador analisado: percentual de pessoas ocupadas, de 10 anos ou mais, segundo o meio que mais utilizavam no deslocamento para o trabalho.</p>", unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    cards=[(c1,'Transporte público',pct(coletivo_total),'soma dos modos coletivos'),(c2,'Ônibus',pct(float(df.loc[df['meio_transporte']=='Ônibus','percentual'].iloc[0])),'principal coletivo'),(c3,'Maior percentual',pct(df['percentual'].max()),'automóvel'),(c4,'Meios analisados',str(len(df)),'categorias na base')]
    for col,label,value,note in cards:
        with col: st.markdown(f"<div class='card'><div class='card-label'>{label}</div><div class='card-value'>{value}</div><div class='card-note'>{note}</div></div>",unsafe_allow_html=True)
    left,right=st.columns([1.2,1])
    with left:
        st.markdown('### Meios de transporte mais usados')
        ordem=df.sort_values('percentual',ascending=True)
        fig=px.bar(ordem,x='percentual',y='meio_transporte',orientation='h',color='categoria',color_discrete_map={'Transporte público':'#17c3b2','Individual motorizado':'#ff9f43','Ativo':'#5975d9','Outros':'#9aa8b8'},labels={'percentual':'Percentual (%)','meio_transporte':''})
        fig.update_layout(height=650,margin=dict(l=0,r=10,t=10,b=10),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(color='#12233f'),legend_title_text='Categoria')
        fig.update_xaxes(ticksuffix='%',gridcolor='#e7edf2'); fig.update_yaxes(categoryorder='array',categoryarray=ordem['meio_transporte'].tolist())
        st.plotly_chart(fig,use_container_width=True)
    with right:
        st.markdown('### Transporte público em destaque')
        pizza=px.pie(coletivo,names='meio_transporte',values='percentual',hole=.55,color_discrete_sequence=['#17c3b2','#087f8c','#ff9f43','#5975d9','#9aa8b8'])
        pizza.update_layout(height=350,margin=dict(l=0,r=0,t=0,b=0),paper_bgcolor='rgba(0,0,0,0)',showlegend=True)
        st.plotly_chart(pizza,use_container_width=True)
        st.markdown(f"<div class='insight'><b>Leitura principal:</b> o ônibus é o transporte público mais utilizado, com 21,4%. Somando ônibus, trem/metrô, vans, mototáxi, táxi, BRT e embarcações, os modos coletivos representam aproximadamente <b>{pct(coletivo_total)}</b> dos deslocamentos analisados.</div>",unsafe_allow_html=True)

elif aba == "Explorar meios":
    st.markdown('### Explore os meios de transporte')
    st.markdown("<p class='section-note'>Selecione uma categoria para comparar seus meios e enxergar a participação do transporte público.</p>",unsafe_allow_html=True)
    categoria=st.selectbox('Filtrar por categoria',['Todas','Transporte público','Individual motorizado','Ativo','Outros'])
    view=df if categoria=='Todas' else df[df['categoria']==categoria]
    col1,col2=st.columns(2)
    with col1: st.metric('Percentual da seleção',pct(view['percentual'].sum()))
    with col2: st.metric('Maior meio da seleção',view.loc[view['percentual'].idxmax(),'meio_transporte'])
    tabela=view.rename(columns={'meio_transporte':'Meio de transporte','percentual':'Percentual (%)','quantidade_milhoes':'Pessoas (milhões)','categoria':'Categoria'}).sort_values('Percentual (%)',ascending=False)
    st.dataframe(tabela,use_container_width=True,hide_index=True,column_config={'Percentual (%)':st.column_config.NumberColumn(format='%.1f%%'),'Pessoas (milhões)':st.column_config.NumberColumn(format='%.1f')})
    st.download_button('Baixar dados em CSV',view.to_csv(index=False).encode('utf-8'),'transporte_trabalho_ibge_2022.csv','text/csv')

else:
    st.markdown('### Método e interpretação')
    st.markdown("<p class='section-note'>Aqui estão os cálculos estatísticos e uma explicação simples para a apresentação.</p>",unsafe_allow_html=True)
    m1,m2=st.columns(2)
    with m1:
        st.markdown('#### Estatísticas dos percentuais')
        resumo=pd.DataFrame({'Medida':['Média','Mediana','Moda','Q1','Q2','Q3','IQR','Amplitude','Desvio padrão'],'Resultado':[pct(stats['media']),pct(stats['mediana']),pct(stats['moda']),pct(stats['q1']),pct(stats['q2']),pct(stats['q3']),pct(stats['iqr']),pct(stats['amplitude']),pct(stats['desvio_padrao'])]})
        st.dataframe(resumo,hide_index=True,use_container_width=True)
    with m2:
        st.markdown('#### Como interpretar')
        st.markdown(f"""- **Média:** {pct(stats['media'])} entre os meios analisados.
- **Mediana:** {pct(stats['mediana'])}; metade dos meios tem percentual até esse valor.
- **Quartis:** Q1 = {pct(stats['q1'])}, Q2 = {pct(stats['q2'])} e Q3 = {pct(stats['q3'])}.
- **IQR:** {pct(stats['iqr'])}; mostra a dispersão dos 50% centrais.
- **Amplitude:** {pct(stats['amplitude'])}, diferença entre automóvel e embarcação de médio/grande porte.
- **Outliers:** pelo critério de Tukey, os percentuais acima de {pct(stats['limite_sup'])} são destacados.""")
    st.markdown(f"<div class='insight'><b>Conclusão para apresentar:</b> o transporte público é importante, mas o ônibus concentra a maior parte dos deslocamentos coletivos. O automóvel aparece como o meio mais usado no total, com 32,3%, enquanto o transporte coletivo somado representa {pct(coletivo_total)}. A mediana ajuda a comparar os meios sem deixar que os maiores percentuais dominem toda a leitura.</div>",unsafe_allow_html=True)
    st.markdown("<p class='source'>Fonte: IBGE, Censo Demográfico 2022 — Deslocamentos para trabalho e para estudo, resultados preliminares da amostra. O meio considerado é aquele em que a pessoa passava mais tempo no trajeto.</p>",unsafe_allow_html=True)
