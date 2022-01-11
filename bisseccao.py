import numpy as np


class Bisseccao:
    """ Otimiza uma função utilizando o método da bissecção
    parâmetros de entrada
    intervalo a ser otmizado (a, b)
    --> mínimo a
    --> máximo b
    analise --> se refere a função a ser analisada
    --> delta: Passo necessário no método da bissecção
    --> tol = tolerância da otimização, por padrão 10e-8
    self.iterações --> quantidade de iterações que o programa demorou para convergir
    self.caminho --> histórico de onde a otimização buscou
    self.residuo --> modulo do último resultado encontrado menos o anterior a ele,
    parâmetro para avaliar a convergência do programa
    """
    def __init__(self,
                 a,
                 b,
                 delta,
                 analise,
                 tol=10e-8):
        self.a = a
        self.b = b
        self.c = None
        self.delta = delta
        self.tol = tol
        self.ya = None
        self.yb = None
        self.yc = None
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
            return ponto ** 2
        elif self.analise == 2:
            return (1.5 - ponto) ** 2 + (2.25 - ponto) ** 2 + (2.625 - ponto ** 2)
        elif self.analise == 3:
            return 2 * ponto ** 2 - 1.05 * ponto ** 4 + ponto ** 6 / 6
        elif self.analise == 4:
            return 10 + sum([(ponto ** 2 - 10 * np.cos(2 * np.pi * ponto))])

    def metodo(self):
        self.ya = self.funcao(self.a)
        self.yb = self.funcao(self.b)
        self.c = 0.5 * (self.a + self.b)
        self.yc = self.funcao(self.c)
        while abs(self.a - self. b) > self.tol:
            self.caminho.append(self.c)
            self.valor.append(self.yc)
            self.iteracoes += 1
            self.residuo.append(abs(self.yb - self.ya))
            if self.funcao(self.c + self.delta) > self.funcao(self.c - self.delta):
                self.b = self.c
                self.yb = self.yc
                self.c = 0.5 * (self.a + self.b)
                self.yc = self.funcao(self.c)
            elif self.funcao(self.c + self.delta) < self.funcao(self.c - self.delta):
                self.a = self.c
                self.ya = self.yc
                self.c = 0.5 * (self.a + self.b)
                self.yc = self.funcao(self.c)
            elif self.funcao(self.c + self.delta) == self.funcao(self.c - self.delta):
                break
            else:
                print("Entre com um novo intervalo [a, b]")
        self.yc = self.funcao(self.c)

        if -10e-8 < self.yc < 10e-8:
            self.yc = 0

        if -10e-8 < self.c < 10e-8:
            self.c = 0
