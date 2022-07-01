class Cuenta:

    def _init_(self,numero,fecha,saldo):
        #Variable de instancia
        self.numero=numero
        self.fecha=fecha
        self.saldo=saldo
        
        #getters
    #metodo de retiro
    def retirar(self):
        while True:
            self.retiro=int(input('Digite el valor a retirar:  '))
            if self.retiro>0 and self.retiro<=self.saldo:
                self.saldo-=self.retiro
                return f'El retiro fue exitoso {self.saldo}'
            else:
                return 'fondos insuficientes'
    
    def consigna(self):
        self.consigna=int(input('digite el valor a consignar : '))
        self.saldo+=self.consigna
        return 'consina exitosa'
    
        
    def setNumero(self):
        return self.numero

    def setFecha(self):
        return self.fecha
    
    def setSaldo(self):
        return self.saldo
    
    def informacion(self):
        return 'numero de cuenta: {}\nfecha de apertura: {}\nsaldo de cuenta: {}',format(self.numero,self.fecha,self.saldo)
    
class cuentaCorriente(Cuenta):
    def _init_(self, numero, fecha, saldo, cheque):
        super()._init_(numero, fecha, saldo)
        self.cheque=cheque

    def numerocheque(self):
        return f'su numero de cheque es {self.cheque}'

cuenta1= Cuenta(12345,'26/01/2004',20000)
print(cuenta1.informacion())
print(cuenta1.setSaldo())
print(cuenta1.setFecha())
print(cuenta1.setNumero())

cuenta2= cuentaCorriente(8765,'03/04/2022',30000)
print(cuenta2.informacion())
print(cuenta2.setSaldo())
print(cuenta2.setFecha())
print(cuenta2.setNumero())
print(cuenta2.numerocheque())