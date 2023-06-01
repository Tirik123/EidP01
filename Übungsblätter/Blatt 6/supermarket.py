from dataclasses import dataclass

#Aufgabe 6.1#

#(a)#

@dataclass
class Food:
    mhd: str # Mindesthaltbarkeitsdatum im Format "2021-02-14"


@dataclass
class NonFood:
    pass # leere Klasse


@dataclass
class Stock:
    name: str # Name der Ware
    units: int # Anzahl gelagerten Ware
    price_per_unit: int # Stückpreis in Cent
    kind: Food | NonFood # kind ist entweder Food oder NonFood


#(b)#

def is_expired(Lagerbestand: Stock, Datum: str) -> bool: # return True: abgelaufen, return False: nicht abgelaufen
    match Lagerbestand.kind:
        case Food():
            return Datum > Lagerbestand.kind.mhd
    return False

            

#(c)#

def get_expired(Liste_Lagerbestände: list[Stock], Datum: str) -> list[Stock]:
    return [i for i in Liste_Lagerbestände if is_expired(i, Datum) == True]



#(d)#


def buy(Lagerbestand: Stock, Stückzahl: int) -> int:
    Neue_Stückzahl = Lagerbestand.units
    Stückzahl_Eins = '1' * Stückzahl
    print(Stückzahl_Eins)
    Stückzahl_Liste = Stückzahl_Eins.split()
    print(Stückzahl_Liste)
    for i in Stückzahl_Liste:
        if Lagerbestand.units - int(i) != 0:
            Neue_Stückzahl -= int(i)
        else:
            while Lagerbestand.units - int(i) >= 0:
                Neue_Stückzahl -= int(i)
    return Lagerbestand.units - Neue_Stückzahl




if __name__ == '__main__':
    Stock("Chocolate", 12, 199, Food("2020-12-07"))
    Stock("Tooth Brush", 30, 299, NonFood())


    print(buy(Stock("Chocolate", 12, 199, Food("2020-12-07")), 2))





'''def test_supermarket():
    # test Stock
    stocks: list[Stock] = [
        Stock("Chocolate", 12, 199, Food("2020-12-07"), ),
        Stock("Tooth Brush", 30, 299, NonFood())
    ]
    print(f"Stocks: {stocks}")
    assert stocks[0].name == "Chocolate"
    assert stocks[0].units == 12
    assert stocks[0].price_per_unit == 199

    assert stocks[1].name == "Tooth Brush"
    assert stocks[1].units == 30
    assert stocks[1].price_per_unit == 299

    # test get_expired
    assert get_expired(stocks, "2020-12-05") == []
    assert get_expired(stocks, "2020-12-09") == [stocks[0]]

    # test buy
    stock: Stock = Stock("Chocolate", 12, 199, Food("2020-12-07"))
    assert stock.units == 12
    assert buy(stock, 5) == 5
    assert stock.units == 7
    assert buy(stock, 25) == 7
    assert stock.units == 0


if __name__ == "__main__":
    test_supermarket()
'''





