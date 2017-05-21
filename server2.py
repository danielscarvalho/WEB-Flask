
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, session, redirect, url_for, escape, request
import random

cores=["Azul","Verde","Vermelho","Amarelo"]

app = Flask(__name__)

app.secret_key = 'ae8e94f51fc8b670da21e404f24c682b' #md5 hash code

def getGame(size):
    gameList=[]
    for i in range(size):
        gameList.append(random.choice(cores))

    return gameList

@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return ('Logged in as ' + str(username) + '<br>' + \
              "<b><a href = '/logout'>click here to log out</a></b>"+ \
              "<p>" + str(session['jogo']) + "</p>")

   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      session['jogo']=getGame(20)
      return redirect(url_for('index'))
   return '''

   <form action = "" method = "post">
      <p><input type = "text" name = "username"/></p>
      <p><input type = "submit" value = "Login"/></p>
   </form>

   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

# Execução local!!!
# Remover isso no caso de rodar no Python Anyware
if __name__ == '__main__':
    app.run(debug=True)
