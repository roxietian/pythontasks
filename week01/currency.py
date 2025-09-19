# Write code below 💖
pesos = float(input("Enter the remaining pesos:"))
soles = float(input("Enter the remaining soles:"))
reais = float(input("Enter the remaining reais:"))
usd = float(0.00026*pesos + 0.29*soles + 0.19*reais)
print(f"\nWhat do you have left in pesos?-->{pesos}")
print(f"\nWhat do you have left in soles?-->{soles}")
print(f"\nWhat do you have left in reais?-->{reais}")
print(f"\ntotal in usd:${usd:.2f}")