import cv2
import os

import cv2
import os

class MarsCamera:
    def __init__(self):
        # Initialize cameras
        self.webCam = cv2.VideoCapture(0)  # Webcam
        self.externalCam = cv2.VideoCapture(1)  # External webcam

        # Check if cameras are successfully initialized
        if not self.webCam.isOpened():
            print("Error: Could not access the webcam (Camera 0).")
        if not self.externalCam.isOpened():
            print("Error: Could not access the external webcam (Camera 1).")

    def generate_frames_cameras(self):
        """Display frames from both cameras."""
        while True:
            ret_web, frame_web = self.webCam.read()
            ret_ext, frame_ext = self.externalCam.read()

            if ret_web:
                cv2.imshow("Webcam", frame_web)
            else:
                print("Failed to retrieve frame from webcam.")
            
            if ret_ext:
                cv2.imshow("External Webcam", frame_ext)
            else:
                print("Failed to retrieve frame from external webcam.")
            
            # Exit on pressing 'q'
            if cv2.waitKey(1) == ord('q'):
                break

        # Release resources
        self.release_cameras()

    def release_cameras(self):
        """Release both cameras and destroy OpenCV windows."""
        if self.webCam.isOpened():
            self.webCam.release()
        if self.externalCam.isOpened():
            self.externalCam.release()
        cv2.destroyAllWindows()

    def generate_frames_external(self):
        """Display frames from the external camera."""
        while True:
            ret, frame = self.externalCam.read()
            if ret:
                cv2.imshow("External Webcam", frame)
            else:
                print("Failed to retrieve frame from external webcam.")
            
            # Exit on pressing 'q'
            if cv2.waitKey(1) == ord('q'):
                break

        # Release resources
        self.release_cameras()

    def take_photo(self, save_path='images/webcamphoto.jpg'):
        """Take a photo with the webcam and save it to a file."""
        ret, frame = self.webCam.read()
        if ret:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            cv2.imwrite(save_path, frame)
            print(f"Photo saved to {save_path}")
        else:
            print("Failed to capture photo.")
