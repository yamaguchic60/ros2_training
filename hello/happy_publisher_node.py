import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HappyPublisher(Node):
    def __init__(self):
        super().__init__('happy_publisher')
        self.publisher_ = self.create_publisher(String, 'happy_topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i=10000

    def timer_callback(self):
        mag=String()
        if self.i>0:
            mag.data = f'Happy {self.i}'
        else:
            mag.data = 'end'
            self.destroy_timer(self.timer)
        self.publisher_.publish(mag)
        self.get_logger().info(f'Publishing: "{mag.data}"')
        self.i-=1

def main(args=None):
    rclpy.init(args=args)
    node = HappyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('ctrl-c detected')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()