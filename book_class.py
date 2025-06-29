class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor that initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a human-readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
