# ski_resorts_eda/utils/utils.py
import matplotlib.pyplot as plt
import seaborn as sns

def remove_invalid_characters(df, pattern = r'[^a-zA-Z0-9\s\w-]', columns=[]):
    temp = df
    for column in columns:
        temp[column] = temp[column].astype(str).str.strip().replace(pattern, '', regex=True)
    return temp

# create a function for generating a scatter with preconfigured parameters
def scatterplot_generator(df, xcol, ycol, title, xlabel, ylabel, figsize=(6.5, 6.5), hue="", size=""):
    # configure the plt settings
    f, ax = plt.subplots(figsize=figsize)
    sns.despine(f, left=True, bottom=True)
    # resolve scientific notation display
    plt.ticklabel_format(style='plain', axis='both')

    # Scatter plot 
    sc_plt = sns.scatterplot(df, x=xcol, y=ycol, size=size, hue=hue, ax=ax)
    # Set title and labels
    sc_plt.set_title(label=title)
    sc_plt.set(xlabel=xlabel, ylabel=ylabel)
    return sc_plt