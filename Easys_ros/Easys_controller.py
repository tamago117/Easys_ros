import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Imu

from .controller.PID_controller import PID_controller

class EasysController(Node):
    def __init__(self):
        super().__init__('Easys_controller')

        # Initialize PID controllers
        config = {
            "rollP": 0.7,
            "rollI": 0.0,
            "rollD": 0.0,
            "pitchP": 0.3,
            "pitchI": 0.0,
            "pitchD": 1.0,
            "dt": 0.02
        }
        self.pid_controller = PID_controller(config)

        self.thruster_pub = self.create_publisher(Float64MultiArray, '/thruster_input', 10)

        # Subscriber for /cmd_vel
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )
        self.subscription

        # Subscriber for /imu
        self.subscription = self.create_subscription(
            Imu,
            '/imu',
            self.imu_callback,
            10
        )
        self.subscription

        self.imu_data = Imu()

    def imu_callback(self, imu_data):
        self.imu_data = imu_data

    def quaternion_to_euler(self, x, y, z, w):
        """四元数からオイラー角への変換"""
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll = math.atan2(t0, t1)
        
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch = math.asin(t2)
        
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = math.atan2(t3, t4)
        
        return roll, pitch, yaw  # yawは現在のところ不要なのでアンダースコアで置き換えました。

    def listener_callback(self, cmd_vel):
        
        # Calculate roll and pitch(euler angles)
        roll, pitch, yaw = self.quaternion_to_euler(self.imu_data.orientation.x,
                                                    self.imu_data.orientation.y,
                                                    self.imu_data.orientation.z,
                                                    self.imu_data.orientation.w)
        

        # Calculate thruster inputs
        input = Float64MultiArray()
        input.data = [0.0, 0.0, 0.0, 0.0]
        input.data = self.pid_controller.control(roll, pitch, cmd_vel.linear.x, cmd_vel.linear.z, cmd_vel.angular.z)
        #print(input.data)
        #print(roll, pitch, yaw)

        #input.data = [0.0, 0.0, 0.0, 0.0]

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