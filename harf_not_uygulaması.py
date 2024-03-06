sayi = int(input("kaç adet not girmek istiyorsunuz: "))
notlar = []

for i in range(sayi):
    veri = input("{}.not ".format(i+1))
    notlar.append(veri)

   

harf_not = ["AA","BA","BB","CB","CC","DC","DD","FF"]
    
for i in notlar:
    if 90 <= int(i) <=100:
      print(i,"→",harf_not[0])

    elif 85 <= int(i) <=89:
      print(i,"→",harf_not[1]) 

    elif 80 <= int(i) <=84:
      print(i,"→",harf_not[2])       

    elif 70 <= int(i) <=79:
      print(i,"→",harf_not[3])

    elif 60 <= int(i) <=69:
      print(i,"→",harf_not[4])

    elif 50 <= int(i) <=59:
      print(i,"→",harf_not[5]) 

    elif 45 <= int(i) <=49:
      print(i,"→",harf_not[6])    

    elif   0 <= int(i) <=44:
      print(i,"→",harf_not[7])
    else:
      print("hatalı not girişi")  

            