# PyCamIP 📷

Simple Python project to connect and stream video from an IP camera using RTSP protocol.

## 🚀 Features

* Connect to IP camera via RTSP
* Real-time video streaming
* Graceful error handling
* Clean exit on window close or key press

## 🛠️ Tech Stack

* Python
* OpenCV

## ⚙️ Setup

1. Clone the repository:

```bash
git clone https://github.com/osdan/PyCamIP.git
cd PyCamIP
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env` file:

```
CAMERA_URL=rtsp://user:password@ip:port/stream
```

4. Run the app:

```bash
python src/camera_stream.py
```

## ⌨️ Controls

* Press **q** to exit
* Close window to stop streaming

## 📌 Notes

* Make sure your IP camera is accessible on the network
* Do not expose credentials in source code

## 👨‍💻 Author

Oscar Martínez
