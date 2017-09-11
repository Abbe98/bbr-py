# BBR-PY

A Python library to work with URIs from Bebyggelseregistret.

BBR-PY can determine the item type using only its URI in 95% of all cases for the other 5% it falls back to making a HTTP lookup. BBR-PY can also get turn a local id into an Kulturarvsdata compatible URI as well as validate such.

## Installation

```bash
pip install bbr
```

## Usage

BBR items can be of three possible types:

 - Building (`b`)
 - Facility (`a`)
 - Environment (`m`)

```python
import bbr

# returns 'b', 'a', or 'm'
bbr.get_item_type('<URI>')

#returns True or False
bbr.validate_uri(<URI>)

# returns an Kulturarvsdata compatible URI as a string
bbr.get_full_uri_from_local_id(<ID>)
```

BBR-PY can handle all types of URIs and URLs used by kulturarvsdata.se:

 - `http://kulturarvsdata.se/raa/bbr/xml/16000300020896`
 - `http://kulturarvsdata.se/raa/bbr/rdf/16000300020896`
 - `http://kulturarvsdata.se/raa/bbr/html/16000300020896`
 - `http://kulturarvsdata.se/raa/bbr/jsonld/16000300020896`
 - `raa/bbr/xml/16000300020896`
 - `raa/bbr/rdf/16000300020896`
 - `raa/bbr/html/16000300020896`
 - `raa/bbr/jsonld/16000300020896`

Note that MuseumDAT resource URIs/URLs isn't supported by Bebyggelseregistret.
