#!/usr/bin/env python3
from pyrplidar import PyRPlidar
import rclpy
from rclpy.node import Node  
import time

class LidarDriver(Node):
    def __init__(self):
        super().__init__('lidar')
        self._lidar = PyRPlidar()
        self._lidar.connect(port="/dev/ttyUSB0", baudrate=115200, timeout=3)
        self._lidar.set_motor_pwm(500)
        time.sleep(2)
        self.simple_scan()

    def simple_scan(self):
        scan_generator = self._lidar.force_scan()
        
        for count, scan in enumerate(scan_generator()):
            print(count, scan)
            if count == 20: break

        self._lidar.stop()
        self._lidar.set_motor_pwm(0)

        
        self._lidar.disconnect()

def main(args=None):
    rclpy.init(args=args)
    driver = LidarDriver()
    rclpy.spin(driver)
    rclpy.shutdown()

if __name__ == "__main__":
    main()