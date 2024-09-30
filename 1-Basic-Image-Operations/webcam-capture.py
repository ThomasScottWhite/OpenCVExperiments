import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open video or camera")
else:
    while True:
        ret, frame = capture.read()
        if not ret:
            print("Error: Unable to read frame")
            break

        # Show the frame
        cv2.imshow("Video Frame", frame)

        # Exit video on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the capture
    capture.release()
