import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CannyEdgeFilter(Node):
    def __init__(self):
        super().__init__('canny_edge_filter')

        # 파라미터 선언
        self.declare_parameter('camera_topic', '/camera')
        self.declare_parameter('thrs1', 2000)
        self.thrs1 = self.get_parameter('thrs1').value
        self.declare_parameter('thrs2', 4000)
        self.thrs2 = self.get_parameter('thrs2').value
        

        self.img_subscriber = self.create_subscription(
            Image,
            '/camera', 
            self.listener_callback,
            10
        )

        self.img_control = self.create_publisher(Image, '/canny_edge', 10)

        self.cv_bridge = CvBridge()

    def listener_callback(self, msg):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        filter_img = self.filter(img)

        pub_img = self.cv_bridge.cv2_to_imgmsg(filter_img, "mono8")
        self.img_control.publish(pub_img)

    def filter(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(gray, self.thrs1, self.thrs2, apertureSize=5)
        return edge


def main():
    rclpy.init()

    node = CannyEdgeFilter()

    rclpy.spin(node)

    node.destroy_node()
    
    rclpy.shutdown()