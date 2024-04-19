import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from my_camera_msgs.srv import camera_control

class CameraControlServer(Node):
    def __init__(self):
        super().__init__('camera_control_server')

        # Initialize camera and other resources (replace with your camera access logic)
        self.cap = cv2.VideoCapture(0)  # Assuming camera index 0

        # Create a service server for camera control
        self.srv = self.create_service(camera_control, 'camera_control', self.handle_request)

    def handle_request(self, request, response):
        # Handle take_still_shot request
        if request.request.take_still_shot:
            filename = request.request.filename
            try:
                # Capture an image from the camera
                ret, frame = self.cap.read()
                if ret:
                    cv2.imwrite(filename, frame)
                    response.success = True
                else:
                    response.success = False
                    response.message = "Failed to capture image"
            except Exception as e:
                response.success = False
                response.message = str(e)

        # Handle start_recording request
        elif request.request.start_recording:
            filename = request.request.filename
            try:
                # Implement video recording logic (replace with your recording library)
                # For example, using OpenCV VideoWriter:
                self.video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame.shape[1], frame.shape[0]))
                response.success = True
            except Exception as e:
                response.success = False
                response.message = str(e)
                self.video_writer = None  # Reset video writer on error

        # Handle stop_recording request
        elif request.request.stop_recording:
            try:
                if self.video_writer:
                    self.video_writer.release()
                    self.video_writer = None
                    response.success = True
                else:
                    response.success = False
                    response.message = "No recording in progress"
            except Exception as e:
                response.success = False
                response.message = str(e)

        return response

def main(args=None):
    rclpy.init(args=args)
    node = CameraControlServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()
