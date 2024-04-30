from os import getcwd
from arffconvert import ArffDFClass

# Carregar o arquivo arff
# Exemplo teste
path = getcwd()
# Tem que ter uma pasta com datasets arff
path_datasets = path + "/datasets"

dataframes = ArffDFClass(path_datasets).arff_to_df()
for df in dataframes.data_frames:
    data = dataframes.load(df)
    x, y = data.data, data.target
    print(df)