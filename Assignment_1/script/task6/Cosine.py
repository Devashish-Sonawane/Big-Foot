subprocess.run(['python', '../cosine_similarity.py', '--inputDir', '../splits', '--outCSV', 'cosine.csv'], check=True)


subprocess.run(['python', '../edit-cosine-circle-packing.py', '--inputCSV', 'cosine.csv', '--cluster', '2'], check=True)


subprocess.run(['python', '../edit-cosine-cluster.py', '--inputCSV', 'cosine.csv', '--cluster', '2'], check=True)


subprocess.run(['python', '../generateLevelCluster.py'], check=True)
