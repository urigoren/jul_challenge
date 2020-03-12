import sys, json
from glob import glob

def main(args):
    ret = []
    for fname in glob("/home/u234-n6rzqpyqtf7e/www/leaderboard.argmax.ml/public_html/jul/*.json"):
        with open(fname, 'r') as f:
            data=json.load(f)
            ret.append((float(data["score"]), data["submission_name"], data["time"]))
    return sorted(ret, reverse=True) 
