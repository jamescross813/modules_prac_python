import random

random_one = random.randint(1,100)
random_list =[random.randint(1,100) for i in range(10)]
random_two = random.choice(random_list)
print(random_one)
print(random_list)
print(random_two)
