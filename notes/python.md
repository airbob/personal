##python notes
===========================



### how to remove punctuations from string?
```python
import re, string
s = "string. With. Punctuation?" # Sample string 
out = re.sub('[%s]' % re.escape(string.punctuation), '', s)
```

### how to remove non-break space from string?
```python
lineString = lineString.replace("\xc2\xa0", " ")
```

### how to filter only chinese characters from string?
```python
#!/usr/bin/env python
# -*- encoding: utf8 -*-
import re

sample = u'I am from 美国。We should be friends. 朋友。'
for n in re.findall(ur'[\u4e00-\u9fff]+',sample):
    print n
```

[reference](http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex)

### how to convert utf-8 BOM file to utf-8 without BOM file?
```python
import os, sys, codecs

BUFSIZE = 4096
BOMLEN = len(codecs.BOM_UTF8)

path = sys.argv[1]
with open(path, "r+b") as fp:
    chunk = fp.read(BUFSIZE)
    if chunk.startswith(codecs.BOM_UTF8):
        i = 0
        chunk = chunk[BOMLEN:]
        while chunk:
            fp.seek(i)
            fp.write(chunk)
            i += len(chunk)
            fp.seek(BOMLEN, os.SEEK_CUR)
            chunk = fp.read(BUFSIZE)
        fp.seek(-BOMLEN, os.SEEK_CUR)
        fp.truncate()
```
[reference](http://stackoverflow.com/questions/2223882/whats-different-between-utf-8-and-utf-8-without-bom)
