prei = 2
aardappel = 3
spruitje = 7

totaal = prei + aardappel + spruitje
gemiddelde_prijs = round((prei + aardappel + spruitje) / 3, 2)

aantal_prei = 2
aantal_aardappel = 7
aantal_spruitje = 10

totaal_prijs = aantal_prei * prei\
               + aantal_aardappel * aardappel\
               + aantal_spruitje * spruitje

korting_percentage = 30
te_betalen_percentage = 1 - korting_percentage / 100

totaal_prijs_met_korting_afgerond = round(totaal_prijs * te_betalen_percentage, 2)

print(totaal_prijs_met_korting_afgerond)
