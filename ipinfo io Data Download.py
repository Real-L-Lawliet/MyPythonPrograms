#paste your token from your ipinfo.io account in place of <token>

import urllib.request
import json
ioinfo = urllib.request.urlopen('https://ipinfo.io/geo?token=<token>')
ioinfo = ioinfo.read()
data = json.loads(ioinfo)
print(data)