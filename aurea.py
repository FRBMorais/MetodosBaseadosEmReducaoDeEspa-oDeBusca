import numpy as np


class Aurea:
    """ Otimiza uma função utilizando o método Áurea
        parâmetros de entrada
        intervalo a ser otmizado (a, b)
        analise --> se refere a função a ser analisada
        --> mínimo a
        --> máximo b
        --> tol = tolerância da otimização, por padrão 10e-8
        self.iterações --> quantidade de iterações que o programa demorou para convergir
        self.caminho --> histórico de onde a otimização buscou
        self.residuo --> modulo do último resultado encontrado menos o anterior a ele,
        parâmetro para avaliar a convergência do programa
        """
    def __init__(self,
                 a,
                 b,
                 analise,
                 tol=10e-8,
                 tal=0.5 * (5 ** (1/2) - 1)):
        self.a = a
        self.b = b
        self.alfa = a + (1 - tal) * (b - a)
        self.beta = a + tal * (b - a)
        self.c = None
        self.tol = tol
        self.ya = None
        self.yb = None
        self.yc = None
        self.tal = tal
        self.iteracoes = 0
        self.analise = analise
        self.caminho = []
        self.valor = []
        self.residuo = []

    def funcao(self, ponto):
        if self.analise == 0:
            lenn = 600  # cm^4
            e = 50_000  # KN/cm^2
            i = 30_000  # cm^4
            w = 2.5  # KN/cm
            return (w / (120 * e * i * lenn)) * (-ponto ** 5 + 2 * lenn ** 2 * ponto ** 3 - lenn ** 4 * ponto)
        elif self.analise == 1:
            return sum([ponto ** 2])
        elif self.analise == 2:
            return (1.5 - ponto) ** 2 + (2.25 - ponto) ** 2 + (2.625 - ponto ** 2)
        elif self.analise == 3:
            return 2 * ponto ** 2 - 1.05 * ponto ** 4 + ponto ** 6 / 6
        elif self.analise == 4:
            return 10 + sum([(ponto ** 2 - 10 * np.cos(2 * np.pi * ponto))])

    def metodo(self):
        self.ya = self.funcao(self.alfa)
        self.yb = self.funcao(self.beta)
        while abs(self.a - self. b) > self.tol:
            self.iteracoes += 1
            if self.ya > self.yb:
                self.a = self.alfa
                self.alfa = self.beta
                self.ya = self.yb
                self.beta = self.a + self.tal * (self.b - self.a)
                self.yb = self.funcao(self.beta)

                self.caminho.append(self.beta)
                self.valor.append(self.yb)
                self.residuo.append(abs(self.ya - self.yb))

            elif self.ya < self.yb:
                self.b = self.beta
                self.beta = self.alfa
                self.yb = self.ya
                self.alfa = self.a + (1 - self.tal) * (self.b - self.a)
                self.ya = self.funcao(self.alfa)

                self.caminho.append(self.alfa)
                self.valor.append(self.ya)

            elif self.ya == self.yb:
                break
            else:
                print("Entre com um novo intervalo [a, b]")
