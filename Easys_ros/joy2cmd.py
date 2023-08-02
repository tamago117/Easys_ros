import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyToTwist(Node):

    def __init__(self):
        super().__init__('joy2cmd')

        # joy topicからデータを購読
        self.joy_sub = self.create_subscription(Joy, 'joy', self.joy_callback, 10)

        # cmd_vel topicにデータをpublish
        self.twist_pub = self.create_publisher(Twist, 'cmd_vel', 10)

    def joy_callback(self, msg):
        # JoyメッセージからTwistメッセージを作成します
        twist = Twist()
        twist.linear.x = msg.axes[4]
        twist.angular.z = msg.axes[0]

        # -1.0 ~ 1.0 -> 0 ~ 1
        twist.linear.z = (msg.axes[5] - 1.0) / 2.0
        if msg.buttons[5] == 1:
            twist.linear.z = -twist.linear.z


        # Twistメッセージをpublishします
        self.twist_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)

    node = JoyToTwist()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()