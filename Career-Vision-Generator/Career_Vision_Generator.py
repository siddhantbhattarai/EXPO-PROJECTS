import os
import base64
import requests
import openai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# OpenAI Configuration
openai.api_key = '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'

# Stability AI Configuration
STABILITY_API_KEY = 'sk-nWK4qjfK9dJqWRudJ7wQQMhiz236oA1gQEUoygNoiOYhqR71'
STABILITY_API_HOST = "https://api.stability.ai"
ENGINE_ID = "stable-diffusion-xl-1024-v1-0"

# Create directories
os.makedirs('static/uploads', exist_ok=True)
os.makedirs('static/generated', exist_ok=True)

def generate_career_prompt(passion_text, gender):
    """
    Use OpenAI to transform passion text into a career-focused, imaginative prompt
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career vision interpreter. Transform a person's passion description into a vivid, professional career visualization prompt."},
                {"role": "user", "content": f"Transform this passionate description into a professional career visualization for a {gender}: {passion_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Prompt Generation Error: {e}")
        return f"A professional {gender} representing passion for {passion_text}, realistic portrait"

def generate_image(prompt):
    """Generate image using Stability AI API"""
    url = f"{STABILITY_API_HOST}/v1/generation/{ENGINE_ID}/text-to-image"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {STABILITY_API_KEY}"
    }
    
    payload = {
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            for i, image in enumerate(data.get("artifacts", [])):
                if image.get("finishReason") == "SUCCESS":
                    image_path = f"static/generated/passion_vision_{i}.png"
                    with open(image_path, "wb") as f:
                        f.write(base64.b64decode(image.get("base64")))
                    return image_path
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Image Generation Error: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        data = request.json

        # Extract data
        image_data = data.get('image', '')
        passion = data.get('passion', '')
        gender = data.get('gender', '').capitalize()

        if image_data and passion and gender:
            # Remove data URL prefix
            image_data = image_data.split(',')[1]

            # Save uploaded image
            upload_path = "static/uploads/captured_image.jpg"
            with open(upload_path, "wb") as fh:
                fh.write(base64.b64decode(image_data))

            # Generate career visualization prompt
            career_prompt = generate_career_prompt(passion, gender)

            # Generate future career image
            full_prompt = f"{career_prompt}, high quality, professional portrait, realistic"
            generated_image = generate_image(full_prompt)

            if generated_image:
                return jsonify({
                    "status": "success",
                    "generated_image": generated_image
                })
            else:
                return jsonify({
                    "status": "error",
                    "message": "Image generation failed"
                }), 500

        return jsonify({
            "status": "error",
            "message": "Invalid input: 'image', 'passion', and 'gender' fields are required."
        }), 400

if __name__ == '__main__':
    app.run(debug=True)