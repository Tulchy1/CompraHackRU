from flask import Flask, jsonify, request
import requests
#from algorithm import algo

app = Flask(__name__)

# Function to process the algorithm using the received parameters
#def process_algorithm(parameters):
    # Call your separate function here and return the result
    #result = algo(parameters)
    #return result

# Endpoint to receive parameters from the backend and process the algorithm
@app.route('/process', methods=['GET'])
def process_request():
    try:
        data = request.get_json()
        parameters = data['parameters']

        # Perform the algorithm computation using the received parameters
        result = process_algorithm(parameters)

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