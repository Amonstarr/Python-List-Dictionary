bilangan_genap = []
bilangan_ganjil = []

for i in range(1, 21):
    if i % 2 == 0:
        bilangan_genap.append(i)
    else:
        bilangan_ganjil.append(i)

print("List pada bilangan Genap", bilangan_genap)
print("List pada bilangan Ganjil", bilangan_ganjil)
