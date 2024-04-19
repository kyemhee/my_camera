import rclpy
from img_publisher import ImgPublisher  # img_publisher.py로부터 ImagePublisher 클래스를 임포트

def main(args=None):
    rclpy.init(args=args)  # ROS2 노드 초기화
    image_publisher = ImgPublisher()  # ImagePublisher 인스턴스 생성
    rclpy.spin(image_publisher)  # 노드 실행
    image_publisher.cap.release()  # 카메라 자원 해제
    image_publisher.destroy_node()  # 노드 파괴
    rclpy.shutdown()  # ROS2 종료

if __name__ == '__main__':
    main()
