# This module has more granulated functions which aid in the manipulation of data
import pandas as pd
import numpy as np

def basic_table(read_path, read_type='csv', sheet_name=None, columns_to_keep=None, columns_rename=None, filters=None, group_by=None, aggregate_columns=None, pre_agg_math_columns=None, post_agg_math_columns=None):
    
    if read_type == 'csv':
        df_basic_table = pd.read_csv(read_path)
    elif read_type == 'excel':
        df_basic_table = pd.read_excel(read_path, sheet_name=sheet_name)
    else:
        print('read_type must be either "csv" or "excel"')
    
    if columns_to_keep is not None:
        df_basic_table = df_basic_table[columns_to_keep]
    if columns_to_keep is not None:
        df_basic_table.columns = columns_rename

    if pre_agg_math_columns is not None:
        for new_column_name, math_expression in pre_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)
    
    if filters is not None:
        for column, operator, value in filters:
            if operator == "==":
                df_basic_table = df_basic_table[df_basic_table[column] == value]
            elif operator == "!=":
                df_basic_table = df_basic_table[df_basic_table[column] != value]
            elif operator == ">":
                df_basic_table = df_basic_table[df_basic_table[column] > value]
            elif operator == ">=":
                df_basic_table = df_basic_table[df_basic_table[column] >= value]
            elif operator == "<":
                df_basic_table = df_basic_table[df_basic_table[column] < value]
            elif operator == "<=":
                df_basic_table = df_basic_table[df_basic_table[column] <= value]
    if group_by and aggregate_columns is not None:
        df_basic_table = df_basic_table.groupby(group_by).aggregate(aggregate_columns).reset_index()

    if post_agg_math_columns is not None:
        for new_column_name, math_expression in post_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)


    return df_basic_table

# def isin

# def cast

# def create_row

# def bucket

# def date_format

# def notna
