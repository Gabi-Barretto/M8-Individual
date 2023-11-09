import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class CoordinatePublisher(Node):
    def __init__(self):
        super().__init__('coordinate_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, 'minhas_coordenadas', 10)
        self.get_logger().info('Publisher initialized, ready to get coordinates...')

    def publish_coordinates(self, x, y, z):
        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"
        msg.pose.position.x = float(x)
        msg.pose.position.y = float(y)
        msg.pose.position.z = float(z)
        msg.pose.orientation.w = 1.0  # assuming no orientation change for simplicity

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    coordinate_publisher = CoordinatePublisher()
    try:
        while True:
            x = input("Enter X coordinate: ")
            y = input("Enter Y coordinate: ")
            z = input("Enter Z coordinate: ")
            coordinate_publisher.publish_coordinates(x, y, z)
    except KeyboardInterrupt:
        pass
    finally:
        coordinate_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
