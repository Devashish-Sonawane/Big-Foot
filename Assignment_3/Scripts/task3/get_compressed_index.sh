#!/usr/bin/env bash
set -e
docker exec task3-solr-1 tar -czvf /tmp/solrIndex.tar.gz /var/solr/data/bigfoot/data/index
docker cp task3-solr-1:/tmp/solrIndex.tar.gz .
