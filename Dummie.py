import cv2

# Open the camera (0 is typically the default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is open. Press 'q' to quit.")
    
# Loop to continuously capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame was read correctly
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Display the resulting frame
    cv2.imshow("Camera Feed", frame)

    # Wait for 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
