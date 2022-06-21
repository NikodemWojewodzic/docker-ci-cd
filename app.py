from flask import Flask
app = Flask(__name__)

data = {
    "countries": [
        {
            "country": "Proland", 
            "currency": "PLN",
            },
            {
            "country": "Germany", 
            "currency": "Euro",
            },
    ]
} 

@app.route("/")
def index():
        return "docker-ci-cd"

@app.route('/countries')
def get_countries():
    return data


if __name__ == "__main__":
    app.debug = True
    app.run()