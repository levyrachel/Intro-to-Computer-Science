#This is a simulation. Please press play! 
import random
import Draw
def backdrop():
	
#Create the Backround
	
	#Clear the canvas (it will clear each time through the loop)
	Draw.clear()
	
	#Set the Backround Color of Green
	green = Draw.color(0, 100, 50)
	Draw.setBackground(green)
	
	#Draw the Sky
	blue = Draw.color(200, 200, 255)
	Draw.setColor(blue)
	Draw.filledRect(0, 0, 1000, 250)	

	#draw the ocean
	Draw.setColor(Draw.BLUE)
	Draw.filledRect(0, 400, 1000, 500)	
	
	#Draw the Waves 
	Draw.filledOval(0, 390, 250, 250)
	Draw.filledOval(250, 390, 250, 250)
	Draw.filledOval(500, 390, 250, 250)
	Draw.filledOval(750, 390, 250, 250)	

	#draw the mountains
	Draw.setColor(Draw.GRAY)
	coords= (0, 250, 100, 250, 50, 200)
	Draw.filledPolygon(coords)
	Draw.setColor(Draw.GRAY)
	coords= (75, 250, 200, 100, 300, 250)
	Draw.filledPolygon(coords)
	
	#Draw four houses 75 Pixels apart
	#Set an original X
	X = 410
	#Loop through the drawings of the house
	for i in range (4):
		
		#Draw the base of the house
		brown = Draw.color(192, 128, 64)
		Draw.setColor(brown)
		Draw.filledRect(X, 190, 60, 60)
		
		#Create the Roof 
		Draw.setColor(Draw.RED)
		coords = [X, 190, X + 30, 140, X + 60, 190]
		Draw.filledPolygon(coords)
		
		#Create the door and windows
		Draw.setColor(Draw.WHITE)
		#Draw the door
		Draw.filledRect(X + 25, 230, 10, 20)
		#Draw the windows
		Draw.filledRect(X + 10, 200, 7, 7)
		Draw.filledRect(X + 43, 200, 7, 7)
		#Add 75 to X so that the next house is 75 to the right 
		X += 75
	
	#Draw a Road 
	Draw.setColor(Draw.DARK_GRAY)
	Draw.filledRect(0, 300, 1000, 60)
	#Draw yellow lines on the road
	Draw.setColor(Draw.YELLOW)
	X = 20
	for i in range (20):
		Draw.filledRect(X, 330, 20, 4)
		X += 50
	
	#Draw a building 
	Draw.setColor(Draw.BLACK)
	Draw.filledRect(760, 100, 100, 150)
	
	#Draw windows for the building
	Draw.setColor(Draw.WHITE)
	#set an original x coord
	X = 770
	for i in range (3):
		#Draw windows (in columns)
		Draw.filledRect(X, 120, 10, 20)
		Draw.filledRect(X, 150, 10, 20)
		Draw.filledRect(X, 180, 10, 20)
		Draw.filledRect(X, 210, 10, 20)
		#Change the x coord by 35 to the right
		#then loop through again drawing the windows
		#at their new X and Y coordinates
		X += 35
		
	#Write out The Water Cycle at the bottom of the screen
	Draw.setFontFamily('Times New Roman')
	Draw.setFontSize(24)
	Draw.setColor(Draw.WHITE)
	Draw.string("The Water Cycle", 375, 450)	

#Create the initial list of evaporation particles
def initialEvap():
	#Create 1000 particles (lists) each with an X and Y coord
	evap = [[0 for i in range (2)] for j in range (1000)]
	for row in range (len(evap)):
		#Choose the X from anywhere on the canvas
		evap[row][0]=random.randint(0, 1000 )
		#Choose the Y from beneath the bottom of the canvas
		evap[row][1]=random.randint(500, 1000)
	return evap

