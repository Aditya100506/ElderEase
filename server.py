from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)

# In-memory storage (acts like mini database)
data_store = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload_vitals", methods=["POST"])
def upload_vitals():
    data = request.json

    # Add timestamp
    data["timestamp"] = datetime.datetime.now().strftime("%H:%M:%S")

    # Simple fall detection logic
    if data["acceleration"] > 2.5:
        data["fall_detected"] = True
    else:
        data["fall_detected"] = False

    data_store.append(data)

    return jsonify({"status": "received"})


@app.route("/latest", methods=["GET"])
def latest():
    if len(data_store) == 0:
        return jsonify({})
    return jsonify(data_store[-1])


@app.route("/history", methods=["GET"])
def history():
    return jsonify(data_store)


@app.route("/sos", methods=["POST"])
def sos():
    return jsonify({
        "message": "🚨 Caregiver Notified Successfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)