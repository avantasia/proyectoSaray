from flask import *
from scripts.script1 import *

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/script1')
def script1():
    sc1=Script1()
    resultado=sc1.funcion1()
    return render_template('script1.html', resultado=resultado)

@app.route('/script2')
def script2():
    sc1=Script1()
    resultado=sc1.funcion1()
    return render_template('script2.html', resultado=resultado)

@app.route('/script2resultado',methods=['POST','GET'])
def script2resultado():
    email = request.form['email']
    return render_template('script2resultado.html', email=email)


@app.route('/script3')
def script3():
    sc1=Script1()
    resultado=sc1.funcion1()
    return render_template('inicio.html', resultado=resultado)

@app.route('/script4')
def script4():
    sc1=Script1()
    resultado=sc1.funcion1()
    return render_template('inicio.html', resultado=resultado)

@app.route('/script5')
def script5():
    sc1=Script1()
    resultado=sc1.funcion1()
    return render_template('inicio.html', resultado=resultado)




if __name__ == '__main__':
    app.run()
