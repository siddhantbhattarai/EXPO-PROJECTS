# Love-Alchemy

**Love-Alchemy** is a Flask-based web application that predicts love compatibility between two individuals based on input data and a machine learning model. The application uses a trained Random Forest model stored in the `models` directory to provide compatibility predictions.

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
Love-Alchemy/
│
├── Datasets/
│   └── love_compatibility_dataset.csv     # Dataset used for training the model
│
├── models/
│   ├── random_forest_model.joblib         # Trained Random Forest model
│   └── training_columns.joblib            # Columns used for training the model
│
├── Notebook/
│   └── Love-Alchemy.ipynb                 # Jupyter notebook for model training
│
├── templates/
│   └── index.html                         # HTML template for the web app
│
├── love-alchemy.py                        # Main Flask application file
└── README.md                              # Project documentation
```

## Features
- User-friendly web interface to input data and get predictions.
- Trained Random Forest model for love compatibility prediction.
- Flask as the web framework for backend integration.
- HTML template to display results dynamically.

## Dataset
The dataset used for training the model is located in the `Datasets/` folder and contains attributes relevant to love compatibility.

### Key Features in Dataset:
- Personality traits
- Interests
- Age differences
- Compatibility factors

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or later
- Flask
- Joblib
- Pandas
- Scikit-learn

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/love-alchemy.git
   cd love-alchemy
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python love-alchemy.py
   ```

4. Access the web app in your browser at `http://127.0.0.1:5000`.

## Usage

1. Open the application in your browser.
2. Input the required details in the form.
3. Click on "Predict" to get the love compatibility result.

## Model Details
The trained model is a **Random Forest Classifier** saved in the `models/random_forest_model.joblib` file. The model was trained using the data in the `love_compatibility_dataset.csv`. The `training_columns.joblib` file stores the column names used during the training process to ensure consistent input formatting during predictions.

## Future Enhancements
- Add more advanced machine learning models for higher accuracy.
- Enable user authentication and session management.
- Include visualizations for compatibility factors.
- Deploy the application on a cloud platform (e.g., AWS, Azure, Heroku).

## Contributing
Contributions are welcome! Please submit a pull request or create an issue to discuss your ideas.

