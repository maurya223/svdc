import subprocess
import time
import os

# Start Django server with SSL in the background
print("Starting Django server with HTTPS...")
django_process = subprocess.Popen(['python', 'manage.py', 'runsslserver', '8000', '--certificate', 'localhost+1.pem', '--key', 'localhost+1-key.pem'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait a moment for the server to start
time.sleep(3)

# Expose the local server to the internet using LocalTunnel
print("Exposing server to the internet via LocalTunnel...")
tunnel_process = subprocess.Popen(['lt', '--port', '8000'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read the tunnel URL from stdout
for line in iter(tunnel_process.stdout.readline, b''):
    line = line.decode('utf-8').strip()
    if 'your url is:' in line:
        public_url = line.split('your url is:')[1].strip()
        print(f"Public URL: {public_url}")
        break

# Keep the tunnel open
try:
    print("Press Ctrl+C to stop the tunnel and server.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")

# Clean up
tunnel_process.terminate()
tunnel_process.wait()
django_process.terminate()
django_process.wait()
print("Server and tunnel stopped.")
