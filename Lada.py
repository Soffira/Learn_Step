from abc import ABC, abstractmethod
from Transport import Cars

class Lada_XRay(Cars):
    sec = 0
    racing = 11.4
    acceleration = 2.44
    refueling = 0

    @abstractmethod
    def refuel2(self):
        self.refueling += 2
        print('Литров заправлено', self.refueling)

Lada = Lada_XRay()
Lada.accelerating()
Lada.accelerating()
Lada.know_speed()
Lada.stopping()
Lada.know_speed()
Lada.stopping()
Lada.know_speed()
Lada.stopping()
Lada.know_speed()

Lada.refuel2()
Lada.refuel2()