def hello():
    print("Hello World!")

def sudy_lichy(cislo):
    if (cislo%2==1):
        print(f"Cislo {cislo} je liche.")
    else:
        print(f"Cislo {cislo} je sude.")

sudy_lichy(5)
sudy_lichy(1000000)