
def decimal_para_binario(num):
    return str(num) if num < 2 else decimal_para_binario(num // 2) + str(num % 2)
print(decimal_para_binario(13)) #1101



"""
def decimal_para_binario(num):
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    
    return decimal_para_binario(num // 2) + str(num % 2)
"""
