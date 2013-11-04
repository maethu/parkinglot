from flask import Flask
from flask import Response
from flask import render_template
from flask import url_for

from parkingslot import ParkingSlotObserver
from json import loads

app = Flask(__name__)


@app.route("/")
def index():
    observer = ParkingSlotObserver(distance=20)
    infos = observer.get_json()
    data = loads(infos)
    return render_template('index.html', parkinglots=data)
    return str(data)

@app.route("/json")
def json():
    observer = ParkingSlotObserver(distance=20)
    infos = observer.get_json()
    response =  Response(response=infos,
                    status=200,
                    mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(debug=True)
