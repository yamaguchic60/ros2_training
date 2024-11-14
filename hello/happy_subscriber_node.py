import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HappySubscriber(Node):
    def __init__(self):
        super().__init__('happy_subscriber_node')
        self.sub=self.create_subscription(String, 'happy_topic', self.callback, 10)
        
    def callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node=HappySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()