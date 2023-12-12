#  Наследование – процесс создания нового класса на основе существующего класса.
# Инкапсуляция означает объединение данных и методов, которые с ними работают, в
# единый объект. Объект скрывает свою внутреннюю реализацию, предоставляя только интерфейс
# для взаимодействия с внешним миром. Это позволяет создавать четкие границы между
#  различными компонентами программы.

# Наследование позволяет создавать новые классы на основе существующих, наследуя их свойства
# и методы. Это позволяет повторно использовать код, делая его более эффективным и
# поддерживаемым.

# Полиморфизм позволяет объектам с различной внутренней реализацией вести себя одинаково
# на уровне интерфейса. Это достигается через использование перегрузки методов или
# интерфейсов. Полиморфизм упрощает работу с объектами разных типов, обеспечивая единый
# интерфейс для их взаимодействия и повышая гибкость системы.

# Абстракция позволяет сосредоточить внимание на ключевых аспектах объекта, игнорируя
# ненужные детали. Создание абстракций помогает упростить сложные системы, делая их более
# понятными и управляемыми. Это также способствует изоляции изменений, позволяя
# модифицировать внутреннюю реализацию объекта, не затрагивая внешний код.


class Book:
    def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

book_instance = Book("Abay Joly","M.Auezov","9865214")

print(book_instance.title)

print(book_instance.author)
print(book_instance.isbn)




