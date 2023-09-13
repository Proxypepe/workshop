import json
import pathlib
import pandas as pd


policies = ('cpol-disallow-default-namespace',)


def parse():
    dir_path = 'reports'
    reports_dir = pathlib.Path(dir_path)
    files = tuple(reports_dir.iterdir())
    sheet_content = {'policy': [], 'namespace': [], 'apiVersion': [], 'kind': [], 'name': []}
    for policy_name in policies:
        filtered_files = filter(lambda x: policy_name in x.name, files)
        content = []
        for file_name in filtered_files:
            with open(file_name, 'r') as file:
                content += json.load(file)
        for frame in content:
            print(frame)
            for resource in frame['resources']:
                sheet_content['namespace'].append(resource['namespace'])
                sheet_content['apiVersion'].append(resource['apiVersion'])
                sheet_content['kind'].append(resource['kind'])
                sheet_content['name'].append(resource['name'])
                sheet_content['policy'].append(frame['policy'])
        df = pd.DataFrame(sheet_content)
        df.to_excel('output.xlsx', sheet_name=policy_name)


if __name__ == '__main__':
    parse()

