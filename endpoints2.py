from flask import Flask, request
app = Flask(__name__)
# Create the appropriate app.route functions, test and see if they work, and paste your URIs in the boxes below.

#Make an app.route() decorator here

@app.route('/puppies')
def puppiesFunction():
  if request.method == 'GET':
      getAllPuppies()
  elif request.method == 'POST':
      makeANewPuppy()
  
  
 
#Make another app.route() decorator here that takes in an integer id in the 
@app.route('/puppies/<int:id>')
def puppiesFunctionId(id):
  if request.method == 'GET':
      getPuppy(id)  	
  elif request.method == 'PUT':
      updatePuppy(id)
  elif request.method == 'DELETE':
      deletePuppy(id)
  	


def getAllPuppies():
  return "Getting All the puppies!"
  
def makeANewPuppy():
  return "Creating A New Puppy!"

def getPuppy(id):
	return "Getting Puppy with id %s" % id
	
def updatePuppy(id):
  return "Updating a Puppy with id %s" % id

def deletePuppy(id):
  return "Removing Puppy with id %s" % id