"""
* @Description: Bio python based on Flask 3.11.x and Flask application.
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
"""
import json
from Bio.Align import PairwiseAligner


def load_json(json_stream):
    """
    * This function loads the json stream and returns the results
    * @param {string} json_stream
    * @return {string} load_dump
    """
    j_load = json.loads(json_stream)
    sequence_alignment(j_load['Target'], j_load['Query'])
    # print(type(load_dump))
    return 0


def sequence_alignment(target: str, query: str):
    """
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    """
    alignments = PairwiseAligner().align(target, query, "+")
    results = []
    with open("static/results.txt", "w") as f:
        for a in alignments:
            results.append(a)
            f.write(str(a))
        f.close()

# ! Testing only will remove later.
test={"Target":"AGTCAAAACC","Query":"ACG"}
load_json(json.dumps(test))
