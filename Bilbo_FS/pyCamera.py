import cv2
import os


class MarsCamera:
    def __init__(self):
        # Initialize cameras
        ## FOR JETSON NANO
        # camera = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")
        self.webCam = cv2.VideoCapture(0)  # Webcam
        self.externalCam = cv2.VideoCapture(1)  # External webcam
        self.externalCam2 = cv2.VideoCapture(2)  # External webcam


        # Check if cameras are successfully initialized
        if not self.webCam.isOpened():
            print("Error: Could not access the webcam (Camera 0).")
        elif not self.externalCam.isOpened():
            print("Error: Could not access the external webcam (Camera 1).")
        elif not self.externalCam2.isOpened():
            print("Error: Could not access the external webcam (Camera 1).")

    # def generate_frames_cameras(self):
    #     """Display frames from both cameras."""
    #     while True:
    #         ret_web, frame_web = self.webCam.read()
    #         ret_ext, frame_ext = self.externalCam.read()

    #         if ret_web:
    #             cv2.imshow("Webcam", frame_web)
    #         else:
    #             print("Failed to retrieve frame from webcam.")
            
    #         if ret_ext:
    #             cv2.imshow("External Webcam", frame_ext)
    #         else:
    #             print("Failed to retrieve frame from external webcam.")
            
    #         # Exit on pressing 'q'
    #         if cv2.waitKey(1) == ord('q'):
    #             break

    #     # Release resources
    #     self.release_cameras()

    def release_cameras(self):
        """Release both cameras and destroy OpenCV windows."""
        if self.webCam.isOpened():
            self.webCam.release()
        if self.externalCam.isOpened():
            self.externalCam.release()
        cv2.destroyAllWindows()

    def generate_frames(self):
        """
        Generator function to yield video frames as byte streams.
        """
        while True:
            success, frame = self.webCam.read()
            if not success:
                break
            else:
                # Encode the frame in JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    def generate_frames1(self):
        """
        Generator function to yield video frames as byte streams.
        """
        while True:
            success, frame = self.externalCam.read()
            if not success:
                break
            else:
                # Encode the frame in JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
    def generate_frames2(self):
        """
        Generator function to yield video frames as byte streams.
        """
        while True:
            success, frame = self.externalCam2.read()
            if not success:
                break
            else:
                # Encode the frame in JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')