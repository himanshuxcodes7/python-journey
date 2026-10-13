class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")

        if not self.reviews:
            print("No reviews yet!")
        else:
            print("Reviews:")
            for review in self.reviews:
                print(f"- {review}")    
            


book1 = Book("Atomic Habit", "James Clear")

book1.add_review("best book in building habits")
book1.add_review("Easy to understand")

book1.display_reviews()
print("Total reviews = ", book1.count_reviews())