class carro:
    def __init__(self, marca, modelo, ano, km=0):
     self.marca = marca
     self.modelo = modelo
     self.ano = ano
     self.km = 0

    def informacoes(self):
        print(f"marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, kilometro: {self.km}")
        
    def acelerar(self, distancia):
        self.km += distancia
        print(f'o carro percorreu {distancia} kilometros')
#objeto

c = carro("Ferrari", "Pegasus", 2024)

c.informacoes()

c.acelerar(10)

#Carro Eletrico

class carroE(carro):
    def __init__(self, marca, modelo, ano, autonomia, km=0):
        super().__init__(marca, modelo, ano, km)
        self.autonomia = autonomia
    def informacoes(self):
        super().informacoes()
        print(f"autonomia: {self.autonomia} km")
        
ce = carroE("Tesla", "ModelS", 2022, 400)

ce.informacoes()

ce.acelerar(50)