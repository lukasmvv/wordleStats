import re
import matplotlib.pyplot as plt
import pandas as df

filepath = "C:\\Users\\lukas\\OneDrive\\Documents\\Git\\wordleStats\\data\\rawData.txt"

pattern = re.compile(r'\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - .+: Wordle \d{1},\d{3} \S/6')
datePattern = re.compile(r'\d{2}/\d{2}/\d{4}')
namePattern = re.compile(r' - .+:  ')

dataDict = {}
df = df.DataFrame()

with open(filepath, 'r', encoding='utf-8') as file:
    for line in file:
        if pattern.match(line.strip()):
            lineStr =  line.strip()
            date = datePattern.match(lineStr).group()
            name = lineStr[lineStr.index(" - ")+3:lineStr.rfind(":")]
            score = lineStr[lineStr.rfind(' ')+1:lineStr.rfind(' ')+2]
            if score == 'X':
                score = 7
            else:
                score = int(score)
            hardmode = "*" in lineStr
            # print(f"Date: {date}, Name: {name}, Score: {score}, Hardmode: {hardmode}")

            if name not in dataDict:
                dataDict[name] = {}
                dataDict[name]['date'] = []
                dataDict[name]['scores'] = []
                dataDict[name]['hardmode'] = []
            dataDict[name]['date'].append(date)
            dataDict[name]['scores'].append(score)
            dataDict[name]['hardmode'].append(hardmode)

# print(dataDict)
num = len(dataDict.keys())

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

for i, (name, data) in enumerate(dataDict.items()):
    # print(name)
    dates = data['date']
    scores = data['scores']
    hardmode = data['hardmode']

    scoreCounts = [scores.count(y) for y in range(1, 8)]
    scoreLabels = [str(y) for y in range(1,8)]

    plt.subplot(2, 2, i+1)
    # plt.plot(dates, scores, marker='o', label=f'Scores ({name})')
    plt.pie(scoreCounts, labels=scoreLabels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Scores totals for {name}')
    plt.legend(scoreLabels)
    # plt.xlabel('Date')
    # plt.ylabel('Score')
    # plt.grid()
    # axs[i].plot(dates, scores, marker='o', label=f'Scores ({name})')
    # axs[i].set_title(f'Scores over Time for {name}')
    # axs[i].set_xlabel('Date')
    # axs[i].set_ylabel('Score')
    # axs[i].legend()
    # axs[i].grid(True)

plt.tight_layout()
plt.show()