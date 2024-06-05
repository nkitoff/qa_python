import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        book_name_1 = 'Гордость и предубеждение и зомби'
        book_name_2 = 'Что делать, если ваш кот хочет вас убить'
        # добавляем две книги
        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        # проверяем, что добавилось именно две
        # прекод изменен т.к. books_rating отсуттвует в основном классе. Данный тест выдавал ошибку
        assert len(collector.books_genre) == 2 and book_name_1, book_name_2 in collector.books_genre

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self, collector):
        collector.add_new_book('New Book')
        assert 'New Book' in collector.get_books_genre()

    def test_add_new_book_with_invalid_name(self, collector):
        collector.add_new_book('')
        collector.add_new_book('О' * 41)
        assert '' not in collector.get_books_genre()
        assert 'О' * 41 not in collector.get_books_genre()

    def test_set_book_genre(self, collector):
        collector.add_new_book('Вторая книга')
        collector.set_book_genre('Вторая книга', 'Фантастика')
        assert collector.get_book_genre('Вторая книга') == 'Фантастика'

    def test_set_invalid_book_genre(self, collector):
        collector.add_new_book('Третья книга')
        collector.set_book_genre('Третья книга', 'Некорректный жанр')
        assert collector.get_book_genre('Третья книга') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_1', 'Фантастика')
        collector.set_book_genre('Книга_2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга_1']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга_2']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        collector.set_book_genre('Книга_1', 'Фантастика')
        collector.set_book_genre('Книга_2', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга_1']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        collector.delete_book_from_favorites('Любимая книга')
        assert 'Любимая книга' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name, genre", [
        ('Книга_1', 'Фантастика'),
        ('Книга_2', 'Комедии'),
    ])
    def test_parametrized_set_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre