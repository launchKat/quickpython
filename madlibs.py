# string concatination (aka how to put strings together)
#  suppose we want to create a string that says "Who is the one who ____"

#speaker = "waits" #some string variable

# a few ways to do this
#print("Who is the one who " + speaker)
#print("Who is the one who {}".format(speaker))
#print(f"Who is the one who {speaker}")

adj = input("Adjective: ")
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famousperson = input("Famous Person: ")

madlib = f"Sailing boats is so {adj}! It makes me wish I could {verb1} \
my captain. She is always trying to {verb2} me. I am {adj2} to have {famousperson}\
as a captain."

print madlib
