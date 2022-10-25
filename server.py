from flask import Flask, render_template
from main import plot


app = Flask(__name__)

@app.route("/")
def index():
    url_plot=plot()
    return render_template('index.html',url_plot=url_plot)

if __name__ == "__main__":
    app.run(debug=True)