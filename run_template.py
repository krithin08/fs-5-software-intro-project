import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

#WRITE CODE HERE

myVelocityList = []
myErorList = []
myTimeList = []

# append all the lists with the values of the car's state variables interating over steps
for i in range(STEPS):
     desired_acceleration, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
     throttle_percentage = acceleration_to_throttle_percentage(desired_acceleration)
     update(car, throttle_percentage)
     myVelocityList.append(car["v"])
     myErrorList.append(error)
     myTimeList.append(car["t"])


 plt.plot(myVelocityList, myTimeList) # plots velocity as a function of time
 plt.ylabel('Time (s) ')                # labelled y axis 
plt.show()

plt.plot(myErrorList, myTimeList). # plots error as a function of time
 plt.ylabel('Time (s) ')            # labelled y axis
plt.show()


#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()



