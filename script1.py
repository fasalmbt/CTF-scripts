

#script for Emdee five for life web challenge in HACKTHEBOX

import hashlib as hl
import re
import requests as req

url = "#replace your URL here"

r = req.session()

o = r.get(url)

o1 = re.search(r"<h3 align='center'>(\w*)</h3>",o.text)

o2 = hl.md5(o1.group(1).encode('utf-8')).hexdigest()

print("Sending MD5:-{}".format(o2))


data = {'hash':o2}

o = r.post(url = url,data=data)

print(o.text)





