from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checkerboard')
def checkerboard_8_8():
    return render_template('index.html', x=8, y=8)


@app.route('/checkerboard/<int:x>')
def checkerboard_4_8(x):
    return render_template('index.html', x=4, y=8)


@app.route('/checkerboard/<int:x>/<int:y>')
def checkerboard_x_y(x, y):
    return render_template('index.html', x=x, y=y)


if __name__=="__main__":
    app.run(debug=True)