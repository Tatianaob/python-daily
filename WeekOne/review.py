# Variable Operations:
def exercise_1():
    my_name =  "Tatiana Obando"
    my_age = 33
    favorite_color = "Turquoise"
    hobbies = ["Run", "Travel", "Dance"]
  
    future_age = my_age + 10
  
    my_info = {
      "name": my_name,
      "age": my_age,
      "future_age": future_age,
      "favorite_color": favorite_color,
      "hobbies": hobbies
    }

    print("This is my info:")
    for key, value in my_info.items():
      print(f" {key}:{value}")

exercise_1()
  
# Loops:
def exercise_2():
    print("Numbers 1 to 10:")
    for i in range(1, 11):
      print(i, end=" ")
    print()

    # print even numbers from 1 to 20:
    num = 2
    while num <= 20:
       print(num, end=" ")
       num += 2
    print()

    sentence = "Python is awesome for programming, I love it"
    vowels = "aeiouAEIOU"

    vowel_count = 0 
    for char in sentence:
       if char in vowels:
          vowel_count += 1
    print(f"El numero de las vocales en '{sentence}' son {vowel_count}")

exercise_2()

