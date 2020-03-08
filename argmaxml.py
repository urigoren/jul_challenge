import json, sys, urllib, string
def api(endpoint, **kwargs):
    data = urllib.parse.urlencode(kwargs).encode()
    req =  urllib.request.Request("http://api.argmax.ml/"+endpoint, data=data)
    resp = urllib.request.urlopen(req)
    resp = json.loads(resp.read().decode("utf8"))
    if type(resp)==dict and "exception" in resp:
        raise SystemError(resp["exception"] + ": " + resp["message"])
    return resp

def leaderboard():
    return api("jul_leaderboard")

def submit(full_name, email, phone, submission_name, submission_content):
    """Submits a test data set to the argmax server, and returns accuracy"""
    assert set(submission_name)<set(string.ascii_letters+string.digits+"_"), "Invalid Character in submission_name"
    try:
        submission = ",".join(["{k}:{v}".format(k=int(k),v=int(v)) for k,v in submission_content.items()])
        resp = api("jul_submit", full_name=full_name, email=email, phone=phone, submission_name=submission_name, submission=submission)
        return float(resp["accuracy"])
    except Exception as e:
        sys.stderr.write (str(e))
        return None