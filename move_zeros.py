
"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""
#Criando função com uma lista de números como parâmetro
def move_zeros(lst):
    #Iniciando uma variável que vai contar a quantidade de 0
    i=0
    #laço while para retirar todos os zeros e incrementar o valor de
    # "I" para saber quantos 'zeros' havia na lista
    while 0 in lst:
        i+=1
        lst.remove(0)
        #Um for para adicionar os 'zeros' a lista final"
    for x in range(0,i):
        lst.append(0)
    return lst