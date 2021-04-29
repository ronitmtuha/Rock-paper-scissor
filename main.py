import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=[rock,paper,scissors]
random_choice=random.randint(0,2)
ask=input("Rock, paper or scissors ")
ask1=ask.lower()
final_choice=choice[random_choice]
if ask1=="rock":
 if final_choice==rock:
    print(f"Computor chose: \n{final_choice} \n Match Drawn ")
 elif final_choice==scissors:
    print(f"Computor chose: \n{final_choice} \n You win ")
 elif final_choice==paper:
    print(f"Computor chose: \n{final_choice} \n You lose ")
 

if ask1=="paper":
 if final_choice==rock:
    print(f"Computor chose: \n{final_choice} \n You win ")
 elif final_choice==scissors:
    print(f"Computor chose: \n{final_choice} \n You lose ")
 elif final_choice==paper:
    print(f"Computor chose: \n{final_choice} \n Match drawn ")
 

if ask1=="scissors":
 if final_choice==rock:
    print(f"Computor chose: \n{final_choice} \n You lose ")
 elif final_choice==scissors:
    print(f"Computor chose: \n{final_choice} \n Match Drawn ")
 elif final_choice==paper:
    print(f"Computor chose: \n{final_choice} \n You win ")
