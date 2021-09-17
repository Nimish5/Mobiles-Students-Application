"""Queue implementation using Flask?
Create an API to push and pop a/ multiple string/ json!"""

from collections import deque
from flask import Flask, request

app = Flask(__name__)

# https://www.geeksforgeeks.org/queue-in-python/
Hobbies = deque()

Hobbies.append('My hobbies is to play Batminton, Reading and Programming!')
Hobbies.append('Improving myself every day personally and professionally, Learn each day!')
# print(Hobbies)

@app.route('/hobbies')
def hobby():
    return {'Hobbies': list(Hobbies)}
# We should convert deque object into a list otherwise it will through an error
# i.e. Object of type deque is not JSON serializable

@app.route('/del_hobbies', methods = ['DELETE'])
def pop_method():
    Hobbies.popleft()
    return 'A hobby is deleted from the starting of the Hobbies list!'

"""Only GET and POST methods can be work through web brewsers,
as we can request to receive the data and respond the data.
But a web browser dosen't allow PUT and DELETE method to directly delete any 
thing from the browser or from server."""

@app.route('/add_hobbies', methods = ['POST'])
def post_hobbies():
    input_data = request.get_json()
    Hobbies.append(input_data['String'])
    return 'A new Item/String/Json has been added to the Hobbies list!'


if __name__ == "__main__":
    app.run(debug=True)