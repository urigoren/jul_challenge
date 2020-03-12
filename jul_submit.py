import sys, json, os, string

def main(args):
    assert 'submission_name' in args.keys()
    assert set(args["submission_name"])<set(string.ascii_letters+string.digits+"_")
    submission=dict([t.split(':', 1) for t in args["submission"].split(',')])
    with open('jul_test.json', 'r') as f:
        truth=json.load(f)
    acc = 0
    for u,p in submission.items():
        acc+=1 if int(p) in truth.get(u,[]) else 0
    acc/=len(truth)
    fname="jul/"+args["submission_name"]+".json"
    with open(fname, 'w') as f:
        args["score"]="{a:0.3f}".format(a=100*acc)
        json.dump(args, f)                                                                                                                                                                                
    return {"accuracy": acc}
