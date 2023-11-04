import pandas as pd
rest_df = pd.read_csv("rests.csv")
cust_df = pd.read_csv("custs.csv")
def create_dict(df):
    names = df["Name"]
    cuisines = df["Cuisines"]
    dictionary = {}
    for n, i in enumerate(names):
        dictionary[i] = cuisines[n]
    return dictionary

cust_dict = create_dict(cust_df)
rest_dict = create_dict(rest_df)

def match(cuisines_c, cuisines_r):
     count = 0
     cc = []
     for i in cuisines_c:
        for j in cuisines_r:
            if i == j:
                count += 1
                cc.append(i)
     if len(cc) >= 3:
        return cc, True
     else:
        return cc, False

cu_re = {}
for cu, cu_c in cust_dict.items():
    for re, re_c in rest_dict.items():
        stat, cc = match(cu_c, re_c)
        if stat:
            cu_re[cu] = re

def create_availability_dict(rest_df):
    rests = rest_df["Name"]
    seats = rest_df["Seats"]

