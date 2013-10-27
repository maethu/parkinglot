from flask import Flask
app = Flask(__name__)

from parkingslot import ParkingSlotObserver


@app.route("/")
def stats():
    observer = ParkingSlotObserver(distance=20)
    return observer.get_slot_informations()

if __name__ == "__main__":
    app.run()
