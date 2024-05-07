from flask import Flask, jsonify

app = Flask(__name__)

# Predefined strings
string_to_reverse = "hello"
string_to_check_palindrome = "radar"

# Route to reverse a predefined string
@app.route('/reverse')
def reverse_string():
    reversed_string = string_to_reverse[::-1]
    return jsonify({'reversed_string': reversed_string})

# Route to check if a predefined string is a palindrome
@app.route('/palindrome')
def check_palindrome():
    is_palindrome = string_to_check_palindrome == string_to_check_palindrome[::-1]
    return jsonify({'is_palindrome': is_palindrome})

if __name__ == '__main__':
    app.run(debug=True)
