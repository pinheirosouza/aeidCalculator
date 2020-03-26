import time
class Calculadora():

    def soma(self, a, b):
        star = time.time()

        cont_a = a
        cont_b = b
        somaproximo = 0
        lista_a = []
        lista_b = []
        resultado = []

        # tratando a entrada

        if cont_a == cont_b:
            while cont_a != 0:
                lista_a.append(5) 
                cont_a-=1
            while cont_b != 0:
                lista_b.append(6)
                cont_b-=1
        
        elif cont_a < cont_b:
            while cont_a != 0:
                lista_a.append(5) 
                cont_a-=1
            while cont_b != 0:
                lista_b.append(6) 
                cont_b-=1
            for n in range(b-a):
                lista_a.insert(0, 0)
        
        elif cont_a > cont_b:
            while cont_a != 0:
                lista_a.append(5) 
                cont_a-=1
            for n in range(a-b):
                lista_b.insert(0, 0)
            
            while cont_b != 0:
                lista_b.append(6) 
                cont_b-=1
        
        cont_a = len(lista_a) -1
        cont_b = len(lista_b) -1
       
        # fazendo operações
         
        for key, value in enumerate(lista_a):
            if (lista_a[cont_a] + lista_b[cont_b] + somaproximo) < 10:
                resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo))
                somaproximo = 0
            elif (lista_a[cont_a] + lista_b[cont_b] + somaproximo) >= 10:
                if 0 == cont_a:
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    resultado.insert(0, 1)
                else:
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    somaproximo = 1
            cont_a-=1
            cont_b-=1
            
        end = time.time()
        return resultado,end-star

    def multiplica(self, a, b):
        pass

while True:
    calc = Calculadora()
    print("Bem vindo:\n 1 - Soma\n 2 - Multiplicação")
    select = int(input("Selecione uma operação:"))
    if select == 1:
        a = int(input("Digite o número de algarismos que serão atribuídos a variável a:\n"))
        b = int(input("Digite o número de algarismos que serão atribuídos a variável b:\n"))
        print("O resultado eh %a\nRealizado em %10.35f segundos"%calc.soma(a, b))
    if select == 2:
        a = input("Digite o número de algarismos que serão atribuídos a variável a:\n")
        b = input("Digite o número de algarismos que serão atribuídos a variável b:\n")
        print(calc.multiplica(a, b))

