from flask import Flask
import config

app = Flask(__name__)
data = config.load_config()


@app.route('/', methods=['GET'])
def index():
    return 'Hello'


app.run(debug=True)
