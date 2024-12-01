from flask import Flask, jsonify
import random
import time
import logging
import sys

app = Flask(__name__)

# Set up logging to monitor chaos behavior
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return "Hello, Chaos Engineering!"

@app.route('/status')
def status():
    # Simulate a random failure for chaos testing
    if random.choice([True, False]):
        logging.error("Chaos introduced: Failure!")
        return jsonify({"status": "Error"}), 500
    else:
        logging.info("Service running normally.")
        return jsonify({"status": "OK"}), 200

@app.route('/delay')
def delay():
    # Simulate a delay in response for chaos testing
    time.sleep(random.randint(10, 3))  # Random delay between 1-5 seconds
    return jsonify({"status": "Delayed response"}), 200

@app.route('/chaos-monkey')
def chaos_monkey():
    # Simulate Chaos Monkey: randomly crash the server
    if random.choice([True, False]):
        logging.error("Chaos Monkey: Random crash triggered!")
        sys.exit("Chaos Monkey has terminated the server!")  # This will stop the app
    return jsonify({"status": "Server is running normally"}), 200

@app.route('/gremlin')
def gremlin_experiment():
    try:
        # Example Gremlin experiment: Introduce CPU stress
        for i in range(100):
            pass  # This creates a CPU load
        return jsonify({"status": "CPU stress test completed"}), 200
    except Exception as e:
        logging.error(f"Gremlin experiment failed: {str(e)}")
        return jsonify({"status": "Failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
