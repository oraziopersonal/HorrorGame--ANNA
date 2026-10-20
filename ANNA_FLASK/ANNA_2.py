import flask as fl

app = fl.Flask(__name__)


@app.route("/")
def home():
    return "ANNA server is running."
def disci_platino():
    return "ANNA PLATINO"
def disci_oro():
    return "ANNA ORO"
def canzoni():
    return "SONG"
def dischi():
    return "dischi"

if __name__ == "__main__":
    app.run()
