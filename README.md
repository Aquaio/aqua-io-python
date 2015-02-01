# aqua-io-python

Official [Aqua-io](https://aqua.io) API library client for python. Currently covers Aqua.io's ICD-9 and ICD-10 APIs.

## Getting Started

To use the Aqua.io API, you need to have proper API credentials, which you can get for free by [signing up](https://aqua.io/developers/sign_up).

You may also want to read up on [the API documentation](https://aqua.io/codes).

## Installation

Make sure you have [pip](https://pypi.python.org/pypi/pip) installed

```bash
$ pip install aqua-io
```

#### Versions

Works with [ 2.6 / 2.7 / 3.2 / 3.3 ]

## Usage

```python
import aqua_io

# Then we instantiate a client (as shown below)
```

### Build a client

##### Get an access token using your aqua.io credentials

```python
client = aqua_io.Client({ 'client_id': '09a8b7', 'client_secret': '1a2b3' }, client_options)

token = client.access_token.retrieve(options)
```

##### All other API calls require an access token

```python
client = aqua_io.Client(token, client_options)
```

### Client Options

The following options are available while instantiating a client:

 * __base__: Base url for the api
 * __user_agent__: Default user-agent for all requests
 * __headers__: Default headers for all requests
 * __request_type__: Default format of the request body

### Response information

__All the callbacks provided to an api call will receive the response as shown below__

```python
response = client.icd9.top_level_codes(options)

response.code
# >>> 200

response.headers
# >>> {'x-server': 'apache'}
```

##### JSON response

When the response sent by server is __json__, it is decoded into a dict

```python
response.body
# >>> {'user': 'pksunkara'}
```

### Method Options

The following options are available while calling a method of an api:

 * __headers__: Headers for the request
 * __query__: Query parameters for the url
 * __body__: Body of the request
 * __request_type__: Format of the request body

### Request body information

Set __request_type__ in options to modify the body accordingly

##### RAW request

When the value is set to __raw__, don't modify the body at all.

```python
body = 'username=pksunkara'
# >>> 'username=pksunkara'
```

##### JSON request

When the value is set to __json__, JSON encode the body.

```python
body = {'user': 'pksunkara'}
# >>> '{"user": "pksunkara"}'
```

### ICD-9 api

Returns an ICD-9 code.

```python
icd9 = client.icd9()
```

##### All top-level codes (GET codes/v1/icd9)

Returns all top-level ICD-9 codes. Useful for helping a user navigate down the ICD-9 hierarchy to find a code.

```python
response = icd9.top_level_codes(options)
```

##### Retrieve a single code. (GET codes/v1/icd9/:code_name)

Returns a single code matching the name, if any exists. Replace periods with hypens (e.g. '066-4' for '066.4')

The following arguments are required:

 * __code_name__: name of code

```python
response = icd9.single_code("066-4", options)
```

##### Search for codes by name. (GET codes/v1/icd9?q[name_cont]=:query)

Returns all codes whose name contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd9.search_by_name("082-2", options)
```

##### Search for codes by description. (GET codes/v1/icd9?q[description_cont]=:query)

Returns all codes whose description contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd9.search_by_description("eastern equine", options)
```

##### Search for codes by name or description. (GET codes/v1/icd9?q[name_or_description_cont]=:query)

Returns all codes whose name or description contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd9.search_by_name_or_description("west nile", options)
```

### ICD-10 api

Returns an ICD-10 code.

```python
icd10 = client.icd10()
```

##### All top-level codes (GET codes/v1/icd10)

Returns all top-level ICD-10 codes. Useful for helping a user navigate down the ICD-10 hierarchy to find a code.

```python
response = icd10.top_level_codes(options)
```

##### Retrieve a single code. (GET codes/v1/icd10/:code_name)

Returns a single code matching the name, if any exists. Replace periods with hypens (e.g. 'R50-9' for 'R50.9')

The following arguments are required:

 * __code_name__: name of code

```python
response = icd10.single_code("R50-9", options)
```

##### Search for codes by name. (GET codes/v1/icd10?q[name_cont]=:query)

Returns all codes whose name contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd10.search_by_name("b05", options)
```

##### Search for codes by description. (GET codes/v1/icd10?q[description_cont]=:query)

Returns all codes whose description contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd10.search_by_description("mumps", options)
```

##### Search for codes by name or description. (GET codes/v1/icd10?q[name_or_description_cont]=:query)

Returns all codes whose name or description contains the search string.

The following arguments are required:

 * __query__: the search query string

```python
response = icd10.search_by_name_or_description("rubella", options)
```

## Contributors
Here is a list of [Contributors](https://github.com/aquaio/aqua-io-python/contributors)

## License
MIT

## Bug Reports
Report [here](https://github.com/aquaio/aqua-io-python/issues).

## Contact
Michael Carroll at Aqua.io

michael@aqua.io

@_aquaio_

__This library is generated by [alpaca](https://github.com/pksunkara/alpaca).__