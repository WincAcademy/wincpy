preiPrijs = 2
print(f'Prei kost {str(preiPrijs)} euro per kilo.')

bestelling = 'prei 4'
bestellingHoeveelheid = int(bestelling[bestelling.find(' '):])
totaalprijs = preiPrijs * bestellingHoeveelheid
print(totaalprijs)

broccoliPrijs = 2.34
bestelling = 'broccoli 1.6'
bestellingHoeveelheid = float(bestelling[bestelling.find(' '):])
totaalprijs = round(broccoliPrijs * bestellingHoeveelheid, 2)
print(f'{bestellingHoeveelheid} kilo broccoli kost {totaalprijs} euro')

