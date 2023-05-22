## Import required libraries
import os
import pandas as pd

## Storing data path
default_data_path = "data/standard_test.csv"
output_path = "data/output.csv"


expected_dtypes = {"first_name": str, "last_name": str, "age": int}
required_columns = ["first_name", "last_name", "age"]


def check_columns(df):
    """
    The check_columns function will extract the required columns.
    """
    try:
        df = df[required_columns]
    except KeyError as e:
        print("Error in column lookup : ", e)
        exit(0)
    return df


def check_datatypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    The check_datatypes function validates the data types of the required columns.
    It will also attempt to change the data type to the expected type.
    """
    for key, value in expected_dtypes.items():
        if df[key].dtype != value:
            try:
                df[key] = df[key].astype(value)
            except ValueError:
                print(f"column {key} cannot be converted to {value}")
                exit(0)
            except:
                print("Error in conversion of column data types")
                exit(0)
    return df


def main():
    ## Taking an input for the input file path, added condition to use default input file
    data_path = (
        input("Enter input file path (or press enter to use default): ")
        or default_data_path
    )

    ## Checking if the input file exists and performing a check to ensure input file is saved in a csv format
    if not os.path.isfile(data_path) or not data_path.endswith(".csv"):
        print("Input file not found/ File not in csv")
        return

    ## reading the input file
    df = pd.read_csv(data_path)

    ## Ensure all column names are as per standards
    df.columns = df.columns.str.strip().str.lower()

    ## checking for getting the required columns
    df = check_columns(df)

    ## trim the string columns to get rid of any leading or trailing spaces
    df[["first_name", "last_name"]] = df[["first_name", "last_name"]].apply(
        lambda x: x.str.strip()
    )

    ## replace nulls with empty strings for str columns and replacing nulls with -1 for age
    df.fillna({"first_name": "", "last_name": "", "age": -1}, inplace=True)

    ## manage data types
    df = check_datatypes(df)

    ## create new column with full names by concatinating first and last names
    df["full_name"] = df["first_name"] + " " + df["last_name"]

    ## Strip full name with any strailing or leading spaces caused by missing first or last name
    df["full_name"] = df["full_name"].str.strip()

    ## save to output.csv file
    df.to_csv(output_path, index=False)
    print(f"Output file successfully generated at {output_path}")


if __name__ == "__main__":
    main()
