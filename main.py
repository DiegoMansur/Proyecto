from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/l1')
def l1():
    return render_template('l1.html')

@app.route('/l2')
def l2():
    return render_template('l2.html')

@app.route('/l3')
def l3():
    return render_template('l3.html')

@app.route('/l4')
def l4():
    return render_template('l4.html')

@app.route('/term')
def term():
    return render_template('term.html')

@app.route('/a1')
def a1():
    return render_template('a1.html')

@app.route('/a2')
def a2():
    return render_template('a2.html')

@app.route('/a3')
def a3():
    return render_template('a3.html')

@app.route('/a4')
def a4():   
    return render_template('a4.html')

@app.route('/a5')
def a5():
    return render_template('a5.html')

@app.route('/b1')
def b1():
    return render_template('b1.html')

@app.route('/b2')
def b2():
    return render_template('b2.html')

@app.route('/b3')
def b3():
    return render_template('b3.html')

@app.route('/b4')
def b4():   
    return render_template('b4.html')

@app.route('/c1')
def c1():
    return render_template('c1.html')

@app.route('/c2')
def c2():
    return render_template('c2.html')

@app.route('/c3')
def c3():
    return render_template('c3.html')

@app.route('/c4')
def c4():
    return render_template('c4.html')

@app.route('/c5')
def c5():
    return render_template('c5.html')

@app.route('/c6')
def c6():
    return render_template('c6.html')

@app.route('/d1')
def d1():
    return render_template('d1.html')

@app.route('/d2')
def d2():
    return render_template('d2.html')

@app.route('/d3')
def d3():
    return render_template('d3.html')

@app.route('/d4')
def d4():
    return render_template('d4.html')

@app.route('/d5')
def d5():
    return render_template('d5.html')

@app.route('/d6')
def d6():
    return render_template('d6.html')

if __name__ == '__main__':
    app.run(debug=True)