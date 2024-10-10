from PIL import Image, ImageFont, ImageDraw
import streamlit as st
import utils

st.title("Higurashi Template")
font = ImageFont.truetype("sazanami-gothic.ttf", 16)

with st.sidebar:
    st.markdown("## Text")
    st.text_area("Script", label_visibility="collapsed")
    st.markdown("## Image")
    bg = st.selectbox("Background", utils.backgrounds)
    num_sprites = st.number_input("Number of sprites", step=1, value=1, min_value=0)
    col1, col2, col3 = st.columns(3)
    for i in range(num_sprites):
        with col1:
            st.selectbox("Character", utils.sprites, key=f"character_{i}")

        with col2:
            st.selectbox("Outfit", [], key=f"outfit_{i}")

        with col3:
            st.selectbox("Expression", [], key=f"expression_{i}")
    st.selectbox("Image Mode", utils.image_modes)


if bg is not None:
    canvas = Image.new("RGB", (256, 256))
    background = Image.open(bg)

    st.image(bg, caption="Template...")