#Update the list of evaporation particles to make them move
def updateEvap(evap):
	#for each evap particle in the evap list
	for row in range (len(evap)):
	
	#decrement the particle's y coordinate by 10 if the evaporation Y coord
	#is more than fifty
		if evap[row][1] >= 50:
			evap[row][1] -= 10

		#if the particle's y coordinate is less than 50
		elif evap[row][1] < 50:
			#reset the y coordinate to below the canvas			
			evap[row][1] = 515
	return evap

#draw the evap
def drawEvap(evap):
	#for each evap particle in the evap list
	for row in range (len(evap)):
	#draw an evap particle at it's x,y
		Draw.setColor(Draw.CYAN)
		Draw.filledOval(evap[row][0], evap[row][1], 3, 7)

#Create an initial list of rain particles			
def initialRain():
	#Create 1000 particles each with an X and Y coordinate
	rain = [[0 for i in range (2)] for j in range (1000)]
	for row in range (len(rain)):
		#Choose an X coordinate anywhere on the canvas
		rain[row][0]=random.randint(0, 1000 )	
		#Choose a Y coord off the top of the canvas
		rain[row][1]=random.randint(-500, 0)
	return rain

#Update the list of rain particles to make them move
#Create a recycle parameter so that the simulation will
#replay over and over until the python shell is reset
def updateRain(rain, recycle = True):
	
	#for each evap particle in the evap list
	for row in range (len(rain)):
	#If the Y coordinate is less than 490 increment by 10
		if rain[row][1] <= 490: 
			rain[row][1] += 10
	
		#if the particle's y coordinate is greater than 490
		#(Because it's almost to the bottom of the canvas)
		elif recycle == True and rain[row][1] > 490:
			#reset the particle's y coordinate to above the canvas
			rain[row][1] = -10
	return rain

#Draw the rain
def drawRain(rain):
	#for each evap particle in the evap list
	for row in range (len(rain)):
		#draw a rain particle at it's x,y
		Draw.setColor(Draw.BLUE)
		Draw.filledOval(rain[row][0], rain[row][1], 3, 7)

#Create a list of clouds (in a row)-->the clouds all move onto the screen together
def cloudList():
	#Choose a spot off of the left of the canvas
	xCoord = -50
	#create a list of 7 clouds each with an X and Y coord and a size 
	clouds = [[0 for i in range (3)] for j in range (7)]
	#Looping through the list
	for row in range (len(clouds)):
		#Set the X coordinate to the Xcoord
		clouds[row][0] = xCoord
		#Then subtract 200 from the X coord
		#So that when you loop through again the new cloud will have
		#a different x coordinate
		xCoord -= 200
		#The Y coordinate for the clouds is 5 for all of them
		clouds[row][1] = 5
		#Set an original size of 15
		clouds[row][2] = 15
	return clouds

#update the clouds by moving them over, if the cloud is almost at the edge
#of the canvas bring it back to the beginning of the canvas
#Set recycle parameter to True so that the clouds reset to the beginning
#of the canvas
def setCloud(clouds, size, recycle = True):
	for row in range (len(clouds)):
		clouds[row][2] = size 
		
		#Incrementing the clouds X value by 5 in order to move it 
		#across the screen 
		clouds[row][0] += 5
	return clouds 
		
#Draw the clouds
def drawCloud(clouds):
	for row in range (len(clouds)):
		#Each cloud is made of 6 circles
		#Who's x and y coords are based off of the clouds list 
		Draw.filledOval(clouds[row][0], clouds[row][1], clouds[row][2], clouds[row][2])	
		Draw.filledOval(clouds[row][0] + 25, clouds[row][1], clouds[row][2], clouds[row][2])
		Draw.filledOval(clouds[row][0] + 25, clouds[row][1] + 25, clouds[row][2], clouds[row][2])	
		Draw.filledOval(clouds[row][0] + 40, clouds[row][1] + 13, clouds[row][2], clouds[row][2])	
		Draw.filledOval(clouds[row][0], clouds[row][1] + 25, clouds[row][2], clouds[row][2])
		Draw.filledOval(clouds[row][0] - 15, clouds[row][1] + 13, clouds[row][2], clouds[row][2])

