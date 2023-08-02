import rclpy
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


"""import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import time
import wiringpi

# Constants
ESC_PIN = 13
MAX_SIGNAL = 2000
MIN_SIGNAL = 1000
MAX_PWM = 1024  # WiringPi's max PWM value

# Scale MAX_SIGNAL and MIN_SIGNAL to WiringPi's range
scaled_max_signal = int((MAX_SIGNAL / 2000.0) * MAX_PWM)
scaled_min_signal = int((MIN_SIGNAL / 2000.0) * MAX_PWM)


class ThrusterController(Node):
    def __init__(self):
        super().__init__('thruster_controller')
        
        # Setup
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(ESC_PIN, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        # PWM Frequency - 50Hz
        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(MAX_PWM)

        self.subscription = self.create_subscription(
            Float64,
            '/input',
            self.listener_callback,
            10)

    def __del__(self):
        # Turn off GPIO when exiting
        wiringpi.pwmWrite(ESC_PIN, 0)
        wiringpi.pinMode(ESC_PIN, wiringpi.GPIO.INPUT)
        
    def listener_callback(self, msg):
        # Scale input from -1 to 1 to MIN_SIGNAL to MAX_SIGNAL
        volume = ((msg.data + 1) / 2) * (MAX_SIGNAL - MIN_SIGNAL) + MIN_SIGNAL
        # Then scale to WiringPi's PWM range
        scaled_volume = int((volume / 2000.0) * MAX_PWM)
        
        # Send PWM signal
        wiringpi.pwmWrite(ESC_PIN, scaled_volume)
        self.get_logger().info('Sent PWM signal: %d' % scaled_volume)


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
    main()"""