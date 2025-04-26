import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

def get_font_paths():
    # Base font directory
    base_dir = "../fonts/captcha_fonts"
    
    # List to store paths of all compatible .ttf fonts
    font_list = []

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
                    font_list.append(font_path)  # Add only if it loads successfully
                except IOError:
                    pass
    
    return font_list
def generate_multi_char_captcha_with_masks(output_dir, num_captchas=10, captcha_length=5):
    # Set CAPTCHA dimensions
    width, height = 150, 50  # Slightly increased height like your second file

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
        # Create blank images
        background_color = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
        image = Image.new('RGB', (width, height), background_color)
        mask_image = Image.new('L', (width, height), 0)

        draw = ImageDraw.Draw(image)
        mask_draw = ImageDraw.Draw(mask_image)

        # Generate random CAPTCHA text
        captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=captcha_length))

        # Precompute widths
        total_text_width = 0
        font_per_char = []

        for char in captcha_text:
            font_path = random.choice(font_paths)
            try:
                font = ImageFont.truetype(font_path, 30)
            except IOError:
                font = ImageFont.load_default()
            
            bbox = draw.textbbox((0, 0), char, font=font)
            text_width = bbox[2] - bbox[0]
            font_per_char.append((font, text_width))
            total_text_width += text_width
        
        # Add spacing between characters
        char_spacing = 10
        total_text_width += (len(captcha_text) - 1) * char_spacing

        # Center starting position
        current_x = (width - total_text_width) // 2

        for idx, (char, (font, text_width)) in enumerate(zip(captcha_text, font_per_char)):
            # Calculate vertical position
            bbox = draw.textbbox((0, 0), char, font=font)
            text_height = bbox[3] - bbox[1]
            y_position = (height - text_height) // 2

            # Random text color for image
            char_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            draw.text((current_x, y_position), char, font=font, fill=char_color)

            # For mask: use grayscale value
            grayscale_value = 50 + idx * 40  # Unique value for each character
            mask_draw.text((current_x, y_position), char, font=font, fill=grayscale_value)

            current_x += text_width + char_spacing

        # Add noise
        for _ in range(random.randint(3, 6)):
            line_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.line([(x1, y1), (x2, y2)], fill=line_color, width=random.randint(1, 2))

        for _ in range(random.randint(40, 60)):
            dot_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            x, y = random.randint(0, width), random.randint(0, height)
            draw.point((x, y), fill=dot_color)

        # Save images
        captcha_file_name = f"{captcha_text}_{i}.png"
        mask_file_name = f"{captcha_text}_{i}_mask.png"
        
        image.save(os.path.join(captcha_dir, captcha_file_name))
        mask_image.save(os.path.join(mask_dir, mask_file_name))

# Define the output directory where CAPTCHAs and masks will be saved
output_directory = "../generated_captchas"

# Generate 10 multi-character CAPTCHAs (5 characters per CAPTCHA) with corresponding masks
generate_multi_char_captcha_with_masks(output_dir=output_directory, num_captchas=10, captcha_length=5)