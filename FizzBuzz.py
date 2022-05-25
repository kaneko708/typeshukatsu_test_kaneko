for num in range(1, 101):
    string = ''

    # ここから記述
    if(num%3==0 and num%5==0):
      print("FizzBuzz")
    elif(num%3==0 and num%5!=0):
      print("Fizz")
    elif(num%3!=0 and num%5==0):
      print("Buzz")
    else:
      print(num)
    # ここまで記述

    print(string)