from flash import Flask
app = Flask(__name__)

app.route("/puppies")
def puppiesFunction():
    return "Yes, puppies"

app.route("<int:id")
def puppiesFunctionID(id):
    return "This method will act on the puppy with id %s" % id