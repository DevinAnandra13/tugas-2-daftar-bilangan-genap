xy=0
xz=0
ls=0

print("DERET BILANGAN GANJIL")
print("--------------------")
y=int(input("Masukkan Range = "))
print("Bilangan Ganjil : ")
for i in range(y) :
    if(i%2)==1:
        print(i)
        xy=xy+1
print("Jumlah Bilangan Ganjil = ",xy)
