import connexion
import six

from swagger_server.models.http_response import HTTPResponse  # noqa: E501
from swagger_server.models.register_new_user import RegisterNewUser  # noqa: E501
from swagger_server import util


def login_user(body=None):  # noqa: E501
    """login_user

    Login a user to Journal # noqa: E501

    :param body: Login to Journal by email or username.
    :type body: dict | bytes

    :rtype: HTTPResponse
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_user():  # noqa: E501
    """logout_user

    Logout a user from Journal # noqa: E501


    :rtype: HTTPResponse
    """
    return 'do some magic!'


def register_user(body=None):  # noqa: E501
    """register_user

    Registers a new users. # noqa: E501

    :param body: New user object that needs to be registered.
    :type body: dict | bytes

    :rtype: HTTPResponse
    """
    if connexion.request.is_json:
        body = RegisterNewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

