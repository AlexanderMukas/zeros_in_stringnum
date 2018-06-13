# -*- coding: utf-8 -*- 
#var_string = "00000111010000111101010101010100011010100011010000010"
var_string = input("Введите тестовое число: ")

def main(var_string):
    print("Выбранное число : " + var_string)
    print("Оно состоит из : " + str(len(var_string)) + " цифр.")
    temp = number = max_zero = 0  
    
    for number in var_string:
        # Попался ноль
        if(number == str(0)):
            max_zero+=1
            if(temp < max_zero):
                temp = max_zero
        else:
            max_zero = 0
            continue
    return temp
    
result = 'Максимальное кол-во нулей между цифрами= ' + str(main(var_string))
print(result)
