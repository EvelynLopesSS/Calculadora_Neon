from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html', expression='', result='')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression', '')
    button_value = request.form.get('button', '')
    result = ''  
    return render_template('calculator.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
