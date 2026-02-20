def SecLarEle(lis):
    lar = -1
    secLar = -1

    for num in lis:
        if num > lar:
            secLar = lar
            lar = num
        elif num > secLar and num != lar:
            secLar = num

    return secLar


ls = [1,4,5,56,67,8,9,0,34,5,6,7] 

print(SecLarEle(ls))
