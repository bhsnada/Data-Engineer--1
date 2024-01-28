import pandas as pd
from database import connect, create_tables, ingest_data, get_sample_data

FILE_PATHS = ['organizations-100.csv', 'organizations-2.csv']


def read_csv(paths):
    """
        read_csv function is able to load data from  different csv file
        paths : list of csv paths
        return Data frame 
    """
    result = [pd.read_csv(_,  encoding='utf-8') for _ in paths]
    if result is not None:
        return pd.concat(result, ignore_index=True)
    else:
        print('Null Data')
        return None


def clean_data(data):
    """
    clean data : this function will do some clean to our data
    """
    try:
        data = data.dropna()
        data["Organization Id"] = data["Organization Id"].astype(str)
        return data.drop_duplicates()
    except Exception as e:
        print(f"An error occured: {e}")
        return None


def load(data):
    """
    load function : connect and ingest data into table
    """
    connection = connect()
    create_tables(connection)
    print('*** ingest {} data into Organization table ***'.format(len(data)))
    for index, row in data.iterrows():
        ingest_data(connection,
                row['Organization Id'],
                row['Name'],
                row['Website'],
                row['Country'],
                row['Description'],
                row['Founded'],
                row['Industry'],
                row['Number of employees'])   
    print("** sample of data ** ")
    get_sample_data(connection)
    


def main():
    data = read_csv(FILE_PATHS)
    cleaned_data = clean_data(data)
    load(cleaned_data)
    return True


if __name__ == '__main__':
    main()
