# Carregando os pacotes
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Função para carregar
@st.cache_data
def load_data():
    return pd.read_csv("dataset/system_recommendation.csv")

# Função de recomendação
def get_recommendations(title, cosine_sim, df):

    # Carregar os dados
    df = load_data()

    # Obter o índice do filme a partir do título
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    if title not in indices:
        return ["Título não encontrado. Por favor, tente outro."]   
    idx = indices[title]

    # Para obter a similaridade do filme fornecido com todos os outros
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Retorna uma lista ordenada de tuplas com os índices e similaridades de 5 títulos
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    # Para selecionar os índices dos 5 filmes mais similares
    movie_indices = [i[0] for i in sim_scores]

    # Retorna a lista com os títulos dos filmes mais similares ao título fornecido
    recommendations = df.iloc[movie_indices][['title', 'platform']].reset_index(drop=True)
    return recommendations

# Construção do aplicativo no Streamlit
def main():
    st.title("Sistema de Recomendação Multiplataforma 🎥")
    st.write("Escolha a plataforma e o filme para obter recomendações de todas as plataformas.")

    # Carregar os dados
    df = load_data()

    # Criando a matriz TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(df['combined_features'])
    cosine_sim = cosine_similarity(matrix, matrix)

    # Escolher a plataforma
    platform = st.selectbox("Selecione uma plataforma inicial:", df['platform'].unique())

    # Filtrar títulos pela plataforma escolhida
    filtered_df = df[df['platform'] == platform]
    title = st.selectbox("Selecione um título:", filtered_df['title'].unique())

    # Botão para gerar recomendações
    if st.button("Mostrar recomendações"):
        recommendations = get_recommendations(title, cosine_sim, df)
        st.write("Filmes/Séries recomendados::")
        st.table(recommendations)

# Rodar o aplicativo
if __name__ == "__main__":
    main()