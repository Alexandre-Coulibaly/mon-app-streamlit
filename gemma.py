import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from PIL import Image

# 📌 Choix du modèle (Gemma-like)
MODEL_NAME = "google/gemma-2b-it"  # ou tout modèle causallm compatible HF

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
    return tokenizer, model

st.title("🦙 Chat avec Gemma")
st.write("Entrez une instruction ou ajoutez une image pour enrichir l'expérience.")

tokenizer, model = load_model()

# Texte d’entrée
prompt = st.text_area("💬 Entrez une instruction :", height=100)

# Upload image (affichage seulement, pas encore traitée par le modèle)
image = st.file_uploader("📷 Optionnel : chargez une image", type=["jpg", "jpeg", "png"])
if image:
    st.image(Image.open(image), caption="Image chargée", use_column_width=True)

# Bouton de génération
if st.button("Générer une réponse") and prompt:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.markdown("### 🤖 Réponse :")
    st.write(response)
