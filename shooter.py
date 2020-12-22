import time
import pygame
import os
import random
import patterns as patterns


os.environ["SDL_VIDEO_WINDOW_POS"] = "680,33"


global width,height,scale
width,height,scale = 600,1000,1
pygame.init()

screen = pygame.display.set_mode((width,height))

character_image = pygame.image.load("./assets/images/character.png")
background_image1 = pygame.image.load("./assets/images/background1.png").convert()
background_image2 = pygame.image.load("./assets/images/background2.png").convert()
bullet1_image = pygame.image.load("./assets/images/bullet1.png")



class Vector():
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Player:
	def __init__(self,name="Aki"):
		self.name = name
		self.momentum = 0
		self.pos = Vector(width//2-32,height-128)
	def __repr__(self):
		return self.name

	def update(self):
		self.draw()
		#collision
		pass


	def draw(self):
		screen.blit(character_image,(self.pos.x,self.pos.y))



def constrain(val,minv,maxv):
	if val > maxv: return maxv
	if val < minv: return minv
	return val




def background(pos,speed):
	screen.blit(background_image1,(0,pos+speed))
	screen.blit(background_image2,(0,pos+speed-height))
	screen.blit(background_image1,(0,pos+speed-height*2))

	pos+=speed
	if pos >= height*2:
		pos = 0
	return pos,speed





#DAY 3
#RANDOM SPAWNING LEVEL ADVANCES DIFFICULTY
#DISPLAY HEALTH
#DAY 4 CHANGE COLOR ETC

class Bullet:
	def __init__(self,x,y,damage,speed):
		self.x = x
		self.y = y
		self.damage = damage
		self.speed = speed
		self.destroy = False
		self.column = extcolumn(self.x)

	def update(self):
		self.y -= self.speed
		if self.y < -69:
			self.destroy = True
		self.draw()

	def draw(self):
		screen.blit(bullet1_image,(self.x-16,self.y))


def custom():
	for n in range(5):
		pygame.draw.rect(screen,(255,255,255),pygame.Rect(16.6+n*116.6,500,100,100))


def togrid(x):
	return 16.6+(x*116.6)

def extcolumn(x):
	return int((x-16.6/2)//116.6)


def darkrgbperc(perc):
	red = [255,0,0]
	green = [0,255,0]
	perc = (255*perc)-1
	return [40+perc/2,40+(255-perc)/2,0]

def rgbperc(perc):
	red = [255,0,0]
	green = [0,255,0]
	perc = (255*perc)-1
	return [perc,255-perc,0]

class Block:


	def __repr__(self):
		return f"Block {self.column,self.row}"


	def __init__(self,column,row,health):
		self.column = column
		self.row = row
		self.y = -600-(16.6+(row*11.6))
		self.health = health
		self.destroy = False
		self.collisionrectangle = pygame.Rect(togrid(self.column),togrid(self.row)+self.y,100,100)
		self.allhealth = health

	def hit(self,bul):
		self.health -= bul.damage
		global score
		score += bul.damage
		if self.health <= 0:
			self.destroy = True

	def update(self,speed):
		self.y += speed
		if self.y > height:
			self.destroy = True
		self.draw()
		self.collisionrectangle = pygame.Rect(togrid(self.column),togrid(self.row)+self.y,100,100)

	def draw(self):
		try:
			#pygame.draw.rect(screen,(rgbperc(self.health/self.allhealth)),pygame.Rect(togrid(self.column),togrid(self.row)+self.y,100,100))

			pygame.draw.polygon(screen,rgbperc(self.health/self.allhealth),[
				(togrid(self.column),togrid(self.row)+self.y+11),
				(togrid(self.column)+100,togrid(self.row)+self.y+11),
				(togrid(self.column)+85,togrid(self.row)+self.y+100),
				(togrid(self.column)+15,togrid(self.row)+self.y+100)])

			pygame.draw.polygon(screen,darkrgbperc(self.health/self.allhealth),[
				(togrid(self.column)+20,togrid(self.row)+self.y),
				(togrid(self.column)+80,togrid(self.row)+self.y),
				(togrid(self.column)+100,togrid(self.row)+self.y+10),
				(togrid(self.column),togrid(self.row)+self.y+10)])

			screen.blit(pygame.font.SysFont(None,30).render(str(self.health),1,(25,232,190)),(togrid(self.column)+40,togrid(self.row)+self.y+40))
		except:
			pass

def rem(lst,inde):
	return lst[:inde-1]+lst[inde:]


def patterntocubelist(difficulty=1):
	pattern = patterns.getpattern()
	ret = [[]for i in range(5)]
	for row in range(5):
		for column in range(5):
			if pattern[row][column] != 0:
				ret[column].append(Block(column,row,random.randint(int(20*difficulty),int(40*difficulty))))
	for row in ret:
		row = row.reverse()


	return ret

def game():
	global score 
	score = 0

	start = time.time()
	clock = pygame.time.Clock()
	player = Player()
	pos,speed = 0,2

	cubes = [[]for i in range(5)]
	for n in range(5):
		cubes[n].append(Block(n,random.randint(0,4),40))
	difficulty = 1
	tick = 0
	bullets = [[]for i in range(5)]
	while True:
		#uncomment this statement and for some reason the code will run faster at lower fps values (30 - 60fps). Without, a 60fps designed game will run at a lower framerate
		#print("",end=" ")

		mx,my = pygame.mouse.get_pos()

		pos,speed = background(pos,speed)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_l:
					print(player)
				if event.key == pygame.K_s:
					cubes = patterntocubelist()

			if event.type == pygame.MOUSEBUTTONDOWN:
				bullets[extcolumn(player.pos.x+32)].append(Bullet(player.pos.x+32,height-150,2,9))



		mx = constrain(mx,0,width-44)
		player.pos.x = mx
				
		if tick %3 == 0:
			bullets[extcolumn(player.pos.x+32)].append(Bullet(player.pos.x+32,height-150,1,10))





		cubr = False
		for m,row in enumerate(cubes):
			for n,cube in enumerate(row):
				if cube.destroy:
					row.pop(n)
				cube.update(speed)
		for m,row in enumerate(bullets):
			for n,bullet in enumerate(row):
				bullet.update()
				if bullet.destroy: bullets[m].pop(n)
			for n in cubes:
				if len(n) != 0:
					cubr = True
			if len(row) != 0 and cubr:
				try:
					if row[0].y	<= togrid(cubes[m][0].row)+cubes[m][0].y+116.6 and cubes[m][0].y < player.pos.y:
						bullets[m] = bullets[m][1:]
						cubes[m][0].hit(row[0])
				except:
					pass
		difficulty+=0.0003
		if tick%1000 ==0:
			cubes = patterntocubelist(difficulty)

		if tick%3==0:
			for row in cubes:
				for cube in row:
					if cube.collisionrectangle.colliderect(pygame.Rect(player.pos.x,player.pos.y+16,44,48)):
						game()
		end = time.time()
		curr_fps = 1//(end-start)
		start = time.time()

		player.update()
		#pygame.draw.rect(screen,(0,255,0),pygame.Rect(player.pos.x,player.pos.y+16,44,48),1)
		screen.blit(pygame.font.SysFont(None,30).render("score : "+str(score),1,(25,232,190)),(20,20))
		screen.blit(pygame.font.SysFont(None,30).render(f"fps : {curr_fps}",1,(25,232,190)),(500,20))
		pygame.display.update()
		clock.tick(90)
		tick+=1
		if tick >= 10000000:
			tick = 1

game()





































