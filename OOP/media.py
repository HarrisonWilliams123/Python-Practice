class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
class Book(Media):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

class Magazine(Media):
    def __init__(self, title, price, subscription):
        super().__init__(title, price)
        self.subscription = subscription
    
class DVD(Media):
    def __init__(self, title, price,length):
        super().__init__(title, price)
        self.length = length

book = Book("Clean Code", 499, "Robert C. Martin")
magazine = Magazine("Wired", 150, "Monthly")
dvd = DVD("Inception", 299, 148)

print(f"Book: {book.title} by {book.author} - Rs.{book.price}")
print(f"Magazine: {magazine.title} ({magazine.subscription}) - Rs.{magazine.price}")
print(f"DVD: {dvd.title}, {dvd.length} mins - Rs.{dvd.price}")
