word = input('Word: ')

isLowerCase = word.lower() == word

if(isLowerCase):
  print("Kelimede büyük harfler yok")
else:
  print("Kelimede büyük harfler var")
