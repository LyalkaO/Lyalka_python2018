def reverse(text):
   text = text.split((' '))
   text.reverse()
   text = ' '.join(text)
   return (text)
    
text = 'please reverse me'
print(reverse(text))