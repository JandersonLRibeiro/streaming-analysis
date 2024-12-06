# Carregando os pacotes
import streamlit as st
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Função para carregar e limpar o dataset
@st.cache_data
def load_data():
    df_netflix = pd.read_csv("dataset/netflix_titles.csv")

    # Preenchendo as colunas que estão em branco
    df_netflix["director"] = df_netflix["director"].fillna("Unknown")
    df_netflix["cast"] = df_netflix["cast"].fillna("Unknown")
    df_netflix["description"] = df_netflix["description"].fillna("No description available!")
    df_netflix["listed_in"] = df_netflix["listed_in"].fillna("Uncategorized")

    # Removendo duplicatas
    df_netflix.drop_duplicates(subset="title", inplace=True)

    # Consolidando as informações das colunas "description", "cast", "director" e "listed_in" em uma única coluna.
    df_netflix["combined_features"] = (df_netflix["description"]+" "+
                                   df_netflix["cast"]+" "+
                                   df_netflix["director"]+" "+
                                   df_netflix["listed_in"]
                                  )

    return df_netflix

# Função para criar o sistema de recomendação
def get_recommendations(title, cosine_sim, df):
    
    # Obter o índice do filme a partir do título
    indices = pd.Series(df.index, index=df["title"]).drop_duplicates()
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
    return df["title"].iloc[movie_indices].tolist()

# Apliicativo no Streamlit
def main():
    st.title("Sistema de Recomendação de Filmes e Séries 🎥")
    st.write("Digite ou selecione um título para obter recomendações.")

    # Chamando a função para  carregar os dados
    df = load_data()

    # Criando a matriz TF-IDF
    tfidf = TfidfVectorizer(stop_words = "english")
    matrix = tfidf.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(matrix, matrix)

    # Campo para seleção de título
    title = st.selectbox("Selecione um título:", df["title"].unique())

    # Botão para gerar recomendações
    if st.button("Mostrar recomendações"):
        recommendations = get_recommendations(title, cosine_sim, df)
        st.write("Filmes/Séries recomendados:")
        for rec in recommendations:
            st.write(f" - {rec}")

if __name__ =="__main__":
    main()
