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

def binary_logicgates(input1, input2, logictype):
    if logictype.lower() == "and":
        if input1 == 1 and input2 == 1:
            return 1
        return 0
    elif logictype.lower() == "not":
        if input1 == 1:
            return 0
        elif input1 == 0:
            return 1
    elif logictype.lower() == "or":
        if input1 == 1 or input2 == 1:
            return 1
        return 0