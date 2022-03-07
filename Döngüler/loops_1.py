import random

choices = ['kağıt', 'taş', 'makas']
computer_choice = random.randint(0, 2)

user_choice = input("(Taş, Kağıt, Makas): ").lower()
is_valid_choice = user_choice in choices

while(not is_valid_choice):
  user_choice = input("(Taş, Kağıt, Makas): ").lower()
  is_valid_choice = user_choice in choices

user_choice_index = choices.index(user_choice)

if(user_choice_index + 1 % len(choices) == computer_choice):
  print('bilgisayar: {} siz: {}, kazandınız'.format(choices[computer_choice], user_choice))
elif (user_choice_index == computer_choice):
  print('bilgisayar: {} siz: {}, berabere'.format(choices[computer_choice], user_choice))
else:
  print('bilgisayar: {} siz: {}, bilgisayar kazandı'.format(choices[computer_choice], user_choice))

