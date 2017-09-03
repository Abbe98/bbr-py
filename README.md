# BBR-PY

A Python library to determine the type of an item from Bebyggelseregistret given its URI.

BBR-PY can determine the item type using only its URI in 95% of all cases for the other 5% it falls back to making a HTTP lookup.

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

# return 'b', 'a' or 'm'
bbr.get_item_type('<URI>')
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
