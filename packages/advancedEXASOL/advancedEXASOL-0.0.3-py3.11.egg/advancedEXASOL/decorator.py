import re

import pandas as pd


def ensure_table_exists(func):
    def wrapper(*args, **kwargs):
        # Get the AdvancedExaFeatures instance
        advanced_exa_features = args[0]

        # Check if the target table exists
        if not advanced_exa_features.table_exists(kwargs["target_table"]):
            # Get the data source
            source = kwargs["source"]

            # Check if the source is a DataFrame
            if isinstance(source, pd.DataFrame):
                # Create the table from the DataFrame
                advanced_exa_features.create_table_from_df(kwargs["target_table"], source)
            else:
                # Create the table from the source table
                advanced_exa_features.create_table_from_table(kwargs["target_table"], source)
        else:
            # Get the column names for the target and source tables
            target_columns = advanced_exa_features.get_column_names(kwargs["target_table"])
            source_columns = advanced_exa_features.get_column_names(kwargs["source"])

            # Get the common columns between the target and source tables
            common_columns = list(set(target_columns) & set(source_columns))

            # Check if there are any missing columns in the target table
            missing_columns = [col for col in source_columns if col not in target_columns]
            if missing_columns:
                # Add the missing columns to the target table
                advanced_exa_features.add_columns(kwargs["target_table"], missing_columns)

            # Check if there are any mismatching data types between the target and source tables
            mismatching_columns = []
            for col in common_columns:
                target_data_type = advanced_exa_features.get_column_data_type(kwargs["target_table"], col)
                source_data_type = advanced_exa_features.get_column_data_type(kwargs["source"], col)
                if target_data_type != source_data_type:
                    mismatching_columns.append(col)
            if mismatching_columns:
                # Raise an error with the mismatching columns
                raise ValueError(
                    f"The following columns have mismatching data types between the target table and the source: {mismatching_columns}")


def ensure_connection(func):
    def wrapper(*args, **kwargs):
        # Get the AdvancedExaFeatures instance
        advanced_exa_features = args[0]

        # Check if the connection is closed
        if advanced_exa_features.conn.closed:
            # Re-establish the connection
            advanced_exa_features.connect(advanced_exa_features.connection_params)

        # Call the decorated function
        return func(*args, **kwargs)

    return wrapper


def handle_transactions(func):
    def wrapper(*args, **kwargs):
        # Get the AdvancedExaFeatures instance
        advanced_exa_features = args[0]

        # Start a transaction
        advanced_exa_features.cursor.execute("START TRANSACTION")

        try:
            # Call the original function
            result = func(*args, **kwargs)

            # Commit the transaction
            advanced_exa_features.cursor.execute("COMMIT")
        except Exception:
            # Rollback the transaction in case of an error
            advanced_exa_features.cursor.execute("ROLLBACK")
            raise

        return result

    return wrapper


def sql_injection_safe(func):
    def wrapper(*args, **kwargs):
        # Get the AdvancedExaFeatures instance
        advanced_exa_features = args[0]

        # Check all SQL queries passed to the decorated function
        for query in kwargs.values():
            # Check if the query contains any potentially dangerous characters
            if re.search(r'[^\w\s]', query):
                # Raise an exception if dangerous characters are found
                raise ValueError(
                    "SQL query contains potentially dangerous characters and may be vulnerable to injection attacks")

        # If no dangerous characters are found, execute the decorated function
        return func(*args, **kwargs)

    return wrapper


def enforce_resource_limits(func):
    def wrapper(*args, **kwargs):
        # Get the AdvancedExaFeatures instance
        advanced_exa_features = args[0]

        # Set the resource limits for the cursor
        advanced_exa_features.cursor.execute("SET MAX_CPU_OPERATION_TIME = 60")
        advanced_exa_features.cursor.execute("SET MAX_MEMORY_USAGE = 100000000")

        # Call the original function
        return func(*args, **kwargs)

    return wrapper