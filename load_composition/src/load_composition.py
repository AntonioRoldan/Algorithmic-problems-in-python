def compute_load_composition(amount, materials):
    threshold = amount
    load_composition = 0
    output = ""
    for material in (sorted(zip(materials.keys(), materials.values()), key=lambda x : x[1][1], reverse=True)): #We have a list of tuples, each tuple contains a string and another tuple defining weight and price
        kg = 0
        amount_left = material[1][0]
        while(amount_left and threshold): #Loop continues for as long as we have a certain component and the amount has not been reached
            load_composition += material[1][1]
            kg += 1
            amount_left -= 1
            threshold -= 1
            if(threshold == 1):
                output += "and "
        if(kg):
            output += str(kg) + "kg of " + material[0] + " "
    return "Load composition: " + str(load_composition) + "\n" + output

materials = {"Copper" : (7, 65), "Gold" : (4, 100) , "Plastic" : (15, 50)}

print(compute_load_composition(10, materials))

