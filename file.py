import face_recognition
import cv2

# Đọc video từ webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Đọc frame từ video
    ret, frame = video_capture.read()

    # Chuyển đổi màu sắc từ BGR sang RGB (Face Recognition yêu cầu)
    rgb_frame = frame[:, :, ::-1]

    # Tìm vị trí các khuôn mặt trong frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Vẽ hình chữ nhật xung quanh các khuôn mặt được nhận diện
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Hiển thị frame đã xử lý
    cv2.imshow('Video', frame)

    # Thoát chương trình nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
cv2.destroyAllWindows()
