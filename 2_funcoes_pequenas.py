def clean_data(data):
    """Remove espaços e converte para minúsculas"""
    return [x.strip().lower() for x in data]

def count_occurrences(items):
    """Conta a ocorrência de cada item"""
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

def process(data):
    cleaned = clean_data(data)
    return count_occurrences(cleaned)