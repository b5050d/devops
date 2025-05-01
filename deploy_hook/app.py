from flask import Flask, request
import subprocess

app = Flask(__name__)

# Define the route to listen for POST requests
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Pull the latest changes from the repository
        try:
            subprocess.run(['git', 'pull'], check=True)
            subprocess.run(['echo', 'hello world'], check=True)

            # Deploy the application (e.g., restart the app or run a script)
            subprocess.run(['systemctl', 'restart', 'your-app-service'], check=True)

            return "Repository updated and application deployed successfully!", 200
        except subprocess.CalledProcessError as e:
            return f"Error during deployment: {e}", 500
    return "Invalid request method", 400

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)