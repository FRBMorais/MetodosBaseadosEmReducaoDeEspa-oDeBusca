# Autor: Felipe Rosa
# Estudante de Engenharia Aeronáutica para o curso de Otimizações de Sistemas Aeronáuticos

import numpy as np
import matplotlib.pyplot as plt
from bisseccao import Bisseccao
from aurea import Aurea
from fibonacci import Fibonacci


# Otimização irrestrita de problemas de uma variável (métodos baseados na redução do espaço de busca)

"""
Os métodos funcionam bem para funções com apenas um máximo ou um mínimo
Métodos para aplicar a função em funções com mais de um mínimo local
1. particionar o intervalo desejado em intervalos menores e avaliar todos eles e encontrar o mínimo global
2. não colocar intervalos simétricos
"""

# Função apresentada no livro
lenn = 600  # cm^4
e = 50_000  # KN/cm^2
i = 30_000  # cm^4
w = 2.5  # KN/cm

x0 = np.linspace(0, 600, num=100)
x1 = np.linspace(-5.15, 5.15, num=100000)

"""
Funções que seram analisadas neste algoritmo
1. Função Default do livro -- link :: y
2. Sphere Function ZDT com apenas uma variável y = 0 :: y1 
3. Beale Function ZDT com apenas uma variável y = 0 :: y2
4. Three Ramp Camel Function ZDT com apenas uma variável y = 0 :: y3
5. Rastrigin Function ZDT com apenas uma variável y = 0 :: y4
"""
y = [(w / (120 * e * i * lenn)) * (-p ** 5 + 2 * lenn ** 2 * p ** 3 - lenn ** 4 * p) for p in x0]  # Função Default
y1 = [sum([p ** 2]) for p in x1]  # Sphere function
y2 = [((1.5 - x) ** 2 + (2.25 - x) ** 2 + (2.625 - x ** 2)) for x in x1]  # Beale Function
y3 = [(2 * x ** 2 - 1.05 * x ** 4 + x ** 6 / 6) for x in x1]  # Three ramp Camel
y4 = [(10 + sum([(x ** 2 - 10 * np.cos(2 * np.pi * x))])) for x in x1]  # Rastrigin


"""
Plot das funções análisadas
"""

plt.subplot(2, 3, 1)
plt.plot(x0, y)
plt.title('Default problem')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')


plt.subplot(2, 3, 2)
plt.plot(x1, y1)
plt.title('Sphere Function')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 3, 3)
plt.plot(x1, y2)
plt.title('Beale Function')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 3, 4)
plt.plot(x1, y3)
plt.title('Three-ramp-camel')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 3, 5)
plt.plot(x1, y4)
plt.title('Rastrigin')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

