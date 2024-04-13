docker cp ../../Dataset1/BFRO_task3.json task3-solr-1:/var/solr/data/BFRO_task3.json
docker exec -it task3-solr-1 solr post -c bigfoot /var/solr/data/BFRO_task3.json
