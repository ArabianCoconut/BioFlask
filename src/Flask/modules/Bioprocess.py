"""
* @Description: Bio python based on Flask 3.11.x and Flask application.
* @Author: ArabianCoconut
* @Version: Alpha build
"""

import json
import requests
import requests.cookies
from Bio.Align import PairwiseAligner
from flask import request


def load_json(json_stream):
    """
    * This function loads the json stream and returns the results
    * @param {string} json_stream
    * @return {string} load_dump
    """
    j_load: object = json.loads(json_stream)
    sequence_alignment(j_load["Target"], j_load["Query"], j_load["Mode"])
    qr_code(j_load["Url"])
    return 0


def sequence_alignment(target: str, query: str, mode: str):
    """
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    """
    USER_COOKIE = usercookie()
    FilePath = f"static/results_{USER_COOKIE}.txt"
    alignments: object = PairwiseAligner()
    alignments.mode = mode
    alignments = alignments.align(target, query)
    results: list = []    
    with open(FilePath, "w", encoding="UTF-8") as file:
        for _a in alignments:
            results.append(_a)
            file.write(str(_a))
    return 0


def qr_code(qr):
    """
    * This function generates the QR code from Google chart API
    * @param {string} hostname, the hostname of the server
    * @param {string} port, the port of the server
    """
    USER_COOKIE = usercookie()

    QR_PATH = f"../static/qr_{USER_COOKIE}.png"
    text: str = qr + "api/results"
    url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="
    encoding = "&choe=" + "UTF-8"
    req = requests.get(url + text + encoding, timeout=120)
    with open(QR_PATH, "wb+") as file:
        file.write(req.content)
    return 0


def usercookie():
    USER_COOKIE = request.cookies.get("Username")
    return USER_COOKIE
