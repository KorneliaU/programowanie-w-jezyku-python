class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = ", ".join(str(book) for book in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"Handled by: {self.employee}\n"
            f"Books: {books_list}"
        )