class tipoJogador:
    def __init__(self, impulsivo, exigente, cauteloso, aleatorio, status, nome):
        self.impulsivo = impulsivo
        self.exigente = exigente
        self.cauteloso = cauteloso
        self.aleatorio = aleatorio
        self.nome = nome
        self.status = True

        def foraDoJogo(self):
            self.status = False

        @property
        def impulsivo(self):
            return self.impulsivo

        @impulsivo.setter
        def impulsivo(self, impulsivo):
            self.impulsivo = impulsivo

        @property
        def exigente(self):
            return self.exigente

        @exigente.setter
        def exigente(self, exigente):
            self.exigente = exigente

        @property
        def cauteloso(self):
             return self.cauteloso

        @cauteloso.setter
        def cauteloso(self, cauteloso):
            self.cauteloso = cauteloso

        @property
        def aleatorio(self):
             return self.aleatorio

        @aleatorio.setter
        def aleatorio(self, aleatorio):
            self.aleatorio = aleatorio

        @property
        def nome(self):
            return self.nome

        @nome.setter
        def nome(self, nome):
            self.nome = nome

class Propriedade(tipoJogador):
    def __init__(self, ctoVenda, aluguel, proprietario, comprada):
        self.ctoVenda = ctoVenda
        self.aluguel = aluguel
        self.proprietario = proprietario
        self.comprada = comprada

        def comprar(self):
            self.comprada = True

        def perder(self):
            self.comprada = False

        @property
        def ctoVenda(self):
            return self.ctoVenda

        @ctoVenda.setter
        def ctoVenda(self, ctoVenda):
            self.ctoVenda = ctoVenda

        @property
        def aluguel(self):
            return self.aluguel

        @aluguel.setter
        def aluguel(self, aluguel):
            self.aluguel = aluguel

        @property
        def proprietario(self):
             return self.proprietario

        @proprietario.setter
        def propretario(self, proprietario):
            self.proprietario = proprietario
