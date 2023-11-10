def check_question(num: str, arg: any):
  if num == '1':
    if arg == 'A':
      message = 'Correct! The basic math operators are "+" for additions, "-" for subtraction, "/" for division and "*" for multiplication'
      print(message)
    else:
      print("Incorrect!")
  elif num == '2':
    if arg == 'C':
      message = 'Correct! The modulo operator gets the remainder!'
      print(message)
    else:
      print("Incorrect!")
  