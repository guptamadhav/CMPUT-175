# Exercise 2
file_path = "Lab 1/rainfall.txt"
with open(file_path, mode = "r") as f:
    data = f.readlines()

rainfall_data = {i.split()[0]:float(i.split()[1]) for i in data}
rainfall_data = {k:v for (k,v) in sorted(rainfall_data.items(), key=lambda item: item[1])}
# here the lambda function is used to extract values or second element for sorting purposes
new_data = {"[50-60 mm)":[], "[60-70 mm)":[], "[70-80 mm)":[], "[80-90 mm)":[], "[90-100 mm)":[]}
for i in rainfall_data:
    if rainfall_data[i]<60:
        new_data["[50-60 mm)"].append([i, rainfall_data[i]])
    elif rainfall_data[i]<70:
        new_data["[60-70 mm)"].append([i, rainfall_data[i]])
    elif rainfall_data[i]<80:
        new_data["[70-80 mm)"].append([i, rainfall_data[i]])
    elif rainfall_data[i]<90:
        new_data["[80-90 mm)"].append([i, rainfall_data[i]])
    elif rainfall_data[i]<100:
        new_data["[90-100 mm)"].append([i, rainfall_data[i]])
    

with open("Lab 1/rainfallfmt.txt", "w") as f:
    for i in new_data:
        f.write(f"{i}\n")
        for j in new_data[i]:
            f.write("{:>15}".format(j[0].upper()) + "{:>10}".format(round(j[1],1))+"\n")