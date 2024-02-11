class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            raise ValueError("Pages should be a positive integer.")

    def __str__(self):
        return super().__str__() + f". Количество страниц: {self.get_pages()}"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        if isinstance(duration, float) and duration > 0:
            self._duration = duration
        else:
            raise ValueError("Duration should be a positive floating-point number.")

    def __str__(self):
        return super().__str__() + f". Продолжительность: {self.get_duration()}"


def main():
    book1 = PaperBook("Война и мир", "Лев Толстой", 1225)
    print(book1)

    book2 = AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 8.3)
    print(book2)


if __name__ == "__main__":
    main()