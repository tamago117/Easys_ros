import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class EasysController(Node):
    def __init__(self):
        super().__init__('Easys_controller')
        
        # Publishers for float64
        self.linear_x_pub = self.create_publisher(Float64, '/input', 10)
        self.angular_z_pub = self.create_publisher(Float64, '/angular_z', 10)

        # Subscriber for /cmd_vel
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        
        # Publish the values as Float64
        linear_x_msg = Float64()
        linear_x_msg.data = linear_x
        self.linear_x_pub.publish(linear_x_msg)
        
        angular_z_msg = Float64()
        angular_z_msg.data = angular_z
        self.angular_z_pub.publish(angular_z_msg)

def main(args=None):
    rclpy.init(args=args)
    easys_controller = EasysController()
    rclpy.spin(easys_controller)

    easys_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()