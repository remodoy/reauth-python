Reauth
======

Reauth client library for python.

Installation
------------
Using distutils.

    python setup.py install

Using precompiled packages
    
    easy_install reauth-latest.tar.gz

Usage
-----

Remember to check system clocks when using ReAuth token!

### Get public key from ReAuth server

Get public key from server using ReAuth server base url (reauth_url)
and optional verify option.

    get_public_key(reauth_url, verify=True)

### Fetch ReAuth token from server

Fetch ReAuth token from server using fetch code.

    fetch_reauth_token(code, reauth_url, verify=True)

### Decode ReAuth token

Decode ReAuth token and return Claims dict on success.
Claims contains values defined in server configration.

    decode_reauth_token(token, public_key)


Compile package
---------------

To compile distribution package, run command

    python setup.py sdist --formats=gztar,zip
