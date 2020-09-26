__human_name__ = 'operators'
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'

switz_lang = 'German (or Swiss German)'
spain_lang = 'Castilian Spanish'
print(switz_lang == spain_lang)

switz_religion = 'Roman Catholic'
spain_religion = 'Roman Catholic'
print(switz_religion == spain_religion)

switz_capital = 'Bern'
spain_capital = 'Madrid'
print(len(spain_capital) != len(switz_capital))

switz_gdp = 580 * 10**9
spain_gdp = 1778 * 10**9
print(switz_gdp > spain_gdp)

switz_popgrowth = 0.0066
spain_popgrowth = 0.0067
print(spain_popgrowth < 0.01 and switz_popgrowth < 0.01)

ten_million = 10**7

switz_popcount = 8.4 * 10**6
spain_popcount = 50 * 10**6
print(spain_popcount > ten_million or switz_popcount > ten_million)

switz_popcount = 8.4 * 10**6
spain_popcount = 50 * 10**6
print((spain_popcount > ten_million and switz_popcount <= ten_million)
      or
      (spain_popcount <= ten_million and switz_popcount > ten_million))
