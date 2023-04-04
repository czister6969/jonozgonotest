students = [
  {"imie": "Tomek", "wiek": 20},
  {"imie": "Karolina", "wiek": 18}
]


stude = list(map(lambda students: students["wiek"], students ))

print(stude)



students.sort(key=lambda students:students["wiek"])

print(students)

print (students[0])

#elements = stude
#size = len(stude)

#print("Before sorting:", stude)

#for i in range(size):
