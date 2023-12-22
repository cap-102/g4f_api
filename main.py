from scripts import Utils
from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# main script

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["500 per day", "50 per minute"],
    storage_uri="memory://",
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getkey')
def getkey():
    return render_template('getkey.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dev/genkey')
def genkey():
    api_key = Utils.getValidKeys()[0]
    return jsonify(api_key=api_key)


@app.route('/api')
def docs():
    return render_template('docs.html')


@app.route('/api/gpt-3', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def handle_data_gpt3():
    if request.method == 'GET':
        return jsonify({'error': 'Please use a POST request.'}), 400

    if request.method == 'POST':
        try:
            # Get data from the request's JSON payload
            data = request.get_json()

            # Validate the presence of required fields
            result = Utils.checkMissingFields(data)
            if result:
                return result

            return Utils.dialogMaker(data, 'gpt-3')

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': f'Unknown server error.'}), 500


@app.route('/api/gpt-4', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def handle_data_gpt4():
    if request.method == 'GET':
        return jsonify({'error': 'Please use a POST request.'}), 400

    if request.method == 'POST':
        try:
            # Get data from the request's JSON payload
            data = request.get_json()

            # Validate the presence of required fields
            result = Utils.checkMissingFields(data)
            if result:
                return result

            return Utils.dialogMaker(data, 'gpt-4')

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': f'Unknown server error.'}), 500


if __name__ == '__main__':
    app.run(debug=True)
