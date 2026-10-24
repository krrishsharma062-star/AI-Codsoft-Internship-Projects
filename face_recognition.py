import cv2

# Load OpenCV's pre-trained Haar Cascade face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Initialize webcam (0 is default camera)
cap = cv2.VideoCapture(0)

print('Press "q" on your keyboard to quit the webcam feed.')

while True:
  # Read frame from webcam
  ret, frame = cap.read()
  if not ret:
    print('Failed to grab frame from camera.')
    break

  # Convert frame to grayscale for faster face detection processing
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces
  faces = face_cascade.detectMultiScale(
      gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
  )

  # Draw a green rectangle around every detected face
  for x, y, w, h in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

  # Display the resulting frame
  cv2.imshow('Face Detection - Press Q to Quit', frame)

  # Break loop when 'q' key is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()