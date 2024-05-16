import asyncio
import datetime
from functools import lru_cache
from Bio.Blast.NCBIWWW import qblast
from Bio.Blast.NCBIXML import parse


@lru_cache(maxsize=2)
async def web_blast(query, database, hit_list):
    try:
        result = qblast("blastn", database, query, hitlist_size=hit_list)
        with open("src/Flask/static/blast.xml", "w") as output:
            output.write(result.read())
    except ConnectionError:
        return "Server didnt respond as expected, please try again later."
    return "200"


asyncio.run(web_blast("8332116", "nt", 10))

result_handle = open("blast.xml")
blast_record = parse(result_handle)
blast_record = next(blast_record)
with open("src/Flask/static/blast.txt", "w") as out_handle:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            out_handle.write("Timestamp: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
            out_handle.write("******Alignment******\n")
            out_handle.write("Sequence: %s\n" % alignment.title)
            out_handle.write("Length: %i\n" % alignment.length)
            out_handle.write("Score: %i\n" % hsp.score)
            out_handle.write("e-value: %f\n" % hsp.expect)
            out_handle.write("Identities: %i\n" % hsp.identities)
            out_handle.write("Gaps: %i\n" % hsp.gaps)
            out_handle.write(hsp.query[0:] + "\n")
            out_handle.write(hsp.match[0:] + "\n")
            out_handle.write(hsp.sbjct[0:] + "\n")
            out_handle.write("*************************************\n\n")
result_handle.close()
