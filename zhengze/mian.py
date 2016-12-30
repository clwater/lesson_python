animal = 'aa.aa@aaa.ccc aa@aaa.ccc'

import re
import requests

# resault = re.findall('[\w.]{3,6}@\w+\.\w+', animal , re.I)
# print(resault)

text = requests.get("http://gank.io/")
src = re.findall('"https?://.*sinaimg.*\.[pngjpg]*' , text.text , re.I)

#print(text.text)
print(src)