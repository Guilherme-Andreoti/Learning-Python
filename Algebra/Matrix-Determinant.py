def determinante(matriz):
    
    ordem = len(matriz) 

    if len(matriz) < 1 or len(matriz[0]) < 1: raise ValueError('Informe uma matriz válida.')
    if ordem != len(matriz[0]): raise ValueError('Não é possível calcular o determinante de uma matriz não quadrada.')
    
    for i in range(ordem):
        if len(matriz[i])  != ordem: raise ValueError('Matriz inválida')  



    if ordem == 1: 
        return matriz[0][0] 
    elif ordem == 2: 
        return (matriz[0][0] * matriz[1][1]) - (matriz[1][0]*matriz[0][1])
    elif ordem == 3: 
        for i in range(ordem):
            for j in range(ordem): 

                if j != 0:
                    col = (j+i)*i
                    if col > ordem: col -= ordem 
                else:
                    col = i 

                print(i,col)
        return 0
    else:
        return 0


        
             

teste = [[5,1,3],[3,-2,8],[3,-2,9]]
print(determinante(teste))
    