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
   def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages
      self.is_read = False
            
   def mark_as_read(self):
      self.is_read = True

   def get_info(self):
      status = "Read" if self.is_read else "Not read"
      return f"'{self.title}' by {self.author}' ({self.pages} pages) - {status}"


class Library:
    def __init__(self):
            self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to library")
        
    def list_books(self):
        print("Library Books:")
        for i, book in enumerate(self.books, 1):
            print(f"  {i}. {book.get_info()}")
        
    def books_read(self):
        read_books = [book for book in self.books if book.is_read]
        return len(read_books)


library = Library()
book1 = Book('Python Crash Course', 'Eric Matthes', '544')
book2 = Book("Clean Code", "Robert Martin", 464)
book3 = Book("The Pragmatic Programmer", "David Thomas", 352)

# print(book1.get_info())
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

book1.mark_as_read()
book3.mark_as_read()
library.list_books()
print(f"\nBooks read: {library.books_read()}/{len(library.books)}")