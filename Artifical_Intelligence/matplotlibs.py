import random

import matplotlib.pyplot as plt
#
# # plot drawing
# #
# # x= ["Mon","Tues","Wed","Thu","Fri","Sat","Sun"]
# # y= [random.randint(1000,5000) for i in range(1,8)]
# # plt.plot(x , y , color='purple',linestyle="--", linewidth= 2, marker= "s",label="❤️")
# # plt.title("Sales_of_week")
# # plt.xlabel("Days")
# # plt.ylabel("Sales per Day")
# # plt.legend(loc = "upper left")
# # plt.grid(color= "gray",linestyle=":",linewidth=1)
# # plt.xticks(x,["D1","D2","D3","D4","D5","D6","D7"])
# # plt.show()
# #
# # # bar drawing
# #
# # k= ["Mon","Tues","Wed","Thu","Fri","Sat","Sun"]
# # j= [random.randint(1000,5000) for i in range(1,8)]
# # plt.bar(k, j, color='orange',label="Sales_2025")
# # plt.title("Sales of 2 week")
# # plt.xlabel("Days")
# # plt.ylabel("Sales per Day")
# # plt.legend()
# # plt.show()
# #
# # # pie drawing

k= ["Mon","Tues","Wed","Thu","Fri","Sat","Sun"]
j= [random.randint(1000,5000) for i in range(1,8)]
plt.pie(j,labels=k,autopct="%1.1f%%",colors=["yellow","orange","blue","gray","purple","green","red"])
plt.title("Love_%_FOR_HER ❤️")
plt.show()
# #
# # # histogram drawing
# # j= [random.randint(1000,5000) for i in range(20)]
# # plt.hist(j,bins=5,color="purple",edgecolor="gray")
# # plt.title("Sales_of_Week")
# # plt.xlabel("Days")
# # plt.ylabel("Sale")
# # plt.show()
# #
# # # Scatter drawing
# # hours = [1,2,3,4,5,6,7,8]
# # score1 = [random.randint(50,100) for i in range(1,9)]
# # score2 = [random.randint(50,100) for i in range(1,9)]
# #
# # plt.scatter(hours,score1, color='purple',marker="^",label="Class A")
# # plt.scatter(hours,score2, color='blue',marker="s",label="Class B")
# # plt.title("Students_Marks Relationship")
# # plt.xlabel("Hours")
# # plt.ylabel("Marks Achieved")
# # plt.grid()
# # plt.legend()
# # plt.show()
#
# # x=[1,2,3,4]
# # y=[25,78,34,67]
# # plt.subplot(1,2,1)
# # plt.plot(x,y)
# # plt.title("Line chart")
# #
# # plt.subplot(1,2,2)
# # plt.bar(x,y)
# # plt.title("Bar chart")
# #
# # plt.tight_layout()
# # plt.show()
# fig, ax = plt.subplots(1,2,figsize=(10,5))
# x=[1,2,3,4]
# y=[25,78,34,67]

# ax[0].plot(x,y,color="red")
# ax[0].set_title("Line chart")

# ax[1].bar(x,y, color="green")
# ax[1].set_title("Bar chart")
# fig.suptitle("Comparsion of Line and Bar chart ❤️")
# plt.tight_layout()
# plt.show()

