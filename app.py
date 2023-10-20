from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT settings
mqtt_broker = "broker.emqx.io"
mqtt_port = 1883
mqtt_topic = "HEALTH"

# Flask route for home page
@app.route('/')
def index():
    return render_template('index.html')

# MQTT on_connect callback function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(mqtt_topic)

# MQTT on_message callback function
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # Do something with the received data
    # For now, just print it

# Set up MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, mqtt_port, 60)

# Run MQTT client in a background thread
client.loop_start()

if __name__ == '__main__':
    app.run(debug=True)
