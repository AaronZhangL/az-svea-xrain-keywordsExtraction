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

# https://spacy.io/models/en#en_core_web_sm
$ python -m spacy download en_core_web_sm

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

## NEO4J

https://neo4j.com/developer/docker/#docker-store

Neo4j 3.0 Docker Image

docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=$HOME/neo4j/logs:/logs \
    neo4j:3.0

### start mutipl neo4j database
Apparently in Community Edition you only have 1 database, so I used docker containers to create one server per db. Modify the ports + data volume as shown below:

docker run \
--rm \
--publish=8474:7474 --publish=8687:7687 \
--volume=$HOME/neo4j/data2:/data \
--volume=$HOME/Downloads/neo4j/import:/var/lib/neo4j/import \
--name=neo4j \
--env NEO4J_AUTH=neo4j/password \
neo4j:3.4


# Defaults:
# --publish=7474:7474 --publish=7687:7687 \
# --volume=$HOME/neo4j/data:/data \

### neo4j cypher

MATCH (n) RETURN n

MATCH (n) DETACH DELETE n

## Init parameters before running svea_neo4jManager.py

$ export NEO4J_USER="neo4j"
$ export NEO4J_PASSWORD="my-password"
$ export NEO4J_URI="bolt://xxx.xxx.xxx.xxx:7687"
$ python svea_neo4jManager.py


