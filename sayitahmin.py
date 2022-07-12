#sayılar random modülü ile rasgele bir değişkene atılacak
#Kullanıcıdan bir sayı girmesi istenecek.
# Kullanıcı sayısı randomdan büyükse küçük girin uyarısı,
# Kullanıcı sayısı randomdan küçükse büyük girin uyarısı versin

# Kullanıcın ilk başta üç hakkı olacak. Üç hakkı da dolan bilemediniz ve sayıyı gösterecek
# İlk defada bilen tebrikler ilk defada bildiniz uyarısı.

 
        
import random,string


print("sayı bulmanız için üç tahmin hakkınız var")
tahminedilensayi = random.randint(1,100)

for sayı in range(1,4):
    tahmin = int(input("Bir sayı giriniz:   "))
    
    if(tahminedilensayi == tahmin):
        print("Tebrikler ilk defada bildiniz: ", tahminedilensayi)
        exit(0)
    else:
        if(tahminedilensayi > tahmin):
          print("büyük sayı girin")
          print("{}.hakkınız gitti" .format(sayı))
        else:
             if(tahminedilensayi < tahmin):
                print("küçük sayı girin")
                print("{}.hakkınız gitti" .format(sayı))
                             
             else:
                     pass
print("üç hakkınız bitti bilemediniz   ", tahminedilensayi )                  
  
       
     
       