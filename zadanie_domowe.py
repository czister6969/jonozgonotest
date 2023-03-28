danilodz = []

while True:
  menu = input("1. Dodaj użytkownika  \n 2. Zobacz dane użytkownika  \n  3. Wyświetl wszystkie imiona użytkowników    \n  4. Na poprawę humoru \n  _______________________________________  \n")




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

  elif menu == "4":
    print("https://www.google.com/search?q=mariusz+pudzianowski&tbm=isch&ved=2ahUKEwjU4c-                ykv79AhVCuyoKHVzsCxcQ2-    cCegQIABAA&oq=mariusz+p&gs_lcp=CgNpbWcQARgAMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQigUQQzoGCAAQBxAeOgQIABAeOgsIABCABBCxAxCDAToKCAAQigUQsQMQQzoICAAQsQMQgwE6DQgAEIoFELEDEIMBEENQ6ghYiSVgwC9oAXAAeAKAAUyIAf0MkgECMjSYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=4ZwiZJTtLsL2qgHc2K-4AQ&bih=961&biw=1920&rlz=1C1GCEU_plPL1049PL1049")
  
