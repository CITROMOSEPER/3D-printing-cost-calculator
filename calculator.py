
#currency = "HUF"
currency = input("What currency are you using?  ")
print(" ")
finishedweigth = input("How much does the finished product weigh in grams (g)?  ")
scrapweigth = input("How much do the supports weigh in grams (g)?  ")
filamentcost = input("How much does one kilogram of filament cost?  ")
printtime = input("How long was the print in hours?  ")
preparationtime = input("How long was the preparation (preheating) in minutes?  ")
printingwattage = input("How much power does your printer use while printing? (in Watts)  ")
preheatingwattage = input("How much power does your printer use while preheating? (in Watts)  ")
electricitycost = input("How much does electricity cost? (" + currency + "/kWh)  ")
hourlyrate = input("Whats the hourly rate?  ")
engineeringfee = input("Engineering fee (Profit)  ")

finishedweigth = finishedweigth.replace(",", ".")
scrapweigth = scrapweigth.replace(",", ".")
filamentcost = filamentcost.replace(",", ".")
printtime = printtime.replace(",", ".")
preparationtime = preparationtime.replace(",", ".")
printingwattage = printingwattage.replace(",", ".")
preheatingwattage = preheatingwattage.replace(",", ".")
electricitycost = electricitycost.replace(",", ".")
hourlyrate = hourlyrate.replace(",", ".")
engineeringfee = engineeringfee.replace(",", ".")

finishedweigth = float(finishedweigth)
scrapweigth = float(scrapweigth)
filamentcost = float(filamentcost)
printtime = float(printtime)
preparationtime = float(preparationtime)
engineeringfee = float(engineeringfee)
printingwattage = float(printingwattage)/1000
preheatingwattage = float(preheatingwattage)/1000
hourlyrate = float(hourlyrate)
electricitycost = float(electricitycost)


usedmaterial = round(finishedweigth + scrapweigth)
materialcost = round(usedmaterial/1000 * filamentcost)
time = printtime + preparationtime / 60
timecost = round(hourlyrate * time)
printelectricitycost = round(printingwattage * printtime * electricitycost)
prepelectricitycost = round(preheatingwattage * preparationtime/60 * electricitycost)
totalcost = round(materialcost + timecost + printelectricitycost + prepelectricitycost + engineeringfee)


print(" ")
print("Material cost: " + str(materialcost) + " " +currency)
print("Hourly rate: " + str(hourlyrate) + " " +currency)
print("Time cost: " + str(timecost) + " " +currency)
print("Print electricity cost: " + str(printelectricitycost) + " " +currency)
print("Preparation electricity cost: " + str(prepelectricitycost) + " " +currency)
print("Engineering fee: " + str(engineeringfee) + " " +currency)
print(" ")
print("Total cost: " + str(totalcost) + " " +currency)

print(" ")
print(" ")
input("Press ENTER to exit")