import cv2

def run_rtsp_stream(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Cannot open stream")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('RTSP Stream', frame)

        # Press 'q' to close the window
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

rtsp_url = 'rtsp://192.168.1.105:8554/stream'
run_rtsp_stream(rtsp_url)
