def frais_livraison(montant):
   
    if montant < 0:
        raise ValueError("Montant negatif")    #les lignes indiquées dans Missing.

    if montant >= 300:
        return 0

    return 25