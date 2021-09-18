"""Queue implementation using Flask?
Create an API to push and pop a/ multiple string/ json!"""

from collections import deque
from flask import Flask, request

app = Flask(__name__)

# https://www.geeksforgeeks.org/queue-in-python/
queUe = deque()

# print(queUe)

@app.route('/retrival')
def strings():
    return {'Queue': list(queUe)}
# We should convert deque object into a list otherwise it will through an error
# i.e. Object of type deque is not JSON serializable

@app.route('/pop', methods = ['DELETE'])
def pop_method():
    queUe.popleft()
    return 'An item/ json is deleted from the starting of the queUe list!'

"""Only GET and POST methods can be work through web brewsers,
as we can request to receive the data and respond the data.
But a web browser dosen't allow PUT and DELETE method to directly delete any 
thing from the browser or from server."""

@app.route('/push', methods = ['POST'])
def post_method():
    input_data = request.get_json()
    queUe.append(input_data['String'])
    return 'A new Item/ Json has been added to the queUe list!'


if __name__ == "__main__":
    app.run(debug=True)