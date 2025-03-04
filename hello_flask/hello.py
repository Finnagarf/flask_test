from flask import Flask, render_template
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

@app.route('/thanks')
   def thanks():
      person = "Bob"
      action = "dancing"
      gift = "cake"
      author = "Levi"
      Closing_word = "Thanks"
      return render_template("tynote.html", name = person, verb = action)
      
if __name__ == '__main__':
   app.run()
