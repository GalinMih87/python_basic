buget = float(input())
noshtuvki = int(input())
cena_noshtuvka = float(input())
dopalnitelni_razhodi = int(input())

if noshtuvki > 7:
    cena_noshtuvka *= 0.95

razhod_za_noshtuvki = noshtuvki * cena_noshtuvka
obshto_razhodi = dopalnitelni_razhodi * buget / 100
total = razhod_za_noshtuvki + obshto_razhodi

diff = abs(buget - total)

if total <=buget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

else:
    print(f"{diff:.2f} leva needed.")
