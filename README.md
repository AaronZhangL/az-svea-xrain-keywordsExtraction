# az-svea-xrain-keywordsExtraction
Keywords extraction web API

### reference
https://github.com/explosion/spacy-services

https://github.com/timothycrosley/hug

https://github.com/explosion/spaCy

https://spacy.io/models/

### How to generate requirements.txt file.
Method 1:

$ pip freeze > requirements-all.txt

*Method 2:

Use pipreqs - pipreqs used to generate requirements.txt file for any project based on imports

$ pip install pipreqs

$ pipreqs /path/to/project

### requirements.txt sample
hug>=x.x.x,<y.y.y

hug-middleware-cors>=x.x.x,<y.y.y

spacy>=x.x.xx,<x.x.x

waitress>=x.x.x,<x.x.x

https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz#egg=en_core_web_sm==2.0.0

--------------------------------------------------------
# svea-xrain-keywordsExtraction

Serve one or more [spaCy models](https://spacy.io/models) and extract syntactic
dependencies, part-of-speech tags and/or entities.

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## API

### GET `/keywords`

[TODO]

#### Example response

```json
{
    "en_core_web_sm": "English - en_core_web_sm (v2.0.0)"
}
```

