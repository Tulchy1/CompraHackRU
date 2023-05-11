from flask import Flask, jsonify, request
import requests
from algorithm import algo

app = Flask(__name__)

# Function to process the algorithm using the received parameters
def process_algorithm(parameters):
    # Call your separate function here and return the result
    result = algo(parameters)
    return result

# Endpoint to receive parameters from the backend and process the algorithm
@app.route('/process', methods=['GET'])
def process_request():
    try:
        data = request.get_json()
        parameters = data['parameters']

        # Perform the algorithm computation using the received parameters
        result = process_algorithm(parameters)

        # Post the result back to the backend service
        backend_url = 'http://backend-service/process-results'
        response = requests.post(backend_url, json={'result': result})

        # Return a response to the backend service
        return jsonify({'message': 'Algorithm executed and results sent successfully'})
    except Exception as e:
        print('Error processing algorithm:', str(e))
        return jsonify({'error': 'An error occurred while processing the algorithm'}), 500

if __name__ == '__main__':
    app.run(port=4001)