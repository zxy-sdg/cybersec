def discount(prices, isPet, nItems):
    if nItems != len(prices) or nItems != len(isPet):
        raise ValueError("nItems deve essere uguale alla lunghezza di prices e isPet")

    num_animali = sum(1 for x in isPet if x)
    num_altri = nItems - num_animali

    if num_animali >= 1 and num_altri >= 5:
        base_sconto = sum(p for p, pet in zip(prices, isPet) if not pet)
        return base_sconto * 0.20

    return 0.0


def leggi_file_vendita(nome_file):
    prices = []
    isPet = []

    with open(nome_file, "r", encoding="utf-8") as f:
        for lineno, riga in enumerate(f, start=1):
            riga = riga.strip()
            if not riga:
                continue  # salta righe vuote

            campi = riga.split()
            if len(campi) != 2:
                raise ValueError(f"Riga {lineno} non valida (attesi 2 campi): {riga!r}")

            prezzo_str = campi[0].replace(",", ".")  # accetta anche virgola decimale
            try:
                prezzo = float(prezzo_str)
            except ValueError:
                raise ValueError(f"Riga {lineno}: prezzo non valido: {campi[0]!r}")

            yn = campi[1].upper()
            if yn not in ("Y", "N"):
                raise ValueError(f"Riga {lineno}: atteso 'Y' o 'N', trovato: {campi[1]!r}")

            prices.append(prezzo)
            isPet.append(yn == "Y")

    return prices, isPet


def main():
    nome_file = "lista_con_sconto.txt"

    try:
        prices, isPet = leggi_file_vendita(nome_file)
        nItems = len(prices)

        sconto = discount(prices, isPet, nItems)

        totale = sum(prices)
        totale_da_pagare = totale - sconto


        print("prices:", prices)
        print("isPet :", isPet)
        print(f"Sconto: {sconto:.2f}")
        print(f"Totale (prima): {totale:.2f}")
        print(f"Totale (dopo) : {totale_da_pagare:.2f}")

    except FileNotFoundError:
        print(f"Errore: file non trovato: {nome_file}")
    except ValueError as e:
        print(f"Errore nel file: {e}")


if __name__ == "__main__":
    main()
