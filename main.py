from magazine.product import Product

from library.library import Library
from library.employee import Employee
from library.book import Book
from library.order import Order

product = Product("Book", 100)
print(product.price_with_tax())

library_1 = Library("Cracow", "Old Town", "34-400", "8-16", "182626838")
library_2 = Library("Warsaw", "Main Street", "40-627", "8-18", "203627819")

employee_1 = Employee(
    "Maria",
    "Sienkiewicz",
    "26.08.2022",
    "17.04.2001",
    "Krakow",
    "Szlak",
    "34-467",
    "576383929",
)

employee_2 = Employee(
    "Karolina",
    "Kowalska",
    "17.04.2020",
    "26.07.1999",
    "Warsaw",
    "Krotka",
    "45-274",
    "863528473",
)

book_1 = Book(library_1, "2012", "Olga", "Tokarczuk", 280)
book_2 = Book(library_2, "2008", "Maria", "Jagielo", 320)
book_3 = Book(library_1, "2005", "Henryk", "Sienkiewicz", 360)

order_1 = Order(employee_1, "Student A", [book_1, book_2], "27.11.2024")
order_2 = Order(employee_2, "Student B", [book_3], "17.07.2025")

print(order_1)
print()
print(order_2)
