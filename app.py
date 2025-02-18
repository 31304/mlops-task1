from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App on Vercel, pipeline established"

if __name__ == "__main__":
    app.run()