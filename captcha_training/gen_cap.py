import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

def get_font_paths():
    # Base font directory
<<<<<<< HEAD
    base_dir = "/usr/share/fonts/truetype"
    
    # List to store paths of all compatible .ttf fonts
    font_list = []
    brokenfonts = [
    "/usr/share/fonts/truetype/samyak/Samyak-Devanagari.ttf",
    "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
    "/usr/share/fonts/truetype/libreoffice/opens___.ttf",
    "/usr/share/fonts/truetype/Gubbi/Gubbi.ttf",
    "/usr/share/fonts/truetype/sinhala/lklug.ttf",
    "/usr/share/fonts/truetype/teluguvijayam/Ponnala.ttf",
    "/usr/share/fonts/truetype/teluguvijayam/LakkiReddy.ttf",
    "/usr/share/fonts/truetype/kacst/KacstDigital.ttf",
    "/usr/share/fonts/truetype/kacst/KacstPen.ttf",
    "/usr/share/fonts/truetype/kacst/KacstTitle.ttf",
    "/usr/share/fonts/truetype/kacst/KacstTitleL.ttf",
    "/usr/share/fonts/truetype/kacst/KacstFarsi.ttf",
    "/usr/share/fonts/truetype/kacst/KacstPoster.ttf",
    "/usr/share/fonts/truetype/kacst/KacstDecorative.ttf",
    "/usr/share/fonts/truetype/kacst/KacstScreen.ttf",
    "/usr/share/fonts/truetype/kacst/KacstOffice.ttf",
    "/usr/share/fonts/truetype/kacst/KacstBook.ttf",
    "/usr/share/fonts/truetype/kacst/KacstArt.ttf",
    "/usr/share/fonts/truetype/kacst/KacstQurn.ttf",
    "/usr/share/fonts/truetype/kacst/KacstLetter.ttf",
    "/usr/share/fonts/truetype/kacst/mry_KacstQurn.ttf",
    "/usr/share/fonts/truetype/kacst/KacstNaskh.ttf",
    "/usr/share/fonts/truetype/malayalam/RaghuMalayalamSans-Regular.ttf",
    "/usr/share/fonts/truetype/teluguvijayam/RaviPrakash.ttf",
    "/usr/share/fonts/truetype/Navilu/Navilu.ttf"]
=======
    base_dir = "/usr/share/fonts/captcha_fonts"
    
    # List to store paths of all compatible .ttf fonts
    font_list = []
>>>>>>> master

    # Loop over each directory in the base font directory
    for root, dirs, files in os.walk(base_dir):
        if '-' in root:  # Skip directories with a dash in their name
            continue

        for file in files:
            if file.endswith(".ttf"):
                font_path = os.path.join(root, file)
                # Test loading the font to ensure compatibility
                try:
                    ImageFont.truetype(font_path, 20)
<<<<<<< HEAD
                    if font_path not in brokenfonts:
                        font_list.append(font_path)  # Add only if it loads successfully
=======
                    font_list.append(font_path)  # Add only if it loads successfully
>>>>>>> master
                except IOError:
                    pass
    
    return font_list
def generate_multi_char_captcha_with_masks(output_dir, num_captchas=10, captcha_length=5):
    # Set CAPTCHA dimensions
    width, height = 150, 40  # Dimensions of the CAPTCHA

    # Create directories if they don’t exist
    captcha_dir = os.path.join(output_dir, "captchas")
    mask_dir = os.path.join(output_dir, "masks")
    os.makedirs(captcha_dir, exist_ok=True)
    os.makedirs(mask_dir, exist_ok=True)

    # Get available fonts
    font_paths = get_font_paths()
    if not font_paths:
        
        return

    for i in range(num_captchas):
        # Randomly select a background color for CAPTCHA (darker for more contrast)
        background_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
        image = Image.new('RGB', (width, height), background_color)
        mask_image = Image.new('L', (width, height), 0)  # Grayscale mask image initialized to black

        draw = ImageDraw.Draw(image)
        mask_draw = ImageDraw.Draw(mask_image)

        # Generate CAPTCHA text
        captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=captcha_length))

        # Calculate the total width to center-align the characters
        text_width_total = sum([draw.textsize(c, font=ImageFont.truetype(random.choice(font_paths), 20))[0] for c in captcha_text])
        spacing_between_chars = (width - text_width_total) // (captcha_length + 1)
        current_x = (width - text_width_total - (spacing_between_chars * (captcha_length + 2))) // 2

        # Draw each character with a randomly selected font
        for idx, char in enumerate(captcha_text):
            # Select a random font for each character
            font_path = random.choice(font_paths)
            # print(font_path)

            font_size = 22
            try:
                font = ImageFont.truetype(font_path, font_size)
                # print(f"Skipping incompatible font: {font_path}")
            except IOError:
                font = ImageFont.load_default()

            # Random color for each character in the CAPTCHA image
            char_color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
            grayscale_value = 50 + idx * 40  # Unique grayscale value for each character in mask

            # Draw character on CAPTCHA with small random offsets and rotations
            x_offset = random.randint(-1, 1)
            y_offset = random.randint(-1, 1)

            text_width, text_height = draw.textsize(char, font=font)
            char_image = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((0, 0), char, font=font, fill=char_color)

            angle = random.uniform(-30, 30)
            rotated_char = char_image.rotate(angle, expand=True)
            scaled_width, scaled_height = rotated_char.size

            # Calculate position for rotated character
            text_y = (height - scaled_height) // 2 + y_offset
            image.paste(rotated_char, (current_x + x_offset, text_y), rotated_char)

            # Draw the character on the mask at the same position without rotation and in grayscale
            mask_draw.text((current_x + x_offset, text_y), char, font=font, fill=grayscale_value)

            # Move x-coordinate for the next character
            current_x += scaled_width + spacing_between_chars

        # Add noise to CAPTCHA (lines and dots)
        for _ in range(random.randint(3, 6)):
            line_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.line([(x1, y1), (x2, y2)], fill=line_color, width=random.randint(1, 2))

        for _ in range(random.randint(40, 60)):
            dot_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            x, y = random.randint(0, width), random.randint(0, height)
            draw.point((x, y), fill=dot_color)

        # Save CAPTCHA and mask images with matching names
        captcha_file_name = f"{captcha_text}_{i}.png"
        mask_file_name = f"{captcha_text}_{i}_mask.png"
        
        image.save(os.path.join(captcha_dir, captcha_file_name))
        mask_image.save(os.path.join(mask_dir, mask_file_name))

        # print(f"Generated CAPTCHA and mask saved as {captcha_file_name} and {mask_file_name}")

# Define the output directory where CAPTCHAs and masks will be saved
output_directory = "/home/midosama/Desktop/CAPTCHA_solving_AI/generated_captchas"

# Generate 10 multi-character CAPTCHAs (5 characters per CAPTCHA) with corresponding masks
generate_multi_char_captcha_with_masks(output_dir=output_directory, num_captchas=10000, captcha_length=5)