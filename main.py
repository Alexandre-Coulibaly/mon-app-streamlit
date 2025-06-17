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
        font-family: 'Open Sans', sans-serif;  /* Texte par défaut */
    }
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;  /* Titres */
    }
    </style>
""", unsafe_allow_html=True)

# Header en haut de la page
st.markdown("<h1 style='text-align: center; color: black;'>A EYE Médicale</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>L’appli qui garde un œil sur vous (et les professionnels) !</p>", unsafe_allow_html=True)

#### ONGLETS #####################################################################

onglet1, onglet2, onglet3, onglet4, onglet5 = st.tabs(["Accueil", "Analyse", "Références","À propos", "Réglementation"])

with onglet1:
    st.markdown("<h2 style='color:red;'>Bienvenue sur l'accueil</h2>", unsafe_allow_html=True)
    st.write("- Cette application assiste les étudiants et professionnels en médecine dans l'analyse d’images radiologiques.")
    st.image(image, caption="Voici mon logo", use_container_width=True)
    st.header("Téléversez une image médicale")
    st.write("- Vous pouvez téléverser une image, la faire analyser automatiquement, l’annoter, ou vous entraîner avec des cas.")
    uploaded_file = st.file_uploader("Image radiologique (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state["image_upload"] = image
        st.success("✅ Image enregistrée pour l'analyse. Veuillez vous rendre sur l'onglet 'Analyse' pour observer les résultats.")
        
with onglet2:
    st.header("Résultats de l'analyse")

    if "image_upload" in st.session_state:
        image = st.session_state["image_upload"]
        st.image(image, caption="🩻 Image à analyser", use_column_width=True)

        # Exemple d’analyse (à remplacer par ton algorithme)
        st.markdown("✅ *Simulation d'analyse IA...*")
        st.write("Résultat : Rien d'anormal détecté ✅")

    else:
        st.warning("⚠️ Aucune image téléversée. Veuillez d'abord importer une image dans l'onglet 'Téléversement'.")

with onglet3:
    st.header("Références")

with onglet4:
    st.header("À propos")
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

with onglet5:
    st.markdown("""
### -- Protection des données (RGPD)

- Les données que vous téléversez sont traitées de manière <span style="color: red;">**confidentielle**</span>.
- Aucune donnée personnelle n’est stockée sans **consentement explicite**.
- Vous pouvez à tout moment demander la **suppression de vos données**.

---

### -- Hébergement des données (HDS)

- Les données médicales sont stockées sur des serveurs **certifiés HDS** (Hébergement de Données de Santé).
- Cela garantit **sécurité, traçabilité et conformité**.

---

### -- Application non-diagnostique

- Cette application est un **outil pédagogique ou d'aide à l'analyse**.
- Elle **ne remplace pas un diagnostic médical professionnel**.

---

### -- Transparence de l'IA

- Les algorithmes utilisés sont en cours de validation et **ne sont pas certifiés dispositif médical**.
- Les résultats proposés sont **indicatifs**.

---

### -- Politique de confidentialité

👉 Vous pouvez consulter notre [politique de confidentialité](#) ou nous contacter à : **support@tonappli.fr**

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

