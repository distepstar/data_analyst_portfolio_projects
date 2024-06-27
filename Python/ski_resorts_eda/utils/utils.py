# ski_resorts_eda/utils/utils.py

def remove_invalid_characters(df, pattern = r'[^a-zA-Z0-9\s\w-]', columns=[]):
    temp = df
    for column in columns:
        temp[column] = temp[column].astype(str).str.strip().replace(pattern, '', regex=True)
    return temp