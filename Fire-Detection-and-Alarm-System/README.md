# Fire Detection and Alarm System

**Fire Detection and Alarm System** is a Python-based project designed to detect fire in video streams or pre-recorded videos and raise an audible alarm when fire is detected. The system leverages image processing and machine learning techniques to analyze frames and identify potential fire hazards.

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
Fire-Detection-and-Alarm-System/
│
├── assets/
│   ├── alarm-sound.mp3                    # Alarm sound played when fire is detected
│   └── videoplayback.mp4                  # Sample video for testing fire detection
│
├── fire-alarm-detection-system.py         # Main Python script
└── README.md                              # Project documentation
```

## Features
- Real-time fire detection in video streams or pre-recorded video files.
- Plays an alarm sound (`alarm-sound.mp3`) when fire is detected.
- Modular and scalable codebase for easy customization and integration.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or later
- OpenCV
- NumPy
- Playsound library

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/fire-detection-alarm-system.git
   cd Fire-Detection-and-Alarm-System
   ```

2. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy playsound
   ```

3. Run the application:
   ```bash
   python fire-alarm-detection-system.py
   ```

## Usage

1. Place your video file (if using custom video) in the `assets/` folder or specify its path in the script.
2. Run the script using the command mentioned above.
3. The system will process the video and play the alarm sound (`alarm-sound.mp3`) when fire is detected.

## How It Works

1. **Input Video:** The system takes a video stream or file as input.
2. **Frame Analysis:** Each video frame is analyzed using OpenCV to detect fire-like regions based on pixel intensity and color thresholds (e.g., orange and red hues).
3. **Alarm Activation:** If fire is detected, the system triggers an audible alarm using the `playsound` library.

## Dependencies
The following Python libraries are required:
- **OpenCV:** For video processing and fire detection.
- **NumPy:** For array operations.
- **Playsound:** For playing the alarm sound.

Install all dependencies with:
```bash
pip install opencv-python numpy playsound
```

## Future Enhancements
- Integrate advanced machine learning models for improved fire detection accuracy.
- Enable support for live camera streams (e.g., CCTV).
- Add email or SMS notifications when fire is detected.
- Develop a GUI for user interaction and configuration.

## Contributing
Contributions are welcome! Please submit a pull request or create an issue to discuss your ideas.
