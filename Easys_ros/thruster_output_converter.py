import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float64

class ThrusterOutputConverter(Node):

    def __init__(self):
        super().__init__('thruster_output_converter')

        # subscriber
        self.thruster_sub = self.create_subscription(Float64MultiArray,'/thruster_input', self.thruster_callback, 10)
        # publisher
        self.left_down_pub = self.create_publisher(Float64, '/left_down/cmd_thruster', 10)
        self.right_down_pub = self.create_publisher(Float64, '/right_down/cmd_thruster', 10)
        self.left_up_pub = self.create_publisher(Float64, '/left_up/cmd_thruster', 10)
        self.right_up_pub = self.create_publisher(Float64, '/right_up/cmd_thruster', 10)

        self.power_gain = 200.0

    def thruster_callback(self, msg):
        left_down = Float64()
        left_down.data = msg.data[0] * self.power_gain
        right_down = Float64()
        right_down.data = msg.data[3] * self.power_gain
        left_up = Float64()
        left_up.data = msg.data[1] * self.power_gain
        right_up = Float64()
        right_up.data = msg.data[2] * self.power_gain

        self.left_down_pub.publish(left_down)
        self.right_down_pub.publish(right_down)
        self.left_up_pub.publish(left_up)
        self.right_up_pub.publish(right_up)

def main(args=None):
    rclpy.init(args=args)

    node = ThrusterOutputConverter()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()