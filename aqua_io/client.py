from .http_client import HttpClient

# Assign all the api classes
from .api.access_token import AccessToken
from .api.icd9 import Icd9
from .api.icd10 import Icd10


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def access_token(self):
        """Retrieve access token using API credentials.
        """
        return AccessToken(self.http_client)

    def icd9(self):
        """Returns an ICD-9 code.
        """
        return Icd9(self.http_client)

    def icd10(self):
        """Returns an ICD-10 code.
        """
        return Icd10(self.http_client)

