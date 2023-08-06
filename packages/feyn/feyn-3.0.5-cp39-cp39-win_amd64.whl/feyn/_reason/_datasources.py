import pandas as pd


class Datasource:
    def __init__(self, datasource_id, server="https://app.reason.is"):
        url = server + "/api/datasources/" + datasource_id + "/data"

        self.dataframe = pd.read_parquet(url)

        self.stypes = {column: 'c' for column in self.dataframe.columns if self.dataframe[column].dtype == 'object'}

