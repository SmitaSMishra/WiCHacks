import pandas as pd

data = pd.read_csv("WFH_WFO_dataset.csv")
gender = {'Male': 1, 'Female': 0}
calm = {'CALMER': 1, 'STRESSED': 0}
digital = {'Yes': 1, 'No': 0}
# money = {'Yes':1, 'No':0}
# sleep = {'Yes':1, 'No':0}
# time = {'Yes': 1, 'No': 0}

data.Gender = [gender[item] for item in data.Gender]
data.calmer_stressed = [calm[item] for item in data.calmer_stressed]
data.digital_connect_sufficient = [digital[item] for item in data.digital_connect_sufficient]
data.RM_save_money = [digital[item] for item in data.RM_save_money]
data.RM_better_sleep = [digital[item] for item in data.RM_better_sleep]
data.RM_quality_time = [digital[item] for item in data.RM_quality_time]

data.to_csv("WFH_WFO_dataset_pre.csv", index=False)