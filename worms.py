import pygame
import time
from tkinter import *
 
class Window(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()
		
	def init_window(self):
		self.master.title('START GUI')
		self.pack(fill=BOTH, expand=1)
		startButton = Button(self,text="Start",command=self.client_start)
		startButton.place(x=200,y=200)
		quitButton = Button(self,text="Quit",command=self.client_quit)
		quitButton.place(x=250,y=200)
		
	def client_quit(self):
		quit()
		
	def client_start(self):
		pygame.init()
		display_width = 1024
		display_height = 864
		gameDisplay = pygame.display.set_mode((display_width,display_height))
		pygame.display.set_caption('WORMS - TURBO MEGA NITRO POWA version 2k17 created by ricomxp level asia master 5000')
		
		red = (255,0,0)
		green = (0,255,0)
		blue = (0,0,255)
		darkBlue = (0,0,128)
		white = (255,255,255)
		black = (0,0,0)
		pink = (255,200,200)
		clock = pygame.time.Clock()
		
		x = int(display_width*0.75)
		y = int(display_height/2)
		x2= int(display_width/4)
		y2= int(display_height/2)
		scorelist1 =[]
		scorelist2 =[]
		
		###########################################
		def text_objects(text, font):
						textSurface = font.render(text, True, white)
						return textSurface, textSurface.get_rect()
					
		def message_display(text):
						largeText = pygame.font.Font('freesansbold.ttf',30)
						TextSurf, TextRect = text_objects(text, largeText)
						TextRect.center = ((display_width/2),(display_height/12))
						gameDisplay.blit(TextSurf, TextRect)
						pygame.display.update()
						time.sleep(2)
						gameDisplay.fill(black)
						game_ON(x,y,x2,y2)
		
		def show_score(count1,count2):
						font = pygame.font.Font('freesansbold.ttf', 30)
						text1 = font.render("Red score: "+str(count1), True, red)
						text2 = font.render("Blue score: "+str(count2), True, blue)
						gameDisplay.blit(text2,(0,0))     
						gameDisplay.blit(text1,(800,0))
					
		def crash():
						message_display('BOOM!HEADSHOT! ')
					
		def crash_w1():
						message_display('RED crashed, You Fo00oo0o0o0OL !!! ')
					
		def crash_w2():
						message_display('BLUE recked, You NOo0o0o00oOB !!! ')
		
		def show_worm(x,y):
						pygame.draw.circle(gameDisplay, red, (x,y), 1, 0)
									
		def show_worm2(x2,y2):
						pygame.draw.circle(gameDisplay, blue, (x2,y2), 1, 0)
					
		def border(x,y):
						if (x > 0 and x < display_width)  and (y > 0 and y < display_height):
										pass
						else:
										#print('BORDER CRASH - worm #1')
										scorelist2.append(1)
										crash_w1()
					
		def border2(x2,y2):
						if (x2 > 0 and x2 < display_width)  and (y2 > 0 and y2 < display_height):
										pass
						else:
										scorelist1.append(1)
										crash_w2()
		
		def worms_check(x,y,x2,y2):
						if (x == x2 and y == y2):
										#print('WORMS CROSSOVER CRASH')
										crash()
						else:
										pass
		
		def game_ON(x,y,x2,y2):
			pause = False
			clockrate = 30
			xy_list = []
			xy2_list = []
			x_change = -1
			y_change = 0
			x2_change = 1
			y2_change = 0
			gameon = True
			while gameon:
				time = pygame.time.get_ticks()                               
				if time >= 5000:
				clockrate+=1
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						gameon = False
						pygame.quit()
						quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT:
							x_change = -1
							y_change = 0
						elif event.key == pygame.K_RIGHT:
							x_change = 1
							y_change = 0
						elif event.key == pygame.K_DOWN:
							x_change = 0
							y_change = 1
						elif event.key == pygame.K_UP:
							x_change = 0
							y_change = -1
						elif event.key == pygame.K_a:
							x2_change = -1
							y2_change = 0
						elif event.key == pygame.K_d:
							x2_change = 1
							y2_change = 0
						elif event.key == pygame.K_s:
							x2_change = 0
							y2_change = 1
						elif event.key == pygame.K_w:
							x2_change = 0
							y2_change = -1                
				if (x,y) in xy_list:
					#print ('Self crash worm #1')
					scorelist2.append(1)
					crash_w1()
				else:
					pass                                      
				if (x2,y2) in xy2_list:
					#print ('Self crash worm #2')
					scorelist1.append(1)
					crash_w2()
				else:
					pass                                      
				if (x,y) in xy2_list:
					#print('WORM #1 CROSSOVER CRASH ')
					scorelist2.append(1)
					print("Red crashed:",len(scorelist2))      
					crash_w1()
				if (x2,y2) in xy_list:
					#print('WORM #2 CROSSOVER CRASH')
					scorelist1.append(1)
					crash_w2()
			xy2_list.insert(0, (x2,y2))
			xy_list.insert(0, (x,y))                                    
			x+=x_change
			y+=y_change
			x2+=x2_change
			y2+=y2_change
			show_worm2(x2,y2)
			show_worm(x,y)
			border2(x2,y2)
			border(x,y)
			worms_check(x,y,x2,y2)
			show_score(len(scorelist1),len(scorelist2))
			pygame.display.update()            
			clock.tick(clockrate)
		
		def main_loop():
			game_ON(x,y,x2,y2)
		##################################
		main_loop()      
		pause = False
		pygame.quit()
		quit()
               
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()