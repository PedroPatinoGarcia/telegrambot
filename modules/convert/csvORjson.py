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
        df.to_json(f'{name}.json')
        return "csv_a_json", info + column_info
    except:
        try:
            df = pd.read_json(file_path)
            name = os.path.splitext(os.path.basename(file_path))[0]
            df.to_csv(f'{name}.csv')
            return "json_a_csv"
        except:
            return "otro_formato"
