import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from spaceship import SpaceShip,Destination
from galaxy import Galaxy


class MazeGame:
    def __init__(self, maze,agent,goal):
        self.gameon=True
        self.agent = agent
        self.goal = goal
        self.maze = maze
        self.cell_size = 50
        self.canvas_width = self.cols * self.cell_size
        self.canvas_height = self.rows * self.cell_size

        self.root = tk.Tk()
        self.root.wm_title('maze')
        self.root.iconphoto(True, ImageTk.photoimage(file = "wall.png"))

        self.canvas = tk.Canvas(self.root, width=self.canvas_width, 
    height=self.canvas_height)
        self.canvas.pack()
        self.canvas.grid(row =1,columnspan =3,rowspan =3)

        self.up_button = tk.Button(self.root,text= "Up",command = lambda
    :self.move("Up"))
        self.up_button.grid(row=4,column=1,)
        self.down_button = tk.Button(self.root,text="Down",command = lambda
    :self.move("Down"))
        self.down_button.grid(row=5,column=1)
        self.rightup_button = tk.Button(self.root,text= "RightUp",command = lambda
    :self.move("RightUp") )
        self.rightup_button.grid(row=4,column=2)
        self.rightdown_button = tk.Button(self.root,text= "RightDown",command = lambda
    :self.move("RightDown") )
        self.rightdown_button.grid(row=5,column=2)
        self.leftup_button = tk.Button(self.root,text= "LeftUp",command = lambda
    :self.move("LeftUp"))
        self.leftup_button.grid(row=3,column=0)
        self.leftdown_button = tk.Button(self.root,text= "LeftDown",command = lambda
    :self.move("LeftDown"))
        self.leftdown_button.grid(row=3,column=-1)

        self.menubar = tk.Menu(self.root)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help", command=lambda : messagebox.showinfo("Help", "HELP YOURSELF"))
        self.helpmenu.add_command(label="About...", command=lambda : messagebox.showinfo("About", "ADRIFT IN SPACE AND TIME"))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menubar)
        
        self.images = {
            0: ImageTk.PhotoImage(Image.open("path.png").resize((self.cell_size, self.cell_size))),
            1: ImageTk.PhotoImage(Image.open("wall.png").resize((self.cell_size, self.cell_size))),
            "agent": ImageTk.PhotoImage(Image.open("agent.png").resize((self.cell_size, self.cell_size)))
        }
        
        self.moves = 0
        self.text = tk.StringVar()
        self.text.set('Number of moves '+str(self.moves))
        self.l = tk.Label ( self.root, textvariable= self.text)
        self.l.grid(row=6,column=0,columnspal =3)

        self.draw_maze()
    def move(self,direction):
        if self.gameon:
            self.moves += 1
            self.text.set('Number of moves '+str(self.moves))
            self.agent.move(direction)
        if self.agent.reached_object(self.goal):
            self.gameon = False
            self.draw_gameover()
        else:
            self.draw_maze()
    
    def draw_gameover(self):
        self.canvas.delete("all")
        x = self.canvas_width//2
        y = self.canvas_height//2
        image= self.images["goal"]
        self.canvas.create_image(x,y, image=image)
    
    def draw_maze(self):
        self.canvas.delete("all")
        for row in range(self.maze.height):
            for col in range(self.maze.width):
                x = col * self.cell_size + self.cell_size//2
                y = row * self.cell_size + self.cell_size//2
                cell_type = self.maze.get(row,col)
                image = self.images[cell_type]
                self.canvas.create_image(x,y, image=image)
                image= self.images["goal"]
                x = self.goal.col * self.cell_size + self.cell_size//2
                y = self.goal.row * self.cell_size + self.cell_size//2
                self.canvas.create_image(x, y, image=image)
                
                image= self.images["agent"]
                x = self.agent.col * self.cell_size + self.cell_size//2
                y = self.agent.row * self.cell_size + self.cell_size//2
                self.canvas.create_image(x, y, image=image)
    
    def run(self):
        self.root.mainloop()

galaxy = Galaxy()
galaxy.load()
ss = SpaceShip(galaxy)
game = MazeGame (galaxy,ss,Destination(*galaxy.finish))
game.run()




    