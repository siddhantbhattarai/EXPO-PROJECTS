# Import necessary libraries
import cv2                  # For video processing
import numpy as np          # For handling image arrays
import smtplib              # For sending email notifications
import playsound            # For playing alarm sound
import threading            # For running tasks concurrently
import os                   # For file path management

# Initialize status flags and counters
Alarm_Status = False        # Tracks if the alarm is currently active
Email_Status = False        # Tracks if the email has been sent
Fire_Reported = 0           # Counter for the number of fire detections

# List of recipient emails for bulk notifications
recipient_emails = [
    "king0fhellsinced1@gmail.com",
    # "recipient2@example.com",
    # "recipient3@example.com",
    # "recipient4@example.com"
]

# Function to play the alarm sound in a loop
def play_alarm_sound_function():
    while Alarm_Status:
        try:
            playsound.playsound('assets/alarm-sound.mp3', True)
        except Exception as e:
            print(f"Error playing alarm sound: {e}")

# Function to send bulk email notifications with a professional template
def send_mail_function():
    sender_email = "king0fhellsinced1@gmail.com"  # Your email address
    sender_password = 'yrhp jgmt imvy eskd'       # Your app-specific password

    # Email subject and body template
    subject = "URGENT: Fire Incident Alert at ISMT College"
    body = """\
Dear Students,

We hope this message finds you well.

This is an urgent notification to inform you that a potential fire incident has been detected at ISMT College premises. Immediate action and verification are required to ensure safety.

Details of the Incident:
Location: ISMT College
Time of Detection: Immediate
Status: Fire Detection Triggered

Please take necessary precautions and alert the relevant authorities promptly.

Thank you for your attention to this matter.

Best regards,  
ISMT College Safety Team  
safety@ismt.edu.np  
"""

    try:
        # Set up an SMTP server and log in
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)

        # Loop through each recipient and send the email
        for recipientEmail in recipient_emails:
            recipientEmail = recipientEmail.lower()
            try:
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail(sender_email, recipientEmail, message)
                print(f"Email sent to {recipientEmail}")
            except Exception as e:
                print(f"Failed to send email to {recipientEmail}: {e}")

        # Quit the server after sending all emails
        server.quit()
    except Exception as e:
        print(f"Failed to set up email server: {e}")

# Function to release resources on exit
def cleanup():
    global Alarm_Status
    Alarm_Status = False
    cv2.destroyAllWindows()
    video.release()

# Main code for fire detection
try:
    # Open a video capture object using the specified video file or webcam
    video = cv2.VideoCapture("assets/videoplayback.mp4")  # Use 0 for webcam, or specify a video file

    while True:
        # Read a frame from the video
        grabbed, frame = video.read()
        if not grabbed:
            break

        # Resize the frame for faster processing
        frame = cv2.resize(frame, (960, 540))

        # Apply Gaussian blur to the frame to reduce noise
        blur = cv2.GaussianBlur(frame, (21, 21), 0)

        # Convert the frame from BGR to HSV color space
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Define the range for detecting fire-like colors (yellow, orange, etc.)
        lower = np.array([18, 50, 50], dtype="uint8")   # Lower bound of HSV values
        upper = np.array([35, 255, 255], dtype="uint8") # Upper bound of HSV values

        # Create a mask to identify fire-like regions in the frame
        mask = cv2.inRange(hsv, lower, upper)

        # Apply the mask to the original frame
        output = cv2.bitwise_and(frame, frame, mask=mask)

        # Count the number of non-zero (fire-like) pixels in the mask
        no_red = cv2.countNonZero(mask)

        # If fire-like pixels exceed a certain threshold, increase the fire report counter
        if int(no_red) > 15000:
            Fire_Reported += 1

        # Display the output with detected regions
        cv2.imshow("output", output)

        # If fire is reported, trigger the alarm and email notification
        if Fire_Reported >= 1:
            if not Alarm_Status:
                Alarm_Status = True
                # Start the alarm sound in a separate thread
                threading.Thread(target=play_alarm_sound_function, daemon=True).start()

            if not Email_Status:
                Email_Status = True
                # Send bulk emails in a separate thread
                threading.Thread(target=send_mail_function, daemon=True).start()

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources after the loop ends
    cleanup()
except KeyboardInterrupt:
    # Clean up if the program is interrupted by the user
    cleanup()
    print("Program interrupted and exited cleanly.")
except Exception as e:
    # Handle any unexpected errors
    cleanup()
    print(f"An error occurred: {e}")
