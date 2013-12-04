from random import choice

choices = open('combination.txt').read().split()

random_choice = choice(choices)

print(random_choice)
