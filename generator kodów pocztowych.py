# import numpy

# kod = int

# kody_graniczne = input("podaj kod początowy i końcowy:\n")

# kody_graniczne = kody_graniczne.replace("-", "")

# lista_kodow = kody_graniczne.split()

kod_poczatkowy = input("podaj kod początkowy:\n")

kod_koncowy = input("podaj kod końcowy:\n")

kod_poczatkowy = kod_poczatkowy.split("-")

kod_koncowy = kod_koncowy.split("-")

# for x in kod_poczatkowy:
    # print(x)

x = 0

while x < len(kod_poczatkowy):
    kod_poczatkowy[x] = int(kod_poczatkowy[x])
    x = x + 1

x = 0

while x < len(kod_koncowy):
    kod_koncowy[x] = int(kod_koncowy[x])
    x = x + 1

# def drukuj_kod(kod):
#     kod_str = kod
#     kod_str = str(kod_str)
#     kod_str.insert(2, "-")
#     print(kod_str)

kod = kod_poczatkowy

kod[1] = kod[1] + 1

while(kod[0] <= kod_koncowy[0]):
    
    if(kod[0] < kod_koncowy[0]):
        
        while(kod[1] <= 999):
            print(str(kod[0]) + "-" + str(kod[1]))
            kod[1] = kod[1] + 1
    
    elif(kod[0] == kod_koncowy[0]):
       
        while(kod[1] <= kod_koncowy[1]):
            print(str(kod[0]) + "-" + str(kod[1]))
            kod[1] = kod[1] + 1
   
    kod[0] = kod[0] + 1
    kod[1] = 000

