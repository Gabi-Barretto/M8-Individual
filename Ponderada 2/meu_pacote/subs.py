import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

class SimpleNavigationSubscriber(Node):

    def __init__(self):
        super().__init__('simple_navigation_subscriber')
        self.subscription = self.create_subscription(
            PoseStamped,
            'minhas_coordenadas',
            self.pose_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.navigator = BasicNavigator()

    def pose_callback(self, msg):
        msg.header.frame_id = 'map'
        self.get_logger().info(f'Received pose: x={msg.pose.position.x}, y={msg.pose.position.y}, z={msg.pose.position.z}')
        # Assuming the "map" frame is used for navigation goals.
        self.navigator.setInitialPose(msg)
        self.navigator.goToPose(msg)

def main(args=None):
    rclpy.init(args=args)
    simple_navigation_subscriber = SimpleNavigationSubscriber()

    rclpy.spin(simple_navigation_subscriber)

    simple_navigation_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
