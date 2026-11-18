import cv2
import pygame
import requests
import time
from ultralytics import YOLO

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Load YOLOv5 model using ultralytics (modern way)
model = YOLO('yolov8n.pt')
# Open laptop camera
cap = cv2.VideoCapture(0)

# Telegram Bot credentials
BOT_TOKEN = "AAEZcVP33wDGFOuxGQvC3lDOUIMi0ArBVtc"
CHAT_ID = "2059378815"  # no leading space

def deterrent_action(label):
    """Play species-specific deterrent sound based on detected label."""
    if label == "dog":
        pygame.mixer.music.load("sounds/tiger_roar.mpeg")
        pygame.mixer.music.play()
    elif label == "cow":
        pygame.mixer.music.load("sounds/siren.mpeg")
        pygame.mixer.music.play()
    elif label == "person":
        pygame.mixer.music.load("sounds/alert.mpeg")
        pygame.mixer.music.play()
    elif label=="wolf":
        pygame.mixer.music.load("sounds/cracker.mpeg")
        pygame.mixer.music.play()
    elif label=="monkey":
        pygame.mixer.music.load("sounds/cracker.mpeg")
        pygame.mixer.music.play()
    elif label=="elephant":
        pygame.mixer.music.load("sounds/cracker.mpeg")
        pygame.mixer.music.play()
    elif label=="cat":
        pygame.mixer.music.load("sounds/tiger_roar.mpeg")
        pygame.mixer.music.play()
    else:
        return

    while pygame.mixer.music.get_busy():
        continue

def send_alert(image_path, label):
    """Send Telegram alert with intruder photo."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": open(image_path, "rb")}
    data = {"chat_id": CHAT_ID, "caption": f"Intruder detected: {label}"}
    response = requests.post(url, files=files, data=data)
    print("Telegram response:", response.text)  # debug output

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from camera")
        break
    
    results = model(frame)

    # Get the first result (ultralytics returns a list)
    result = results[0]

    # Show detection window
    try:
        img = result.plot()
        cv2.imshow("Detection", img)
    except Exception as e:
        print(f"Error displaying image: {e}")

    # Extract labels from detections
    if result.boxes is not None and len(result.boxes) > 0:
        boxes = result.boxes.xyxy.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()
        
        for box, cls in zip(boxes, classes):
            label = result.names[int(cls)]
            print("Detected:", label)

        # Save intruder image
        timestamp = int(time.time())
        image_path = f"intruder_{timestamp}.jpg"
        cv2.imwrite(image_path, frame)

        # Trigger deterrent + alert
        deterrent_action(label)
        send_alert(image_path, label)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
