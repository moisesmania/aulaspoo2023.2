class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O carro {self.marca} {self.modelo} está ligado.')
        else:
            print('O carro já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print(f'O carro {self.marca} {self.modelo} está desligado.')
        else:
            print('O carro já está desligado.')

    def acelerar(self, quantidade):
        if self.ligado:
            self.velocidade += quantidade
            print(f'O carro acelerou para {self.velocidade} km/h.')
        else:
            print('Você precisa ligar o carro antes de acelerar.')

    def frear(self, quantidade):
        if self.ligado:
            if self.velocidade >= quantidade:
                self.velocidade -= quantidade
                print(f'O carro freou para {self.velocidade} km/h.')
            else:
                print('O carro já está parado.')
        else:
            print('Você precisa ligar o carro antes de frear.')

# Programa demonstrativo
if __name__ == "__main__":
    meu_carro = Carro("Toyota", "Corolla", 2023, "Prata")
    
    meu_carro.ligar()
    meu_carro.acelerar(60)
    meu_carro.frear(20)
    meu_carro.desligar()
