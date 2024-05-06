import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import Adafruit_PCA9685

MIN_PULSE = 204  # Corresponds to a 1ms pulse at 50Hz
MAX_PULSE = 409  # Corresponds to a 2ms pulse at 50Hz
MAX_CHANNELS = 16  # PCA9685 supports 16 channels

class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller')
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'thruster_input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50) # Set frequency to 50hz

    def listener_callback(self, msg):
        for i, input in enumerate(msg.data):
            if i < MAX_CHANNELS:  # Ensure we don't go beyond our defined channels

                # reverse direction of thruster
                input = -input

                # constrain -1 to 1
                if input > 1:
                    input = 1
                elif input < -1:
                    input = -1

                pulse_length = self.scale_input(input)
                self.pwm.set_pwm(i, 0, pulse_length)
            else:
                self.get_logger().warning('Input data has more elements than available ESC channels.')

    def scale_input(self, input):
        # Scale input from -1 - 1 to MIN_PULSE - MAX_PULSE
        return int(((input + 1) / 2) * (MAX_PULSE - MIN_PULSE) + MIN_PULSE)

def main(args=None):
    rclpy.init(args=args)

    thruster_controller = ThrusterController()

    rclpy.spin(thruster_controller)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

