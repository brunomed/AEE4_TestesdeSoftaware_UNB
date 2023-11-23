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
    
    if numbers[0:2] == "//":
        delimitador, string_num = numbers[2:].split("\n", 1)

        if not delimitador:
            raise Exception("Invalid delimiter")

        for i in range(len(string_num)):
            if string_num[i] != delimitador and not string_num[i].isnumeric():
                raise Exception(f"'{delimitador}' esperado, mas encontrado '{string_num[i]}'")
            
        
        return sum([int(num) for num in re.split(delimitador, string_num)])
    
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
    

    
add("//|\n1|2,3")
    