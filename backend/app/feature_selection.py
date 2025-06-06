import pandas as pd
from sklearn.preprocessing import StandardScaler

# Input: a dataframe with one row of miRNA data
# Output: a dataframe with some of the coloums selected
# Reducing based on the highest performing feature set
def select_features(df, target=None):

    feature_set = ['hsa-mir-203b', 'hsa-mir-5690', 'hsa-mir-6766', 'hsa-mir-1283-2', 'hsa-mir-4663', 'hsa-mir-4637', 'hsa-mir-571', 'hsa-mir-518f', 'hsa-mir-524', 'hsa-mir-181d', 'hsa-mir-4300', 'hsa-mir-1181', 'hsa-mir-548ak', 'hsa-mir-3922', 'hsa-mir-519d', 'hsa-mir-5583-1', 'hsa-mir-187', 'hsa-mir-451b', 'hsa-mir-523', 'hsa-mir-515-2', 'hsa-mir-6071', 'hsa-mir-3661', 'hsa-mir-526a-2', 'hsa-mir-520d', 'hsa-mir-4257', 'hsa-mir-4731', 'hsa-mir-1825', 'hsa-mir-520e', 'hsa-mir-8082', 'hsa-mir-509-1', 'hsa-mir-760', 'hsa-mir-3973', 'hsa-mir-1253', 'hsa-mir-520h', 'hsa-mir-631', 'hsa-mir-185', 'hsa-mir-8066']

    df_selected = df.loc[:, feature_set]
    
    return df_selected