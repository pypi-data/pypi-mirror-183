"""
Module for parsing sql queries and returning columns,
tables, names of with statements etc.
"""
# pylint:disable=unsubscriptable-object
from pysqlutil.parser import Parser
from pysqlutil.keywords_lists import QueryType

__all__ = ["Parser", "QueryType"]
