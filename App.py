import streamlit as st
import pandas as pd

# --- Styles CSS ---
st.markdown("""
    <style>
        body {
            background-color: #C7D2D7;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #BBC9D1;
            color: white;
            text-align: center;
            padding: 10px;
        }
        .title {
            text-align: center;
            font-size: 40px;
            color: #3498db;
            font-weight: bold;
        }
        .github {
            max-width: 20%;
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo ---
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
with col3:
    st.image("Logo.png", use_container_width=True)

col1_navbar, col2_navbar, col3_navbar = st.columns([1, 2, 1])
with col2_navbar:
    st.sidebar.image("Logo.png", width=100)

st.markdown("""<link rel="icon" href="Logo.png" type="image/x-icon">""", unsafe_allow_html=True)

# --- Titre ---
st.markdown("<h1 style='text-align: center; font-size: 40px; color: #3498db; font-weight: bold;'>Mes IA préférées...</h1>", unsafe_allow_html=True)

# --- Navbar ---
st.sidebar.title("Mes IA préférées")
page = st.sidebar.radio("Naviguer par catégories :", 
                        ["Générateurs de texte", "Générateurs d'images", "Générateurs de vidéos", 
                         "Détecteurs d'IA", "Traducteurs automatiques/autocorrecteurs", "Autres"])

# --- Contenu ---
if page == "Générateurs de texte":
    st.subheader("Générateurs de texte")
    data_texte = {
        "Nom": ["ChatGPT", "Copilot", "Le Chat", "Deepseek", "Llama", "Qwen", "Gemini", "Apple Intelligence"],
        "Entreprise": ["OpenAI", "Microsoft", "Mistral AI", None, "Meta", None, "Google", "Apple"]
    }
    st.dataframe(pd.DataFrame(data_texte))

elif page == "Générateurs d'images":
    st.subheader("Générateurs d'images")
    data_images = {
        "Nom": ["ChatGPT", "Copilot", "Canva", "Pixlr", "Le Chat", "Apple Intelligence"],
        "Entreprise": ["OpenAI", "Microsoft", None, None, "Mistral AI", "Apple"]
    }
    st.dataframe(pd.DataFrame(data_images))

elif page == "Générateurs de vidéos":
    st.subheader("Générateurs de vidéos")
    data_videos = {
        "Nom": ["Kapwing", "Sora"],
        "Entreprise": [None, "OpenAI"]
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
        "Nom": ["ChatGPT", "DeepL", "Google Translate", "Microsoft Translator", "Apple Traduction", "Reverso"],
        "Entreprise": ["OpenAI", "DeepL", "Google", "Microsoft", "Apple", None]
    }
    st.dataframe(pd.DataFrame(data_lang))

elif page == "Autres":
    st.subheader("Autres IA")
    data_others = {
        "Nom": ["Luma", "Suno"],
        "Entreprise": [None, None]
    }
    st.dataframe(pd.DataFrame(data_others))

# --- Footer ---
st.markdown("""
    <div style='position: fixed; bottom: 0; left: 0; width: 100%; background-color: #BBC9D1;
                color: white; text-align: center; padding: 10px;'>
        <p>&copy; 2025 Guillaume DUPUIS</p>
    </div>
""", unsafe_allow_html=True)
