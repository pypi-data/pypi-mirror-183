## dot.parser

[![Generic badge](https://img.shields.io/badge/python-3.10-success.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/GUI-WIP-success.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/CLI-no-red.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/projectStatus-developing-yellow.svg)](https://shields.io/)
![Maintainer](https://img.shields.io/badge/maintainer-koushikdutta-blue)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Tests](https://github.com/macbre/sql-metadata/actions/workflows/python-ci.yml/badge.svg)](https://github.com/macbre/sql-metadata/actions/workflows/python-ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/macbre/sql-metadata/badge.svg?branch=master&1)](https://coveralls.io/github/macbre/sql-metadata?branch=master)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Maintenance](https://img.shields.io/badge/maintained%3F-yes-green.svg)](https://github.com/macbre/sql-metadata/graphs/commit-activity)

### Project Phase One:

- SQL ( Parsing SQL ) Till now I could only managed to create SQL Parser
- Phase Status - initial Development

### Project Phase Two:

- JSON ( JSON Parser )
- CSV ( CSV Parser )
- YAML 
- TOML

- Phase Status - Not Started Yet

### SQL Dialects Supported 

- MySQL
- PostreSQL ( Redshift in progress )
- Sqlite 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

---

### How to use this python module

```
pip install dotparse
```

### Extracting raw sql-metadata tokens

```python
from pysqlutil import parser

# extract raw sql-metadata tokens
parser("SELECT * FROM test_table").tokens
parser("SELECT test, id FROM test_table1,test_table2").columns
# you will get column names

parser_object = parser("<your custom SQL>")
parser_object.columns
# you will get column names as a list

# but you can still extract aliases names
parser_object.columns_aliases
# column alias list 
```
