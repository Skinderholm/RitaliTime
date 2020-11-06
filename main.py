#RitaliAte.py

#importer tid
from datetime import datetime, timedelta

#make timestamp
now = datetime.now()
#readable timestamp with stringify time
current_time = now.strftime("%H:%M")
#ask for user input (hour), with "input-time" as helptext
userinput = input("input-time: ")
#use input valuse if filled
if userinput:
	usertime = userinput
#use time now as input if empty
if not userinput:
	print("No input; using", current_time),
	usertime = now.strftime("%H")
#if input is not empty fill usertime with input
usertime_calc = now.replace(hour=int(usertime))


#userspecifik setup
plasma_max = 2
plasma_begin = 45
plasma_end = 7

#funktion til at vise plasmamakstid for Ritalin Uno

#plasma_max_time = (datetime.now() + timedelta(hours=plasma_max)).strftime('%H:%M')
plasma_max_time = (usertime_calc + timedelta(hours=plasma_max)).strftime('%H:%M')


#plasma_begin_time = (datetime.now() + timedelta(minutes=plasma_begin)).strftime('%H:%M')
plasma_begin_time = (usertime_calc + timedelta(minutes=plasma_begin)).strftime('%H:%M')


#Next Medication time
plasma_end_time = (usertime_calc + timedelta(hours=plasma_end)).strftime('%H:%M')


#user output "sep""" er et argument man sender med for at undgå mellemrum efter kald 
print("Du har taget din medicin kl. ", usertime_calc.strftime('%H:%M'), ", den begynder at virke ca. kl ", plasma_begin_time, " og den har fuld effekt kl ", plasma_max_time, sep="")
print("Du må tage medicin igen kl ", plasma_end_time,)

#function to store input from user, to external file, for shits and giggles
#a for append, w for overwrite
file = open("userinput.txt", "a")
file.write("Timestamp: ")
file.write(now.strftime('%H:%M'))
file.write(", ")
file.close()