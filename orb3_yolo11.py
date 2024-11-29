import cv2
import subprocess
from ultralytics import YOLO

# Start ORB-SLAM3 in a subprocess
orbslam_process = subprocess.Popen(["/home/ben/Dev/ORB_SLAM3/Examples/Monocular/myvideo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

model = YOLO("yolo11n.pt") 
# Open the video file (replace with your video path or webcam index)
cap = cv2.VideoCapture("/home/ben/Dev/ORB_SLAM3/Examples/Monocular/video.mp4")  # Use 0 for webcam, or a video path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv11 on the frame
    results = model(frame)  # Perform inference on the frame

    # Annotate the frame with YOLOv11 detections
    annotated_frame = results[0].plot()  # Use YOLO's built-in plotting function to annotate the frame

    # Display the YOLOv11 result
    cv2.imshow("YOLOv11 + ORB-SLAM3", annotated_frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#cv2.destroyAllWindows()
#orbslam_process.terminate()  # Terminate ORB-SLAM3 process
