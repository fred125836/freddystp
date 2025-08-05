import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to create PDF from user input
def create_pdf(user_inputs):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    text_object = c.beginText(40, height - 50)
    text_object.setFont("Helvetica", 12)

    for key, value in user_inputs.items():
        text_object.textLine(f"{key}: {value}")
        text_object.textLine("")  # Add space between entries

    c.drawText(text_object)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Streamlit UI
st.title("User Input to PDF")

# Collect user input
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
message = st.text_area("Your message:")

# Store all inputs in a dictionary
user_data = {
    "Name": name,
    "Email": email,
    "Message": message
}

# Button to generate and download PDF
if st.button("Generate PDF"):
    pdf_buffer = create_pdf(user_data)
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="user_input.pdf",
        mime="application/pdf"
    )
