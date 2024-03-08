

subprocess.run(['python', '../jaccard_similarity.py', '--inputDir', '../chunks-test', '--outCSV', 'jaccard.csv'], check=True)


subprocess.run(['python', '../edit-cosine-circle-packing.py', '--inputCSV', 'jaccard.csv', '--cluster', '2'], check=True)


subprocess.run(['python', '../edit-cosine-cluster.py', '--inputCSV', 'jaccard.csv', '--cluster', '2'], check=True)


subprocess.run(['python', '../generateLevelCluster.py'], check=True)
