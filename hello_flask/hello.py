from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello')
def hello():
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>g
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)
   return page.format(num)

@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/results', methods=["POST"])
def results():
   color = request.form['color']
   luck_num = request.form['luck_num']
   fav_class = request.form['fav_class']
   best_pix = request.form['best_pix']

   return render_template('form_results.html', color = color, luck_num = luck_num, fav_class = fav_class, best_pix = best_pix)

@app.route('/thanks')
def thanks():
    person = "Bob"
    action = "dancing"
    gift = "cake"
    author = "Levi"
    Closing_word = "Thanks"
    noun = "car"
    return render_template("tynote.html", name = person, verb = action, gift = gift, author = author, closing_word = Closing_word, noun = noun)      
if __name__ == '__main__':
   app.run()
