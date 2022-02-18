"""Utility functions for querying and returning SQLAlchemy models."""

import json

import numpy as np
import pandas as pd
from pandas.api.types import is_datetime64_any_dtype as is_datetime
import sqlalchemy as sqla

from ..models.base import BaseModel
from .. import db
from config import Config


def array_of(input):
    """Return input as an array if not already."""

    if not type(input) in [list, str]:
        raise TypeError("Input must be a list or a string.")
    return [input] if isinstance(input, str) else input


def create_table(table_names):
    """Create a table from a model using the __tablename__(s)."""

    table_names = array_of(table_names)
    table_objects = [BaseModel.metadata.tables[table] for table in table_names]
    engine = sqla.create_engine(Config.SQLALCHEMY_DATABASE_URI)
    BaseModel.metadata.create_all(engine, tables=table_objects)


def create_upsert(meta):
    """Return a pandas to_sql insert method callable."""

    def method(table, conn, keys, data_iter):
        # Find table class by name
        sql_table = sqla.Table(table.name, meta, autoload=True)
        # Construct insert statement with data_iter
        insert_stmt = sqla.dialects.mysql.insert(sql_table).values(
            [dict(zip(keys, data)) for data in data_iter]
        )
        # Use on_duplicate_key_update
        upsert_stmt = insert_stmt.on_duplicate_key_update(
            {x.name: x for x in insert_stmt.inserted}
        )
        conn.execute(upsert_stmt)

    return method


def get_all_subclasses(cls):
    """Recursively return all subclasses."""

    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


def if_then(arg, clause):
    """Factored out ternary for when a filter clause contains a None arg."""

    return clause if arg is not None else True


def df_json(df):
    """Return SQLA query results as a json string."""
    return json.loads(df.to_json(orient="records"))


def json_df(j):
    """Return JSON as a pandas DataFrame."""

    df = pd.read_json(j, orient="records")
    # Convert datetimes outside of to_json to avoid UTC time ("Z" suffix)
    for col in df:
        if is_datetime(df[col].dtype):
            df[col] = df[col].dt.strftime("%Y-%d-%mT%H:%M:%S")

    return df


def query_df(query):
    """Return SQLA query results as a pandas DataFrame."""

    return pd.DataFrame(data=serialize(db.session.execute(query).all()))


def query_json(query):
    """Return SQLA query results as a json string."""

    return df_json(query_df(query))


def serialize(result):
    """Return SQLA results as a dict or list regardless of result type."""

    # Test if result is empty
    if result == []:
        return result

    # If the result is a SQLAlchemy row instance (i.e., one query result)
    if type(result).__name__ == "Row":
        # If the row contains a model instance
        if issubclass(result[0].__class__, BaseModel):
            # Return a dict of the model instance columns and values
            return result[0].as_dict()
        # Else, return a dict of the row columns and values
        return dict(result)
    # Else, if the result is of multiple row intances
    elif type(result).__name__ == "list":
        # If the rows are model instances
        if issubclass(result[0][0].__class__, BaseModel):
            # Return a list of dicts of the model instance columns and values
            return [row[0].as_dict() for row in result]
        # Return a list of dicts of the result columns and values
        return [dict(row) for row in result]
