import re

def trata_num(num):
    for i in range(len(num)):
        if '\n' in num[i]:
            pass


def add(numbers: str) -> int:
    if numbers == '':
        return 0
    
    # retorna o proprio numero
    if len(numbers) == 1:
        return int(numbers)
    
    # soma os numeros
    if '\n' in numbers:
        try:
            num_list = [int(num) for  num in re.split(',|\n', numbers)]
            return sum(num_list)
        
        except:
            raise Exception('Invalid String')
            

    if ',' in numbers:
        numbers = numbers.split(',')

        try:
            return sum([int(n) for n in numbers])
        
        except:
            raise Exception('Invalid String')
        

    
    # nao permite valor decimal
    if '.' in numbers:
        raise Exception('ERRO DECIMAL')
    


    
    