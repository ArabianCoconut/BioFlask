import json
from Bio.Align import PairwiseAligner

def load_json(json_stream):
    """
    * This function loads the json stream and returns the results
    * @param {string} json_stream
    * @return {string} load_dump
    """
    jload = json.loads(json_stream)
    load_dump = sequence_alignment(jload["Target"], jload["Query"])
    return load_dump


def sequence_alignment(target: str, query: str):
    """
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    """
    alignments = PairwiseAligner().align(target, query, "+")
    results = []
    for alignment in alignments:
        results.append({
            "score": alignment.score,  # type: ignore
            "aligned": str(alignment),
        })
    return json.dumps(results)