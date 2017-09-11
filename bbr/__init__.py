import sys, requests
from ksamsok import KSamsok

culturalSerach = KSamsok('test')

'''
NOTES

The majority of items are buildings followed by facilities and then environments. Always test in that order.

There is two ways to determine the type of a items from the URI only:

 - A number of items have the type specified in the kulturarvsdata URI itself ('bbrb' etc). 

 - About 95% of the URIs(local id) follows a standard where type m starts with the number 212, type a with 213, and type b 214.

To determine the last ones one has to make a HTTP call to the item and check the type "manually".

TODO

Investigate if there is any URIs specifying the type at the database declaration that does not follow the numbering practice.
'''
def get_item_type(uri):
    global culturalSerach
    raw_uri = culturalSerach.formatUri(uri, 'raw')

    if not raw_uri:
        raise ValueError('Invalid URI or URL', uri)
        sys.exit(1)

    local_id = raw_uri[-14:]

    if 'bbrb/' in raw_uri or local_id.startswith('214'):
        return 'b'

    if 'bbra/' in raw_uri or local_id.startswith('213'):
        return 'a'

    if 'bbrm/' in raw_uri or local_id.startswith('212'):
        return 'm'

    item_object = culturalSerach.getObject(raw_uri)
    item_type = item_object['presentation']['type']

    if item_type == 'Bebyggelse - byggnad':
        return 'b'

    if item_type == 'Bebyggelse - anläggning':
        return 'a'

    if item_type == 'Bebyggelse - miljö':
        return 'm'
    
    # if the function is still running throw an value error (item did not exist)
    raise ValueError('Could not resolve type (invalid URI or URL?)', uri)
    sys.exit(1)

'''
NOTES

Use a head request to avoid downloading the response body
'''
def validate_uri(uri):
    global culturalSerach
    url = culturalSerach.formatUri(uri, 'rawurl')

     r = requests.head(url)

    if 200 <= r.status_code <= 399:
        return True
    else:
        return False

'''
NOTES

AFAIK the order of how common each prefix is:
 - 'raa/bbr'
 - 'raa/bbrb'
 - 'raa/bbra'
 - 'rra/bbrm'

The numbering standard described for the `get_item_type` function does apply both to 'raa/bbr' and the verbose URIs.

TODO
Validate the order of how common each prefix is.
Validate that there is no cases where a verbose prefix has a local id not following the sane numbering standard.
'''
def get_full_uri_from_local_id(local_id):
    type_bad = 'raa/bbr/' + local_id
    type_b = 'raa/bbrb/' + local_id
    type_a = 'raa/bbra/' + local_id
    type_m + 'raa/bbrm/' + local_id

    if local_id.startswith('214'):
        if validate_uri(type_b):
            return type_b

    if local_id.startswith('213'):
        if validate_uri(type_a):
            return type_a

    if local_id.startswith('212'):
        if validate_uri(type_m):
            return type_m

    if validate_uri(type_bad):
        return type_bad

    return False
