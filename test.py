class hichem :
    def __init__(self, name, age, profession, phone):
        self.name = name
        self.age = age
        self.profession = profession
        self.phone = phone
h1 = hichem("chichon", 33, "developpeur", "0744549619")

print(h1.name)
print(h1.age)
print(h1.profession)
print(h1.phone)

h2= hichem("jean", 99, None, None)
print(h2.name)
print(h2.age)


def afficher(param):
    for i in range(param+1, 0, -1):
        for j in range(0, i-1):
            print("*", end='')
        print("")

afficher(6)