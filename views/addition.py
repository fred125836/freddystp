import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="Background Remover with Color Replace", layout="centered")

st.title("🎨 Background Remover + Background Color Changer")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Select background color
bg_color = st.color_picker("Pick a background color", "#ffffff")

if uploaded_file is not None:
    input_image = Image.open(uploaded_file).convert("RGBA")
    st.image(input_image, caption="Original Image", use_column_width=True)

    with st.spinner("Removing background..."):
        # Convert input image to bytes
        input_bytes = io.BytesIO()
        input_image.save(input_bytes, format='PNG')
        input_bytes = input_bytes.getvalue()

        # Remove background
        output_bytes = remove(input_bytes)
        foreground = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        # Create new background color image
        background = Image.new("RGBA", foreground.size, bg_color)

        # Composite foreground over colored background
        final_image = Image.alpha_composite(background, foreground)

        st.image(final_image, caption="Image with New Background", use_column_width=True)

        # Download button
        final_bytes = io.BytesIO()
        final_image.save(final_bytes, format="PNG")
        st.download_button(
            label="📥 Download Image with New Background",
            data=final_bytes.getvalue(),
            file_name="new_background.png",
            mime="image/png"
        )
