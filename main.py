#!/usr/bin/env pybricks-micropython
from math import floor, ceil
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Stop, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


class Robot:

    def __init__(self):
        self.init_vars()
        self.init_hardware()

        # self.open()

        while not self.Button1.pressed():
            ...


    def init_hardware(self):
        self.ev3 = EV3Brick()



    def init_vars(self):

        self.timer = StopWatch()
        
        # self.motor1 = Motor(A, positive_direction=Direction.CLOCKWISE)
        # self.motor2 = Motor(B, positive_direction=Direction.CLOCKWISE)
        # self.motor3 = Motor(C, positive_direction=Direction.CLOCKWISE)
        
        # self.button1 = TouchSensor(3)
        # self.button2 = TouchSensor(4)
        
        # self.LS = ColorSensor(2)
        
        self.US = UltrasonicSensor(1)
        
        
        

        self.number = 0
    
    def beep(self, frequrency=300): # гудок
        self.ev3.speaker.beep(frequrency)

    # ввод и вывод данных
    def enter(self): # ввод числа
        while not Button.CENTER in self.ev3.buttons.pressed():
            if Button.UP in self.ev3.buttons.pressed():
                self.number += 1
                wait(200)
            if Button.DOWN in self.ev3.buttons.pressed():
                self.number -= 1
                wait(200)
            if Button.RIGHT in self.ev3.buttons.pressed():
                self.number += 10
            if Button.LEFT in self.ev3.buttons.pressed():
                self.number -= 10
                wait(50)
            # if self.Button1.pressed():
            #     self.number = self.number * 10
            #     wait(400)
            self.ev3.screen.clear()
            self.ev3.screen.print(self.number)
            wait(10)

    # высота экрана 128 (0-127), ширина 178 (0-177), (0; 0) - в левом верхнем углу
    def print(self, data): # вывод текста на дисплей
        self.ev3.screen.print(data)
        
    def clear(self): # вывод текста на дисплей
        self.ev3.screen.clear()

    def screen_draw_line(self, x1, x2, y1, y2, width): # вывод линии
        self.ev3.screen.draw_line(x1, x2, y1, y2, width)

    def screen_draw_box(self, x1, y1, x2, y2, r, fill): # вывод прямоугольника
        self.ev3.screen.draw_box(x1, y1, x2, y2, r, fill)

    def screen_draw_circle(self, x, y, r, fill): # вывод круга
        self.ev3.screen.draw_circle(x, y, r, fill)
        self.ev3.screen.draw_box(x1, y1, x2, y2, r, fill)

    def screen_draw_dot(self, x, y): # вывод точки
        self.ev3.screen.draw_line(x, y, x, y, 1)






    def main(self):
        # -----------------------------------------------КОД-----------------------------------------------
        ...


# конец класса



robot = Robot()
robot.main()



# сделать функции возврата значения со всех датчиков (цвет, отражённый свет,
# яркость внешнего освещения, угол гироскопа, энкодер, расстояние, высота объекта,
# кнопка или датчик касания,
# ожидание нажатия кнопки, ожидание нажатия 1 из нескольких кнопок,
# ожидание нажатия нескольких из нескольких кнопок (кнопки на хабе и датчики касания))



# принадлежность интервалу или диап-у:
# функция с 3 параметрами - начало, конец и значение
# 1 функция для диапазона (нестрогое неравенство) 1 для интервала (строгое неравенство)

# сравнение с порогом:
# в функцию вводится порог и значение и сравнивается


# map из c++ (перевод из 1 промежутка в другой (например из диапазонаот 3 до 8,
# перевести число в диапазон от 6 до 16 или от 0 до 10 и т.д.))
