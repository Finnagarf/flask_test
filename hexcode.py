from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

# Function to validate the hex code
def valid_hex_chars(hex_code):
    # Ensure the hex code starts with '#' and has exactly 6 valid hex characters (0-9, a-f)
    if hex_code.startswith('#') and len(hex_code) == 7:
        hex_code = hex_code[1:]  # Remove the '#' before checking the characters
        return all(c in '0123456789ABCDEFabcdef' for c in hex_code)
    return False

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():
    feedback = ""
    if request.method == 'POST':
        hex_code = request.form['hex']
        if valid_hex_chars(hex_code):
            feedback = "Successful submission!"
        else:
            feedback = "Invalid hex code! Please enter a valid hex color code (e.g., #FF0000)."
    else:
        hex_code = 'FF0000'  # Default hex code if no form submission

    return render_template('hex_form.html', hex=hex_code, feedback=feedback)

if __name__ == '__main__':
    app.run()


# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
