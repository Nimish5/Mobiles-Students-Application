"""queue implementation using Flask
Simple API based queue, which can hold objects of type String"""

from collections import deque
from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

queue = deque()


MAX_QUEUE_LENGTH = 10


@app.route('/stats')
def get_stats():
    resp = {'queue_size': list(queue), "max_queue_size" : MAX_QUEUE_LENGTH}
    return jsonify(resp), 200


@app.route('/get_queue')
def retrieve_queue():
    resp = {'full_queue': list(queue)}
    return jsonify(resp), 200


@app.route('/pop', methods = ['DELETE'])
def pop():
    if len(queue) == 0:
        resp = {"status": "Fail", "message": "No element in Queue","queue_size": len(queue)}
        return jsonify(resp), 200

    item = queue.popleft()
    print('An item/ json is deleted from the starting of the queue list!')
    resp = {"data": item["data"], "status": "Success", "queue_size": len(queue)}
    return jsonify(resp), 200


@app.route('/push', methods = ['POST'])
def post_method():
    input_data = request.get_json()
    print(f"input_data:{input_data}")

    if len(queue) >= MAX_QUEUE_LENGTH:
        resp = {"status":"Fail", "message":"Queue Size limit reached", "queue_size": len(queue)}
        return jsonify(resp), 406

    queue.append({"data": input_data['data'], "created_at":datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]})
    print('Item added to the queue')
    resp = {"status":"Success", "message":"Object Added to queue", "queue_size": len(queue)}
    return jsonify(resp), 200



if __name__ == "__main__":
    app.run(debug=True)