class AccessToken(object):

    """Retrieve access token using API credentials.
    """

    def __init__(self, client):
        self.client = client

    def retrieve(self, options={}):
        """Returns an access token (required for making all other API calls).

        'oauth/token?grant_type=client_credentials' POST
        """
        body = options['body'] if 'body' in options else {}

        response = self.client.post('oauth/token?grant_type=client_credentials', body, options)

        return response

