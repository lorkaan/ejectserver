from flask import Flask, jsonify, request

app = Flask(__name__)

class Checker:
    responses = {
        "septicDC": True
    }

    name_key = "name"

    @classmethod
    def is_good(cls, data):
        name = data.get(cls.name_key)
        if type(name) == str and len(name) > 0:
            return cls.responses.get(name, None)
        else:
            return None

output_key = "result"

@app.route('/', methods=['POST'])
def run():
    if request.is_json:
        data = request.json
        output_dict = {}
        try:
            output_dict[output_key] = Checker.is_good(data)
            return jsonify(output_dict), 200
        except Exception as e:
            return e, 500
    else:
        return "Expected JSON input", 400

if __name__ == '__main__':
    app.run(debug=True)