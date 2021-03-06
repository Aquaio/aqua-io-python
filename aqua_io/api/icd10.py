class Icd10(object):

    """Returns an ICD-10 code.
    """

    def __init__(self, client):
        self.client = client

    def top_level_codes(self, options={}):
        """Returns all top-level ICD-10 codes. Useful for helping a user navigate down the ICD-10 hierarchy to find a code.

        'codes/v1/icd10' GET
        """
        body = options['query'] if 'query' in options else {}

        response = self.client.get('codes/v1/icd10', body, options)

        return response

    def single_code(self, code_name, options={}):
        """Returns a single code matching the name, if any exists. Replace periods with hypens (e.g. 'R50-9' for 'R50.9')

        'codes/v1/icd10/:code_name' GET

        Args:
            code_name: name of code
        """
        body = options['query'] if 'query' in options else {}
        body['code_name'] = code_name

        response = self.client.get('codes/v1/icd10/' + code_name + '', body, options)

        return response

    def search_by_name(self, query, options={}):
        """Returns all codes whose name contains the search string.

        'codes/v1/icd10?q[name_cont]=:query' GET

        Args:
            query: the search query string
        """
        body = options['query'] if 'query' in options else {}
        body['query'] = query

        response = self.client.get('codes/v1/icd10?q[name_cont]=' + query + '', body, options)

        return response

    def search_by_description(self, query, options={}):
        """Returns all codes whose description contains the search string.

        'codes/v1/icd10?q[description_cont]=:query' GET

        Args:
            query: the search query string
        """
        body = options['query'] if 'query' in options else {}
        body['query'] = query

        response = self.client.get('codes/v1/icd10?q[description_cont]=' + query + '', body, options)

        return response

    def search_by_name_or_description(self, query, options={}):
        """Returns all codes whose name or description contains the search string.

        'codes/v1/icd10?q[name_or_description_cont]=:query' GET

        Args:
            query: the search query string
        """
        body = options['query'] if 'query' in options else {}
        body['query'] = query

        response = self.client.get('codes/v1/icd10?q[name_or_description_cont]=' + query + '', body, options)

        return response

