
# EDA-Econ: Análise Exploratória de Dados Econômicos

Este projeto oferece uma aplicação interativa usando **Streamlit** para análise exploratória de indicadores macroeconômicos por país e continente. O painel permite a seleção de ano e variáveis para visualização dinâmica de dados como crescimento do PIB, inflação, taxa de juros real e taxa de câmbio efetiva real (REER).

---

## 📁 Estrutura do Projeto

```
eda-econ/
├── app.py                 # Aplicação Streamlit
├── eda_report.py         # Funções de carregamento, tratamento e fusão de dados
├── data.csv              # Dataset principal com indicadores macroeconômicos
├── continents.csv        # Mapeamento de países para continentes
├── requirements.txt      # Dependências do projeto
├── __main__.py           # Alternativa para execução do projeto como pacote
└── README.md             # (Este arquivo)
```

---

## 🚀 Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/eda-econ.git
cd eda-econ
```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # no Windows use `venv\Scripts\activate`
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
streamlit run app.py
```

---

## 📊 Funcionalidades

- **Visualização interativa** de variáveis macroeconômicas por continente e ano.
- **Boxplots** comparativos por continente.
- **Gráficos de dispersão** entre variáveis selecionadas.
- Filtros laterais para selecionar o **ano** e as **variáveis** X e Y.

---

## 📦 Dados Utilizados

- **data.csv**: Indicadores econômicos por país e ano.
- **continents.csv**: Relacionamento país–continente.

As variáveis disponíveis são:
- `gdp_growth`: Crescimento do PIB
- `inflation`: Inflação
- `real_interest_rate`: Taxa de juros real
- `reer`: Taxa de câmbio efetiva real

---

## 🧠 Tecnologias

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [Python 3.7+](https://www.python.org/)

---