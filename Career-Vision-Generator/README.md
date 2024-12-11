# 🚀 Career-Vision-Generator

This project is a web application that takes a user's image, their passion description, and their gender to generate a realistic professional career visualization. The app leverages **OpenAI's GPT-3.5** for generating prompts and **Stability AI's Stable Diffusion** for generating images based on those prompts.

---

## 📂 Project Structure

```
Career-Vision-Generator/
│
├── static/
│   ├── uploads/          # Directory for storing uploaded images
│   └── generated/        # Directory for storing generated images
│
├── templates/
│   └── index.html        # HTML template for the frontend
│
└── Career_Vision_Generator.py  # Flask backend application
```

---

## 💻 Features

1. **Image Upload**: Users can upload a photo.
2. **Passion Input**: Enter a description of a passion or interest.
3. **Gender Selection**: Specify the gender to personalize the career visualization.
4. **AI Prompt Generation**: Uses OpenAI's GPT-3.5 to convert passion descriptions into career-oriented prompts.
5. **Image Generation**: Generates professional career images using Stability AI's Stable Diffusion.

---

## 🛠️ Setup and Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/siddhantbhattarai/Career-Vision-Generator.git
    cd Career-Vision-Generator
    ```

2. **Install Dependencies**:

    ```bash
    pip install Flask Flask-Cors openai requests
    ```

3. **Set API Keys**:

    Replace placeholders in `Career_Vision_Generator.py` with your actual API keys:

    ```python
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    STABILITY_API_KEY = 'YOUR_STABILITY_API_KEY'
    ```

4. **Run the Application**:

    ```bash
    python Career_Vision_Generator.py
    ```

5. **Access the App**:

    Visit the app in your browser at: `http://127.0.0.1:5000/`

---

## 🔧 API Endpoints

- **GET `/`**: Serves the HTML interface.
- **POST `/`**: Accepts JSON data containing:
  - `image`: Base64-encoded image.
  - `passion`: User's passion description.
  - `gender`: Gender of the user.

  **Example Request**:

  ```json
  {
    "image": "data:image/jpeg;base64,...",
    "passion": "I love solving complex mathematical problems.",
    "gender": "male"
  }
  ```

  **Response**:

  ```json
  {
    "status": "success",
    "generated_image": "static/generated/passion_vision_0.png"
  }
  ```

---

## 🌐 Dependencies

- **Flask**: Web framework.
- **Flask-Cors**: Enables Cross-Origin Resource Sharing.
- **OpenAI API**: For generating career visualization prompts.
- **Stability AI API**: For generating images using Stable Diffusion.

---

## 🔒 Security Note

⚠️ **Do not expose your API keys** in production environments. Consider using environment variables to manage API keys securely.

---

## 🤝 Contributing

Contributions are welcome! Please create an issue or submit a pull request to improve the project.


