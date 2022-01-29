import streamlit as st


def front():
    text = """
            # Comparardor de similitudes en títulos de canciones  

            Usando el top 100 de la bilboard sacaremos la sumilitud de sus titulos usando el modelo
            https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2

  
            """
    st.write(text)

    image_huggingface_url = "https://avatars.githubusercontent.com/u/25720743?s=200"
    st.image(image_huggingface_url)

    text = "HuggingFace"
    url = "https://huggingface.co/"
    link = "[%s](%s)" % (text, url)
    st.write(link)