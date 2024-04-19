import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class RedFilterNode(Node):
    def __init__(self):
        super().__init__('blue_filter')
        
        # Define color conversion constants (optional)
        self.BGR2RED = (1, 0, 0)  # Set only red channel to 1

        # 카메라 이미지 구독 (Camera image subscription)
        self.subscription = self.create_subscription(
            Image,
            'camera_image',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Image, 'blue_filtered_image', 10)
        self.br = CvBridge()

    def listener_callback(self, msg):
        cv_image = self.br.imgmsg_to_cv2(msg, 'bgr8')
        
        # Apply red filter using constant or channel selection
        # Option 1: Using constant (BGR2RED)
        # cv_image[:] = self.BGR2RED * cv_image  # Element-wise multiplication

        # Option 2: Selecting channels
        cv_image[:, :, 1] = 0  # Set blue channel to 0
        cv_image[:, :, 2] = 0  # Set green channel to 0
        
        msg_out = self.br.cv2_to_imgmsg(cv_image, 'bgr8')
        self.publisher_.publish(msg_out)

def main(args=None):
    rclpy.init(args=args)
    red_filter_node = RedFilterNode()
    rclpy.spin(red_filter_node)
    red_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
