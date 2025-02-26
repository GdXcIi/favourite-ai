import streamlit as st
import pandas as pd

# --- Styles CSS ---
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #3498db;
            font-weight: bold;
        }
        .github {
             max-width: 20%;
    </style>
""", unsafe_allow_html=True)

# --- Logo ---
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
with col3:
    st.image("Logo.png", width=50, use_container_width=True)

st.sidebar.image("Logo.png", width=25)
st.markdown("""
    <link rel="icon" href="logo.png" type="image/x-icon">
""", unsafe_allow_html=True)

# --- Titre ---
st.markdown("<h1 class='title'>Mes IA préférées...</h1>", unsafe_allow_html=True)

# --- Navbar ---
st.sidebar.title("Mes IA préférées")
page = st.sidebar.radio("Naviguer par catégories :", 
                        ["Générateurs de texte", "Générateurs d'images", "Générateurs de vidéos", 
                         "Détecteurs d'IA", "Traducteurs automatiques/autocorrecteurs", "Autres"])

# --- Contenu ---
if page == "Générateurs de texte":
    st.subheader("Générateurs de texte")
    data_texte = {
        "Nom": ["ChatGPT", "Le Chat", "Deepseek", "Llama", "Qwen", "Gemini", "Apple Intelligence"],
        "Entreprise": ["OpenAI", "Mistral AI", "-", "Meta", "-", "Google", "Apple"]
    }
    st.dataframe(pd.DataFrame(data_texte))

elif page == "Générateurs d'images":
    st.subheader("Générateurs d'images")
    data_images = {
        "Nom": ["ChatGPT", "Canva", "Pixlr", "Le Chat", "Apple Intelligence"],
        "Entreprise": ["OpenAI", "-", "-", "Mistral AI", "Apple"]
    }
    st.dataframe(pd.DataFrame(data_images))

elif page == "Générateurs de vidéos":
    st.subheader("Générateurs de vidéos")
    data_videos = {
        "Nom": ["Kapwing", "Sora"],
        "Entreprise": ["-", "OpenAI"]
    }
    st.dataframe(pd.DataFrame(data_videos))

elif page == "Détecteurs d'IA":
    st.subheader("Détecteurs d'IA")
    data_detect = {
        "Nom": ["Zero GPT (net)", "Zero GPT (com)", "Zero GPT (plus)", "Is Gen"],
        "Domaine": ["zerogpt.net", "zerogpt.com", "zerogpt.plus", "isgen.ai"]
    }
    st.dataframe(pd.DataFrame(data_detect))

elif page == "Traducteurs automatiques/autocorrecteurs":
    st.subheader("Traducteurs automatiques/autocorrecteurs")
    data_lang = {
        "Nom": ["DeepL", "Google Translate", "Microsoft Translator", "Apple Traduction", "Reverso"],
        "Entreprise": ["DeepL", "Google", "Microsoft", "Apple", "-"]
    }
    st.dataframe(pd.DataFrame(data_lang))

elif page == "Autres":
    st.subheader("Autres IA")
    data_others = {
        "Nom": ["Luma", "Suno"],
        "Entreprise": ["-", "-"]
    }
    st.dataframe(pd.DataFrame(data_others))

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>&copy; 2025 Guillaume DUPUIS</p>
    <a href='https://github.com/GdXcIi/favourite-ai'><img class='github' src='IMG_1658.png' alt='Dépôt GitHub'></a>
""", unsafe_allow_html=True)
