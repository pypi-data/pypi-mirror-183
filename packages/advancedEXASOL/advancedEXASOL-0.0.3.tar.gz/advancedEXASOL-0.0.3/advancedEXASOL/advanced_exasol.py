import json

from .decorator import ensure_table_exists, ensure_connection, handle_transactions, sql_injection_safe, enforce_resource_limits
import pyexasol
import dask.dataframe as dd
import pandas as pd
import requests
import csv
import xlwt


def _get_source_type(source):
    if isinstance(source, pd.DataFrame):
        return 'pandas'
    elif isinstance(source, dd.DataFrame):
        return 'dask'
    elif isinstance(source, str):
        if source.endswith('.csv'):
            return 'csv'
        elif source.endswith('.json'):
            return 'json'
        elif source.endswith('.xml'):
            return 'xml'
        elif source.endswith('.xls') or source.endswith('.xlsx'):
            return 'excel'
        else:
            try:
                json.loads(source)
                return 'json_str'
            except json.JSONDecodeError:
                raise ValueError(
                    'Unable to determine source type. Please provide a valid file path or a valid DataFrame.')
    else:
        raise ValueError('Unable to determine source type. Please provide a valid file path or a valid DataFrame.')


class Features(pyexasol.ExaConnection):
    DATATYPE_MAPPING = {
        'int8': 'TINYINT',
        'int16': 'SMALLINT',
        'int32': 'INTEGER',
        'int64': 'BIGINT',
        'uint8': 'TINYINT',
        'uint16': 'SMALLINT',
        'uint32': 'INTEGER',
        'uint64': 'BIGINT',
        'float16': 'FLOAT',
        'float32': 'FLOAT',
        'float64': 'DOUBLE',
        'bool': 'BOOLEAN',
        'object': 'VARCHAR',
        'category': 'VARCHAR',
        'datetime64': 'TIMESTAMP',
        'timedelta[ns]': 'INTERVAL'
    }

    def __init__(self, connection_params):
        self.conn = None
        self.cursor = None
        self.connect(connection_params)

    @enforce_resource_limits
    @ensure_connection
    @sql_injection_safe
    def connect(self, connection_params):
        self.conn = pyexasol.connect(**connection_params)
        self.cursor = self.conn.cursor()

    @enforce_resource_limits
    @ensure_connection
    @sql_injection_safe
    def close(self):
        self.cursor.close()
        self.conn.close()
        self.conn = None
        self.cursor = None

    @enforce_resource_limits
    @ensure_connection
    @ensure_table_exists
    @handle_transactions
    @sql_injection_safe
    def execute(self, sql, **kwargs):
        return self.cursor.execute(sql, **kwargs)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @sql_injection_safe
    def fetchall(self, **kwargs):
        return self.cursor.fetchall(**kwargs)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @sql_injection_safe
    def fetchone(self, **kwargs):
        return self.cursor.fetchone(**kwargs)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @sql_injection_safe
    def fetchmany(self, size=None, **kwargs):
        return self.cursor.fetchmany(size=size, **kwargs)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @sql_injection_safe
    def commit(self):
        return self.conn.commit()

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @sql_injection_safe
    def rollback(self):
        return self.conn.rollback()

    def _convert_to_dask_df(self, source, source_type):
        if source_type == 'pandas_df':
            return dd.from_pandas(source, npartitions=self.npartitions)
        elif source_type == 'csv':
            return dd.read_csv(source, blocksize=self.blocksize)
        elif source_type == 'json':
            return dd.read_json(source, blocksize=self.blocksize)
        elif source_type == 'xml':
            return dd.read_xml(source, blocksize=self.blocksize)
        elif source_type == 'excel':
            return dd.read_excel(source, blocksize=self.blocksize)
        else:
            raise ValueError(f"Unrecognized source type: {source_type}")

    @enforce_resource_limits
    @ensure_connection
    def get_column_names(self, table_name):
        """Get the column names for a table, query, or CTE in Exasol."""
        self.cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
        column_names = [d[0] for d in self.cursor.description]
        return column_names

    @enforce_resource_limits
    @ensure_connection
    def table_exists(self, table_name):
        # Check if the table exists by querying the EXA_ALL_TABLES system view
        result = self.cursor.execute(f"SELECT 1 FROM EXA_ALL_TABLES WHERE TABLE_NAME = '{table_name}'")
        return bool(result.fetchone())

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    def create_table_from_df(self, table_name, df):
        # Create a list of column definitions
        column_defs = []
        for col, dtype in zip(df.columns, df.dtypes):
            # Get the Exasol data type for the column
            exa_data_type = self.DATATYPE_MAPPING[str(dtype)]
            # Add the column definition to the list
            column_defs.append(f"{col} {exa_data_type}")
        # Join the column definitions with a comma separator
        column_defs_str = ",\n".join(column_defs)
        # Build the CREATE TABLE statement
        create_stmt = f"""
            CREATE TABLE {table_name} (
            {column_defs_str}
            )
        """
        # Execute the CREATE TABLE statement
        self.cursor.execute(create_stmt)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    def create_table_from_table(self, target_table, source_table):
        # Build the CREATE TABLE AS SELECT statement
        create_stmt = f"CREATE TABLE {target_table} AS SELECT * FROM {source_table}"
        # Execute the CREATE TABLE AS SELECT statement
        self.cursor.execute(create_stmt)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    def add_columns(self, table_name, column_names):
        # Iterate over the column names
        for column_name in column_names:
            # Build the ALTER TABLE ADD COLUMN statement
            alter_stmt = f"ALTER TABLE {table_name} ADD COLUMN {column_name} VARCHAR"
            # Execute the ALTER TABLE ADD COLUMN statement
            self.cursor.execute(alter_stmt)

    @enforce_resource_limits
    @ensure_connection
    def get_column_data_type(self, table_name, column_name):
        # Query the EXA_ALL_COLUMNS system view to get the data type for the column
        result = self.cursor.execute(
            f"SELECT COLUMN_TYPE FROM EXA_ALL_COLUMNS WHERE COLUMN_TABLE = '{table_name}' AND COLUMN_NAME = '{column_name}'")
        # Return the data type from the result
        return result.fetchone()[0]

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    def export_to_dask(self, sql, chunksize=10000):
        """Export data from Exasol to a Dask DataFrame using HTTP transport."""
        # Set up HTTP connection to Exasol
        self.conn.http_setup()

        # Send HTTP request to Exasol to execute the SQL query
        response = requests.post(self.conn.http_url, json={'sql': sql})

        # Get the column names and data types from the response
        column_names = response.json()['column_names']
        column_types = response.json()['column_types']

        # Convert the column types to Dask data types
        dtypes = {name: self.DATATYPE_MAPPING[typ] for name, typ in zip(column_names, column_types)}

        # Create an empty Dask DataFrame with the correct column names and data types
        df = dd.from_pandas(pd.DataFrame(columns=column_names), dtype=dtypes)

        # Iterate over the data chunks in the response and append them to the Dask DataFrame
        for chunk in response.iter_content(chunk_size=chunksize):
            chunk_df = pd.read_json(chunk, orient='records')
            df = df.append(dd.from_pandas(chunk_df, dtype=dtypes))

        return df

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @ensure_table_exists
    def import_from_dask(self, df, table_name, if_exists='fail'):
        """Import data from a Dask DataFrame to Exasol using HTTP transport."""
        # Set up HTTP connection to Exasol
        self.conn.http_setup()

        # Get the column names and data types from the Dask DataFrame
        column_names = df.columns.tolist()
        dtypes = df.dtypes.to_dict()

        # Convert the Dask data types to Exasol data types
        column_types = [self.DATATYPE_MAPPING[typ] for name, typ in dtypes.items()]

        # Create a table in Exasol with the correct column names and data types
        create_table_sql = f'CREATE TABLE {table_name} ({", ".join(f"{name} {typ}" for name, typ in zip(column_names, column_types))})'
        self.cursor.execute(create_table_sql)

        # Iterate over the partitions in the Dask DataFrame and insert the data into the Exasol table
        for partition in df.to_delayed():
            # Convert the partition to a Pandas DataFrame
            partition_df = partition.compute()

            # Convert the Pandas DataFrame to a list of dictionaries
            data = [row.to_dict() for _, row in partition_df.iterrows()]

            # Send an HTTP request to Exasol to insert the data into the table
            url = self.conn.http_url + f'/{table_name}'
            requests.post(url, json=data)

    @staticmethod
    def to_pandas(df):
        """Convert a Dask DataFrame to a Pandas DataFrame."""
        return df.compute()

    @staticmethod
    def to_json(self, df, path):
        """Convert a Dask DataFrame to a JSON file."""
        df.to_csv(path, index=False)

    @staticmethod
    def to_csv(self, df, path):
        """Convert a Dask DataFrame to a CSV file."""
        df.to_csv(path, index=False)

    @staticmethod
    def csv_to_excel(self, csv_file, excel_file):
        """Convert a CSV stream to an Excel file."""
        # Create a Pandas DataFrame from the CSV stream
        df = pd.read_csv(csv_file)

        # Use the Pandas 'to_excel' method to write the DataFrame to an Excel file
        df.to_excel(excel_file, index=False)

    @staticmethod
    def to_xml(self, df, path):
        """Convert a Dask DataFrame to an XML file."""
        # Open a file handle to the destination XML file
        with open(f'{path}.xml', 'w') as xml_file:
            # Use the Dask 'to_csv' method to write the DataFrame to a CSV stream
            df.to_csv(xml_file, index=False)

            # Seek back to the beginning of the stream
            xml_file.seek(0)

            # Write the XML header
            xml_file.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
            xml_file.write('<root>\n')

            # Create a CSV reader and iterate through the rows of the CSV stream
            reader = csv.reader(xml_file)
            for row in reader:
                # Write an XML element for each row, with each column as an attribute
                xml_file.write('  <row')
                for i, col in enumerate(row):
                    xml_file.write(f' col{i}="{col}"')
                xml_file.write('/>\n')

            # Write the XML footer
            xml_file.write('</root>\n')

    def to_excel(self, df, path):
        """Convert a Dask DataFrame to an Excel file."""
        # Open a file handle to the destination Excel file
        with open(f'{path}.xlsx', 'wb') as excel_file:
            # Use the Dask 'to_csv' method to write the DataFrame to a CSV stream
            df.to_csv(excel_file, index=False)

            # Seek back to the beginning of the stream
            excel_file.seek(0)

            # Use the 'csv_to_excel' function to convert the CSV stream to an Excel file
            self.csv_to_excel(excel_file, excel_file)

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @ensure_table_exists
    def merge_tables(self, source, source_type, target_table, primary_columns, exclude_columns=[]):
        """Merge a table or query with an Exasol table, updating common columns and inserting new ones."""
        try:
            # Get the column names for the target table
            target_columns = self.get_column_names(target_table)

            # Determine the common columns between the source and target tables
            if source_type == "table":
                # Get the column names for the source table
                source_columns = self.get_column_names(source)
                common_columns = list(set(source_columns) & set(target_columns))
            elif source_type == "query":
                # Get the column names for the source query
                source = f'({source})'
                self.cursor.execute(f"SELECT * FROM {source} LIMIT 0")
                source_columns = [d[0] for d in self.cursor.description]
                common_columns = list(set(source_columns) & set(target_columns))

            # Remove the primary columns from the list of common columns
            common_columns = [col for col in common_columns if col not in primary_columns]

            # Remove the excluded columns from the list of common columns
            common_columns = [col for col in common_columns if col not in exclude_columns]

            # Build the ON clause for the MERGE INTO statement
            on_clause = " AND ".join([f"TGT.{col} = SRC.{col}" for col in primary_columns])

            # Build the UPDATE SET clause for the MERGE INTO statement
            update_clause = ", ".join([f"TGT.{col} = SRC.{col}" for col in common_columns])

            # Build the INSERT clause for the MERGE INTO statement
            insert_clause = ", ".join(common_columns)

            # Build the full MERGE INTO statement
            merge_stmt = f"""
                MERGE INTO {target_table} TGT
                USING {source} SRC
                ON {on_clause}
                WHEN MATCHED THEN
                    UPDATE SET {update_clause}
                WHEN NOT MATCHED THEN
                    INSERT ({insert_clause})
                    VALUES ({insert_clause})
            """

            # Execute the MERGE INTO statement
            result = self.cursor.execute(merge_stmt)
        except Exception as e:
            # Print the error message and raise the exception
            print(f"Error: {e}")
            raise e
        else:
            # Print the number of rows affected by the MERGE INTO statement
            print(f"{result.rowcount} rows affected")

    @enforce_resource_limits
    @ensure_connection
    @handle_transactions
    @ensure_table_exists
    def merge_from_external(self, target_table, source, primary_columns, source_type=None):
        try:
            # Check if the source type is not provided
            if source_type is None:
                # Get the source type
                source_type = _get_source_type(source)

            # Convert the source to a Dask DataFrame
            source_df = self._convert_to_dask_df(source, source_type)

            # Build the ON clause
            on_clause = " AND ".join([f"TGT.{col} = SRC.{col}" for col in primary_columns])

            # Get the column names for the target and source tables
            target_columns = self.get_column_names(target_table)
            source_columns = source_df.columns.tolist()

            # Get the common columns between the target and source tables
            common_columns = list(set(target_columns) & set(source_columns))

            # Build the UPDATE clause
            update_clause = ", ".join([f"TGT.{col} = SRC.{col}" for col in common_columns])

            # Build the INSERT clause
            insert_clause = ", ".join(common_columns)

            # Build the full MERGE INTO statement
            merge_stmt = f"""
                MERGE INTO {target_table} TGT
                USING {source_df} SRC
                ON {on_clause}
                WHEN MATCHED THEN
                    UPDATE SET {update_clause}
                WHEN NOT MATCHED THEN
                    INSERT ({insert_clause})
                    VALUES ({insert_clause})
            """

            # Execute the MERGE INTO statement
            result = self.cursor.execute(merge_stmt)
        except Exception as e:
            # Print the error message and raise the exception
            print(f"Error: {e}")
            raise e
        else:
            # Print the number of rows affected by the MERGE INTO statement
            print(f"{result.rowcount} rows affected")
