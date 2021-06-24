import pyarrow as pa
import pandas as pd
import pyarrow.parquet as pq
from pyarrow import csv



def main():
  df = pd.read_csv('files/people.csv')

  table = pa.Table.from_pandas(df)

  pq.write_table(table, 'files/people.parquet')


main()
