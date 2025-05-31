import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

#from queries.core import create_table, insert_data
from queries.orm import create_table, async_insert_data

create_table()
async_insert_data()