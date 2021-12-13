try:
    N=int(input("Введите число от 1 до 100:"))
except ValueError:
    print("Вы ошибаетесь милорд, это не число")
else:
    if 0>N>100:
        print("Читайте условие внимательнее, млорд")
    else:
        if 11<=N<=19 or N%10==1:
            print("год")
        else:
            if 2<=N%10<=4:
                print("года")
            else:
                print("лет")
