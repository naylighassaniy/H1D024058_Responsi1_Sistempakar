from flask import Flask, render_template, request, jsonify
from expert_engine import ExpertEngine

app = Flask(__name__)
engine = ExpertEngine()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/diagnose", methods=["POST"])
def diagnose():
    data     = request.get_json()
    symptoms = set(data.get("symptoms", []))
    result   = engine.evaluate(symptoms)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)