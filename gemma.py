import streamlit as st
from PIL import Image
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

st.title("Demo Gemma 3 Multimodal")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])
input_text = st.text_input("Enter a prompt")

if uploaded_image and input_text:
    image = Image.open(uploaded_image)
    # Prétraitement de l'image
    # image_features = vision_model.encode(image)

    # Combine image features + texte
    # combined_input = build_input(image_features, input_text)

    # Générer réponse
    # output = model.generate(combined_input)

    st.write("Réponse simulée : Ceci est une réponse du modèle multimodal.")