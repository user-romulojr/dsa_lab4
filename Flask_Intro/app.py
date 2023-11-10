from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    answer = None
    pi = 3.14
    if request.method == 'POST':
        input_radius = float(request.form.get('inputRadius', ''))
        answer = pi * input_radius * input_radius
    return render_template('areaOfcircle.html', result=answer)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    answer = None
    if request.method == 'POST':
        input_base = float(request.form.get('inputBase', ''))
        input_height = float(request.form.get('inputHeight', ''))
        answer = 0.5 * input_base * input_height
    return render_template('areaOfTriangle.html', result=answer)


if __name__ == "__main__":
    app.run(debug=True)
