meny = 0
grejer = []

print("\n<<< Välkommen till programmet >>>")

while meny != 4:

    print("\n1. Skriv ut")
    print("2. Mata in")
    print("3. Rensa")
    print("4. Avsluta")

    try:
        meny = int(input("\nGör ditt val: "))
    
    except:
        print("Du måste ange en siffra!")

    if meny == 1:
        for l in grejer:
            print(l)

    elif meny == 2:
        saker = {}
        saker = input("\nSkriv: ")

        saker.append(grejer)
    
    elif meny == 3:
        print("")
    
    else:
        print("\nDet här syns inte")