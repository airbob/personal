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
