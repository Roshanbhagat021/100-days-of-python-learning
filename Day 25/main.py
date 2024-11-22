# with open (r"weather_data.csv") as weather_Data:
#     Data = weather_Data.readlines()
#     print(Data)

# Getting the data with the inbuilt csv library
# import csv
# with open("weather_data.csv") as file_data:
#     data = csv.reader(file_data)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)       





# Working with "PANDAS" library 
import pandas  

data = pandas.read_csv("squrell_data.csv")

color_obj = {}

colors = data["Primary Fur Color"]
# print(colors)
for co in colors:
 
    if co in color_obj:
       color_obj[str(co)] += 1
    else:
        color_obj[str(co)] = 1

del color_obj["nan"]
# print(color_obj)
        
Squrell_fur_color_data = {
    "Fur_Color" : list(color_obj.keys()),
    "Count" : list(color_obj.values())
}    

squrell_color_file = pandas.DataFrame(Squrell_fur_color_data)
squrell_color_file.to_csv("Squrell_fur_color_data.csv")

# print(Squrell_fur_color_data)     

# print(color_obj.keys())
# s1 =  data["temp"]
# print(s1.min())


# print(data[data.temp == s1.min()])

# monday =  data[data.day == "Monday"]
# monday_temp = monday.temp[0]

# print(monday_temp*9/5+32)

# Mahindra_business_data = {
#     "V_Name":["Thar", "Suv", "Sedan", "Thar", "Sedan"],
#     "Quaterly_Sales":[12,7,19,1,5],
#     "Net_Profit":[7,5,6,7,9]
# }

# new_data = pandas.DataFrame(Mahindra_business_data)
# print(new_data)
# # x= (new_data["Quaterly_Sales"].max())
# # print(new_data[new_data.Quaterly_Sales == x])

# names_of_V = new_data["V_Name"]
# # print(len(names_of_V))
# obj = {
    
# }
# for i in names_of_V:
#     if i in obj:
#         obj[i] += 1
#     else:
#         obj[i] = 1    

# print(obj)
# new_data.to_csv("Mahindar.csv")