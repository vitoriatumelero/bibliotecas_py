import numpy as np #colocar sigla para simplificar

array= np.array ([1,2,3,4,5]) #método, em poo é def, funções

print(array)

elemento= array [2]
print (elemento)

array_2d= np.array ([[1,2,3], [4,5,6], [7,8,9]])

print (array_2d)

elemento_2d= array_2d [1,2]
print (elemento_2d)

array1= np.array ([1,2,3])
array2 = np.array ([4,5,6 ])
soma= array1 +array2
print(soma)

multiplicacao= array1*2
print (multiplicacao)

divisao= array1/array2
print(divisao)

array = np.array([1, 2, 3, 4, 5])
media = np.mean(array)
print(media)


soma = np.sum(array)
print(soma)

desvio_padrao = np.std(array)
print(desvio_padrao)


array = np.array([1, 2, 3, 4, 5])

selecao_indices = array[1:4]  
print(selecao_indices)


array = np.array([1, 4, 2, 5, 3])

selecao_condicao = array[array > 3]  
print(selecao_condicao)


array_2d = np.array([[1, 2, 3], [4, 5, 6]])

transposta = array_2d.T  
print(transposta)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

concatenacao_h = np.hstack((array1, array2))
print(concatenacao_h)

concatenacao_v = np.vstack((array1, array2))
print(concatenacao_v)