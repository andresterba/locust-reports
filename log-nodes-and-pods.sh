#!/bin/sh
set -eu -o pipefail

currentNodeCount=0
outputCsvName=$1
deploymentName=$2

printf '%s\n' timetamp nodeCount podCount | paste -sd ',' >> $outputCsvName.csv

while sleep 1
do
    currentNodeCount=$(kubectl get nodes | awk '$2 == "Ready" {print $1}' | wc -l)
    currentPodCount=$( kubectl get deployments.apps $deploymentName | awk 'NR>1 {print $4}')
    #echo $currentNodeCount
    #echo $currentPodCount

    printf '%s\n' $(date +%s) $currentNodeCount $currentPodCount | paste -sd ',' >> $outputCsvName.csv
done
