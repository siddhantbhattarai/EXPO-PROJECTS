# Facial Expression Recognition System (FER-System)

The **Facial Expression Recognition System** is a Python-based machine learning application designed to classify human facial expressions into various emotion categories using a deep learning model. It uses a pre-trained model and supports real-time prediction.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Setup and Usage](#setup-and-usage)
- [Model Details](#model-details)
- [Customization](#customization)
- [Future Enhancements](#future-enhancements)

---

## Features

- **Emotion Detection:** Recognizes seven basic human emotions:
  - Anger
  - Disgust
  - Fear
  - Happy
  - Neutral
  - Sadness
  - Surprise
- **Pre-trained Model:** Uses a Keras model for efficient predictions.
- **Emoji Representation:** Displays emojis corresponding to detected emotions.
- **Real-time Predictions:** Capable of processing real-time video streams.
- **Web Interface:** Includes a user-friendly web interface for easy interaction.

---

## Project Structure

```
FER-System/
│
├── Datasets/
│   └── fer2013.csv                             # FER2013 dataset used for training the model
│
├── emojis/                                     # Emoji representations of emotions
│   ├── anger.png
│   ├── disgust.png
│   ├── fear.png
│   ├── happy.png
│   ├── neutral.png
│   ├── sadness.png
│   └── surprise.png
│
├── models/
│   └── best_facial_expression_model.keras      # Pre-trained model for emotion classification
│
├── Notebook/
│   └── Facial_Expression_Recognition_System.ipynb # Jupyter Notebook for training and evaluation
│
├── templates/
│   └── index.html                              # Web interface template
│
├── facial_expression_system.py                 # Flask application for real-time prediction
└── README.md                                   # Project documentation
```

---

## Dataset

The model is trained on the **FER2013** dataset, a benchmark dataset for facial expression recognition. It contains thousands of grayscale images of human faces categorized into seven emotions.

- **Dataset Location:** `Datasets/fer2013.csv`

---

## Technologies Used

- **Python:** Core programming language.
- **Flask:** Backend framework for serving predictions through a web interface.
- **Keras:** Deep learning library used for model development.
- **OpenCV:** For real-time video stream processing.
- **Bootstrap:** For responsive web design.
- **Pandas and NumPy:** For data manipulation and preprocessing.

---

## Setup and Usage

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- Required Python libraries (see `requirements.txt`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/fer-system.git
   cd FER-System
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python facial_expression_system.py
   ```

4. **Access the web interface:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Model Details

- **Architecture:** The model is a Convolutional Neural Network (CNN) trained on the FER2013 dataset.
- **File:** `models/best_facial_expression_model.keras`
- **Performance Metrics:**
  - Accuracy: Achieved [specific accuracy, e.g., 70%+ depending on training results]
  - Loss: [specific loss, e.g., categorical crossentropy]

---

## Customization

- **Train Your Own Model:**
  Use the Jupyter notebook `Facial_Expression_Recognition_System.ipynb` to train a new model on a custom dataset.
- **Add New Emojis:**
  Replace or add custom emoji images in the `emojis/` folder.
- **Modify the Web Interface:**
  Edit `templates/index.html` for UI changes.

---

## Future Enhancements

- **Multi-language Support:** Add translations for a global audience.
- **Advanced Model:** Use transfer learning for improved accuracy.
- **Additional Emotions:** Include complex emotions like "Contempt" or "Confusion."
- **Deployment:** Deploy the application to a cloud platform such as AWS, Heroku, or Azure.
- **Mobile Application:** Extend the system to a mobile app.

