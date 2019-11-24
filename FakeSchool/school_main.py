from FakeSchool.student import Student, Frosh

student1 = Student("Lameena Wright", 1)
freshmen1 = Frosh("Henford Kaiden", 2)

student1.profile()
student1.set_units(100)
student1.has_enough_units()

freshmen1.profile()
freshmen1.set_units(10)
freshmen1.units