# Copia a matriz garantindo independência entre as mesmas
def copiaMatriz(matriz_original):
    matriz_copia = [row[:] for row in matriz_original]
    return matriz_copia 

def validaMatrizQuadrada(matriz_original,ordem):
    
    # Verifica se possuí um elemento ao menos
    if len(matriz_original) < 1 or len(matriz_original[0]) < 1: raise ValueError('Informe uma matriz válida.')

    # Verifica se é quadrada linha a linha
    for i in range(ordem):
        if len(matriz_original[i])  != ordem: raise ValueError('Por favor, forneça uma matriz quadrada.') 

# Calcula o determinante
def determinante(matriz_original):
    
    ordem = len(matriz_original)

    # Garante que a matriz é quadrada
    validaMatrizQuadrada(matriz_original,ordem)

    # Efetua o cálculo de acordo com a ordem. 

    if ordem == 1: 
        return matriz_original[0][0] 

    elif ordem == 2: 
        return matriz_original[0][0] * matriz_original[1][1] - matriz_original[1][0]*matriz_original[0][1]
    
    else:
            
        indices = list(range(len(matriz_original)))
        total = 0 
        
        for col in indices:  # Para cada coluna calcula a submatriz
            matriz_auxiliar = copiaMatriz(matriz_original)  # Efetua uma cópia
            matriz_auxiliar = matriz_auxiliar[1:]  # Apaga a primeira linha
            altura = len(matriz_auxiliar)

            for i in range(altura):  
                matriz_auxiliar[i] = matriz_auxiliar[i][0:col] + matriz_auxiliar[i][col+1:]  

            sinal = (-1) ** (col % 2)  # Altera os sinais de acordo com a necessidade
            sub_det = determinante(matriz_auxiliar)  # Passa recursivamente
            total += sinal * matriz_original[0][col] * sub_det  # Incementa o total com base na recursão

        return total

def cramer(matriz_original,matriz_resultado):
    ordem = len(matriz_original) 
    
    matriz_resultado_icognitas =[]

    determinante_geral = determinante(matriz_original)

    for i in range(ordem):
        matriz_copia = copiaMatriz(matriz_original)
        for j in range(ordem): 
            matriz_copia[j][i] = matriz_resultado[j][0] #susbtitui as icógnitas na coluna correspondente

        #Salva o resultado da equação na matriz correspondente
        matriz_resultado_icognitas.append(determinante(matriz_copia) / determinante_geral)

    #Exibe o resultado    
    for i in range(ordem):
        print('A icógnita ',i + 1,' possui o valor: ',matriz_resultado_icognitas[i])


def matriz(nLinhas, nColunas):
    matriz = []
    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            valor = int(input("Digite o elemento [" + str(i+1) + "][" + str(j+1) + "]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def exibirMatriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for l in range(linhas):
        line = ''
        for c in range(colunas):
            line += '   ' + (' ' if matriz[l][c]  > 0 else '')  + str(matriz[l][c]) + '   '
        print(line)


linhas = int(input("Digite o numero de linhas da matriz principal:"))
colunas = int(input("Digite o numero de colunas da matriz principal:"))

ordem = linhas

matriz_principal = matriz(linhas,colunas) # Cria a matriz de acordo com o número de linhas e colunas desejadas
validaMatrizQuadrada(matriz_principal,ordem) # Garante que é uma matriz quadrada, se não for gera uma exceção

print('Agora entre com os dados da matriz de resultados')
matriz_resultado = matriz(ordem,1) # Precisa ter a mesma quantidade de linhas que a anterior, mas somente uma coluna

print('Matriz Principal:')
exibirMatriz(matriz_principal) #Exibe a matriz principal

print('Matriz de Resultados:')
exibirMatriz(matriz_resultado) # Exibe a matriz principal

print('Aplicação da Regra de Cramer:')
cramer(matriz_principal,matriz_resultado) # Calcula as icógnitas de acordo com a regra de Cramer e exibe o resultado