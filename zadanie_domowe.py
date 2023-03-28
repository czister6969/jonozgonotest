danilodz = []

while True:
  menu = input("1. Dodaj użytkownika  \n 2. Zobacz dane użytkownika  \n  3. Wyświetl wszystkie imiona użytkowników    \n  4. Na poprawę humoru \n  _______________________________________  \n")




  if menu == "1":
    imie  = input("Podaj imię: ")
    mail  = input("Podaj adres email: ")
    wiek = input("Podaj wiek:  ")
    user={"imie":imie,"mail":mail,"wiek":wiek}
    danilodz.append(user)
  
  elif menu == "2":
    pokaz = input("Daj imie uzytkownika: ")
    for z in danilodz:
      if z["imie"] == pokaz:
          print(z)

  elif menu == "3":
      for z in danilodz:
        print(z["imie"])

  elif menu == "4":
    print("https://www.youtube.com/watch?v=wGeFVtLo1RA")
    print("Have an incredibly gorgeus day")
  
