class Person:
  height = 160
  age = 22
  name = "Kiril"
  is_male = True
  hobby = "plaing guitar"

  def __init__(self,surname):
    self.surname = surname

  def do_my_thing(self):
    print("I love", self.hobby)

  

me = Person("Kobzar")
me.hobby = "reading"
me.do_my_thing()

my_friend = Person("Andrey")
my_friend.hobby = "Plaing guitar"
my_friend.do_my_thing()