import glob
from pandas import DataFrame
from nginx_logs_parser_and_process.domain.Server.Server import Server
from urllib.parse import unquote


class ReadAllLogsFileIntoMemoryUsingPandas:
    def __init__(self, pd):
        self.pd = pd

    def process(self, server: Server) -> DataFrame:
        data: DataFrame = DataFrame()
        data_frames: list = []
        for log_file in self.get_files_list(server.source_path, server.includes):
            df = self.pd.read_csv(
                log_file,
                sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])',
                engine="python",
                usecols=[0, 3, 4, 5, 6, 7, 8],
                names=["ip", "str_datetime", "request", "status", "size", "referer", "user_agent"],
                na_values="-",
                header=None,
                encoding="utf-8-sig",
                converters={"request": unquote},
            )
            data_frames.append(df)

            data = self.pd.concat(data_frames, axis=0, ignore_index=True)
        return data

    def get_files_list(self, path: str, files_pattern: str) -> list[str]:
        files_patterns_list = files_pattern.split(",")
        files_list: list = []
        for pattern in files_patterns_list:
            files: list = glob.glob(f"{path}{pattern}")
            files.sort()
            files_list.extend(files)
        return files_list
