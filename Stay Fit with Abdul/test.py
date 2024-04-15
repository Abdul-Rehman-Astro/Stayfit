# import cv2

# # Create a VideoCapture object
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     print("Unable to open camera")
#     exit()

# # Capture a frame
# while True:
#     ret, frame = cap.read()

#     # Check if the frame is not empty
#     if not ret:
#         print("No frame received")
#         break

#     # Display the frame
#     cv2.imshow('Frame', frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the camera
# cap.release()

# # Destroy all windows
# cv2.destroyAllWindows()


import cv2

camera_index = 0  # Replace with the correct camera index from the output of the above script
cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Test Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to grab frame")
cap.release()
cv2.destroyAllWindows()