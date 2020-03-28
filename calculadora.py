import time

class Calculadora():
   
    def listToInt(self, list): 
        s = [str(i) for i in list] 
        res = int("".join(s)) 
        return res

    def soma(self, a, b):
        start = time.time()
        cont_a = 0
        cont_b = 0
        somaproximo = 0
        lista_a = []
        lista_b = []
        resultado = []

        intResultado = 0

        for num in str(a):
            lista_a.append(int(num))

        for num in str(b):
            lista_b.append(int(num))

        # print(lista_a)
        # print(lista_b)

        cont_a = len(lista_a)
        cont_b = len(lista_b)

        # print(cont_a)
        # print(cont_b)

        if cont_a == cont_b:
            pass

        elif cont_a < cont_b:
            for n in range(cont_b - cont_a):
                lista_a.insert(0, 0) 
       
        elif cont_a > cont_b:
            for n in range(cont_a - cont_b):
                lista_b.insert(0, 0) 
        
        cont_a = len(lista_a) - 1
        cont_b = len(lista_b) - 1
        tam = len(lista_a) - 1

        # print("Lista a:", lista_a)
        # print("Lista b:", lista_b)
        
        # fazendo operações
         
        for key, value in enumerate(lista_a):
            # print("key: ",key)
            # print("cont_a", cont_a)
            # print("cont_b", cont_a)
            if (lista_a[cont_a] + lista_b[cont_b] + somaproximo) < 10:
                resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo))
                somaproximo = 0
                # print("Chegou here")
            elif (lista_a[cont_a] + lista_b[cont_b] + somaproximo) >= 10:
                if key == tam:
                    # print("Chegou aqui")
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    resultado.insert(0, 1)
                else:
                    # print("Chegou aqui em baixo")
                    resultado.insert(0, (lista_a[cont_a] + lista_b[cont_b] + somaproximo)%10)
                    somaproximo = 1
            cont_a-=1
            cont_b-=1

            # intResultado = self.listToInt(resultado)

        end = time.time()
        print("Tempo gasto: ", end-start)
        return resultado 
    
    def multiplica(self, a, b):
        pass

while(True):
    calc = Calculadora()
    print("Bem vindo:\n 1 - Soma\n 2 - Multiplicação")
    select = int(input("Selecione uma operação:"))
    if select == 1:
        a = int(input("Digite o número  que será atribuído a variável a:\n"))
        b = int(input("Digite o número  que será atribuído a variável b:\n"))
        print("resultado: ", calc.soma(a, b))
    if select == 2:
        a = input("Digite o número  que será atribuído a variável a:\n")
        b = input("Digite o número  que será atribuído a variável b:\n")
        print(calc.multiplica(a, b))

