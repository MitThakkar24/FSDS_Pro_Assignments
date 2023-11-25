from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (Replace with database)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    # Add more books as needed
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# CREATE a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if not new_book or 'title' not in new_book or 'author' not in new_book:
        return jsonify({"error": "Invalid request"}), 400
    
    # Generate a unique ID (replace with database logic)
    new_book['id'] = len(books) + 1
    books.append(new_book)
    
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# UPDATE a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book_to_update = next((book for book in books if book['id'] == book_id), None)
    if not book_to_update:
        return jsonify({"error": "Book not found"}), 404
    
    updated_book = request.get_json()
    if not updated_book or 'title' not in updated_book or 'author' not in updated_book:
        return jsonify({"error": "Invalid request"}), 400
    
    book_to_update['title'] = updated_book['title']
    book_to_update['author'] = updated_book['author']
    
    return jsonify({"message": "Book updated successfully", "book": book_to_update})

# DELETE a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
