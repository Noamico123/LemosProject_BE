from dotenv import load_dotenv
from flask import Flask, request

from external_api_requests.printnode_api import PrintNodeAPI
from server_mgmt.firebase_admin_mgmt import FirebaseMGMT

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Lemos!'


@app.route('/users')
def flask_get_users():
    firebase_db = FirebaseMGMT()
    users_data = firebase_db.get_users_from_auth()

    users_data_list = []

    for user in users_data:
        user_dic = user.__dict__
        users_data_list.append(user_dic)

    return users_data_list


@app.route('/users/db', methods=['GET'])
def flask_get_users_from_storage():
    firebase_db = FirebaseMGMT()
    users_data_db = firebase_db.get_users_from_storage()

    if not users_data_db or len(firebase_db.get_users_from_auth()) > len(users_data_db):
        users_data_db = firebase_db.get_users_from_auth()
        firebase_db.post_users()

    users_data_list = []

    for user in users_data_db:
        users_data_list.append(user)

    return users_data_list


@app.route('/users', methods=['POST'])
def flask_post_users():
    firebase_db = FirebaseMGMT()
    users_data = firebase_db.post_users()

    return users_data


@app.route('/users/add_user', methods=['POST'])
def flask_post_new_user():
    email = request.args.get('email', '')
    is_admin = request.args.get('is_admin', '')
    api_key = request.args.get('api_key', '')

    firebase_db = FirebaseMGMT()
    users_data = firebase_db.post_user(email=email, api_key=api_key, is_admin=is_admin)

    return users_data


@app.route('/users/permission', methods=['PUT'])
def flask_update_user_permissions():
    email = request.args.get('email')
    is_admin = request.args.get('is_admin')

    firebase_db = FirebaseMGMT()
    users_data = firebase_db.update_user(email=email, is_admin=is_admin)

    return users_data


@app.route('/printers', methods=['GET'])
def flask_get_printers():
    firebase_db = FirebaseMGMT()
    printers_data = firebase_db.get_printers()

    return printers_data


@app.route('/printers_by_key', methods=['GET'])
def flask_get_printers_by_key():
    api_key = request.args.get('api_key', '')

    print_node_api = PrintNodeAPI()
    res_json = print_node_api.get_user_data_from_printnode_api_by_key(api_key=api_key)

    printers_data = print_node_api.get_printers_list(res_json)

    printers_data_list = []

    for printer in printers_data:
        printer_dic = printer.__dict__
        printers_data_list.append(printer_dic)

    return printers_data_list


@app.route('/printers', methods=['POST'])
def flask_post_printers():
    firebase_db = FirebaseMGMT()
    printers_data = firebase_db.post_printers()

    return printers_data


@app.route('/printers/nickname', methods=['PUT'])
def flask_update_printer_nickname():
    pid = request.args.get('pid')
    name = request.args.get('name')

    firebase_db = FirebaseMGMT()
    printers_data = firebase_db.update_printer_nickname(printer_id=pid, printer_name=name)

    return printers_data


@app.route('/printers/state', methods=['PUT'])
def flask_update_printer_state():
    pid = request.args.get('pid')
    state = request.args.get('state')

    firebase_db = FirebaseMGMT()
    printers_data = firebase_db.update_printer_state(printer_id=pid, printer_state=state)

    return printers_data


@app.route('/orders', methods=['GET'])
def flask_get_orders():
    firebase_db = FirebaseMGMT()
    orders_data = firebase_db.get_orders()

    return orders_data


@app.route('/orders', methods=['POST'])
def flask_post_orders():
    firebase_db = FirebaseMGMT()
    orders_data = firebase_db.post_orders()

    return orders_data


@app.route('/orders/add_order', methods=['PUT'])
def flask_update_orders_list():
    comments = request.args.get('comments')
    address = request.args.get('address')
    customer_name = request.args.get('customer_name')
    time = request.args.get('time')

    firebase_db = FirebaseMGMT()
    firebase_db.add_order_to_json(
        comments=comments,
        address=address,
        customer_name=customer_name,
        time=time
    )

    orders_data_list = firebase_db.get_orders()

    return orders_data_list


def run_server():

    load_dotenv()
    app.run(debug=True, port=8003)
