# mergepdf.py 

> this script is based on [this](based on this script and modify a bit:http://jasonmaur.com/merge-pdf-files-using-python/) and modified based on my own needs

#### functions

Merge pages from a a collection of PDF files into a single PDF file.

#### usage

```
   ./mergepdf.py [--path  <path containing pdf files to merge>]  [--sort <sort the pdf files in source directory by: name/date asc/decending order>]  [--output] [--output path and file name]"
```

#### example usage

```
./mergepdf.py --path ~/Desktop/test/ --sort nameasc --output ~/Desktop/merge.pdf
```
