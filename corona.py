#import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

X= ["KERELA","MAHARASHTRA","TAMIL NADU","J&K", "UP","KARNATAKA","BIHAR","RAJASTHAN","PUNJAB","GUJURAT","AP","ASSAM","TELENGANA","WEST BENGAL","GOA","MP","ODISHA","JHARKHAND","HARYANA","MANIPUR","CHATTISHGARH","UTTARAKHAND","HIMACHAL PRADESH","NAGALAND","DELHI","TRIPURA","MEGHALAYA","ARUNACHAL","MIZORAM","LADAKH","PUDUCHERRY"]
Y= [11,116,26,11,38,51,5,36,29,38,10,0,39,10,3,18,2,0,21,1,7,4,4,0,30,0,0,0,1,13,1]
Z= [0,3,1,0,0,1,1,0,1,2,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]
plt.bar( X,Y,label = "Affected" , color ='y')
plt.bar( X,Z,label = "Died",color = 'r')
plt.xticks(fontsize = 6, rotation=45)

plt.legend()
plt.xlabel('Corona hua')
plt.ylabel('mar gye')

plt.title('Corona Statistics in India')

plt.show()
