import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray

class EasysController(Node):
    def __init__(self):
        super().__init__('Easys_controller')

        self.thruster_pub = self.create_publisher(Float64MultiArray, '/thruster_input', 10)

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
        
        # Calculate thruster inputs
        input = Float64MultiArray()
        input.data = [linear_x, -linear_x, angular_z, -angular_z]

        # Publish thruster inputs
        self.thruster_pub.publish(input)


def main(args=None):
    rclpy.init(args=args)
    easys_controller = EasysController()
    rclpy.spin(easys_controller)

    easys_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()