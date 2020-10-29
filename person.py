class Person:
    # class attribute
    counter     = 0     # public attribute

    def __init__(self, name, age, height, password = ''):
        # instance attribute
        self.setName(name)
        self.setHeight(height)
        self.setAge(age)
        self.__password = password

        self.counter += 1

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        if (age >= 150 or age < 0):
            print('Umur tidak valid!')
        else:
            self.age = age

    def setHeight(self, height):
        if (height > 300):
            print('Anda terlalu tinggi gan')
        else:
            self.height = height

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
 
    def getHeight(self):
        return self.height

    def test(self):
        print('Test', dir(self))

# proses instansiasi class Person
gilang = Person('Gilang', 20, 180, '123456')
dida = Person('Dida', 20, 180)
print(gilang.getName(), dida.getName())

dida = Person('Dida', 20, 160)

users = [
    # ['Nama', 'Umur', 'Tinggi']
    ['Dida', 20, 160],
    ['Gilang', 20, 180],
    ['Firman', 20, 190]
]

for user in users:
    # proses instansiasi class Person
    person = Person(user[0], user[1], user[2])

    # memanggil method dari sebuah class.
    # person.setAge(21)

    print('Nama:', person.getName(), 'Umur:', person.getAge(), 'Tinggi:', person.getHeight())


print('Tinggi Gilang:', gilang.getHeight(), 'Species:', gilang.species)
print('Tinggi Dida:', dida.getHeight(), 'Species:', dida.species)
print('Total Person:', dida.counter)