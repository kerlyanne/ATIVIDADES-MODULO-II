class animal:
    def fazer(self):
        return "som de animal"

class cachorro(animal):
    def falar(self):
        return "au au"

class gato(animal):
    def falar(self):
        return "Miau!"

animais = [cachorro(), gato(), cachorro(), gato()]
for animal in animais:
    print(animal.falar())



class Forma:
    def area(self):
        return 0

class quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio * self.raio

def mostrar_area(formas):
    for forma in formas:
        print("Área:", forma.area())

formas = [quadrado(4), circulo(3), quadrado(2)]
mostrar_area(formas)



class funcionario:
    def salario(self):
        return 0
class gerente(funcionario):
    def salario(self):
        return 5000

class Estagiario(funcionario):
    def salario(self):
        return 1500

funcionarios = [gerente(), Estagiario(), gerente(), Estagiario()]
for f in funcionarios:
    print("salario:", f.salario())



class Veiculo:
    def mover(self):
        print("Veículo em movimento...")

class Carro(Veiculo):
    def mover(self):
        print("Dirigindo...")
class Bicicleta(Veiculo):
    def mover(self):
        print("Pedalando...")
class Aviao(Veiculo):
    def mover(self):
        print("Voando...")
veiculos = [Carro(), Bicicleta(), Aviao()]

for v in veiculos:
    v.mover()