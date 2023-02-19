class Person:
  height = 160
  age = 22
  name = "Kyryl"
  is_male = True

  def __init__(self,surname):
    self.surname = surname
    print(self.name)

me = Person("Kobzar")
You = Person("Test")

print(me.age)
me.age += 1
print(me.age)