import random

class Student:
        def __init__(self,name):
            self.name = name
            self.gladness = 50
            self.progress = 0
            self.alive=True

        def to_study(self):
            print('Time to study')
            self.progress += 0.12
            self.glodness -= 3


        def to_sleep(self):
             print('I will sleep')
             self.glodness += 3

        def to_chill(self):
             print('Rest time')
             self.progress += 5
             self.glodness -= 0.1


         def is_alive(self):
            if self.progress < -0.5:
              print('Cast out...')
              self.alive = False

              elif self.gladness <= 0
              print('Depresion...')
              self.alive = False

            elif self.progress > 5:
                print('Passed externally...')
                self.alive=False








