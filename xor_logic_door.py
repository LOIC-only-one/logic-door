a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]

def xor(a:list,b:list)->list:

    if len(a) == len(b):

        tab_final = []

        for i in range(len(a)):
            if a[i] == b[i]:
                tab_final.append(0)
            elif a[i] == 1 and b[i] == 0 or a[i] == 0 and b[i] == 1:
                tab_final.append(1)

        return tab_final


    return False


print(xor(a,b))
