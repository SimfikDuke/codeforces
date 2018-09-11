names = {
        0 : 'Sheldon',
        1 : 'Leonard',
        2 : 'Penny',
        3 : 'Rajesh',
        4 : 'Howard'    
        }

def f(n):
    n -= 1
    m = 0
    i = 1

    

    while m + i * 5 <= n:
        m += i * 5
        i *= 2

    ans = int((n-m)/i)

    return names[ans]

print(f(int(input())))