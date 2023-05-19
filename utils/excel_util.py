import pandas as pd
import os


def write_to_excel(records, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    df = pd.DataFrame(records)
    df.to_excel(path, index=False)


def update_excel_cell(path, sheet_name, row, col, value):
    df = pd.read_excel(path, sheet_name=sheet_name)
    df.iloc[row, col] = value
    df.to_excel(path, index=False)


if __name__ == '__main__':
    update_excel_cell(r"E:\novel-ai\data\output\爽文\story_1\task.xlsx", "Sheet1", 2, 5, '语音已生成')
