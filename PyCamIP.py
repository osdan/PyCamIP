import cv2

url_camara = "rtsp://admin:admin123@192.168.0.117/:554/stream"

cap = cv2.VideoCapture(url_camara)

if not cap.isOpened():
    print("Error: No se pudo conectar a la cámara.")
    exit()

cv2.namedWindow('Camara IP', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Se perdió la conexión.")
        break

    cv2.imshow('PyCamIP', frame)

    if cv2.getWindowProperty('PyCamIP', cv2.WND_PROP_VISIBLE) < 1:
        print("Ventana cerrada por el usuario.")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
