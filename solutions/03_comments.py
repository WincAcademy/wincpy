prei = 2
aardappel = 3
spruitje = 7 # dure spruitjes

totaal = prei + aardappel + spruitje
print(totaal)

gemiddelde_prijs = round((prei + aardappel + spruitje) / 3, 2)
print(gemiddelde_prijs)

aantal_prei = 2
aantal_aardappel = 7
aantal_spruitje = 10 # en dan ook nog 10 daarvan

totaal_prijs = aantal_prei * prei\
               + aantal_aardappel * aardappel\
               + aantal_spruitje * spruitje
print(totaal_prijs)

# Note: korting wordt nog niet gespecificeerd in de opdracht.
korting_percentage = 30
te_betalen_percentage = 1 - korting_percentage / 100

""" Trek je porto-met-niks maar. """
totaal_prijs_met_korting_afgerond = round(totaal_prijs * te_betalen_percentage, 2)

# Joepie, we zijn klaar.
print(totaal_prijs_met_korting_afgerond)
""" Dit is het einde van de geschiedenis. """
