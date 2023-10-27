class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.esta_latindo = False

    def latir(self):
        if not self.esta_latindo:
            self.esta_latindo = True
            print(f'{self.nome}, o cachorro da raça {self.raca}, está latindo.')
        else:
            print(f'{self.nome} já está latindo.')

    def parar_de_latir(self):
        if self.esta_latindo:
            self.esta_latindo = False
            print(f'{self.nome} parou de latir.')
        else:
            print(f'{self.nome} não está latindo no momento.')

# Programa demonstrativo
if __name__ == "__main__":
    meu_cachorro = Cachorro("leão", 3, "Labrador")
    
    meu_cachorro.latir()
    meu_cachorro.parar_de_latir()
    meu_cachorro.latir()
