import os


path = os.getcwd()
filenames = os.listdir(path+os.sep+"New")
if "MvoieEpisodeCounter.py" in filenames:
    filenames.remove("MvoieEpisodeCounter.py")

#reagion structure
episode = "E"

#endregion

x = 0
while x < len(filenames):
    filenames[x] = filenames[x].replace("e","E").replace(episode+"0",episode)
    filenames[x] = filenames[x][filenames[x].rfind(episode):filenames[x].rfind(".")].replace(episode,"")
    filenames[x] = int(filenames[x])
    x +=1

filenames = list(filter(None,filenames))
filenames = sorted(filenames)

d = []
count = 0
while count < max(filenames):
    count+=1
    d.append(str(count))

toPrint = []
for du in d:
    if du not in str(filenames):
        toPrint.append(du)

print("All missing episodes are : "+str(toPrint).replace("\'","").replace("\"",""))
input()