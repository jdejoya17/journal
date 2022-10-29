from flask import Blueprint, request

user_routes = Blueprint('user', __name__, url_prefix='/api/v1')


@user_routes.route('/users', methods=['GET'])
def users():
    if request.method =='GET':
        return {'message': 'all users'}

@user_routes.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        return {'message': 'create new user'}

@user_routes.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def userWithId(user_id: int):
    if request.method == 'GET':
        return {'message': 'get user ' + str(user_id)}
    if request.method == 'PUT':
        return {'message': 'update user ' + str(user_id)}
    if request.method == 'DELETE':
        return {'message': 'delete user ' + str(user_id)}
    