import subprocess

subprocess.run(['python', '../edit-value-similarity.py', '--inputDir', '../splits', '--outCSV', 'edit.csv'], check=True)


subprocess.run(['python', '../edit-cosine-circle-packing.py', '--inputCSV', 'edit.csv', '--cluster', '0'], check=True)


subprocess.run(['python', '../edit-cosine-cluster.py', '--inputCSV', 'edit.csv', '--cluster', '2'], check=True)


subprocess.run(['python', '../generateLevelCluster.py'], check=True)
