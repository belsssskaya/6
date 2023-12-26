class Author:
    def __init__(self, name):
        self.name = name

class Publication:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

class Journal:
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.publications = []

    def add_author(self, author):
        self.authors.append(author)

    def add_publication(self, publication):
        self.publications.append(publication)

    def display_contents(self):
        print(f"Журнал: {self.name}")
        print("Авторы:")
        for author in self.authors:
            print(author.name)

        print("Публикации:")
        for publication in self.publications:
            print(f"Название: {publication.title}, Год: {publication.year}")

    def display_representation(self):
        print(f"Журнал: {self.name}")
        print("Авторы и их публикации:")
        for author in self.authors:
            print(f"Автор: {author.name}")
            publications_by_author = [publication.title for publication in self.publications if
                                      publication.author == author]
            if publications_by_author:
                print("Публикации:")
                for publication in publications_by_author:
                    print(publication)
            else:
                print("Нет публикаций этого автора")


journals = []

# Главный цикл программы
def main ():
    while True:
        print("Меню:")
        print("1. Создать новый журнал")
        print("2. Вывести содержимое журналов")
        print("3. Вывести представление конкретного журнала")
        print("4. Завершить работу программы")
        choice = int(input("Введите номер выбранного пункта: "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            print("Программа завершена.")
            break
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт из меню (1-4).")
if __name__ == "__main__":
    main()