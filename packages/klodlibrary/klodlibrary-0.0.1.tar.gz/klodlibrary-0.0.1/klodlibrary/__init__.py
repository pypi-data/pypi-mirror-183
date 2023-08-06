def clamp(number, min=1, max=10):
    result = number
    if number < min: result = min
    if number > max: result = max
    return result

def abs(number):
    result = str(number)
    if number < 0: result = result[1:]
    return int(result)

def neg(number):
    result = str(number)
    if number >= 0: result = f"-{result}"
    return int(result)

def opposite(number):
    if number >= 0: return neg(number)
    else: return abs(number)