import cv2
import face_recognition
import os
import numpy as np

class FaceRegister:
    # Set up webcam
    cap = cv2.VideoCapture(0)

    # Set up face recognition
    known_faces = []
    known_names = []

    # Function to save face image to directory
    @staticmethod
    def save_face_image(face_image, name):
        # Create directory if not exist
        if not os.path.exists('faces'):
            os.makedirs('faces')

        # Save image to directory
        cv2.imwrite(f'faces/{name}.jpg', face_image)
        print(f'{name} has been registered!')

    # Loop to capture and register face images
    while True:
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_angles = face_recognition.face_landmarks(rgb_frame)

        for (top, right, bottom, left), landmarks in zip(face_locations, face_angles):
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Check if the face is already registered
            face_encoding = face_recognition.face_encodings(rgb_frame, [(top, right, bottom, left)])
            if len(face_encoding) > 0:
                match_results = face_recognition.compare_faces(known_faces, face_encoding[0])
                if True in match_results:
                    index = match_results.index(True)
                    name = known_names[index]
                    cv2.putText(frame, f'{name} (Registered)', (left, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 0, 255), 2)
                else:
                    # Ask user to input name for registration
                    print("Press Enter to register this face or press Q to skip")
                    while True:
                        key = cv2.waitKey(1) & 0xFF
                        if key == ord('q') or key == 27:  # 'q' key or 'esc' key
                            print("Skipping face registration...")
                            break
                        elif key == 13:  # Enter key
                            # Check if user is looking straight at the screen
                            landmarks = face_recognition.face_landmarks(rgb_frame, [(top, right, bottom, left)])
                            if landmarks:
                                # Get the vertical position of the eyes
                                left_eye_top = np.min(landmarks[0]['left_eye'], axis=0)[1]
                                left_eye_bottom = np.max(landmarks[0]['left_eye'], axis=0)[1]
                                right_eye_top = np.min(landmarks[0]['right_eye'], axis=0)[1]
                                right_eye_bottom = np.max(landmarks[0]['right_eye'], axis=0)[1]
                                eye_center = (left_eye_top + left_eye_bottom + right_eye_top + right_eye_bottom) / 4
                                screen_center = frame.shape[0] / 2
                                tolerance = 20  # Tolerance in pixels

                                if abs(eye_center - screen_center) <= tolerance:
                                    name = input('Enter your name:  ')
                                    save_face_image(frame[top:bottom, left:right], name)
                                    known_faces.append(face_encoding[0])
                                    known_names.append(name)
                                    cv2.putText(frame, f'{name} (Registered)', (left, bottom + 25),
                                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                                (0, 0, 255), 2)
                                else:
                                    print("Please look straight at the screen to register your face.")
                            else:
                                print("Could not detect facial landmarks. Please try again.")
                            break
            else:
                # Draw a red rectangle around the face to indicate that it was not recognized
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, "Unknown Face", (left, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)