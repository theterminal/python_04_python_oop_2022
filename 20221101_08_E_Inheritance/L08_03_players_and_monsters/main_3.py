from project.hero import Hero
from project.elf import Elf


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

print('\n_________ tests ___________\n')

print(elf)                                          # E of type Elf has level 4         - returns the statement from the __str__ method from 'Hero'
print(elf.__class__)                                # <class 'project.elf.Elf'>         - returns the class object of the instance
print(elf.__class__.__bases__)                      # (<class 'project.hero.Hero'>,)    - returns the base class object of the instance - it is a tuple
print(elf.__class__.__bases__[0])                   # <class 'project.hero.Hero'>       - returns the 1-st element (an object) from the tuple described above
print(elf.__class__.__bases__[0].__name__)          # Hero                              - returns the name of the class for the instance
