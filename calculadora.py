class Calculadora():

    def soma(self, a, b):
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
        
        print("Lista a:", lista_a)
        print("Lista b:", lista_b)

        cont_a = len(lista_a) -1
        cont_b = len(lista_b) -1

        print(cont_a)
        print(cont_b)
        
        # fazendo operações
         
        for key, value in enumerate(lista_a):
            print(key)
            print("cont_a", cont_a)
            print("cont_b", cont_a)
            if (lista_a[cont_a] + lista_b[cont_b] + somaproximo) < 10:
                resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo))
                somaproximo = 0
                print("Chegou here")
            elif (lista_a[cont_a] + lista_b[cont_b] + somaproximo) >= 10:
                if key == cont_a and key == 0:
                    print("Chegou aqui")
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    resultado.insert(0, 1)
                else:
                    print("Chegou aqui em baixo")
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    somaproximo = 1
            cont_a-=1
            cont_b-=1
            
        return resultado

    def multiplica(self, a, b):
        pass

while(True):
    calc = Calculadora()
    print("Bem vindo:\n 1 - Soma\n 2 - Multiplicação")
    select = int(input("Selecione uma operação:"))
    if select == 1:
        a = int(input("Digite o número de algarismos que serão atribuídos a variável a:\n"))
        b = int(input("Digite o número de algarismos que serão atribuídos a variável b:\n"))
        print(calc.soma(a, b))
    if select == 2:
        a = input("Digite o número de algarismos que serão atribuídos a variável a:\n")
        b = input("Digite o número de algarismos que serão atribuídos a variável b:\n")
        print(calc.multiplica(a, b))

