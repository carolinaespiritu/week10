from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filepath = "/Users/carolinaespiritu/Desktop/virtualenv/virtualenv/week10/static/info.txt"):
    with open(filepath, 'r') as f:
        
        return [line for line in f]
    
def index():
    text = readDetails('/Users/carolinaespiritu/Desktop/virtualenv/virtualenv/week10/static/info.txt')
    return render_template('homepage.html', text = text)
    
#Make a homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')


filepath = "/static/info.txt"
@app.route('/')
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]
    
@app.route('/')
def index():
    text = readDetails(filepath)
    return render_template('homepage.html', text = text)

@app.route('/hello/<name>')
def hello(name):
    listOfNames = [name, "YO", "Yennifer"]
    return render_template('name.html', name = name, nameList = listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

#Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug = True)
