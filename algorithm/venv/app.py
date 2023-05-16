from flask import Flask, jsonify, request
import requests
from costumer_bot import coverstation_gen

app = Flask(__name__)

# Endpoint to receive parameters from the backend and process the algorithm
@app.route('/process', methods=['POST'])
def process_request():
    try:
        data = request.get_json()['data']
        # Perform the algorithm computation using the received parameters
        result = coverstation_gen(data, "")
        # Return a response to the backend service
        return jsonify({'message': 'Algorithm executed and results sent successfully',
                        'data': result})
    except Exception as e:
        print('Error processing algorithm:', str(e))
        return jsonify({'error': 'An error occurred while processing the algorithm'}), 500

if __name__ == '__main__':
    print("Starting Flask app on port 4001")
    app.run(port=4001)
    print("Flask app is running")