import os
import random
import string
import io
from flask import Flask, render_template, redirect, url_for, request, session, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
app.secret_key = "your_secret_key"


# Path to the font folder (you can modify this path based on your environment)
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Function to generate random CAPTCHA text
def generate_random_text(captcha_length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=captcha_length))

# Function to generate a CAPTCHA image
def generate_captcha_image(captcha_text, width=150, height=50):
    image = Image.new('RGB', (width, height), (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50)))  # Background color
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype(FONT_PATH, 30)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text width to center-align
    text_width, text_height = draw.textsize(captcha_text, font=font)
    x_position = (width - text_width) // 2
    y_position = (height - text_height) // 2
    
    # Draw text on the image
    draw.text((x_position, y_position), captcha_text, font=font, fill=(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    
    # Add noise: lines and dots
    for _ in range(random.randint(3, 6)):
        line_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=line_color, width=random.randint(1, 2))

    for _ in range(random.randint(40, 60)):
        dot_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill=dot_color)

    # Return the image in a format suitable for Flask
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/verify', methods=['POST'])
def verify():
    try:
        # Vérifications initiales
        if 'captcha_text' not in session or 'remaining_lives' not in session or 'score' not in session:
            app.logger.error("Session data missing or expired")
            return jsonify({'error': 'Session data missing or expired'}), 400

        # Récupérer les données du formulaire
        user_input = request.form.get('captcha_input')
        if not user_input:
            app.logger.error("Captcha input is missing in the form data")
            return jsonify({'error': 'Captcha input is missing'}), 400

        remaining_lives = session['remaining_lives']
        score = session['score']
        correct_captcha = session['captcha_text']

        feedback = "Incorrect! Try again."  # Default feedback in case of wrong answer
        # Vérification du CAPTCHA lettre par lettre
        correct_letters = 0
        for i in range(min(len(user_input), len(correct_captcha))):
            if user_input[i] == correct_captcha[i]:
                correct_letters += 1

        if correct_letters > 0:
            score += correct_letters  # Chaque lettre correcte donne 1 point
            session['score'] = score
            feedback = f"Correct letters: {correct_letters}. Your score has increased."

        # Générer la nouvelle image CAPTCHA
        session['captcha_text'] = generate_random_text()  # Générer un nouveau CAPTCHA
        new_captcha_url = url_for('captcha') + f'?v={random.randint(0, 100000)}'

        return jsonify({
            'feedback': feedback,
            'score': score,
            'remaining_lives': remaining_lives,
            'game_over': False,  # Pas de fin de jeu ici
            'captcha_image': new_captcha_url
        })

    except Exception as e:
        app.logger.error(f"Error in /verify route: {str(e)}", exc_info=True)
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/solo/survival/<difficulty>')
def survival_game(difficulty):
    if difficulty not in ['easy', 'medium', 'hard']:
        return redirect(url_for('survival_mode'))
    
    session['mode'] = 'Survival'
    session['difficulty'] = difficulty
    session['score'] = 0
    session['remaining_lives'] = 5 if difficulty == 'easy' else 3 if difficulty == 'medium' else 1
    session['game_over'] = False
    session['captcha_text'] = generate_random_text()
    
    return render_template('survival_game.html', difficulty=difficulty)

@app.route('/captcha')
def captcha():
    captcha_text = generate_random_text()  # Générer un texte aléatoire
    session['captcha_text'] = captcha_text  # Stocker dans la session
    img_io = generate_captcha_image(captcha_text)
    return send_file(img_io, mimetype='image/png')

# Route to handle CAPTCHA form submission
@app.route('/validate-captcha', methods=['POST'])
def validate_captcha():
    user_input = request.form['captcha']
    if user_input == session.get('captcha_text'):
        return redirect(url_for('home'))  # Redirect to home page on success
    else:
        return render_template('game.html', error="Incorrect CAPTCHA. Please try again.")  # Show error message

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Solo Mode Selection Route
@app.route('/solo')
def solo_mode():
    return render_template('solo.html')

# Survival Mode Route
@app.route('/solo/survival')
def survival_mode():
    return render_template('survival.html')

# Timer Challenge Route
@app.route('/solo/timer')
def timer_challenge():
    return render_template('timer.html')

# Timer Challenge Start Route
@app.route('/solo/timer/start')
def timer_game():
    # Initialize timer game session
    session['mode'] = 'Timer Challenge'
    session['timer'] = 60  # 60 seconds countdown
    session['score'] = 0  # Track score
    return render_template('timer_game.html')

if __name__ == '__main__':
    app.run(debug=True)

