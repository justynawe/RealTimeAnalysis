from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Witaj, {name}!"
    else:
        return "Witaj!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        # Pobieranie parametrów num1 i num2
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        
        # Logika decyzyjna
        prediction = 1 if (num1 + num2) > 5.8 else 0

        # Zwracanie odpowiedzi
        return jsonify({
            "prediction": prediction,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input parameters."}), 400

if __name__ == '__main__':
    app.run()
