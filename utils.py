def add_numbers(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

def parse_query_string(query):
    # Basic query string parser
    if not query:
        return {}
    pairs = query.split("&")
    result = {}
    for pair in pairs:
        key_value = pair.split("=")
        if len(key_value) == 2:
            result[key_value[0]] = key_value[1]
    return result
