def main():
  
    print("-----Bienvenue dans le programme pour l'auto completion-----")
    while True:
        print("Un entier D compris entre 1 et 200 indiquant le nombre de mots du dictionnaire")
        D = int(input("N="))
        print(f"L'entier entré est: {D}")
        if not (D < 1 or D > 100):
            break
        
    while True:
        print("Un mot du dictionnaire")
        Mot = input("Mot =")
        print(f"Le mot entré est: {Mot}")
        if not (Mot.islower == False or len(Mot)<15):
            break
        
if __name__ == "__main__":
    main()
