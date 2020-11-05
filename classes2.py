class Transport():
    def speed(self, sec=0, acceleration=5):
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

class Lamb_Diablo(Transport):
    sec = 0
    racing = 4.1
    acceleration = 6.78

class Lada_XRay(Transport):
    sec = 0
    racing = 11.4
    acceleration = 2.44


Lamb = Lamb_Diablo()
Lamb.stopping()
Lamb.know_speed()
Lamb.accelerating()
Lamb.accelerating()
Lamb.know_speed()

Lada = Lada_XRay()
Lada.accelerating()
Lada.accelerating()
Lada.know_speed()

Lada.stopping()
Lada.know_speed()
Lada.stopping()
Lada.know_speed()