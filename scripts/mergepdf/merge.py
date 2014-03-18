#! /usr/bin/python
#
# mergepdf 
#   Merge pages from a a collection of PDF files into a single PDF file.
#   based on this script and modify a bit:http://jasonmaur.com/merge-pdf-files-using-python/
#
#   ./mergepdf.py [--path  <path containing pdf files to merge>]  [--sort <sort the pdf files in source directory by: name/date asc/decending order>]  [--output] [--output path and file name]"
#
#   Parameter:
#
#   --path
#       path of pdf files intend to merge	
#
#   --sort
#       sort the pdf files by: by their name or modified time
#
#   --output
#       output path and file name
#   example:
#       ./mergepdf.py --path ~/Desktop/test/ --sort nameasc --output ~/Desktop/merge.pdf
import os
import pyPdf
import argparse


#Parse the command-line arguments, and assign them to the appropriate variables.
parser = argparse.ArgumentParser(description='Blindly merge multiple PDF files together.')

parser.add_argument('-p', '--path', dest='path', default='', help='The path to where the pdf files reside, with trailing slash.')
parser.add_argument('-s', '--sort', dest='sort', default='', help='sort by name/date in asending/desending order')
parser.add_argument('-o', '--output', dest='output', default='', help='The full path to the output pdf file.')

args = parser.parse_args()

path = args.__dict__['path'].strip()
output_filename = args.__dict__['output'].strip()
output = pyPdf.PdfFileWriter()
sortby = args.__dict__['sort'].strip()

files = [os.path.join(path, fname) for fname in os.listdir(path) if fname.endswith('.pdf')];
print '\noriginal files are' 
print files 

## sort files: 
##     nameasc: by name ascending order
##     namedec: by name decending order
##     timeasc: by time ascending order
##     timedec: by time decending order

if sortby.lower() == 'nameasc': 
    files.sort(key=lambda x: os.path.basename(x),reverse=False);
elif sortby.lower() == 'namedec': 
    files.sort(key=lambda x: os.path.basename(x),reverse=True);
elif sortby.lower() == 'timeasc': 
    files.sort(key=lambda x: os.path.getmtime(x),reverse=False);
elif sortby.lower() == 'timedec': 
    files.sort(key=lambda x: os.path.getmtime(x),reverse=True);

print '\nsorted files are' 
print files 

for filename in files:
    input = pyPdf.PdfFileReader(file(filename.strip(), "rb"))
    for page in input.pages:
        output.addPage(page)

outputstream = file(output_filename, "wb")
output.write(outputstream)
outputstream.close()
