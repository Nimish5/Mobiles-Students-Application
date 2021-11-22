## Simple API Based Queue implemented in Flask


### APIs 
- /push [POST]  -> push a single element to the queue
- /pop [DELETE] -> remove an element from the queue (earliest first)
- /stats [GET]  -> get stats of the queue
- /get_queue [GET]  -> get entire queue


### prerequisites
    - Python 3

### Run
1. Clone the project (git clone https://github.com/Nimish5/Queue-Implementation-Using-Flask.git)
2. Install dependencies
    `pip3 install -r requirements.txt`
3. Run the server
    `python3 app.py`
4. Use postman collection (etc/flask_queue_postman.json) to test.


### TODO
1. Create a test script to test functionality. 
2. Performance Testing script.


### Known limitations and issues
1. Non Persistent Data 
    - Once the server is restarted, all the data in will be lost
2. Only string data supported