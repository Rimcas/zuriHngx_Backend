from flask import Flask, request, jsonify

app = Flask(__name__)

    
@app.route('/get_info', methods=['GET'])
def get_info():
    # Get the two GET request parameters from the URL
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both parameters are provided
    if slack_name is None or track is None:
        return jsonify({'error': 'Both parameters (slack_name and track) are required'}), 400

    # Create a JSON response with specific information
    response_data = {
        'Slack_name': "rimcas",
        "current_day": "Tuesday",
        "utc_time": "2023-09-21T15:06:05Z",
        'Track': 'Backend',
         "status_code": 200,
    }

    return jsonify(response_data)

if __name__ == '__main__':
     app.run(debug=True, port=5005)
