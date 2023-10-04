import typing
from pydantic import BaseModel
import pandas as pd
import math


class ArtefactStatistic(BaseModel):
    file_path: str
    file_name: str
    repo_key: str
    file_size: int
    created: str
    last_modified: str
    last_download: typing.Optional[str]
    directory_path: typing.Optional[str]

    def __init__(self, **data):
        # .removeprefix(f"{data['repo_key']}:")
        data["directory_path"] = data["file_path"].removesuffix(data['file_name'])
        super().__init__(**data)


def read_log_file(filename: str) -> typing.List[str]:
    row_lines = []
    with open(filename, mode='r', encoding='utf-8') as file:
        while line := file.readline():
            row_lines.append(line.rstrip().split('###')[1])

    return row_lines


def prepare_data(row_lines: typing.List[str]) -> typing.List[ArtefactStatistic]:
    artefactStatistics: typing.List[ArtefactStatistic] = []
    for line in row_lines:
        attributes = line.split(';')
        file_path = attributes[0].split('@')[1]
        file_name = attributes[1].split('@')[1]
        repo_key = attributes[2].split('@')[1]
        file_size = int(attributes[3].split('@')[1])
        last_downloaded = attributes[4].split('@')[1]
        created = attributes[5].split('@')[1]
        last_modified = attributes[6].split('@')[1]
        artefactStatistics.append(ArtefactStatistic(
            file_path=file_path,
            file_name=file_name,
            repo_key=repo_key,
            file_size=file_size,
            created=created,
            last_modified=last_modified,
            last_download=last_downloaded,
        ))
    return artefactStatistics


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def main():
    pd.set_option("display.max_columns", 10)
    filename_log_file = "console.log"
    row_lines = read_log_file(filename_log_file)
    prepared_data = prepare_data(row_lines)
    dataframe = pd.DataFrame([s.__dict__ for s in prepared_data])

    repo_key_sum = dataframe.groupby('repo_key')['file_size'].sum()
    directory_sum = dataframe.groupby('directory_path')['file_size'].sum()
    # directory_sum['file_size'] = directory_sum['file_size'].map(convert_size)
    print(directory_sum.sort_values(ascending=False).apply(convert_size))
    # print(*map(convert_size, directory_sum.array))
    print('-----------------------###############-----------------')
    print(repo_key_sum.sort_values(ascending=False).apply(convert_size))
    print('-----------------------###############-----------------')

    print(dataframe.sort_values(by=['file_size'], ascending=False)[['file_name', 'file_size', 'directory_path']])


if __name__ == '__main__':
    main()
