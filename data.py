import pandas as pd
import random
import statistics
df = pd.read_csv("data.csv")
data = df["average"].tolist()

averages_100 = []
for o in range(0,100):
    random_100_number = []
    for i in range(0,100):
        k = random.randint(0,len(data)-1)
        element = data[k]
        random_100_number.append(element)
    mean = statistics.mean(random_100_number)
    averages_100.append(mean)
average = statistics.mean(averages_100)

print(average)



