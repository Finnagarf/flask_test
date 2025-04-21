from flask import Flask, render_template, request
from encrypt import encrypt_with_shift, encrypt_with_keyword, build_keyword_alphabet

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_message', methods=['GET', 'POST'])
def user_message():
    user_text = ''
    shift = ''
    action = ''
    keyword = ''
    result = ''
    error = ''

    if request.method == 'POST':
        user_text = request.form.get('message', '')
        shift = int(request.form.get('quantity', 0))
        action = request.form.get('action', '')
        keyword = request.form.get('keyword', '')

        print(f"Keyword received: '{keyword}'")

        if len(set(keyword.lower())) != len(keyword.lower()):
            error = "Keyword cannot have repeated letters."
        else:
            if action == 'Encrypt':
                result = encrypt_with_keyword(user_text, shift, keyword)
            elif action == 'Decrypt':
                result = encrypt_with_keyword(user_text, -shift, keyword)

    return render_template('user_message.html', original=user_text, result=result, error=error)


if __name__ == '__main__':
    app.run()
