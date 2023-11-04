import pandas as pd

def create_dict(df):
    names = df["Name"]
    cuisines = df["Cuisines"]
    dictionary = {}
    for n, i in enumerate(names):
        dictionary[i] = list(cuisines[n].split(" "))
    return dictionary

def match(cuisines_c, cuisines_r):
     count = 0
     cc = []
     for i in cuisines_c:
        for j in cuisines_r:
            if i == j:
                count += 1
                cc.append(i)
     if len(cc) >= 2: # Change as required
        return True
     else:
        return False

def create_availability_list(rest_df,  required):
    rests = rest_df["Name"]
    seats = rest_df["Seats"]
    available = []
    for n, i in enumerate(seats):
        if i >= required:
            available.append(rests[n])
    return available


rest_df = pd.read_csv("rests.csv")
cust_df = pd.read_csv("custs.csv")
cu_re = {}
cust_dict = create_dict(cust_df)
rest_dict = create_dict(rest_df)
print(rest_dict, cust_dict)
for cu, cu_c in cust_dict.items():
    required = int(input("Enter number of seat required: "))
    available = create_availability_list(rest_df, required)
    res = []
    for re, re_c in rest_dict.items():
        if re in available:
            stat = match(cu_c, re_c)
            if stat:
                res.append(re)
    cu_re[cu] = res
print(cu_re)