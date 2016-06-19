# PrettyCSV
A Python script for displaying the data contained within delimited files (CSV et al) in a MySQL-like format.
### Usage
```
prettycsv.py [delimiter] [col name] [col name] ... [file]
```
### Examples
```
prettycsv.py * User "Password Hash" mysql.txt
prettycsv.py : ID Username Password Email phpbb.txt
prettycsv.py , "Full Name" SSN City State Zip experian.csv
```