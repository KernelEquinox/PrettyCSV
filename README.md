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
### Sample Usage
Contents of example.txt:
```
1,jdoe123,John Doe,johndoe@gmail.com
2,janesmith,Jane Smith,j.smith@corp.org
3,cjohnson,Cave Johnson,tier3@aperturescience.com
4,,,nobody@nowhere.nope
```

Output of `prettycsv.py , ID Username "Real Name" Email example.txt`:
```
+----+-----------+--------------+---------------------------+
| ID | Username  | Real Name    | Email                     |
+----+-----------+--------------+---------------------------+
| 1  | jdoe123   | John Doe     | johndoe@gmail.com         |
| 2  | janesmith | Jane Smith   | j.smith@corp.org          |
| 3  | cjohnson  | Cave Johnson | tier3@aperturescience.com |
| 4  |           |              | nobody@nowhere.nope       |
+----+-----------+--------------+---------------------------+
```
