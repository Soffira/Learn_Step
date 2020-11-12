class Cars():
    
    def __init__(self, sec=0, acceleration=5):
        self.sec = sec
        self.acceleration = acceleration
        
    def know_speed(self):
        self.speed_now = self.sec * self.acceleration
        print('Скорость', self.speed_now)
    
    def accelerating(self):
        self.sec = self.sec + 1
        self.speed_now = self.sec * self.acceleration
    
    def stopping(self):
        if self.sec == 0:
            print('Вы стоите')
        else:
            self.sec = self.sec - 1
            self.speed_now = self.sec * self.acceleration
