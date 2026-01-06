import time
import RPi.GPIO as GPIO_PINS
from src.Motor.motor import MotorClass

class LineTracking:
    def __init__(self,left_sensor, right_sensor, middle_sensor, motor_configurations):
    # def __init__(self, left_sensor: int, middle_sensor: int , right_sensor:int, motor_configurations: MotorClass):
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.middle_sensor = middle_sensor
        self.motor = motor_configurations

    def setup(self):
        # GPIO_PINS.setmode(GPIO_PINS.BOARD)
        GPIO_PINS.setmode(GPIO_PINS.BCM)
        GPIO_PINS.setup(self.left_sensor,GPIO_PINS.IN)
        GPIO_PINS.setup(self.middle_sensor,GPIO_PINS.IN)
        GPIO_PINS.setup(self.right_sensor,GPIO_PINS.IN)
        GPIO_PINS.setwarnings(False)


    def run(self):
        line_detection_right_sensor = GPIO_PINS.input(self.right_sensor)
        line_detection_left_sensor = GPIO_PINS.input(self.left_sensor)
        line_detection_middle_sensor = GPIO_PINS.input(self.middle_sensor)


        print(f"Left Sensor: {line_detection_left_sensor}")
        print(f"Right Sensor: {line_detection_right_sensor}")
        print(f"Middle Sensor: {line_detection_middle_sensor}")





if __name__ == '__main__':
    motor_class = MotorClass()
    line_tracking = LineTracking(14,23,15,motor_class)
    while True:
        line_tracking.run()



    

    



