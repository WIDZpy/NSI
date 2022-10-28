import turtle as tt

def rectangle():
	tt.color(0.9,0.40,.5)
	tt.width(6)
	lst = [60, 120, 60, 120]
	for loop in lst:
		tt.fd(loop)
		tt.right(90)
	tt.color(0, 0, 0)
	tt.width(1)

def sablier(rect=(0,0,60,120), margin=(15,15)):
	point = [(rect[0]+margin[0], rect[1]-margin[1]),
			 (rect[0]+rect[2]-margin[0], rect[1]-margin[1]),
			 (rect[0]+margin[0], rect[1]-rect[3]+margin[1]),
			 (rect[0]+rect[2]-margin[0], rect[1]-rect[3]+margin[1])]
	tt.begin_fill()
	tt.fillcolor('green')
	tt.up()
	
	for loop in point:

		tt.goto(loop)
		tt.down()
	tt.goto(point[0])
	tt.end_fill()

def nb_de_VOITURES_ET_NON_PAS_WAGON(n):
	print(n+35//36)
	# ne fonctione pour aucune des valeur de N car si n==1 alor la fonction done 0 alor qu'il faudrai une voiture

def exagone():
	# tt.right((360 / 6) / 2)
	for loop in range(6):
		tt.fd(100)
		tt.right(360 / 6)

def flocon():
	for loop in range(6):
		tt.fd(100)
		tt.bk(100)
		tt.right(360 / 6)

def nucleaire():
		tt.begin_fill()
		for loop in range(3):
			tt.fd(100)
			for i in range(2):
				tt.left(360/3)
				tt.fd(100)
		tt.end_fill()

def triforce():
	tt.right(180/3)
	for i in range(3):
		tt.begin_fill()
		for loop in range(4):
			tt.fd(100)
			tt.right(360/3)
		tt.fd(100)
		tt.end_fill()

def ying_yang():
	tt.begin_fill()
	tt.circle(100,180)
	tt.circle(200,180)
	tt.circle(100,-180)
	tt.end_fill()
	tt.circle(100, 180)
	tt.circle(200, 180)
	tt.circle(100, -180)

	tt.up()
	tt.setpos(0,80)
	tt.down()
	tt.color('white')
	tt.fillcolor('white')
	tt.begin_fill()
	tt.circle(20)
	tt.end_fill()

	tt.up()
	tt.setpos(0,0)
	tt.setpos(0, -80)
	tt.down()
	tt.color('black')
	tt.fillcolor('black')
	tt.begin_fill()
	tt.left(180)
	tt.circle(20)
	tt.end_fill()

def escalier(n, angle):
	for i in range(n):
		tt.left(90*angle)
		tt.fd(10)
		tt.right(90*angle)
		tt.fd(10)

def grid(n,m):
	for i in range(m):
		tt.right(90)
		tt.fd(10*n)
		tt.bk(10*n)
		tt.left(90)
		tt.fd(10)
	tt.right(90)
	for i in range(n):
		tt.right(90)
		tt.fd(10*m)
		tt.bk(10*m)
		tt.left(90)
		tt.fd(10)
	tt.right(90)
	tt.fd(10*m)

def degrade(n):
	for loop in range(n,0,-1):
		color = ((loop/n),(loop/n),(loop/n))
		tt.fillcolor(color)
		tt.begin_fill()
		tt.color(color)
		for i in range(2):
			tt.fd(30)
			tt.right(90)
			tt.fd(100)
			tt.right(90)
		tt.end_fill()
		tt.fd(30)



def main():
	for loop in range(9,10):
		grid(loop,loop)
		tt.home()
	pass

if __name__ == '__main__':
	main()
	tt.exitonclick()
