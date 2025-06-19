import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import base64
from io import BytesIO

# Convertir image locale en base64
def image_to_base64(path):
    img = Image.open(path)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

img_base64 = image_to_base64("IA/backend.png")
img3_base64 = image_to_base64("IA/paint.png")
img4_base64 = image_to_base64("IA/data.png")
image = Image.open("IA/radio.jpg")


# Application de plusieurs polices
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter&family=Playfair+Display&family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&displ');
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swa');

    html, body, [class*="css"]  {
        font-family: 'Open Sans', sans-serif; 
    }
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;  
    }
    </style>
""", unsafe_allow_html=True)

# Header en haut de la page
col1, col2, col3 = st.columns([1, 2, 1])  

with col1:
    st.image("IA/Logo.png", width=150)  

with col2:
    st.markdown("<h1 style='text-align: center; color: #3ba3ae;'>A EYE Médicale</h1>", unsafe_allow_html=True)
    
with col3:
    st.image("IA/Logo.png", width=150)  # ajuste le chemin et la taille

st.markdown("<p style='text-align: center; color: #2f2a85;'><big><strong>L’appli qui garde un œil sur vous (et les professionnels) !</strong></big></p>", unsafe_allow_html=True)

### SIDEBAR ##############################################################

st.sidebar.markdown("<h2>Réglementations</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
### -- Protection des données (RGPD)

- Les données que vous téléversez sont traitées de manière <span style="color: red;"><strong>confidentielle</strong></span>.
- Aucune donnée personnelle n’est stockée sans <strong>consentement explicite</strong>.
- Vous pouvez à tout moment demander la <strong>suppression de vos données</strong>.

---

### -- Hébergement des données (HDS)

- Les données médicales sont stockées sur des serveurs <strong>certifiés HDS</strong> (Hébergement de Données de Santé).
- Cela garantit <strong>sécurité, traçabilité et conformité</strong>.

---

### -- Application non-diagnostique

- Cette application est un <strong>outil pédagogique ou d'aide à l'analyse</strong>.
- Elle <strong>ne remplace pas un diagnostic médical professionnel</strong>.

---

### -- Transparence de l'IA

- Les algorithmes utilisés sont en cours de validation et <strong>ne sont pas certifiés dispositif médical</strong>.
- Les résultats proposés sont <strong>indicatifs</strong>.

---

### -- Politique de confidentialité

👉 Vous pouvez consulter notre <a href="#">politique de confidentialité</a> ou nous contacter à : <strong>support@tonappli.fr</strong>
""", unsafe_allow_html=True)

#### ONGLETS #####################################################################

onglet1, onglet2, onglet3, onglet4 = st.tabs(["Accueil", "Analyse", "Références","À propos"])

with onglet1:
    st.markdown("<h2 style='text-align: center; color:#2f2a85;'>Bienvenue sur l'accueil</h2>", unsafe_allow_html=True)
    st.write("- Cette application assiste les étudiants et professionnels en médecine dans l'analyse d’images radiologiques.")
    st.image(image, caption="Exemple d'image", use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#2f2a85;'>Téléversez une image médicale</h2>", unsafe_allow_html=True)
    st.write("- Vous pouvez téléverser une image, la faire analyser automatiquement, l’annoter, ou vous entraîner avec des cas.")
    uploaded_file = st.file_uploader("Image radiologique (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state["image_upload"] = image
        st.success("✅ Image enregistrée pour l'analyse. Veuillez vous rendre sur l'onglet 'Analyse' pour observer les résultats.")
        
with onglet2:
    st.markdown("<h2 style='text-align: center; color:#2f2a85;'>Résultats de l'analyse</h2>", unsafe_allow_html=True)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state["image_upload"] = image
        st.success("✅ Image enregistrée pour l'analyse. Veuillez vous rendre sur l'onglet 'Analyse' pour observer les résultats.")

with onglet3:
    st.markdown("<h2 style='text-align: center; color:#2f2a85;'>Références</h2>", unsafe_allow_html=True)

with onglet4:
    st.markdown("<h2 style='text-align: center; color:#2f2a85;'>À propos</h2>", unsafe_allow_html=True)
    st.write("- Créé par des élèves de E3E")
    st.markdown("- Intégration d'un modèle multimodal <strong> (texte + image) </strong> dans une application pour assister les étudiants ou professionnels en médecine à analyser des images radiologiques.", unsafe_allow_html=True)
    st.markdown(f"""
    <style>
    .container {{
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }}
    .block {{
        background-color: #f9f9f9;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        width: 300px;
        text-align: center;
    }}
    .block img {{
        width: 100%;
        border-radius: 8px;
    }}
    </style>

    <div class="container">
        <div class="block">
            <img src="data:image/png;base64,{img4_base64}" alt="Bloc 1">
            <p>TRICOT Guillaume</p>
        </div>
        <div class="block">
            <img src="data:image/png;base64,{img4_base64}" alt="Bloc 2">
            <p>ZERAH Samuel</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
    .container {{
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }}
    .block {{
        background-color: #f9f9f9;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        width: 300px;
        text-align: center;
    }}
    .block img {{
        width: 100%;
        border-radius: 8px;
    }}
    </style>

    <div class="container">
        <div class="block">
            <img src="data:image/png;base64,{img_base64}" alt="Bloc 3">
            <p>PANZA Lorenzo</p>
        </div>
        <div class="block">
            <img src="data:image/png;base64,{img_base64}" alt="Bloc 4">
            <p>TIMITE Youssouf</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
    .container {{
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
    }}
    .block {{
        background-color: #f9f9f9;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        width: 300px;
        text-align: center;
    }}
    .block img {{
        width: 100%;
        border-radius: 8px;
    }}
    </style>

    <div class="container">
        <div class="block">
            <img src="data:image/png;base64,{img3_base64}" alt="Bloc 5">
            <p>COULIBALY Alexandre</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer (en bas de la page)
st.markdown("---")
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)
st.markdown(f"""
    <footer style='text-align: center; color: gray;'>
        "© 2025 ESIEE Paris | Créé avec Streamlit"
        <div class="reseaux-sociaux" style="margin-top: 10px">
            <a href="https://www.facebook.com/esieeparis?locale=fr_FR" target="_blank"><i class="fab fa-facebook-square" style="font-size: 25px;"></i></a>
            <a href="https://twitter.com/ESIEEPARIS" target="_blank"><i class="fab fa-twitter-square" style="font-size: 25px;"></i></a>
            <a href="https://www.instagram.com/esieeparis/" target="_blank"><i class="fab fa-instagram-square" style="font-size: 25px;"></i></a>
        </div>
    </footer>
""", unsafe_allow_html=True)

