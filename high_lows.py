filename='sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    date, high=[],[]
    dates,highs=[],[]
    for row in reader:
      
       high.append(row[1])
       date.append(row[0])
    
    high.remove('Max')
    date.remove('Jul')
    print (high)
    
    aa=[]
    bb=[]
  
    print (date)
    for index in high:
       aa=int(index)
       highs.append(aa)
       
    print(highs)
    print (date)

    for index in date:
       current_date=datetime.strptime(index,"%d")
       dates.append(current_date)
    print(dates)
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='blue')                
    plt.title("Daily high temperature , July 2014",fontsize=24)
    plt.xlabel("",fontsize=8)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=8)
    plt.show()
