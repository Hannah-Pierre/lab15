#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="navy")
player = drawpad.create_rectangle(240,240,260,260, fill="purple")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "pink")
		self.up.grid(row=0,column=0)
		
		self.button5 = Button(self.myContainer1)
		self.button5.configure(text="Left", background= "pink")
		self.button5.grid(row=0,column=1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "pink")
		self.button2.grid(row=0,column=2)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Down", background= "pink")
		self.button4.grid(row=1,column=1)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                self.button5.bind("<Button-1>", self.button5Click)
		self.button2.bind("<Button-1>", self.button2Click)
		self.button4.bind("<Button-1>", self.button4Click)
		
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if y1-1 > 0 :
		    drawpad.move(player, 0, -20)
               
        
        def button2Click(self, event):  
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if x2+1 < 480 :
                    drawpad.move(player, 20, 0)
	
	def button5Click(self, event):   
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if x1-1 > 0 :
		    drawpad.move(player, -20, 0)
	def button4Click(self, event):   
		
                global oval
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
		if y2+1 < 320 :
		    drawpad.move(player, 0, 20)
	def animate(self):
            global target
            global direction
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            if targetx2 > drawpad.winfo_width():
                direction = - 1
            elif targetx1 < 0: 
                direction = 1
            drawpad.move(target,direction,0)
            didWeHit = self.collisionDetect()
            if didWeHit == False :
                drawpad.after(1,self.animate)
            
	    # Insert the code here to make the target move, bouncing on the edges    
	
	def collisionDetect(self):
            global target
            global drawpad
            global player
            targetx1,targety1,targetx2,targety2 = drawpad.coords(target)
            x1,y1,x2,y2 = drawpad.coords(player)    
            if x1 > targetx1 and x2 < targetx2 :
                if y1 > targety1 and y2 < targety2 :
                    return True
            return False
                    
                

                # Do your if statement - remember to return True if successful!     
	        
            
            
            #  This will trigger our collision detect function
        
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
           # Use a function to do our collision detection	
    
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
direction = 1


               
		
		
myapp = MyApp(root)

root.mainloop()