bi0 = Bisseccao(0, 600, 0.01, 0)
bi0.metodo()
print(f'Default problem\n'
      f'Método Bissecção\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(bi0.c, 3)}\n'
      f'Valor da função no ponto: {round(bi0.yc, 3)}\n'
      f'Quantidade de iteacoes: {bi0.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x0, y, bi0.caminho, bi0.valor, 'o--')
plt.title('Default problem')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.grid()
plt.savefig(f"Default problem Bisseccao.png", dpi=300)
plt.show()

plt.plot(range(len(bi0.residuo)), bi0.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Default problem Bisseccao - residuo.png", dpi=300)
plt.show()

bi1 = Bisseccao(-6, 4, 0.01, 1)
bi1.metodo()
print(f'Sphere function\n'
      f'Método Bissecção\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(bi1.c, 3)}\n'
      f'Valor da função no ponto: {round(bi1.yc, 3)}\n'
      f'Quantidade de iteacoes: {bi1.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y1, bi1.caminho, bi1.valor, 'o--')
plt.title('Sphere function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Sphere function Bisseccao.png", dpi=300)
plt.show()

plt.plot(range(len(bi1.residuo)), bi1.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Sphere function Bisseccao - residuo.png", dpi=300)
plt.show()

bi2 = Bisseccao(-6, 4, 0.0001, 2)
bi2.metodo()
print(f'Beale Function\n'
      f'Método Bissecção\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(bi2.c, 3)}\n'
      f'Valor da função no ponto: {round(bi2.yc, 3)}\n'
      f'Quantidade de iteacoes: {bi2.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y2, bi2.caminho, bi2.valor, 'o--')
plt.title('Beale function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Beale function Bisseccao.png", dpi=300)
plt.show()

plt.plot(range(len(bi2.residuo)), bi2.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Beale function Bisseccao - residuo.png", dpi=300)
plt.show()

bi3 = Bisseccao(-2, 0.5, 0.01, 3)
bi3.metodo()
print(f'Three ramp camel\n'
      f'Método Bissecção\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(bi3.c, 3)}\n'
      f'Valor da função no ponto: {round(bi3.yc, 3)}\n'
      f'Quantidade de iteacoes: {bi3.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y3, bi3.caminho, bi3.valor, 'o--')
plt.title('Three Ramp Camel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"ThreeRampCamel Bisseccao.png", dpi=300)
plt.show()

plt.plot(range(len(bi3.residuo)), bi3.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"ThreeRampCamel Bisseccao - residuo.png", dpi=300)
plt.show()

bi4 = Bisseccao(-0.8, 0.7, 0.01, 4)
bi4.metodo()
print(f'Rastrigin\n'
      f'Método Bissecção\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(bi4.c, 3)}\n'
      f'Valor da função no ponto: {round(bi4.yc, 3)}\n'
      f'Quantidade de iteacoes: {bi4.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y4, bi4.caminho, bi4.valor, 'o--')
plt.title('Rastrigin')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Rastrigin Bisseccao.png", dpi=300)
plt.show()

plt.plot(range(len(bi4.residuo)), bi4.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Rastrigin Bisseccao - residuo.png", dpi=300)
plt.show()

# Método 2 - Seção Áurea ----------------------------------------------------------------------------------
au0 = Aurea(0, 600, 0)
au0.metodo()
print(f'Default problem\n'
      f'Método Aurea\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(au0.b, 3)}\n'
      f'Valor da função no ponto: {round(au0.yb, 3)}\n'
      f'Quantidade de iteacoes: {au0.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x0, y, au0.caminho, au0.valor, 'o--')
plt.title('Default problem')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.grid()
plt.savefig(f"Default problem Aurea.png", dpi=300)
plt.show()

plt.plot(range(len(au0.residuo)), au0.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Default problem Aurea - residuo.png", dpi=300)
plt.show()


au1 = Aurea(-6, 4, 1)
au1.metodo()
print(f'Sphere function\n'
      f'Método Aurea\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(au1.b, 3)}\n'
      f'Valor da função no ponto: {round(au1.yb, 3)}\n'
      f'Quantidade de iteacoes: {au1.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y1, au1.caminho, au1.valor, 'o--')
plt.title('Sphere function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Sphere function Aurea.png", dpi=300)
plt.show()

plt.plot(range(len(au1.residuo)), au1.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Sphere function Aurea - residuo.png", dpi=300)
plt.show()


au2 = Aurea(-6, 4, 2)
au2.metodo()
print(f'Beale Function\n'
      f'Método Aurea\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(au2.b, 3)}\n'
      f'Valor da função no ponto: {round(au2.yb, 3)}\n'
      f'Quantidade de iteacoes: {au2.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y2, au2.caminho, au2.valor, 'o--')
plt.title('Beale function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Beale function Aurea.png", dpi=300)
plt.show()

plt.plot(range(len(au2.residuo)), au2.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Beale Aurea - residuo.png", dpi=300)
plt.show()


au3 = Aurea(-6, 4, 3)
au3.metodo()
print(f'Three ramp camel\n'
      f'Método Aurea\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(au3.b, 3)}\n'
      f'Valor da função no ponto: {round(au3.yb, 3)}\n'
      f'Quantidade de iteracoes: {au3.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y3, au3.caminho, au3.valor, 'o--')
plt.title('Three Ramp Camel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"ThreeRampCamel Aurea.png", dpi=300)
plt.show()

plt.plot(range(len(au3.residuo)), au3.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Three Ramp Camel Aurea - residuo.png", dpi=300)
plt.show()


au4 = Aurea(-0.8, 0.7, 4)
au4.metodo()
print(f'Rastrigin\n'
      f'Método Aurea\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(au4.b, 3)}\n'
      f'Valor da função no ponto: {round(au4.yb, 3)}\n'
      f'Quantidade de iteracoes: {au4.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y4, au4.caminho, au4.valor, 'o--')
plt.title('Rastrigin')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Rastrigin Aurea.png", dpi=300)
plt.show()

plt.plot(range(len(au4.residuo)), au4.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Rastrigin Aurea - residuo.png", dpi=300)
plt.show()

# Método 3 - Fibonacci  -----------------------------------------------------------------------------------------
fb0 = Fibonacci(0, 600, 0)
fb0.metodo()
print(f'Default problem\n'
      f'Método Fibonacci\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(fb0.b, 3)}\n'
      f'Valor da função no ponto: {round(fb0.yb, 3)}\n'
      f'Quantidade de iteacoes: {fb0.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x0, y, fb0.caminho, fb0.valor, 'o--')
plt.title('Default problem')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.grid()
plt.savefig(f"Default problem Fibonacci.png", dpi=300)
plt.show()

plt.plot(range(len(fb0.residuo)), fb0.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Default problem Fibonacci - residuo.png", dpi=300)
plt.show()

fb1 = Fibonacci(-6, 4, 1)
fb1.metodo()
print(f'Sphere function\n'
      f'Método Fibonacci\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(fb1.b, 3)}\n'
      f'Valor da função no ponto: {round(fb1.yb, 3)}\n'
      f'Quantidade de iteacoes: {fb1.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y1, fb1.caminho, fb1.valor, 'o--')
plt.title('Sphere function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Sphere function Fibonacci.png", dpi=300)
plt.show()

plt.plot(range(len(fb1.residuo)), fb1.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Sphere function Fibonacci - residuo.png", dpi=300)
plt.show()

fb2 = Fibonacci(-6, 4, 2)
fb2.metodo()
print(f'Beale Function\n'
      f'Método Fibonacci\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(fb2.b, 3)}\n'
      f'Valor da função no ponto: {round(fb2.yb, 3)}\n'
      f'Quantidade de iteacoes: {fb2.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y2, fb2.caminho, fb2.valor, 'o--')
plt.title('Beale function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Beale function Fibonacci.png", dpi=300)
plt.show()

plt.plot(range(len(fb2.residuo)), fb2.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Beale function Fibonacci - residuo.png", dpi=300)
plt.show()

fb3 = Fibonacci(-6, 4, 3)
fb3.metodo()
print(f'Three ramp camel\n'
      f'Método Fibonacci\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(fb3.b, 3)}\n'
      f'Valor da função no ponto: {round(fb3.yb, 3)}\n'
      f'Quantidade de iteracoes: {fb3.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y3, fb3.caminho, fb3.valor, 'o--')
plt.title('Three Ramp Camel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"ThreeRampCamel Fibonacci.png", dpi=300)
plt.show()

plt.plot(range(len(fb3.residuo)), fb3.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Thee Ramp Camel Fibonacci - residuo.png", dpi=300)
plt.show()

fb4 = Fibonacci(-0.8, 0.7, 4)
fb4.metodo()
print(f'Rastrigin\n'
      f'Método Fibonacci\n {"-" * 30}\n'
      f'Ponto Ótimo: {round(fb4.b, 3)}\n'
      f'Valor da função no ponto: {round(fb4.yb, 3)}\n'
      f'Quantidade de iteracoes: {fb4.iteracoes}\n'
      f'{"-" * 30}')
plt.plot(x1, y4, fb4.caminho, fb4.valor, 'o--')
plt.title('Rastrigin')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig(f"Rastrigin Fibonacci.png", dpi=300)
plt.show()

plt.plot(range(len(fb4.residuo)), fb4.residuo, 'o--')
plt.title('Residuo')
plt.xlabel('Iteracoes')
plt.ylabel('abs(ya - yb)')
plt.grid()
plt.savefig(f"Rastrigin Fibonacci - residuo.png", dpi=300)
plt.show()
