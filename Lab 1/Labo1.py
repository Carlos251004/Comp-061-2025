temperature= int(input("Temperature in degrees (In degrees):"))
budget= float(input("the user's available budget:"))
weathercondition= (input("weather condition (sunny, rainy, cloudy):"))

activity= ""

if weathercondition == "sunny" and temperature > 75:
    if budget > 20.00:
        activity= "Go have a beach day"
    else:
        activity= "Go to the park and have a picnic"

if weathercondition == "rainy":
    if budget > 15.00:
        activity = "Take a trip to the museum"
    else:
        activity = "Watch a movie from the comfort of your home"

if weathercondition == "cloudy" or temperature < 60:
    activity = "Enjoy a nice cup of coffee"

print("\nrecomended a new activity:")
if activity:
    print(activity)
if not activity:
    print("not possible")

