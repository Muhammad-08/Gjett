import random # Vi trenger random for å lage et tilfeldig tall

lowest_num = 1  # Laveste tall vi kan gjette
highest_num = 100  # Laveste tall vi kan gjette
answer = random.randint(lowest_num, highest_num) # Velger et hemmelig tall

guesses = 0 # Teller hvor mange ganger vi gjetter
is_running = True # Teller hvor mange ganger vi gjetter

print("Tall Gjett Spill")
print(f"Gjett nummer fra {lowest_num} og {highest_num}")

while is_running:# Så lenge spillet er i gang

    guess = input("skriv din gjettning: ")  # Spør spilleren om et tall
    if guess.isdigit(): # Sjekker om svaret faktisk er et tall

        guess = int(guess)  # Gjør om fra tekst til tall
        guesses += 1     # Teller en gjett til


        if guess < lowest_num or guess > highest_num:
            print("nummer er ut av Rangen")  # Hvis tallet er for lavt eller høyt
            print("gjett nummer mellom {lowest_num} og {highest_num}")
        elif guess < answer:
            print("For lavt! prøv igjen!") # Hvis vi gjettet for lavt   
        elif guess > answer:
            print("For høyt! prøv igjen!") # Hvis vi gjettet for høyt
        else:
            print(f"korrekt! Svaret var")  # Hvis vi gjetter riktig
            print (f"ganger du har gjettet: {guesses}")

            is_running = False   # Da stopper spillet

    else:
        print("Feil svar")  # Hvis vi skrev noe som ikke er tall 
        print(f"Gjett nummer fra {lowest_num} og {highest_num}") 
