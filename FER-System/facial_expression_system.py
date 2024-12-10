import os
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, Response

# Disable GPU usage warnings
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Initialize Flask app
app = Flask(__name__)

# Load the model
def load_model():
    try:
        model = tf.keras.models.load_model('models/best_facial_expression_model.keras', compile=False)
        print("[INFO] Model loaded successfully.")
        return model
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        return None

# Define global variables for emotions, emoji paths, and funny comments
CLASS_LABELS = ['Anger', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sadness', 'Surprise']
EMOJI_PATHS = {
    'Anger': 'emojis/anger.png',
    'Disgust': 'emojis/disgust.png',
    'Fear': 'emojis/fear.png',
    'Happy': 'emojis/happy.png',
    'Neutral': 'emojis/neutral.png',
    'Sadness': 'emojis/sadness.png',
    'Surprise': 'emojis/surprise.png'
}
FUNNY_COMMENTS = {
    'Anger': "Uh-oh, someone's about to Hulk out! 💥",
    'Disgust': "Eww! Did someone forget the garbage? 🤢",
    'Fear': "Don't worry, it's just a camera! 😱",
    'Happy': "Keep shining like a star! 🌟",
    'Neutral': "Hmm... Poker face activated. 😐",
    'Sadness': "Cheer up! A smile is just around the corner. 😊",
    'Surprise': "Wow! Did you just see a ghost? 👻"
}

# Camera initialization
def find_working_camera():
    print("[INFO] Searching for available cameras...")
    for index in range(4):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"[SUCCESS] Camera found at index {index}")
                return cap
        cap.release()
    print("[CRITICAL] No working camera found!")
    return None

# Global variables for the model and camera
model = load_model()
camera = find_working_camera()

def overlay_bottom_left(frame, emoji_path, emotion, comment):
    """
    Display emoji, emotion, and comment at the bottom-left of the frame.
    """
    try:
        # Load and resize the emoji
        emoji = cv2.imread(emoji_path, cv2.IMREAD_UNCHANGED)
        emoji_height, emoji_width = 64, 64  # Standard emoji size
        emoji = cv2.resize(emoji, (emoji_width, emoji_height))

        # Determine bottom-left position
        frame_height, frame_width, _ = frame.shape
        emoji_x = 10  # Left margin
        emoji_y = frame_height - emoji_height - 20  # Bottom margin

        # Overlay the emoji
        if emoji.shape[2] == 4:  # Check for alpha channel
            alpha = emoji[:, :, 3] / 255.0
            for c in range(3):  # Apply transparency
                y1, y2 = emoji_y, emoji_y + emoji_height
                x1, x2 = emoji_x, emoji_x + emoji_width
                frame[y1:y2, x1:x2, c] = (1 - alpha) * frame[y1:y2, x1:x2, c] + alpha * emoji[:, :, c]

        # Overlay the text next to the emoji
        text_x = emoji_x + emoji_width + 10  # Text starts right after emoji
        text_y = emoji_y + emoji_height - 10  # Align text with emoji vertically
        cv2.putText(frame, f"{emotion}: {comment}", (text_x, emoji_y + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    except Exception as e:
        print(f"[ERROR] Failed to overlay emoji and text: {e}")

def generate_frames():
    global camera, model, CLASS_LABELS, EMOJI_PATHS, FUNNY_COMMENTS

    if not model or not camera:
        print("[ERROR] Model or Camera not initialized.")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        success, frame = camera.read()
        if not success:
            print("[WARNING] Failed to read frame from camera.")
            break

        # Convert frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Process only if faces are detected
        if len(faces) > 0:
            x, y, w, h = faces[0]  # Process the first detected face
            face = gray_frame[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (48, 48)).reshape(1, 48, 48, 1) / 255.0

            # Predict emotion
            prediction = model.predict(face_resized, verbose=0)
            emotion_index = np.argmax(prediction)
            emotion = CLASS_LABELS[emotion_index]

            # Get emoji and comment
            emoji_path = EMOJI_PATHS.get(emotion, 'emojis/neutral.png')
            comment = FUNNY_COMMENTS.get(emotion, "Looking good!")

            # Display at bottom-left
            overlay_bottom_left(frame, emoji_path, emotion, comment)

        # Encode frame
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    if not camera:
        return "[ERROR] Camera not initialized. Please check your camera."
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def cleanup():
    global camera
    print("[INFO] Cleaning up resources...")
    if camera and camera.isOpened():
        camera.release()
        print("[INFO] Camera released successfully.")
    print("[INFO] Cleanup completed.")

if __name__ == '__main__':
    try:
        if camera and model:
            app.run(debug=False, host='0.0.0.0', port=5000)
        else:
            print("[CRITICAL] Cannot start app. Camera or Model initialization failed.")
    except Exception as e:
        print(f"[ERROR] Flask application failed to start: {e}")
    finally:
        cleanup()
