class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Criação de lista vazia para armazenar os valores da soma do número alvo
        lista=[]
        #Utilizando um for duplo que irá percorrer a mesma lista 2 vezes
        for i in range(0,len(nums)):
            #Aqui temos no primeiro paramentro do range(i+1) para que não seja repetido o mesmo valor na busca com a funcao index()
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:#Se os valores dos items dos repectivos indices tenham o resultado do número alvo 
                        lista.append(i)
                        lista.append(j)
                        #Será armazenado os valores na lista e exibido
                        return lista



                        
sol = Solution()
nums = [3,3]
target = 6
resultado = sol.twoSum(nums, target)