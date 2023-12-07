#Наслідування класів
class Parent:
    pass
class Child(Parent):
    pass
#приклад
class Human:
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
kate = Worker()
print(nick.height, kate.height)