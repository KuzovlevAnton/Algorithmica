#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor, GyroSensor
from pybricks.parameters import Port, Direction, Button, Stop
from pybricks.parameters import Color as Col
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import math


class Robot:

    def __init__(self):
        self.init_vars()
        self.init_hardware()


    # инит хардваре
    def init_hardware(self): # инициализация оборудования
        self.ev3 = EV3Brick()

        # Initialize the motors.
        self.motor_1 = Motor(Port.A)
        self.motor_2 = Motor(Port.B)

        # Initialize the color sensor.
        self.light_sensor = ColorSensor(Port.S2)
        self.ultrasonic_sensor = UltrasonicSensor(Port.S1)

        self.touch_sensor_1, self.touch_sensor_2 = None, None

        try:
            self.touch_sensor_1 = TouchSensor(Port.S4)
            self.touch_sensor_2 = TouchSensor(Port.S3)

        except:
            pass


    # инитим переменные
    def init_vars(self): # инициализация переменных

        self.counter = 1 # инициализация counter

        self.colors_int = { # инициализация цветов
            Col.BLACK: 1,
            Col.BLUE: 2,
            Col.GREEN: 3,
            Col.YELLOW: 4,
            Col.RED: 5,
            Col.WHITE: 6,
            Col.BROWN: 7,
            Col.ORANGE: 8,
            Col.PURPLE: 9,
        }


    # функция для воспроизведения сигнала
    def beep(self): 
        self.ev3.speaker.beep(300)


    # чтение значения отражения с датчика освещенности
    def read_reflection(self):
        return self.light_sensor.reflection()

    
    # чтение значения цвета с датчика освещенности
    def read_color(self):
        return self.light_sensor.color()


    # чтение значения внешней освещенности с датчика освещенности
    def read_ambient(self):
        return self.light_sensor.ambient()


    # функция для ожидания нажатия датчика касания
    def wait_pressed(self):
        while not self.touch_sensor_1.pressed(): pass
        wait(300)

    
    # высота экрана 128 (0-127), ширина 178 (0-177), (0; 0) - в левом верхнем углу
    # вывод текста на дисплей
    def print(self, data): 
        self.ev3.screen.print(data)

    
    # вывод текста на дисплей
    def clear(self): 
        self.ev3.screen.clear()


    # вывод линии
    def screen_draw_line(self, x1, x2, y1, y2, width):
        self.ev3.screen.draw_line(x1, x2, y1, y2, width)


    # вывод прямоугольника
    def screen_draw_box(self, x1, y1, x2, y2, r, fill): 
        self.ev3.screen.draw_box(x1, y1, x2, y2, r, fill)


    # вывод круга
    def screen_draw_circle(self, x, y, r, fill): 
        self.ev3.screen.draw_circle(x, y, r, fill)
        self.ev3.screen.draw_box(x1, y1, x2, y2, r, fill)


    # вывод точки
    def screen_draw_dot(self, x, y): 
        self.ev3.screen.draw_line(x, y, x, y, 1)


    # функция для поворота на градусы первого мотора
    def control_motor_1(self, deg: int, speed: int = 500, then=Stop.BRAKE):
        self.motor_1.run_angle(deg, speed, then=then)

    
    # функция для поворота на градусы второго мотора
    def control_motor_2(self, deg: int, speed: int = 500, then=Stop.BRAKE):
        self.motor_2.run_angle(deg, speed, then=then)

    
    # функция для определения угла поворота первого мотора
    def get_angle_motor_1(self):
        return self.motor_1.angle()


    # функция для определения угла поворота первого мотора
    def get_angle_motor_2(self):
        return self.motor_2.angle() 


    # функция для вывода информации на экран
    def update_screen(self, data):
        self.ev3.screen.clear()
        self.ev3.screen.draw_text(0, 0, data)


    # чекнуть лимиты (граница)
    def check_limits(self, val, min, max):
        if min > val: val = min
        if max < val: val = max

        return val


    # считывание с датчика расстояния
    def read_us_dist(self):
        return self.check_limits(self.ultrasonic_sensor.distance(), 30, 800)


    # функция для ввода числа
    def input_number(self, limits=(), typeTouch=False):
        """
        limits: диапазон значений для ввод
        typeTouch: вводим ентер кнопкой внешней или нет
        """

        def check_limits_counter():
            if limits:
                min, max = limits

                if min > self.counter: self.counter = min
                if max < self.counter: self.counter = max

        self.update_screen(self.counter)

        while Button.CENTER not in self.ev3.buttons.pressed():

            if typeTouch == False:

                if Button.UP in self.ev3.buttons.pressed():
                    self.counter += 1

                    check_limits_counter()

                    self.update_screen(self.counter)
                    wait(300)

                elif Button.DOWN in self.ev3.buttons.pressed():
                    self.counter -= 1

                    check_limits_counter()

                    self.update_screen(self.counter)
                    wait(300)

            else:

                if self.touch_sensor_1.pressed():
                    self.counter += 1

                    check_limits_counter()

                    self.update_screen(self.counter)
                    wait(300)

                elif self.touch_sensor_2.pressed():
                    self.counter -= 1

                    check_limits_counter()

                    self.update_screen(self.counter)
                    wait(300)

        wait(500)
        return self.counter


    # проверяет на вхождение в интервал ( )
    def in_interval(self, start, end, value):
        return start < value < end


    # проверяет на вхождение в диапазон []
    def in_range(self, start, end, value):
        return start <= value <= end

    
    # определяет трешолд больше или меньше
    def greater_than(self, thereshold, value):
        return value > thereshold
    
    
    # сменяет диапазон значений, аналог функци map из C++
    def change_range(self, value, start1, end1, start2, end2):
        k1 = end1 - start1
        k2 = end2 - start2
        return (value - start1) / k1 * k2 + start2


    # main (для использования выше написанных функций)
    def main(self) -> None:
        ...


r = Robot()
r.main()
