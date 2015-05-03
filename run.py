from flask import Flask, render_template
import datetime
current_time=datetime.datetime.now()

app = Flask(__name__)

@app.route("/")
def template_test():
  return render_template('template.html',
                         my_title="Hello World!",
                         my_comment="Welcome to a Hello World Jinja Web Application",
                         my_name="This is a cute Yorkshire Terrier named Oliver Queen!",
                         my_object="celebrity",
                         my_image="http://www.artistryyorkies.com/images/Parallax%20Slide/slide%202.jpg",
                         my_explain="My decision and so will all your identity names!",
                         current_time=datetime.datetime.now())

@app.route("/human")
def human():
  firstname = "Oliver"
  lastname = "Queen"
  return render_template('template.html',
                        my_title="Human Name Generator!",
                        my_comment="Ah! Such a splendid human name, your name shall remain...",
                        my_name=firstname + " " + lastname,
                        my_object="person",
                        my_image="http://m1.paperblog.com/i/63/638384/mr-bean-herido-al-estrellarse-su-mcclaren-f1-L-jBB_uA.jpeg",
                        my_explain="Taking your name and assuring yourself that it is your name.",
                        current_time=datetime.datetime.now())

@app.route("/jedi")
def jedi():
  firstname = "Oliver"
  lastname = "Queen"
  jediname = lastname[0:3] + firstname[0:2]
  return render_template('template.html',
                        my_title="Jedi Name Generator!",
                        my_comment="You are knighted as a Jedi and you shall now be called...",
                        my_name=jediname.title(),
                        my_object="jedi",
                        my_image="http://i10.servimg.com/u/f10/11/24/37/35/14773610.jpg",
                        my_explain="Taking the first three letters of your last name and the first two letters of your first name.",
                        current_time=datetime.datetime.now())

@app.route("/digimon")
def digimon():
  firstname = "Oliver"
  lastname = "Queen"
  digimonname = firstname[0:2] + lastname[0:2] + "mon"
  return render_template('template.html',
                        my_title="Digimon Name Generator!",
                        my_comment="You were warped to the digital world and became...",
                        my_name=digimonname.title(),
                        my_object="digimon",
                        my_image="http://i178.photobucket.com/albums/w255/EB_TES/Digimon/Patamon.png",
                        my_explain="Taking the first two letters of your first and last name, and then adding a -mon at the end.",
                        current_time=datetime.datetime.now())

@app.route("/pokemon")
def pokemon():
  firstname = "Oliver"
  lastname = "Queen"
  minLen = min(len(firstname), len(lastname))
  pokemonname = "".join(y for x in zip(firstname, lastname) for y in x) + firstname[minLen:] + lastname[minLen:]
  return render_template('template.html',
                        my_title="Pokemon Name Generator!",
                        my_comment="You came out of the PokeBall as...",
                        my_object="pokemon",
                        my_name=pokemonname.title(),
                        my_image="https://pokemonaustralia.files.wordpress.com/2012/08/mew.png",
                        my_explain="Alternating the letters of your first and last name.",
                        current_time=datetime.datetime.now())

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
  """Convert a datetime to a different format."""
  return value.strftime(format)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)