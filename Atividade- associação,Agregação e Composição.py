class motor:
    def __init__(self, potencia):
        self.potencia = potencia

class carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor

    def detalhes(self):
        return f"Modelo: {self.modelo}, Potência do motor: {self.motor.potencia}cv"
motor1 = motor(150)
carro1 = carro("Sedan", motor1)
print(carro1.detalhes())



class Professor:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area

    def detalhes(self):
        return f"{self.nome} ({self.area})"


class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []   
    def contratar(self, professor):
        self.professores.append(professor)
    def mostrar_professores(self):
        print(f"Professores da universidade {self.nome}:")
        for prof in self.professores:
            print(prof.detalhes())
uni = Universidade("UFABC")
prof1 = Professor("Ana", "Matemática")
prof2 = Professor("Bruno", "Física")
uni.contratar(prof1)
uni.contratar(prof2)
uni.mostrar_professores()


class Autor:
    def __init__(self, nome):
        self.nome = nome
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 
    def info(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor.nome}")
autor1 = Autor("cassandra clare")
autor2 = Autor("Hannah Grace")
livro1 = Livro("cidade das almas perdidas", autor1)
livro2 = Livro("No calor do momento", autor2)

livro1.info()
livro2.info()