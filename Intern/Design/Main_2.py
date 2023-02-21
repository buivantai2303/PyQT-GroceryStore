import os
import sys
import cv2
import face_recognition
from PyQt5.QtWidgets import QMainWindow
from ui_main import Ui_MainWindow
from Intern.Database.Connect_Database import connect_db
from Intern.Functions.face_recognition.recognition import FaceRecognition, face_confidence

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        super().init()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1) # Hiển thị trang đầu tiên của chương trình
        # Toggle/Menu
        self.ui.Btn_Toggle.clicked.connect(lambda: self.ui.stackedWidget_Menu.setHidden(not self.ui.stackedWidget_Menu.isHidden()))

        # Pages
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # Connect to database
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

        # Load table data
        self.load_table_data()

        # Camera recognition
        self.process_current_frame = True  # Xác định xem khung hình hiện tại được xử lý hay không
        self.known_face_encodings, self.known_face_names = FaceRecognition().get_known_faces()  # Lấy danh sách các khuôn mặt đã biết
        self.face_locations = []  # Vị trí khuôn mặt trong khung hình
        self.face_encodings = []  # Mã hóa khuôn mặt
        self.face_names = []  # Tên của khuôn mặt


    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        recognized = False  # Tạo biến recognized để kiểm tra khuôn mặt đã được nhận dạng hay chưa

        while not recognized:  # Vòng lặp sẽ ngừng nếu khuôn mặt được nhận dạng
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if self.process_current_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding,
                                                             tolerance=self.tolerance)
                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_face_names[first_match_index]

                    self.face_names.append(name)

                # check if there is a known face and it has a confidence score of at least 0.98
                for face_encoding, face_name in zip(self.face_encodings, self.face_names):
                    face_conf = face_confidence(face_encoding, self.known_face_encodings)
                    if face_name != 'Unknown' and face_conf >= 0.98:
                        recognized = True
                        break

            self.process_current_frame = not self.process_current_frame

            # if face is recognized, release the video capture and show Ui_MainWindow
            if not recognized:  # Vòng lặp sẽ ngừng nếu khuôn mặt được nhận dạng
                ret, frame = video_capture.read()

                # Only process every other frame of video to save time
                if self.process_current_frame:
                    # Resize frame of video to 1/4 size for faster face recognition processing
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                    rgb_small_frame = small_frame[:, :, ::-1]

                    # Find all the faces and face encodings in the current frame of video
                    self.face_locations = face_recognition.face_locations(rgb_small_frame)
                    self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                    self.face_names = []
                    for face_encoding in self.face_encodings:
                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding,
                                                                 tolerance=self.tolerance)
                        name = "Unknown"

                        # If a match was found in known_face_encodings, just use the first one.
                        if True in matches:
                            first_match_index = matches.index(True)
                            self.face_names.append(self.known_face_names[first_match_index])
                            recognized = True

                    self.process_current_frame = not self.process_current_frame

                    # Display the results
                    for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4

                        # Draw a box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                        # Draw a label with a name below the face
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                    # Display the resulting image
                    cv2.imshow('Video', frame)

                    # Press 'q' to quit
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                    # Release handle to the webcam
                video_capture.release()
                cv2.destroyAllWindows()

            def __init__(self, known_faces_dir_path):
                self.known_face_encodings = []
                self.known_face_names = []
                self.face_locations = []
                self.face_encodings = []
                self.face_names = []
                self.process_current_frame = True
                self.face_recognition_tolerance = 0.6

                # Load known faces and their encodings
                for filename in os.listdir(known_faces_dir_path):
                    image = face_recognition.load_image_file(os.path.join(known_faces_dir_path, filename))
                    face_encoding = face_recognition.face_encodings(image)[0]
                    self.known_face_encodings.append(face_encoding)
                    self.known_face_names.append(filename[:-4])  # Lấy tên file và loại bỏ đuôi .jpg hay .png

                print('Loaded known faces:', self.known_face_names)


if __name__ == '__main__':
    known_faces_dir_path = 'known_faces'
    face_recognition = FaceRecognition(known_faces_dir_path)
    face_recognition.run_recognition()