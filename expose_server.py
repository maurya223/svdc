from pyngrok import ngrok, conf
import subprocess
import time
import os

# Set the ngrok path to the local executable
conf.get_default().ngrok_path = os.path.join(os.getcwd(), "ngrok.exe")

# Set your ngrok auth token if you have one (optional but recommended for more features)
# ngrok.set_auth_token("YOUR_AUTH_TOKEN")

# Start Django server with SSL in the background
print("Starting Django server with HTTPS...")
django_process = subprocess.Popen(['python', 'manage.py', 'runsslserver', '8000', '--certificate', 'localhost+1.pem', '--key', 'localhost+1-key.pem'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait a moment for the server to start
time.sleep(3)

# Expose the local server to the internet with HTTPS
print("Exposing server to the internet via ngrok with HTTPS...")
tunnel = ngrok.connect(8000, "https")
print(f"Public HTTPS URL: {tunnel.public_url}")

# Keep the tunnel open
try:
    print("Press Ctrl+C to stop the tunnel and server.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")

# Clean up
ngrok.disconnect(tunnel.public_url)
ngrok.kill()
django_process.terminate()
django_process.wait()
print("Server and tunnel stopped.")
