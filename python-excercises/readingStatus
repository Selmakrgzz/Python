def readingStatus(library):
    output="Output: \n"


    for book in library:
        if book['readingStatus'] == True:
            output+=f"You have read the book = {book['title']} by {book['author']} \n"
        if book['readingStatus'] == False:
            output+=f"You have not read the book = {book['title']} by {book['author']} \n"

    print(output)

library = [
    {'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'readingStatus': True},
    {'title': 'Sapiens', 'author': 'Yuval Noah', 'readingStatus': False},
    {'title': 'Factfulness', 'author': 'Hans Rosling', 'readingStatus': True}
]

readingStatus(library)
            
