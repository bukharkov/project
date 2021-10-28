#7
import json

final_list = []
dict_profit = {}
dict_loss = {}
with open('text#7') as file:
    average_profitlist = []
    for line in file.readlines():
        name, form, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profitlist.append(profit)
            dict_profit.update({name: profit})
        else:
            dict_loss.update({name: profit})
    final_list.append(dict_profit)
    final_list.append(dict_loss)
    final_list.append({"average profit": sum(average_profitlist)/len(average_profitlist)})
with open('File#7.json', 'w') as file:
    json.dump(final_list, file)





