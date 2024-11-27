from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import os

def create_certificate(name, output_path="certificate.pdf"):
    # Certificate details
    template_path = "certificate_template.jpg"  # Path to the certificate template image
    font_path = "arial.ttf"  # Font file (can use other fonts)
    font_size = 40
    text_color = (0, 0, 0)  # Text color (black)

    # Load the certificate template
    try:
        image = Image.open(template_path)
    except FileNotFoundError:
        print("Certificate template not found. Please check the path.")
        return

    draw = ImageDraw.Draw(image)

    # Define the text position (adjust based on the template design)
    text_position = (300, 250)  # Modify coordinates as needed

    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except FileNotFoundError:
        print("Font file not found. Please check the path.")
        return

    # Draw the user's name on the certificate
    draw.text(text_position, name, fill=text_color, font=font)

    # Save the certificate as a temporary image
    temp_image_path = "temp_certificate.jpg"
    image.save(temp_image_path)

    # Convert the certificate to a PDF using ReportLab
    c = canvas.Canvas(output_path)
    c.drawImage(temp_image_path, 0, 0, width=600, height=400)  # Page size
    c.save()

    # Remove the temporary image file
    os.remove(temp_image_path)

    print(f"Certificate successfully created: {output_path}")


# Example usage
user_name = input("Enter the user's name: ")
create_certificate(user_name)
