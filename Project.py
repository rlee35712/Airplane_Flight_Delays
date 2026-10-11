import pandas as pd 
import matplotlib.pyplot as plt 


delayed_flights = pd.read_csv("/Users/Ryan/.cache/kagglehub/datasets/giovamata/airlinedelaycauses/versions/2/DelayedFlights.csv")



#This shows how the time difference can be more easily interpreted. 
delayed_flights["DepTime_min"] = (delayed_flights["DepTime"] // 100) * 60 + (delayed_flights["DepTime"] % 100)
delayed_flights["CRSDepTime_min"] = (delayed_flights["CRSDepTime"] // 100) * 60 + (delayed_flights["CRSDepTime"] % 100)
delayed_flights["ArrTime_min"] = (delayed_flights["ArrTime"] // 100) * 60 + (delayed_flights["ArrTime"] % 100)
delayed_flights["CRSArrTime_min"] = (delayed_flights["CRSArrTime"] // 100) * 60 + (delayed_flights["CRSArrTime"] % 100)

delayed_flights["DepDelay_calc"] = delayed_flights["DepTime_min"] - delayed_flights["CRSDepTime_min"]
delayed_flights.loc[delayed_flights["DepDelay_calc"] > 720, "DepDelay_calc"] -= 1440
delayed_flights.loc[delayed_flights["DepDelay_calc"] < -720, "DepDelay_calc"] += 1440

delayed_flights["ArrDelay_calc"] = delayed_flights["ArrTime_min"] - delayed_flights["CRSArrTime_min"]
delayed_flights.loc[delayed_flights["ArrDelay_calc"] > 720, "ArrDelay_calc"] -= 1440
delayed_flights.loc[delayed_flights["ArrDelay_calc"] < -720, "ArrDelay_calc"] += 1440

difference = delayed_flights["ArrDelay_calc"] - delayed_flights["DepDelay_calc"] 

airlines = delayed_flights['UniqueCarrier'].unique() #the list of airlines 


#This goes through each airline, and adds any time differences that is greater than 100. 
airline_dictionary = {}

for i in delayed_flights.index:
    if delayed_flights["UniqueCarrier"][i] != "None" :
        if delayed_flights["UniqueCarrier"][i] == delayed_flights["UniqueCarrier"][i]:
            if abs(difference[i]) > 100.0:
                diff = abs(float(difference[i]))
                if delayed_flights["UniqueCarrier"][i] in airline_dictionary: #is the airline in the dictionary
                    mini_list = airline_dictionary[delayed_flights["UniqueCarrier"][i]]
                    mini_list.append(diff)
                    airline_dictionary[delayed_flights["UniqueCarrier"][i]] = mini_list
                else: 
                    airline_dictionary[delayed_flights["UniqueCarrier"][i]] = [diff]


#This shows the number of flights with a major delay per each airline 
count_airlines = {}

for each_key in airline_dictionary:
    print(each_key)
    count_airlines[each_key] = len(airline_dictionary[each_key])
    print(count_airlines) 

user_input = input("Would you like to view the pie chart or the bar graph of the data? Press q to quit.") 
while True: 
    if user_input == ("pie chart").lower(): 

    #This step shows the data put into a pie chart 
        airlines = list(count_airlines.keys()) 
        pie_chart = list(count_airlines.values()) 
        airline_colors = ["#ff0000", "#ff4000", "#ffff00", "#cc00ff", "#00ff91", "#ff7b00", "#00b3ff", "#00ffff", "#bbff00", "#88ff00", 
                        "#0004ff", "#ff0088", "#ff94cb", "#f47f55", "#6200ff", "#00ff1a", "#8de1ff", "#c2629c", "#ffae00", "#553970"] 
        sorted_pairs = sorted(zip(pie_chart, airlines), reverse=True)
        pie_chart_sorted, airlines_sorted = zip(*sorted_pairs)
        plt.pie(pie_chart_sorted, labels = airlines_sorted, autopct = "%1.2f%%", colors = airline_colors, wedgeprops = {'width': 0.75}) 
        plt.title("Airlines") 
        plt.show() 
        break 

    elif user_input == ("bar graph").lower(): 

    #This step shows the data put into a bar graph instead of a pie chart 
        airlines = list(count_airlines.keys()) 
        bar_graph = list(count_airlines.values()) 
        bar_graph, airlines = zip(*sorted(zip(bar_graph, airlines), reverse=True)) 
        airline_colors = ["#ff0000", "#ff4000", "#ffff00", "#cc00ff", "#00ff91", "#ff7b00", "#00b3ff", "#00ffff", "#bbff00", "#88ff00", 
                        "#0004ff", "#ff0088", "#ff94cb", "#f47f55", "#6200ff", "#00ff1a", "#8de1ff", "#c2629c", "#ffae00", "#553970"] 
        plt.bar(airlines, bar_graph, color = airline_colors) 
        plt.title("Airlines") 
        plt.xlabel("Different Airlines") 
        plt.ylabel("Number of Flights with Major Delays") 
        plt.show() 
        break 

    elif user_input == ("q").lower(): 
        break 

    else: 
        print("You did not input either pie chart or bar graph.") 
        break 

#Key: 
# WN - Southwest Airlines 
# XE - XEJet 
# YV - Mesa Airlines 
# OH - PSA Airlines 
# OO - SkyWest Airlines 
# UA - United Airlines 
# US - US Airways 
# DL - Delta Airlines 
# EV - EVA Air 
# F9 - Frontier Airlines 
# FL - Flair Airlines 
# MQ - Envoy Air 
# NW - Northwest Airlines 
# 9E - Endeavor Air 
# AA - American Airlines 
# B6 - JetBlue Airways 
# CO - Continental Airlines 
# HA - Hawaiian Airlines 
# AS - Alaska Airlines 
