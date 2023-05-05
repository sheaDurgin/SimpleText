# SimpleText Task 1

This repository includes all of the programs and optimal results for my team's (Team Donut Graph, comprised of SJ Franklin and I, Shea Durgin) submission for SimpleText Task 1.

## Table of Contents

- [Installation](#Installation)
- [Text Files](#Text-Files)
- [Steps to Run](#Steps-to-Run)
- [Model Details](#Model-Details)
- [Results](#Top-100-Per-Query-Baseline-Results)
- [Conclusion](#Conclusion)

## Installation

To run this code, you will need access to the [dataset](http://simpletext-project.com/2023/clef/) for task 1 of SimpleText CLEF lab, and login details to access their servers. I will be assuming you have access for the rest of the explanation.

The necessary installs for the code are as such

    torch
    tqdm
    sentence_transformers
    transformers
    textstat
    ranx
    markdown

You can install them using pip:

    pip install torch tqdm sentence_transformers transformers textstat ranx markdown
    
Clone the repository all to one folder to properly run. Directories may need to be changed to fit your machine.

## Text Files
- baseline.txt -> the top 100 results from elastic search for each query
- selective.txt -> the top results (up to 100) from elastic search for each query (no work done to get extra results)
- rr_baseline.txt -> results from cross_encoder.py using baseline.txt as argument
- final_results.txt -> results from combine_scores.py using rr_baseline.txt and selective.txt

## Steps to Run

- Get the SimpleText dataset from CLEF and have both the qrels and topics csv file in repository
- run run_everything.py (can modify names of files and directories in this file)

## Model Details

Our final results come from a combination of the ms-marco-electra-base cross encoder and the two baseline results from elastic search. The cross encoder does its own reranking of the top 100 results from elastic search, then that output is directed into a comination program that does a final reranking using a combination of the cross encoder ranking and the selective baseline results. This results in higher NDCG and MAP scores than any of the individual results.

## Baseline Results

    NDCG@10: 0.374
    MAP: 0.438
    flesch average: 28.673
    smog average: 14.792
    Coleman Liau average: 15.923
    
## Selective Results (Gives less total results)

    NDCG@10: 0.409
    MAP: 0.456
    flesch average: 28.673
    smog average: 14.792
    Coleman Liau average: 15.923
    
## Reranking Results

    NDCG@10: 0.307
    MAP: 0.316
    flesch average: 28.673
    smog average: 14.792
    Coleman Liau average: 15.923

## Final Results

    NDCG@10: 0.460
    MAP: 0.506
    flesch average: 28.673
    smog average: 14.792
    Coleman Liau average: 15.923

## Conclusion

With the use of a cross encoder and a combination algorithm, we were able to improve the baseline results in both NDCG@10 and MAP scores. If we were to continue on the project, we would attempt to fine-tune the cross encoder on the labelled data and implement a way to select more readable passages than just the entire abstract (as our current implementation has no improvement in the readability department). 
