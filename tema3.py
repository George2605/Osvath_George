meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Part 1
numar_guias = 0
numar_ceafa = 0
numar_papanasi = 0
while studenti:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    if(comanda == "guias"):
        numar_guias += 1
    if(comanda == "papanasi"):
        numar_papanasi += 1
    if(comanda == "ceafa"):
        numar_ceafa += 1
    print(f"Studentul {student} a comandat {comanda}.")
    istoric_comenzi.append([student, comanda])
    tavi.pop()

print (istoric_comenzi)

# Part 2

print(f"S-au comandat {numar_guias} portii de guias, {numar_papanasi} portii de papanasi si {numar_ceafa} portii de ceafa.")

print (f"Au mai ramas {len(tavi)} tavi disponibile.")

meniu= "papanasi" * (10 - numar_papanasi) + "ceafa" * (3 - numar_ceafa) + "guias" * (6 - numar_guias)
if meniu.count("papanasi"):
    print ("Inca mai sunt papanasi disponibile in meniu.")
else:
    print ("Nu mai avem in papanasi in meniu boss, data viitoare :(")
if meniu.count("ceafa"):
    print ("Inca mai este ceafa disponibila in meniu.")
else:
    print ("Nu mai avem ceafa in meniu boss, data viitoare :*")
if meniu.count("guias"):
    print ("Inca mai avem guias disponibil in meniu.")
else:
    print ("Sarachieee, azi mananci supa la plic.")


# Part 3

mancare_accesibila = []

for pret_mancare in preturi:
    pret = pret_mancare[1]
    denumire_mancare = pret_mancare[0]
    if pret <= 7:
        mancare_accesibila.append(denumire_mancare)

print(f"Mancare accesibila: {mancare_accesibila}")
castig_cantina = numar_ceafa * 10 + numar_papanasi * 7 + numar_guias * 5
print (f"Cantina a incasat suma de {castig_cantina} lei.")


