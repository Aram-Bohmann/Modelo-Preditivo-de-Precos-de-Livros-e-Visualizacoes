import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Carregando Dados e configurando Streamlit
df = pd.read_csv("dataset/livros.csv")

st.title("Modelo Preditivo de Preço de Livros")
st.subheader("1. Visualização dos dados usados:")
st.dataframe(df)

# 2. Tratando Dados
df["pages"] = (
    df["pages"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)

transformando_em_numero = ["numRatings", "rating", "price"]
for col in transformando_em_numero:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["rating", "pages", "numRatings", "price"])


# 3. PREPARAÇÃO PARA O MODELO
st.subheader("2. Treinando o modelo")

caracteristica = df[["rating", "pages", "numRatings"]]
alvo = df["price"]

# Dividindo dados para treino e teste
caracteristica_train, caracteristica_test, alvo_train, alvo_test = train_test_split(
    caracteristica, alvo, test_size=0.2, random_state=42
)

st.write(f"Tamanho do treino: {len(caracteristica_train)} linhas")
st.write(f"Tamanho do teste: {len(caracteristica_test)} linhas")


# 4. Treinando o Modelo Preditivo
modelinho = LinearRegression()
modelinho.fit(caracteristica_train, alvo_train)

# Previsão com dados de teste
previsao = modelinho.predict(caracteristica_test)

# Avaliação
mse = mean_squared_error(alvo_test, previsao)
st.write(f"Erro Médio Quadrático (MSE): {mse:.4f}")


# 5. Usando Streamlit para criar uma interface para o imput de dados:
st.subheader("3. Descubra o preço do Livro!")

nota_input = st.number_input("Nota do Livro:", value=4.0, step=0.01)
pages_input = st.number_input("Número de páginas:", value=300)
numRatings_input = st.number_input("Número de avaliações feitas:", value=10000)

if st.button("Prever o preço"):
    new_data = pd.DataFrame({
        "rating": [nota_input],
        "pages": [pages_input],
        "numRatings": [numRatings_input],
    })

    prediction = modelinho.predict(new_data)[0]
    st.success(f" O Preço previsto foi de: ${prediction:.2f} doláres!")