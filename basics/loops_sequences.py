
# For loop
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

# range(start, stop, steps)
for num in range(1, 5):
    print(num)

for index, language in enumerate(programming_languages):
    print(f'Index {index} and language {language}')

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id})


# While loop
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')
