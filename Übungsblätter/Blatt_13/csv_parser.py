#a)
def lines(path: str):
    with open(path) as f:
        for line in f:
            yield line


#b)
def parse_csv(lines):
    for line in lines:
        yield line.replace('\n', '').split(",")


def skip(n: int, xs):
    for x in xs:
        if n > 0:
            n -= 1
        else:
            yield x


def update_balance(balance: float, csv_path: str) -> float:
    for row in skip(1, parse_csv(lines(csv_path))):
        balance += float(row[2])
    return balance
    

if __name__ == '__main__':
    for line in lines("/Users/claud/OneDrive/Desktop/Studium/SS_23/Informatik/EidP01/Übungsblätter/Blatt_13/umsatz.csv"):
        print(line)
    print(list(parse_csv(["Datum,Verwendungszweck,Betrag",
                        "30.12.2020,Bafoeg-Foerdergeld,+514.00"])))
    print(update_balance(100, "/Users/claud/OneDrive/Desktop/Studium/SS_23/Informatik/EidP01/Übungsblätter/Blatt_13/umsatz.csv"))