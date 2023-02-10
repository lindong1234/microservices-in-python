# Import Flask and other required modules
from flask import Flask, jsonify, render_template 
import socket

# Create a flask object named app
app = Flask(__name__)

# Function to get the hostname and IP address of the current system
def fetch_details():
   host_name = socket.gethostname() # Get the hostname of the system
   host_ip = socket.gethostbyname(host_name) # Get the IP address of the system
   print("HostName : ", host_name) # Print the hostname
   print("HostIP : ", host_ip) # Print the IP address
   # Return the hostname and IP address as string values
   return str(host_name), str(host_ip)

# Route for the root URL with a message 'hello world'
@app.route('/')
def hello_world():
    return ('hello world')

# Route for '/health' URL with a message 'status up'
@app.route('/health')
def health():
    return jsonify(status="up")

# Route for '/details' URL with the hostname and IP address information
@app.route('/details')
def details():
    hostname, ip = fetch_details() # Get the hostname and IP address using fetch_details()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

# The if __name__ == '__main__' line allows your flask application to be run both standalone, and as part of another application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Start the flask application on IP 0.0.0.0 and port 500

