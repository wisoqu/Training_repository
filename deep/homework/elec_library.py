class Book:
    def __init__(self, title: str, author: str, weight: float):
        self._title = title
        self._author = author
        self._weight = weight
        self._progress = 0  # процент прочтения

    # --- Только чтение ---
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def weight(self):
        return self._weight

    # --- Можно менять только прогресс ---
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if value > 100:
            raise ValueError("Процент не может быть больше 100")
        self._progress = value  # отрицательные допустимы по условию

    def __str__(self):
        return f"{self.title} — {self.author}, вес: {self.weight} кг, прочитано: {self.progress}%"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)