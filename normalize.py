import sys
from collections import defaultdict
import os

args = sys.argv[1:]

score_file_path = args[0]

topic_scores = defaultdict(list)

with open(score_file_path, 'r+') as f:
    for line in f:
        topic_id, _, doc_id, rank, score, _ = line.split()

        score = float(score)

        topic_scores[topic_id].append(score)

    # move the file pointer to the beginning of the file
    f.seek(0)

    # erase the contents of the file
    f.truncate()

    max_scores = {}
    for topic_id, scores in topic_scores.items():
        max_score = max(scores)
        max_scores[topic_id] = max_score

    for line in open(score_file_path):
        topic_id, _, doc_id, rank, score, _ = line.split()
        score = float(score)
        max_score = max_scores[topic_id]
        normalized_score = score / max_score
        f.write(f"{topic_id} 1 {doc_id} {rank} {normalized_score} donut_graph\n")
