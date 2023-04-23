"""
* @Description: Bio python based on Flask 3.11.x and Flask application.
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
"""
import json
from Bio.Align import PairwiseAligner



def load_json(json_stream):
    '''
    * This function loads the json stream and returns the results
    * @param {string} json_stream
    * @return {string} load_dump
    '''
    jload=json.loads(json_stream)
    load_dump=sequence_alignment(jload["target"],jload["query"],jload["mode"])
    return load_dump

def sequence_alignment(target:str, query:str,mode:str):
    '''
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    '''
    alignments = PairwiseAligner().align(target, query,"+")
    results=[]
    for alignment in alignments:
        results.append({
            "mode": mode,
            "score": alignment.score, # type: ignore
            "aligned": str(alignment),
        })
    return json.dumps(results)

# ! Testing only will remove later.
# test={"target":"ACCGGT","query":"ACG","mode":"local"}
# load_json(json.dumps(test))
print(__name__)
print(__package__)