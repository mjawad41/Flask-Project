from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# OpenCV video capture (use 0 for webcam, or specify the path for a video file)
video_capture = cv2.VideoCapture('rtsp://admin:admin12345@10.36.216.47:554/h264ESVideoTest')
 
def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Encode the frame as JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            break

        # Convert JPEG to bytes
        frame_bytes = jpeg.tobytes()

        # Yield the frame in bytes for the response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Return the response object with the streaming content
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
