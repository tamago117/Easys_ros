import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import Adafruit_PCA9685

MAX_CHANNELS = 16  # PCA9685 supports 16 channels

class ThrusterController(Node):
    def __init__(self, pwm_frequency=50):
        super().__init__('thruster_controller')
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'thruster_input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.set_pwm_frequency(pwm_frequency)

    def set_pwm_frequency(self, frequency):
        self.pwm.set_pwm_freq(frequency)  # Set frequency
        self.min_pulse, self.max_pulse = self.calculate_pulse_limits(frequency)

    def calculate_pulse_limits(self, frequency):
        # Calculate the pulse lengths based on the provided frequency
        pulse_length_per_step = 1000000 / (frequency * 4096)  # microseconds per step
        min_pulse = int(1000 / pulse_length_per_step)  # 1ms pulse width
        max_pulse = int(2000 / pulse_length_per_step)  # 2ms pulse width
        return min_pulse, max_pulse

    def listener_callback(self, msg):
        for i, input in enumerate(msg.data):
            if i < MAX_CHANNELS:  # Ensure we don't go beyond our defined channels
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
        # Scale input from -1 - 1 to min_pulse - max_pulse
        return int(((input + 1) / 2) * (self.max_pulse - self.min_pulse) + self.min_pulse)

def main(args=None):
    rclpy.init(args=args)

    # You can change the PWM frequency here
    pwm_frequency = 50  # Set desired frequency
    thruster_controller = ThrusterController(pwm_frequency)

    rclpy.spin(thruster_controller)

    rclpy.shutdown()

if __name__ == '__main__':
    main()