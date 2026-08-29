leiviskät = float(input("Anna leiviskät:\n"))
naulat = float(input("Anna naulat:\n"))
luodit = float(input("Anna luodit:\n"))

luoti_grammoina = 13.3
naula_luoteina = 32
leiviskä_nauloina = 20

kokonaisluodit = (leiviskät * luoti_grammoina * naula_luoteina) + (naulat * naula_luoteina) + luodit
kokonaisgrammat = kokonaisluodit * luoti_grammoina

kilogrammat = int(kokonaisgrammat // 1000)
grammat = kokonaisgrammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kg ja {grammat:.2f} g.")