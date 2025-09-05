from flask import Flask, request, render_template
from utils.search import semantic_search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        results = semantic_search(query)
        return render_template("results.html", results=results, query=query)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)