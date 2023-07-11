cena_qgodi  = float(input())
banani = float(input())
portokali = float(input())
malini = float(input())
qgodi = float(input())

cena_malini = cena_qgodi / 2
cena_portokali = cena_malini - (cena_malini * 0.4)
cena_banani = cena_malini - (cena_malini * 0.8)

sum_malini = malini * cena_malini
sum_portokali = portokali * cena_portokali
sum_bani = banani * cena_banani
sum_qgodi = qgodi * cena_qgodi

total = sum_malini + sum_portokali + sum_bani + sum_qgodi

print(f"{total:.2f}")
