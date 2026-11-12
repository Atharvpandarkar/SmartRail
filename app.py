from flask import Flask, jsonify, request
app = Flask(__name__)

TRAINS = [
    {"no": "12127", "name": "Intercity Express", "from": "Pune", "to": "Mumbai", "dep": "06:00"},
    {"no": "11029", "name": "Koyna Express", "from": "Pune", "to": "Kolhapur", "dep": "22:30"},
]

@app.route("/")
def home():
    return "Smart Rail Ticket Booking System is running"

@app.route("/search")
def search():
    s, d = request.args.get("from"), request.args.get("to")
    return jsonify([t for t in TRAINS if t["from"] == s and t["to"] == d])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
