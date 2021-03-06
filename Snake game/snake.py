import curses
import random

screen_init = curses.initscr()

curses.curs_set(0) #curs_set sets the cursor; we'll set it to 0

height,width = screen_init.getmaxyx() #setting height & width 

window = curses.newwin(height,width, 0,0) #Generating a window, to the size of the terminal-- o/p screen


#Allows keypad input & refreshes screen after every 100 milisecond
window.keypad(1)
window.timeout(100)

#initializing snakes initial position// and creating snake
snake_x = width/4
snake_y = height/2

snake = [ [snake_y, snake_x],[snake_y,snake_x-1],[snake_y,snake_x-1]]

food = [height/2, width/2]
window.addch(food[0], food[1], curses.ACS_PI)

#Setting where the snake will move initially
key = curses.KEY_LEFT

#We'll start a loop for every movement of the snake
#How the snake will die, how it's size will increase after every slice
#of pie lol; etc etc

while True:
	next_key = window.getch() #to determine the next key pressed
	key = key if next_key == -1 else next_key
	
	#how the snake will die
	if snake[0][0] in [0,height] or snake[0][1] in [0,width] or snake[0] in snake[1:]:
	    curses.endwin()
	    quit()
	
	#New head of the snake 
	new_head = [snake[0][0], snake[0][1]]	 
	
	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[0] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)

	if snake[0] == food:
		food = None
		while food is None:
			new_food = [   random.randint(1,height-1), random.randint(1, width -1)]
		
			food = new_food if new_food not in snake else None
			window.addch(food[0], food[1], curses.ACS_PI)
		window.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()
		window.addch(tail[0], tail[1], ' ')
	window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)	