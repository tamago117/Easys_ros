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


"""import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import pigpio

ESC_PIN = 13  #ESCへの出力ピン
MIN_WIDTH = 1000  # 1 ms pulse
MAX_WIDTH = 2000  # 2 ms pulse

class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller')
        self.subscription = self.create_subscription(
            Float64,
            'input',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pi = pigpio.pi()
        if not self.pi.connected:
           exit()

    def listener_callback(self, msg):
        # constrain -1 to 1
        if msg.data > 1:
            msg.data = 1
        elif msg.data < -1:
            msg.data = -1

        pulse_width = self.scale_input(msg.data)
        self.pi.set_servo_pulsewidth(ESC_PIN, pulse_width)

    def scale_input(self, input):
        # Scale input from -1 - 1 to MIN_WIDTH - MAX_WIDTH
        return ((input + 1) / 2) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH

    def on_shutdown(self):
        self.pi.set_servo_pulsewidth(ESC_PIN, 0)  # Stop servo pulses
        self.pi.stop()  # Disconnect pigpio

def main(args=None):
    rclpy.init(args=args)

    thruster_controller = ThrusterController()

    rclpy.spin(thruster_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    thruster_controller.destroy_node()
    del thruster_controller
    rclpy.shutdown()


if __name__ == '__main__':
    main()
"""

