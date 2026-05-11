import cv2
#Camara UNV IP CAMERA IPC2122LR3-PF40M-D
# Reemplaza con la URL de tu cámara
url_camara = "rtsp://admin:admin123@192.168.0.117/:554/substream"

# Crear el objeto de captura de video
cap = cv2.VideoCapture(url_camara)

if not cap.isOpened():
    print("Error: No se pudo conectar a la cámara.")
    exit()

while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()

    if not ret:
        print("Error: Se perdió la conexión.")
        break

    # Mostrar el video
    cv2.imshow('Camara IP', frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
