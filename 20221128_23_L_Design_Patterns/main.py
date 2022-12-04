from singleton.Person import Person

p1 = Person()
p2 = Person()
p3 = Person()

print(p1)                       # [<singleton.Person.Person object at 0x107606230>]
print(p2)                       # [<singleton.Person.Person object at 0x107606230>]
print(p3)                       # [<singleton.Person.Person object at 0x107606230>]
