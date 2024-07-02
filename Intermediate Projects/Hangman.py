import random

chain=""".............
            .
            .
            .
        .........
        .  O O  .
        . ..... .
        .........
            .
"""

head="""          . . .
         .  .  .
        .   .   .
            .
            .
"""
feet="""           ...
          .   .
         .     .
        .       .
"""


words = [
    {
        "word":"Apple",
        "cat":"fruit"
    },
    {
        "word":"Banana",
        "cat":"fruit"
    },
    {
        "word":"Computer",
        "cat":"tech"
    },
]

random_word=random.choice(words)
attempts=3
word=input(f"you have {attempts} to write a word with {len(random_word["word"])} characters and in {random_word["cat"]} category: ")

while attempts>0:
    if word.lower()==random_word["word"].lower():
        print("Congratulations, you won!")
        break
    else:
        attempts-=1
        if attempts==2:
            print(chain)
        elif attempts==1:
            print(chain+head)
        else:
            print(chain+head+feet)
            print("Game over!")
            break
        word=input(f"Incorrect. You have {attempts} attempts left: ")