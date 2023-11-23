

def add(numbers: str) -> int:
    if numbers == '':
        return 0
    
    # retorna o proprio numero
    if len(numbers) == 1:
        return int(numbers)
    
    # soma os numeros
    if ',' in numbers:
        numbers = numbers.split(',')
        return sum(numbers)
    
    # nao permite valor decimal
    if '.' in numbers:
        raise Exception('ERRO DECIMAL')
    
    
    