# **🎥 Análise de Plataformas de Streaming e Sistema de Recomendação Multiplataforma**

Este repositório contém dois projetos complementares que ajudam usuários a explorar e escolher serviços de streaming de forma eficiente:

1️⃣ **Dashboard em Power BI**: Uma ferramenta para famílias que buscam comparar plataformas de streaming e tomar decisões informadas.

2️⃣ **Sistema de Recomendação**: Um aplicativo interativo desenvolvido em Python (usando Streamlit) que sugere filmes e séries com base em preferências.

## **📊 Parte 1: Dashboard em Power BI**

### **Contexto**

Sou um freelancer de desenvolvimento de software BI em início de carreira, buscando criar projetos impactantes e úteis. Identifiquei que hoje, com tantas opções de serviços de streaming disponíveis, famílias enfrentam dificuldades para decidir qual plataforma assinar.

Este dashboard foi criado com o objetivo de:

- **Facilitar a decisão** sobre qual serviço de streaming assinar, com base em preferências individuais ou familiares;

- **Disponibilizar informações claras e visualmente atraentes** para ajudar na comparação entre Netflix, Disney+, Amazon Prime e Hulu.

### **O Projeto**

- O dashboard foi desenvolvido para familiares ou pequenos grupos que desejam otimizar suas escolhas de assinaturas;

- Ele compara os catálogos das plataformas com base em gêneros, classificações de conteúdo e avaliações;

- Além disso, inclui uma análise geral para identificar as diferenças e os destaques de cada serviço.

### **Ferramentas Utilizadas**

- Jupyter Notebook: Para o tratamento dos dados e preparação do arquivo final;
- Power BI: Para a construção de visualizações dinâmicas e interativas.

### **Visualização**

<p align="center">
  <img src="https://github.com/JandersonLRibeiro/streaming-analysis/blob/main/assets/PBIDesktop_YVC79hvJpZ.gif" alt="PBI">
</p>

## **🤖 Parte 2: Sistema de Recomendação Multiplataforma**

### **O Que é?**

Um sistema de recomendação interativo que sugere filmes e séries da Netflix `Aplicativo 1`  ou de qualquer uma das quatro plataformas de streaming (Netflix, Disney+, Amazon Prime e Hulu) `Aplicativo 2`. O sistema é baseado em técnicas avançadas de Machine Learning para análise de texto.

### **Como Funciona?**

1️⃣ O usuário escolhe uma plataforma inicial (por exemplo, Netflix);

2️⃣ Seleciona um filme ou série que gostou;

3️⃣ O sistema retorna até 5 títulos similares.

### **O Algoritmo**
O sistema foi desenvolvido com o algoritmo TF-IDF (Term Frequency-Inverse Document Frequency), que mede a relevância de palavras no texto. Aqui está um resumo técnico:

- **Matriz TF-IDF:**

    - Converte o texto (descrições, elenco, diretor e gêneros) em vetores numéricos;

    - As palavras mais importantes recebem maior peso, enquanto palavras comuns como "o", "de", ou "e" são desconsideradas.

- **Cálculo da Similaridade:**

    - Utiliza a **similaridade do cosseno**, que mede o ângulo entre os vetores gerados pela matriz TF-IDF.

    - Resultado:
        - 1 → Filmes completamente similares.
        - 0 → Filmes sem relação.
- **Otimização:**

    - Similaridades calculadas sob demanda para evitar sobrecarga de memória.
    - Matriz TF-IDF armazenada em formato esparso para reduzir consumo de recursos.
### **Ferramentas Utilizadas**

- **Python:**
    - `pandas` e `numpy`: para manipulação e análise dos dados;
    - `sklearn`: para criação da matriz TF-IDF e cálculo de similaridade;
    - `Streamlit`: para desenvolvimento de uma interface interativa.
  
## **🚀 Como Rodar o Projeto**

### **Dashboard Power BI**

1️⃣ Abra o arquivo .pbix no Power BI Desktop;

2️⃣ Explore as páginas do dashboard e interaja com os filtros disponíveis.

### **Sistema de Recomendação**

1️⃣ Clone este repositório:

``` 
git clone https://github.com/JandersonLRibeiro/streaming-analysis.git

```

2️⃣ Execute o aplicativo Streamlit:

```
streamlit run streamlit_app_v1.py

```
```
streamlit run streamlit_app_v2.py
```

