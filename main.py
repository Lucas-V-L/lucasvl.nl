from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html",\
            homepage=render_template("pages/homepage.html"),\
            aboutpage=render_template("pages/aboutpage.html"))

if __name__ == "__main__":
    app.run(debug=True)
