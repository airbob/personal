# csvsplit.py 

> Splits a CSV file into multiple pieces based on input options.


### Arguments:

<code>
        `-h`: help file of usage of the script  
        `-i`: input file name 
        `-o`: output file, A %s-style template for the numbered output files.
        `-r`: row limit to split 
        `-c`: A %s-style template for the numbered output files.
</code>

- default settings of the script

<code>

        `output_path`: current directory
        `keep_headers`: Whether or not to print the headers in each output file.
</code>


### Example usage:

```
        ###split by every 10000 rows
        >> ./csvsplit.py -i input.csv -o rownumber -r 10000   
        ###split by unique items in column 0 
        >> ./csvsplit.py -i input.csv -o userid -c 0   
        >> ./csvsplit.py -h for help 
```    