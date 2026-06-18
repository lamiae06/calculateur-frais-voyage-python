def hotel_frais(nuits):
    prix_par_nuit = 90
    return prix_par_nuit * nuits


def location_voiture(jours):
    prix_par_jour = 35

    if jours >= 7:
        reduction = 50 / 100
    elif jours >= 3:
        reduction = 20 / 100
    else:
        reduction = 0

    prix_final = prix_par_jour * (1 - reduction)
    return prix_final * jours


def vol_frais(ville):
    ville = ville.lower()

    if ville == "marakech":
        return 35
    elif ville == "paris":
        return 200
    elif ville == "new york":
        return 500
    elif ville == "tokyo":
        return 700
    elif ville == "londres":
        return 250
    else:
        return 0  


def voyage_frais(nuits, jours, ville):
    return hotel_frais(nuits) + location_voiture(jours) + vol_frais(ville)