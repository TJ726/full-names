This code takes a csv file with 3 columns (first_name, last_name, age) as input,\
It returns an output csv with a fourth column (full_name).\
The fourth column is a concatenation of first_name and last_name columns.

## To run this code -

First, install dependencies
```
pip install -r requirements.txt
```

Next, Run the python script
```
python app.py
```

The script will prompt the user for input file path.\
The user can choose to enter the desired input file path, \
or continue with the default input file path - 'data/standard_test.csv'

## Assumptions - 
1. The columns are named 'first_name', 'last_name' and 'age', however, the code does accept incorrect casing.
2. The data types for first_name, last_name and age are str, str and int respectively.
3. Null values are replaced with empty strings for the first_name and last_name.
4. Null values are replaced with -1 for age.
