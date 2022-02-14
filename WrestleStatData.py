


from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from csv import writer


from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    
    
    with open('wrestler_data.csv','w', newline='', encoding = 'utf8') as f:
        my_writer = writer(f)
        header= ['Rank','Wins','Losses']
        my_writer.writerow(header)
    df = pd.read_csv('wrestler_data.csv')
    
    prefix = "https://www.wrestlestat.com"
    webpage_response = requests.get('https://www.wrestlestat.com/wrestler/50273/caffey-cameron/profile')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage,"html.parser")
    
    data = soup.select('tbody', attrs={'class':"small"})
    for element in data[1:]:
        name = element.get_text()
        print(name)
    

    rank = []
    wins = []
    losses = []
    #this one is fire
    test = soup.select('tbody', attrs={'class':"small"})
    for element in test[1:]:
        data = element.get_text(strip = True)
        #list.append(data)
        for stat in element:
            trash = stat.get_text(strip = True)
            if("197W" in trash):
                info = (([int(s) for s in re.findall(r'\d+', trash)]))
                rank.append(info[0])
                wins.append(info[1])
                losses.append(info[2])
                print(trash)
                print(info)
                print('\n')
                
           # if("197L" in trash):
                #losses.append(trash)
    
    print(wins)
    print(losses)
  
    d = {"OpponentRank": rank, "Wins":  wins, "Losses": losses}
    df = pd.DataFrame.from_dict(d)
    print(df)
    

    plt.scatter(df.Wins, df.OpponentRank)
    
    z = np.polyfit(df.Wins, df.OpponentRank, 1)
    line_function = np.poly1d(z)
    plt.plot(df.Wins, line_function(df.OpponentRank), "r--")
    
  
    plt.show()


    
 
