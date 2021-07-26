"""
Kullanıcıdan 10 sayı isteyin 
bu sayıların ilk ve en son 
girdiği sayıları ekrana yazdırın. Ayrıca 10 sayının toplamını ekrana yazdırın. 
"""
toplam = 0
ilk = input("1.sayıyı girin:")
toplam = (toplam + int(ilk))
s = input("2.sayıyı girin:")
toplam = (toplam + int(s))
s = input("3.sayıyı girin:")
toplam = (toplam + int(s))
s = input("4.sayıyı girin:")
toplam = (toplam + int(s))
s = input("5.sayıyı girin:")
toplam = (toplam + int(s))
s = input("6.sayıyı girin:")
toplam = (toplam + int(s))
s = input("7.sayıyı girin:")
toplam = (toplam + int(s))
s = input("8.sayıyı girin:")
toplam = (toplam + int(s))
s = input("9.sayıyı girin:")
toplam = (toplam + int(s))
son = input("10.sayıyı girin:")
toplam = (toplam + int(son))
print("ilk girdiğiniz sayı"+str(ilk))
print("son girdiğiniz sayı"+str(son))