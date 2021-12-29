### Yemeksepeti Patika Bootcamp - Homework1
### Arda Cem Ozmen - @ardaozmen

""" Bir metnin uzunluğunu hesaplamak için bir Python programı yazınız. ipucu Len fonksiyonu """

def metinUzunluguHesapla(metin):
    uzunluk = len(metin)
    return uzunluk

# print(metinUzunluguHesapla("yemeksepeti patika bootcamp")) # 27

""" Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız. """

def metinKarakter(metin):
    sonuc = metin[:2] + metin[-2:]
    return " ".join(sonuc)

# print(metinKarakter("yemeksepeti")) # y e t i

"""Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp 
sonucu ekrana yazdıran Python programını yazınız."""

def metniDegistir(metin:input, eski:input, yeni:input):
    metin = input("Değiştirilecek metni girin: ")
    eski = input("Eski harf: ")
    yeni = input("Yeni harf: ")
    metin = metin.replace(eski, yeni)
    return metin

"""Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma 
operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız. """

def palindrom(kelime):
    if kelime == kelime[::-1]:
        print("Palindrom")
    else:
        print("Palindrom Degil") 

# print(palindrom("aya"))

"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. 
* aritmetik operatöründen faydalanabilirsiniz. """

def karakterCogalt(metin):
    sonuc = metin + metin[-2:]*4
    return sonuc

# print(karakterCogalt("merhaba"))

""" 5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız. """

def listeElemaniDegistir():
    liste = int(input("Liste elemanlari sayisi: "))
    sonuc = list(map(int,input("\nElemanlari giriniz : ").strip().split()))[:liste]
    sonuc[1] = 100
    return sonuc

# print(listeElemaniDegistir())

"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız
liste1 = [1,2,3] liste2 = [4,5,6] liste3 = ????? """

liste1 = [1,2,3]
liste2 = [4,5,6]

liste3 = liste1.copy()
liste3.append(liste2)
liste3 = liste1 + liste2
liste3.extend(liste2)

# print(liste3)

"""Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz. """

l = [1,2,"Araba"]
l.insert(0, 'Elma')

# print(l)

"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. """

liste_3 = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
liste_3.remove(3)

# print(liste_3)

""" liste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız. 
Beklenen Çıktı: ["1",1,2,"3"] => Liste1 Çıktısı ["1",1,2,"3",250] => Liste2 Çıktısı """

liste1 = ["1",1,2,"3"]
liste2 = liste1.copy()
liste2.insert(len(liste2), 250)

# print(liste1)
# print(liste2)

""" Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60} 
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4 = {**dict1, **dict2, **dict3} # using **kwargs

# print(dict4)

"""sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız 
Beklenen Çıktı :(6,60) """

sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# print(sozluk.popitem())

"""dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30} """

dict1={1:10, 2:20}
dict1[3] = 30

# print(dict1)

"""liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun b.sözlüğün her alamanının karşılığına 
değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. 
Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50} """

liste = [1,2,3,4,5]
dict_a = dict.fromkeys(liste, 0)
# print(dict_a)

for s in dict_a:
    dict_a[s] = s*10

# print(dict_a)

"""sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde 
setdefault fonksiyonunu kullanarak ekleyiniz"""

sozluk = {1:10,2:20,3:30,4:40,5:50}
sozluk.setdefault(6, 60)
# print(sozluk)

""" Seven Segment Display https://en.wikipedia.org/wiki/Seven-segment_display 
8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a kadar olan sayılar için yazalım"""

### without hex,bin,zfill, tek satırda if
def seven_seg(no):
    holder_arr=list(str(no))
    result = [[0]*5 for i in range(len(holder_arr))]
    hold_dict={"0":["***","* *","* *","* *","***"],"1":["  *","  *","  *","  *","  *"],
    "2":["***","  *","***","*  ","***"],
    "3":["***","  *","***","  *","***"],
    "4":["* *","* *","***","  *","  *"],
    "5":["***","*  ","***","  *","***"],
    "6":["***","*  ","***","* *","***"],
    "7":["***","  *","  *","  *","  *"],
    "8":["***","* *","***","* *","***"],
    "9":["***","* *","***","  *","***"],
    ".":[" "," "," "," ","*"]}
    for s in range(0,len(holder_arr)):
        for w in range(0,5):
            result[s][w]=hold_dict[str(holder_arr[s])][w]
    hold_string=""
    for w in range(0,5):
        for s in range(0,len(holder_arr)):
            hold_string+=result[s][w]
            hold_string+=" "
        print(hold_string)
        hold_string=""
   
# print(seven_seg(10))

""" Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} """

def sorte(dic):
    for s in dic:
        dic[s]=sorted(dic[s])
    return dic
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 

# print(sorte(num))

"""sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. """

sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}

holder={}
for s in sozluk:
    holder[s.replace(" ","")]=sozluk[s]
sozluk=holder

# print(sozluk)

""" liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz? """

liste1 = [1,2,3]
liste2 = [4,5,6,7,8]
liste3 = liste1 + liste2

# print(liste3)

"""liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz?""" 

liste=[1,2,3,4,5,6]
del liste[0]

# print(liste)

""" liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz? """

liste=["elma" , "armut", "çilek"]
liste.append(3)

# print(liste)

"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""

def max3():
    numbers = [int(input('Sayi giriniz: ')) for i in range(10)]
    sonuc = sorted(numbers)[-3:]
    return sonuc[::-1]
    
# print(max3())

"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""

def harfbul(metin):
    lower=[]
    upper=[]
    for i in list(metin):
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    print('Kucuk Harfler: ',lower,'\nBuyuk Harfler: ',upper)

# print(harfbul("YemekSepeti"))

"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

def sayac():
    sayilar = [int(input('Sayi giriniz: ')) for i in range(10)]
    cift=0;
    tek=0;
    for i in sayilar:
        if i%2==0:
            cift+=1
        else:
            tek+=1
    print("Cift Sayilar:"+str(cift))
    print("Tek Sayilar:"+str(tek))

# print(sayac())