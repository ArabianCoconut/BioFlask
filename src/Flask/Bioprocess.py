"""
* @Description: Bio python based on Flask 3.11.x and Flask application.
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
"""
from ast import List
import json
from typing import Any
import requests
from Bio.Align import PairwiseAligner


def load_json(json_stream):
    """
    * This function loads the json stream and returns the results
    * @param {string} json_stream
    * @return {string} load_dump
    """
    j_load = json.loads(json_stream)
    sequence_alignment(j_load['Target'], j_load['Query'])
    return 0


def sequence_alignment(target: str, query: str):
    """
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    """
    alignments: PairwiseAligner = PairwiseAligner().align(target, query, "+")
    results: List() = []
    with open("static/results.txt", "w",encoding='UTF-8') as _f:
        for _a in alignments:
            results.append(_a)
            _f.write(str(_a))
        _f.close()
    return 0


def QRcode(hostname, port):
    '''
    * This function generates the QR code from google chart API
    * @param {string} hostname, the hostname of the server
    * @param {string} port, the port of the server
    '''
    text: Any = "http://" + hostname + ":" + str(port) + "/api/results"
    req: requests = requests.get('https://chart.googleapis.com/chart?cht=qr&cht=qr&chs=200x200&chl=' + text + '&choe=UTF-8',timeout=60)
    with open('static/qr.png', 'wb+') as _f:
        _f.write(req.content)
