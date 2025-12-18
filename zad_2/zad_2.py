class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"Library {self.city}, {self.street}, {self.zip_code}"
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f'Book: {self.author_name} {self.author_surname}, pages: {self.number_of_pages}, {self.library}'
class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        books_list = ', '.join(str(book) for book in self.books)
        return (
            f'Order date: {self.order_date}\n'
            f'Handled by: {self.employee}\n'
            f'Books: {books_list}'
        )

Library_1 = Library('Cracow','Old Town', '34-400', '8-16', '182626838')
Library_2 = Library('Warsaw', 'Main Street', '40-627', '8-18', '203627819')
Employee_1 = Employee('Maria', 'Sienkiewicz', '26.08.2022', '17.04.2001', 'Krakow', 'Szlak', '34-467', '576383929')
Employee_2 = Employee('Karolina', 'Kowalska', '17.04.2020', '26.07.1999', 'Warsaw', 'Krotka', '45-274', '863528473')
Employee_3 = Employee('Adam', 'Nowak', '05.11.2018', '20.01.1994', 'Krakow', 'Mala', '36-362', '638295738')
Book_1 = Book(Library_1, '2012', 'Olga', 'Tokarczuk', '280')
Book_2 = Book(Library_2, '2008', 'Maria', 'Jagielo', '320')
Book_3 = Book(Library_1, '2005', 'Henryk','Sienkiewicz', '360')
Book_4 = Book(Library_2, '2010', 'Olga', 'Tokarczuk', '300')
Book_5 = Book(Library_1, '2008', 'Stephen', 'King', '420')
Order_1 = Order(Employee_1, 'Student A',[Book_1, Book_2], '27.11.2024')
Order_2 = Order(Employee_2, 'Srudent B', [Book_3, Book_4, Book_5], '17.07.2025')
print(Order_1)
print()
print(Order_2)