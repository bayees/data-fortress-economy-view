import os
import duckdb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
MINIO_HOST = os.environ.get("MINIO_HOST")
MINIO_SSL = os.environ.get("MINIO_SSL", "False") == "True"
MINIO_REGION = os.environ.get("MINIO_REGION")


def read_curated(file: str, columns:list=['*'], filter:str = '') -> pd.DataFrame:
    # Adding empty dataframe to enforce columns
    with duckdb.connect() as con:
        con.sql("INSTALL httpfs")
        con.sql("LOAD httpfs")
        con.sql(f"SET s3_region='{MINIO_REGION}';")
        con.sql(f"SET s3_endpoint='{MINIO_HOST}';")
        con.sql(f"SET s3_access_key_id='{MINIO_ACCESS_KEY}';")
        con.sql(f"SET s3_secret_access_key='{MINIO_SECRET_KEY}';")
        con.sql(f"SET s3_use_ssl={MINIO_SSL};")
        con.sql("SET s3_url_style='path';")
        df = con.sql(f"SELECT {', '.join(columns)} FROM read_parquet('s3://{file}') {filter};").df()
        return df


def get_budget():
    df = read_curated('curated/dash/budget.parquet')
    return df

def get_actuals():
    df = read_curated('curated/dash/actuals.parquet', filter="where account_name = 'C&V Budget'")
    return df

if __name__ == "__main__":
    print(get_actuals())