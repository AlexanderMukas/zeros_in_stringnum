# -*- coding: utf-8 -*-

var_string = "011101000001"

def main(var_string):
    print("New version!!!")
    first = ""
    z = 0
    zmax = 0
    a = 0
    for i in var_string:
        if (first != i) or (i == "0"):
            first = i
            if (i == "1"):
                a += 1

            if (a == 1) and (i == "0"):
                z += 1

            if (a == 2):
                a = 1
                if (zmax < z):
                    zmax = z
                z=0
        else:
            continue
    return zmax

result = 'Максимальное кол-во нулей между единиц = ' + str(main(var_string))

print("Значение -", var_string)
print(result)
