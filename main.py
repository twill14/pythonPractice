from incrementer import Incrementer


def count_five_times(count):
    for i in range(0, 4):
        print(count.up_one())


counter1 = Incrementer()
counter2 = Incrementer(10)
counter3 = Incrementer(100)

print("Five values for counter1")
count_five_times(counter1)

print("Five values for counter2")
count_five_times(counter2)

print("Five values for counter3")
count_five_times(counter1)
