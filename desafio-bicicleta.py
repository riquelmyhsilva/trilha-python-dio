class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BIII")

    def parar(self):
        print("Parando...")
        print("Bicicleta parada.")

    def correr(self):
        print("Vrummmm...")

    def get_cor(self):
        return self.cor

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloicross", "2024", 600)

b1.buzinar()
b1.correr()
b1.parar()

b2 = Bicicleta("verde", "monark", "2023", 2340)
Bicicleta.buzinar(b2)
b2.buzinar()
print(b2.get_cor())
print(b2.cor)
print(b2)
