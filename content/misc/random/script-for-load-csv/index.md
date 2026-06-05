---
title: "Script for Load CSV"
date: 2025-11-08
draft: false
---

**Load CSV**

For loading the csv datas, the load_csv will the main driver:

1. First it will get the data from another function that parses the file

2. Then it will create a list of student objects by going through each student record, pair the header with their student fields into a dictionary, then we feed this dict into the Student class to create a Student Object for each student. Collect each Student Object in a list

3. We assign each Student Object by their class into a new dictionary, 
New class keys will be created as they are being assigned

4. Then we will output this dictionary with list of student object assigned by class

-(1.)------------------------------------------------
 
I will explain how the thing is parsed parse_csv function is the main driver 
- it will first open the file using a context manager to get the header line
- Then it will iterate through the rest of the files, to get the record lines

- Then now we go and individually parse the raw header and the raw record, which is 2 steps for each: 

A. First is, formatting the strings so its easier to manipulate
- format we will strip the leading and trailing characters for each field individually

B. Second is field validation, check if the fields have any format errors

For validating headers
- we will do presence check, then type check, then length check, then membership check, then we will do order check if order matters
- if either of these checks fail it will return false, otherwise return true
- membership check uses symmetric difference which i have manually implemented

For validating records
- i only thought of 2 checks that can be done explicitly, which is presence and length check


defaultdict()


