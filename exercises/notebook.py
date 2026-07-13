class Notebook:
    def __init__(self):
        self.book = []
    
    def add_note(self, note):
        self.book.append(note)
        
    def show_notes(self):
        for i in range(len(self.book)):
            print(f"{i+1}. {self.book[i]}")
    
book = Notebook()
book.add_note("Buy groceries")
book.add_note("Read a book")
book.add_note("Call the doctor")
book.show_notes()