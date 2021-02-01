from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {'name': 'First store',
     'item': 
     [{"name": "first item",
         "price": 15.99

    }]}]

@app.route('/')
#endpoint or request to understand by the app
def home():
    return "Hey you! Heroku is finally working."

@app.route('/store', methods=['POST']) #to create a new store using the new name coming from request method
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data['name'],
                 "item": []
                }
    stores.append(new_store)
    return jsonify(new_store) 

@app.route('/store/<string:name>') #to retreive a specific store
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store') #, methods=['GET']) #default method is get
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'],
                        'price': request_data['price']}
            store['item'].append(new_item)
            return jsonify({'items': store})
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['item']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)