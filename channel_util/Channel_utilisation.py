import matplotlib
import matplotlib.pyplot as plt

def plots(no_list,title):
    y=[]
    for x in range(len(no_list)):
        y.append(x)
    plt.plot(y,no_list,'.', color='blue')
    plt.title(title)
    plt.xlabel('no.s')
    plt.ylabel('Measured values')
    plt.show()                                                             
    plt.savefig('utilisation.png')
    
def access_data(catch_start, catch_middle, catch_end):                              #to access a part of req data and check for channel no.s 
    results =[]
    channel_lines =[]
    word_chnline =[]
    lists=[]
    lists1=[]
    measure=[]
    with open('router_stats.txt', 'r') as f1:
        lines = f1.readlines()
    i = 0
    while i < len(lines):
        if catch_start in lines[i]:
            for j in range(i + 1, len(lines)):
                if catch_end in lines[j]  and catch_middle not in lines[j] or j == len(lines)-1:
                    results.append(lines[i:j])
                    i = j
                    break
        else:
            i += 1
    for a in results:                                                                   #for loop for extracting lines having the word channel
        for b in a:
            if "Channel " in b:
               word_chnline.extend(b.split())
               channel_lines.append(b)
    channel_nos =list(set(word_chnline[1::10]))                                         #to extract unique channel no.s Eg=3,48
    for x in range(len(channel_nos)):                                                   #to to create unique no. of empty lists
        lists.append([])
        lists1.append([])
        measure.append([])
    count=0
    for a in channel_nos :                                                              #to seperate each channel data into each empty list
        count+=1
        for b in channel_lines:
            if "Channel "+a in b:                                                       #"channel 3" or "channel 48" line is checked as these no.s may be 'Measured' values too
                lists[count-1].append(b)
    c=0
    for x in lists:                                                                     #channel lines list are split into words list                                                                    
       c+=1
       for s in x:
           lists1[c-1].extend(s.split())              
    for abc in range(len(channel_nos)):                                                  #function call for plotting graph, sends measured values
        measure=lists1[abc]
        plots(measure[4::10],'Channel '+channel_nos[abc])
    
access_data('(echo "bandmon s"; sleep 1) | hyt' , '@ Blackout state ' , '@ ')           # the start, middle and end strings used for accessing data
