# -*- coding: utf-8 -*-

class FizzBuzz:
    """FizzBuzzクラス"""

    def __init__(self,max):
        """コンストラクタ"""
        self.max = max

    def execute(self):
        for i in range(1, self.max + 1):
            if(i % 15 == 0):
                print(str(i) + ":FizzBuzz")
            elif(i % 5 == 0):
                print(str(i) + ":Buzz")
            elif(i % 3 == 0):
                print(str(i) + ":Fizz")

fizzBuzz = FizzBuzz(30)
fizzBuzz.execute()
