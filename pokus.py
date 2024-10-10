import sys

def main(soubor):
  otevreny_soubor = open(soubor, "r")
  for radka in otevreny_soubor:
    print(radka)

if __name__ == "__main__":
  soubor = sys.argv[1]
  main(soubor)
