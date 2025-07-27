from flask import Flask, request
import requests # Use an old, vulnerable version

app = Flask(__name__)

# Hardcoded Secret
API_KEY = "fakedevsec_sk_test_1234567890abcdefghijklmnop"

@app.route('/')
def hello_world():
    # SAST issue: Potential command injection (for demo purposes)
    user_input = request.args.get('name')
    # In a real scenario, this would be more complex
    return f'Hello, {user_input}!'

if __name__ == '__main__':
    app.run(debug=True)
