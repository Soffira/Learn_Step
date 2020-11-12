from abc import ABC, abstractmethod
from Transport import Cars

class Lamb_Diablo(Cars):
    sec = 0
    racing = 4.1
    acceleration = 6.78
    refueling = 0
    
    @abstractmethod
    def refuel(self):
        self.refueling += 1
        print('Литров заправлено', self.refueling)


Lamb = Lamb_Diablo()
Lamb.stopping()
Lamb.know_speed()
Lamb.accelerating()
Lamb.accelerating()
Lamb.know_speed()
Lamb.refuel()
Lamb.refuel()
