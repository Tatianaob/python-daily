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
  
