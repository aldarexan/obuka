def set_data (name, value):
    data = {}
    data["name"] = name
    data["value"] = value
    return data

def get_data (data):
    return data

titanik = set_data("titanik", 269)
rudo = set_data("rudo", 85.3)
genex_tower = set_data("genex_tower", 135)
saturn_v = set_data("saturn_v", 110.6)
kursk = set_data("kursk", 154.9)
iss = set_data("iss", 109)
toplana_konjarnik = set_data("toplana_konjarnik", 96)

data_list = [titanik, rudo, genex_tower, saturn_v, kursk, iss, toplana_konjarnik]
for data in data_list:
    print(get_data(data))

#print(list(titanik.keys())[0])
#print(list(titanik.keys())[1])
  
print(f'ukupna visina svih objekata je: {sum(get_data(data)["value"] for data in data_list)} metara')