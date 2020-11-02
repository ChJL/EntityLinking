#!/bin/sh
echo "Processing webpages ..."
python3 starter_code.py data/sample.warc.gz > sample_predictions.tsv
echo "Computing the scores ..."
python3 score.py data/sample_annotations.tsv sample_predictions.tsv
