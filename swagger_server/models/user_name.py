# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserName(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, username: str=None):  # noqa: E501
        """UserName - a model defined in Swagger

        :param username: The username of this UserName.  # noqa: E501
        :type username: str
        """
        self.swagger_types = {
            'username': str
        }

        self.attribute_map = {
            'username': 'username'
        }
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'UserName':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserName of this UserName.  # noqa: E501
        :rtype: UserName
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UserName.

        user unique public identifcation name handle  # noqa: E501

        :return: The username of this UserName.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UserName.

        user unique public identifcation name handle  # noqa: E501

        :param username: The username of this UserName.
        :type username: str
        """

        self._username = username
