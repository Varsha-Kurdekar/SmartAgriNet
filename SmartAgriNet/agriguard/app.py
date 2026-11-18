from flask import Blueprint, render_template, Response
import cv2
from ultralytics import YOLO

agriguard_page = Blueprint(
    'agriguard_page',
    __name__,
    template_folder='templates'
)

# LOAD YOLO MODEL
model = YOLO("yolov8n.pt")

# OPEN CAMERA
camera = cv2.VideoCapture(0)

# =========================
# HOME PAGE
# =========================
@agriguard_page.route('/agriguard')
def agriguard_home():

    return render_template('agriguard.html')


# =========================
# GENERATE FRAMES
# =========================
def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break

        # YOLO DETECTION
        results = model(frame)

        annotated_frame = results[0].plot()

        # CONVERT FRAME
        ret, buffer = cv2.imencode('.jpg', annotated_frame)

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               frame + b'\r\n')


# =========================
# VIDEO FEED
# =========================
@agriguard_page.route('/video_feed')
def video_feed():

    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )