#!/usr/bin/python

import sys,os, getopt
import csv

"""
    Splits a CSV file into multiple pieces based on input options.
    Arguments:

        `-h`: help file of usage of the script  
        `-i`: input file name 
        `-o`: output file, A %s-style template for the numbered output files.
        `-r`: row limit to split 
        `-c`: A %s-style template for the numbered output files.

        default settings of the script
        `output_path`: current directory
        `keep_headers`: Whether or not to print the headers in each output file.

    Example usage:
        ###split by every 10000 rows
        >> ./csvsplit.py -i input.csv -o rownumber -r 10000   
        ###split by unique items in column 0 
        >> ./csvsplit.py -i input.csv -o userid -c 0   
        >> ./csvsplit.py -h for help 
    
"""



def main(argv):
   inputfile = ''
   outputfile = ''
   rowlimit = ''
   columnindex = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:r:c:",["ifile=","ofile=","rowlimit=","columnindex="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'csvsplit.py -i <inputfile> -r <row limit> -c <column index> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-r", "--rowlimit"):
         rowlimit = arg
      elif opt in ("-c", "--columnindex"):
         columnindex = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   print 'rowlimit is "', rowlimit 
   if not columnindex :
      print 'columninex is null'
   if rowlimit and columnindex:
      print 'please take only one option: -r/-c'
      sys.exit()
   #####here begins the split#####   

   if rowlimit:               #split csv file certain rownumber 
      rowlimit = int(rowlimit)
      output_name_template= outputfile+'_%s.csv'
      output_path='.'
      keep_headers=True
      delimiter=','
      filehandler = open(inputfile,'r')
      reader = csv.reader(filehandler, delimiter=delimiter)
      current_piece = 1
      current_out_path = os.path.join(
           output_path,
           output_name_template  % current_piece
      )
      current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
      current_limit = rowlimit
      if keep_headers:
          headers = reader.next()
          current_out_writer.writerow(headers)
      for i, row in enumerate(reader):
          if i + 1 > current_limit:
              current_piece += 1
              current_limit = rowlimit * current_piece
              current_out_path = os.path.join(
                 output_path,
                 output_name_template  % current_piece
              )
              current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
              if keep_headers:
                  current_out_writer.writerow(headers)
          current_out_writer.writerow(row)

   elif columnindex:               #split csv file accrording to unique values of certain column,it's like filter only certain item in excel 
      itemlist = []
      columnindex = int(columnindex)
      output_name_template= outputfile+'_%s.csv'
      output_path='.'
      keep_headers=True
      delimiter=','
      filehandler = open(inputfile,'r')
      reader = csv.reader(filehandler, delimiter=delimiter)
      if keep_headers:
          headers = reader.next()

      for i, row in enumerate(reader):

          current_out_path = os.path.join(
               output_path,
               output_name_template  % row[columnindex] )
          if row[columnindex] not in itemlist:
             try:
                 current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
             except IOError:
                 continue
             else:
                 itemlist.append(row[columnindex])
                 if keep_headers:
                     current_out_writer.writerow(headers)
                 current_out_writer.writerow(row)
          else:
             current_out_writer = csv.writer(open(current_out_path, 'a'), delimiter=delimiter)
             current_out_writer.writerow(row)
      print 'totally %i unique items in column %i \n' % (len(itemlist),columnindex)
   else:
      print "oops, please check instruction of script by >>./csvsplit.py -h"

if __name__ == "__main__":
   main(sys.argv[1:])
