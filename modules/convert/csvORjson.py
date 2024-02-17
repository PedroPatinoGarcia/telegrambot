import os
import pandas as pd

def csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        info = f"Filas: {df.shape[0]}\tColumnas: {df.shape[1]}\n"
        
        column_info = ""
        for column in df.columns:
            column_info += f"\n{column}\n"
            column_info += str(df[column].describe()) + "\n"
        
        name = os.path.splitext(os.path.basename(file_path))[0]
        json_path = f'{name}.json'
        df.to_json(json_path)

        return "csvORjson", info + column_info, json_path
    except:
        try:
            df = pd.read_json(file_path)
            name = os.path.splitext(os.path.basename(file_path))[0]
            csv_path = f'{name}.csv'
            df.to_csv(csv_path)
            return "json2csv", csv_path
        except:
            return "otro_formato"
