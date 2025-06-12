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

# Data manipulation:

def exercise_3():
   movies = ["Mike 17", "Black Bag", "Monkey"]
   movies.append("Gladiator")
   
   favorite_food = ("Plantains", "Carbonara", "Lentejas")
   programming_languages = {"Python", "JS", "Java"}

   capitals = {
      "France": "Paris",
      "United Kingdom": "London",
      "Colombia": "Bogota"
   }

   print(f"favorite movies: {movies} ")
   print(f"favorite food: {favorite_food}")
   print(f"Languages: {programming_languages}")
   print(f"Capitals visited: {capitals}")

exercise_3()

# OOP

class Book:
   def __init__(self, titulo, autor, paginas):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas
      self.leido = False
      
      
   def mark_as_read(self):
      self.leido = True

   def get_info(self):
      status = "Leido" if self.leido else "No Leido"
      return f"'{self.titulo}' by {self.autor}' ({self.paginas} paginas) - {status}"


book1 = Book('Python Crash Course', 'Eric Matthes', '544')
print(book1.get_info())