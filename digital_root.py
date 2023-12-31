'''DESCRIPTION:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''

def digital_root(n):
    #transformando um inteiro em lista
    lista = list(map(int, str(n)))
        #somando os valores da lista
    total = sum(lista)
    while total > 9:
        lista = list(map(int, str(total)))
        total = sum(lista)
    if total < 10:
        return total

    a = digital_root(493193)

    print(a)

    lista =[1, 2, 3 ,4, 5]
    x = lambda(x : x*  2)