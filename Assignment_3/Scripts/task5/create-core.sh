#!/bin/bash

CMD='cd /home/Solr/solr-5.3.1/ && ./bin/solr create_core -c bigfoot'
docker exec -it docker-memex-geoparser-1 bash -c "$CMD"

