#!/usr/bin/env bash
set -e
docker exec task4-imagespace-imagecat-1 tar -czvf imageCat.tar.gz /deploy/solr4/example/solr/imagecatdev/data/index
docker cp task4-imagespace-imagecat-1:/imagecat/auto/imageCat.tar.gz .
