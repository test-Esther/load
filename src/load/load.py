import pandas as pd
from tabulate import tabulate

def load(path="~/tmp/team_jkl/"):
    df=pd.read_parquet("~/tmp/team_jkl/")

    print(tabulate(df,headers=["movieNm","openDt","salesAmt"], tablefmt="outline"))
