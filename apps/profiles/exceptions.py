from rest_framework import APIException


class ProfileNotFound(APIException):
    status = 404
    default_detail = "The requested profile does not exists"


class NotYourProfile(APIException):
    status = 403
    default_detail = "You can'/t edit a profile that doesn't belong to you"
