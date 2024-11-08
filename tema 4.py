import random


cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]


incercari_ramase = 6
litere_incercate = []

print("Bine ai venit! Trebuie sa ghicesti cuvantul.")
print("Cuvantul care trebuie ghicit: ", " ".join(progres))

while incercari_ramase > 0 and "_" in progres:


    litera = input("Te rog sa introduci o litera: ").lower()


    if len(litera) != 1 or not litera.isalpha():
        print("Te rog sa introduci o litera valida.")
        continue


    if litera in litere_incercate:
        print("Ai incercat deja aceasta litera!")
        continue


    litere_incercate.append(litera)


    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print("Corect! Progresul tau: ", " ".join(progres))
    else:
        incercari_ramase -= 1
        print(f"Litera incorecta! Iti mai raman inca {incercari_ramase} incercari.")


    print("Progresul tau: ", " ".join(progres))
    print("Litere incercate: ", " ".join(litere_incercate))


if "_" not in progres:
    print("Felicitari! Ai ghicit cuvantul: ", cuvant_de_ghicit)
else:
    print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}")