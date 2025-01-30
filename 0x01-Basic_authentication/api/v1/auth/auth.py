#!/usr/bin/env python3
""" Authentication module """

from flask import request
from typing import List, TypeVar

class Auth:
    """ Template for all authentication systems """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for a given path """
        if path is None:
            return True
        if not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        for ex_path in excluded_paths:
            if ex_path.rstrip('/') + '/' == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header from the request """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current authenticated user (to be implemented later) """
        return None

