class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.title < other.title
        return False

    def __le__(self, other):
        if isinstance(other, Book):
            return self.author < other.author
        return False

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.year > other.year
        return False
