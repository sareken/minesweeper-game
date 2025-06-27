#İNDEXLER 0'DAN BAŞLAMAKTADIR.
kontrol= 0
while kontrol==0:
    secim = int(input("LUTFEN OYUN MODUNU SEÇİN ( 1 , 2 ) \n"
                      "[1] - GİZLİ MOD \n"
                      "[2] - AÇIK MOD \n"))
    boyut = int(input("BİR BOYUT GİRİNİZ :"))
    while boyut < 10:
        boyut = int(input("LUTFEN 10 YA DA 10'DAN BÜYÜK BİR SAYİ GİRİNİZ :"))
    import random
    hamle=0
    mayin_list = []
    mayin_sayisi = int((boyut ** 2) * 0.3)
    mayin_tarlasi = [['? ' for _ in range(boyut)] for _ in range(boyut)]
    gizli_tarla = [['? ' for _ in range(boyut)] for _ in range(boyut)]
    while len(mayin_list) != mayin_sayisi:
        x = random.randint(0, boyut - 1)
        y = random.randint(0, boyut - 1)
        if (x, y) not in mayin_list:
            mayin_list.append((x, y))
            mayin_tarlasi[x][y] = 'X '
    if secim == 1:
        for i in range(boyut):
            for j in range(boyut):
                print(gizli_tarla[i][j], end=" ")
            print("\n")
    if secim == 2:
        for i in range(boyut):
            for j in range(boyut):
                print(mayin_tarlasi[i][j], end=" ")
            print("\n")
    kontrol=1
    while True:
        if hamle == int(boyut*boyut*0.7):
            hamle -= 1
            print("TEBRİKLER.KAZANDINIZ PUANINIZ :{}".format(hamle))
            secim2 = int(input("LUTFEN YAPMAK İSTEDİGİNİZ İSLEMİ SECİN ( 1 , 2 ) \n"
                              "[1] - YENİ OYUNA GEÇME  \n"
                              "[2] - ÇIKIŞ \n"))
            if secim2 == 2:
                break
            else:
                kontrol=0
            break
        a = int(input("Lutfen bir koordinat seciniz: -> "))
        b = int(input("Lutfen bir koordinat seciniz: -> "))
        hamle += 1
        if gizli_tarla[a][b] != '? ':
            hamle -=1 #aynı koordinat girildiğinde tekrar azaltıyoruz
            a = int(input("Lutfen farklı bir koordinat seciniz: -> "))
            b = int(input("Lutfen farklı bir koordinat seciniz: -> "))
            hamle += 1
        sayac = 0
        puan = 0
        if mayin_tarlasi[a][b] == 'X ':
            hamle -=1
            print("KAYBETTİNİZ PUANINIZ : {}".format(hamle))
            for i in range(boyut):
                for j in range(boyut):
                    print(mayin_tarlasi[i][j], end=" ")
                print("\n")
            break
        elif a == 0:
            if b == 0:
                if mayin_tarlasi[a][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b + 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
            elif b == (boyut - 1):
                if mayin_tarlasi[a][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
            else:
                # örn:[0][2]
                if mayin_tarlasi[a][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b + 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
        elif a == (boyut - 1):
            if b == 0:
                # ör:[9][0]
                if mayin_tarlasi[a - 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b + 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
            elif b == (boyut - 1):
                # ör:[9][9]
                if mayin_tarlasi[a - 1][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b - 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
            else:
                # ör:[9][1]
                if mayin_tarlasi[a - 1][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b + 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
        elif b == 0:
            if a != 0 or a != (boyut - 1):
                # ör:[3][0]
                if mayin_tarlasi[a - 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b + 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
        elif b == (boyut - 1):
            if a != 0 or a != (boyut - 1):
                # ör:[1][9]
                if mayin_tarlasi[a - 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a - 1][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a][b - 1] == 'X ':
                    sayac += 1
                if mayin_tarlasi[a + 1][b - 1] == 'X ':
                    sayac += 1
                gizli_tarla[a][b] = str(sayac) + ' '
                for i in range(boyut):
                    for j in range(boyut):
                        print(gizli_tarla[i][j], end=" ")
                    print("\n")
                sayac = 0
        else:
            # ör:[2][2]
            if mayin_tarlasi[a - 1][b - 1] == 'X ':
                sayac += 1
            if mayin_tarlasi[a - 1][b] == 'X ':
                sayac += 1
            if mayin_tarlasi[a - 1][b + 1] == 'X ':
                sayac += 1
            if mayin_tarlasi[a][b - 1] == 'X ':
                sayac += 1
            if mayin_tarlasi[a][b + 1] == 'X ':
                sayac += 1
            if mayin_tarlasi[a + 1][b - 1] == 'X ':
                sayac += 1
            if mayin_tarlasi[a + 1][b] == 'X ':
                sayac += 1
            if mayin_tarlasi[a + 1][b + 1] == 'X ':
                sayac += 1
            gizli_tarla[a][b] = str(sayac) + ' '
            for i in range(boyut):
                for j in range(boyut):
                    print(gizli_tarla[i][j], end=" ")
                print("\n")
