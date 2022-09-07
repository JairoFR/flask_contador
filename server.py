from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = '4511vs5d1v56sv51a' # establece una clave secreta


@app.route('/')
def index():
    session['visitas'] = 1
    return render_template("index.html")

@app.route('/click', methods=['POST'])
def click():
    if 'visitas' in session:
        session['visitas'] +=1
    else:
        session['visitas'] +=1
    return render_template('index.html')

@app.route('/restar')
def reset():
    if 'visitas' in session:
        session.pop('visitas')
    return redirect('/')

@app.route('/masdos', methods=['POST'])
def masdos():
    session['visitas'] +=2
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

