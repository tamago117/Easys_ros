import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import Adafruit_PCA9685

class ServoControllerNode(Node):

    def __init__(self, channel):
        super().__init__('servo_controller_node')

        self.channel = channel

        self.subscription = self.create_subscription(
            Bool,
            'arm_control_command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)

        self.ON_ANGLE = 220
        self.OFF_ANGLE = 50

    def listener_callback(self, msg):
        if msg.data:
            self.set_servo_angle(self.channel, self.ON_ANGLE)
        else:
            self.set_servo_angle(self.channel, self.OFF_ANGLE)

    def angle_to_pwm(self, angle):
        pulse_length = 1000 + (angle / 180.0) * 1000
        pwm_value = int((pulse_length * 4096) / 20000)
        return pwm_value

    def set_servo_angle(self, channel, angle):
        pwm_value = self.angle_to_pwm(angle)
        self.pwm.set_pwm(channel, 0, pwm_value)

    def close(self):
        self.pwm.set_all_pwm(0, 0)

def main(args=None):
    rclpy.init(args=args)
    servo_controller_node = ServoControllerNode(channel = 8)

    try:
        rclpy.spin(servo_controller_node)
    except KeyboardInterrupt:
        pass
    finally:
        servo_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()