from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the saved model and training columns
model = joblib.load('models/random_forest_model.joblib')
with open('models/training_columns.joblib', 'rb') as f:
    training_columns = joblib.load(f)  # Load the training column order

# Define routes
@app.route('/')
def home():
    return render_template('index.html', compatibility_percentage=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    boy_name = request.form.get('boy_name', '')
    girl_name = request.form.get('girl_name', '')
    boy_age = int(request.form.get('boy_age', 0))
    girl_age = int(request.form.get('girl_age', 0))
    boy_fav_color = request.form.get('boy_fav_color', '')
    girl_fav_color = request.form.get('girl_fav_color', '')
    boy_hobby = request.form.get('boy_hobby', '')
    girl_hobby = request.form.get('girl_hobby', '')
    boy_movie_genre = request.form.get('boy_movie_genre', '')
    girl_movie_genre = request.form.get('girl_movie_genre', '')
    boy_zodiac = request.form.get('boy_zodiac', '')
    girl_zodiac = request.form.get('girl_zodiac', '')

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'Boy_Age': [boy_age],
        'Girl_Age': [girl_age],
        'Boy_FavColor': [boy_fav_color],
        'Girl_FavColor': [girl_fav_color],
        'Boy_Hobby': [boy_hobby],
        'Girl_Hobby': [girl_hobby],
        'Boy_FavMovieGenre': [boy_movie_genre],
        'Girl_FavMovieGenre': [girl_movie_genre],
        'Boy_Zodiac': [boy_zodiac],
        'Girl_Zodiac': [girl_zodiac]
    })

    # Preprocess input data (ensure same one-hot encoding as training)
    input_data_encoded = pd.get_dummies(input_data)
    input_data_encoded = input_data_encoded.reindex(columns=training_columns, fill_value=0)

    # Convert input data to numpy array for prediction
    feature_array = input_data_encoded.values

    # Predict compatibility as probabilities
    prediction_probability = model.predict_proba(feature_array)[0][1]  # Probability of compatibility
    compatibility_percentage = int(prediction_probability * 100)

    # Generate funny comment based on compatibility percentage
    if compatibility_percentage >= 90:
        comment = "You two are a match made in heaven! 💕 Cupid approves! 🏹✨"
    elif compatibility_percentage >= 70:
        comment = "Pretty solid match! ❤️ A little spark can ignite a flame. 🔥"
    elif compatibility_percentage >= 50:
        comment = "Could work with a bit of effort! 🤔 Love is an adventure! 🧗‍♀️"
    else:
        comment = "It’s complicated... 💔 Maybe friendship is the way to go? 🤝"

    # Render the result in the same template
    return render_template(
        'index.html',
        boy_name=boy_name,
        girl_name=girl_name,
        compatibility_percentage=compatibility_percentage,
        comment=comment
    )

if __name__ == '__main__':
    app.run(debug=True)

