import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage
from pid_template import integral_accumulated # import the integral_accumulated function from pid_template.py
from pid_template import derivative_term # import the derivative_term function from pid_template.py




K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

#WRITE CODE HERE

myVelocityList = []
myErrorList = []
myTimeList = []

# append all the lists with the values of the car's state variables interating over steps
for i in range(STEPS):
     desired_acceleration, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
     throttle_percentage = acceleration_to_throttle_percentage(car,desired_acceleration)
     update(car, throttle_percentage)
     myVelocityList.append(car["v"])
     myErrorList.append(error)
     myTimeList.append(car["t"])

     

# allign next branches of code to break off for loop
# and plot the velocity and error as a function of time using matplotlib.pyplo===-==-t
plt.plot(myVelocityList, myTimeList) # plots velocity as a function of time
plt.ylabel('Time (s) ')                # labelled x axis 
plt.show()

plt.plot(myErrorList, myTimeList) # plots error as a function of time
plt.ylabel('Time (s) ')            # labelled x axis
plt.show()


#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()
 
 



