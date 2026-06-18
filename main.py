from voyage import hotel_frais, location_voiture, vol_frais, voyage_frais

print("=== CALCULATEUR DE FRAIS DE VOYAGE ===\n")


nuits = int(input("Nombre de nuits à l'hôtel : "))
jours = int(input("Nombre de jours de location de voiture : "))
ville = input("Ville de destination : ")


hotel = hotel_frais(nuits)
voiture = location_voiture(jours)
vol = vol_frais(ville)
total = voyage_frais(nuits, jours, ville)


print("\n--- DÉTAIL DES FRAIS ---")
print("Hôtel :", hotel, "DH")
print("Voiture :", voiture, "DH")
print("Vol :", vol, "DH")

print("\n--- TOTAL ---")
print("Prix total du voyage :", total, "DH")