def levensteinova_vzdalenost(dotaz1, dotaz2):
    vzdalenost = 0
    i = 0
    length = max(len(dotaz1), len(dotaz2))
    while i < length:
        if i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                vzdalenost += 1
        else:
            vzdalenost += 1
        i += 1
    return vzdalenost 

def levensteinova_vzdalenost2(dotaz1, dotaz2):
    vzdalenost = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            vzdalenost += 1
    vzdalenost += abs(len(dotaz1) - len(dotaz2))
    return vzdalenost


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))