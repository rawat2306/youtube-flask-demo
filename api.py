from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS
import project   # import the function we just made

app = Flask(__name__)
CORS(app)  # enable CORS right after app = Flask(__name__)


@app.route("/")
def home():
    return "✅ Flask server is running! Try /search?q=your+topic"

@app.route("/search")
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Please provide a search query using ?q="}), 400

    results = project.get_videos(query)   # pass query into project
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