#Outline the clouds
def drawCloudsOutline(clouds):
	for row in range (len(clouds)):
		#Outline the clouds in black
		Draw.setColor(Draw.BLACK)
		Draw.oval(clouds[row][0]- 1, clouds[row][1] - 1, clouds[row][2] + 4, clouds[row][2] + 4)	
		Draw.oval(clouds[row][0] + 24, clouds[row][1] - 1, clouds[row][2] + 4, clouds[row][2] + 4)
		Draw.oval(clouds[row][0] + 24, clouds[row][1] + 24, clouds[row][2] + 4, clouds[row][2] + 4)	
		Draw.oval(clouds[row][0] + 39, clouds[row][1] + 12, clouds[row][2] + 4, clouds[row][2] + 4)	
		Draw.oval(clouds[row][0] - 1, clouds[row][1] + 24, clouds[row][2] + 4, clouds[row][2] + 4)
		Draw.oval(clouds[row][0] - 14, clouds[row][1] + 12, clouds[row][2] + 4, clouds[row][2] + 4)	
	
def main():
	#Set the canvas size and create the backdrop
	Draw.setCanvasSize(1000, 500)
	backdrop()
		
	#Start a "timer" to run through the different parts of simulation
	#The while true makes sure that the particles and clouds are only being
	#reset when they are supposed to be. 
	while True:
		#Set the initial lists of Evaporation, Rain and Clouds outside the loop
		initEvap = initialEvap()
		listOfClouds = cloudList()	
		initRain = initialRain()	
		
		for i in range (0, 575):
			
			#If the timer is between 0 and 75 then the evaporation should run
			if i >= 0 and i < 75: 
				backdrop()
				updateEvap(initEvap)
				drawEvap(initEvap)
				Draw.show(1)
				Draw.clear()
				
			#If the timer is between 75 and 275
			#the Evaporation should run
			#And clouds should form
			elif i >= 75 and i <= 300: 
				#Create an initial size and create the backdrop
				size = 40
				backdrop()
				
				#If the timer is between 75 and 150
				if i >= 75 and i <= 150:
					#The clouds should form with size 60
					size = 60
					#And light grey color
					CloudColor = Draw.color (175,175,175)
					
				#If the timer is between 150 and 225
				elif i > 150 and i <= 225:
					#The clouds should form with size of 70 
					size = 70
					#And darker grey color
					CloudColor = Draw.color (150, 150, 150)	
					
				#If the timer is between 225 and 300
				elif i > 225 and i <= 300:
					#The clouds should form with size 80
					size = 80
					#And the darkest grey color
					CloudColor = Draw.color(128, 128, 128)
					
				#Now actually make the clouds form with
				#the correct size and color
				#The evaporation is still going
				newEvap = updateEvap(initEvap)
				drawEvap(newEvap)
				newCloud = setCloud(listOfClouds, size)
				
				#Draw the clouds outline and the correct color
				drawCloudsOutline(newCloud)						
				Draw.setColor(CloudColor)
				
				#Draw the cloud
				drawCloud(newCloud)
				Draw.show(1)				
			
			#If the timer is between 300 and 375			
			elif i > 300 and i <= 575:
				backdrop()
				
				#Clouds should be there with a size of 80
				#and darkest grey
				size = 80
				CloudColor = Draw.color(128, 128, 128)
				
				#Update the rain and then draw again 
				if i <= 375:
					newRain = updateRain(initRain)
					newCloud = setCloud(listOfClouds, size)
				#Once the timer has run out
				#Set the recycle factor to False
				#so that the particles and clouds stop resetting
				#And the whole simulation will begin again
				#This allows rain to stop dropping and clouds to
				#move off of the screen
				else:
					newRain = updateRain(initRain, False)
					newCloud = setCloud(listOfClouds, \
							    size, False)
				drawRain(newRain)			
				drawCloudsOutline(newCloud)			
				Draw.setColor(CloudColor)			
				drawCloud(newCloud)
				Draw.show(1)
			
main()
