import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [10,30,19,34,23,17,29]

plt.plot(x,y,color='r',label = 'Time&Distance',marker = "o")
plt.title("Time and distance graph")
plt.xlabel('Time')
plt.ylabel('Distance')
plt.grid()

plt.legend()
plt.savefig("Graph.png",dpi = 300,bbox_inches = 'tight')
plt.show()