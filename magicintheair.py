class Book:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.title}:{self.author}:{self.number_of_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.number_of_pages < other.number_of_pages

    def __gt__(self, other):
        return self.number_of_pages > other.number_of_pages

    def __add__(self, other):
        return f"{self.number_of_pages + other.number_of_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title


book1 = Book("Damn it morty", "Rick Sanchez", 300)
book2 = Book("How to be unemployed", "Jerry Smith", 400)
book3 = Book("How to operate on a horse", "Beth Smith", 300)
book4 = Book("Let's do poppers", "Summer smith", 200)
book5 = Book("Life in matrix prision", "Morty Smith", 50)
book6 = Book("Life in matrix prision", "Morty Smith", 50)
print(book5 == book6)
print(book1)
print(book2)
print(book3)
print(book4)
print(book5)
print(book6 < book1)
print(book6 > book1)
print(book6 + book1)
print("Lion" in book6)
print(book1.title)
print(book1['title'])
