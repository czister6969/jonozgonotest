danilodz = []

while True:
  menu = input("1. Dodaj użytkownika  \n 2. Zobacz dane użytkownika  \n  3. Wyświetl wszystkie imiona użytkowników  \n  _______________________________________  \n")




  if menu == "1":
    imie  = input("Podaj imię: ")
    mail  = input("Podaj adres email: ")
    wiek = input("Podaj wiek:  ")
    user={"imie":imie,
    "mail":mail,
    "wiek":wiek}
    danilodz.append(user)
  
  elif menu == "2":
    reggin = input("Daj imie uzytkownika: ")
    for z in danilodz:
      if z["imie"] == reggin:
          print(z)

  elif menu == "3":
      for z in danilodz:
        print(z["imie"])
  
