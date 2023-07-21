import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()

        self.playlist=['Hello' ,'world']
        self.creater_frames()
        self.track_widgets()
        self.control_widgets()
        self.tracklist_widgets()


    def creater_frames(self):
        self.track=tk.LabelFrame(self,text='Song Track',
                               font=("times new roman",15,"bold"),
                               bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.track.configure(width=410,height=300)
        self.track.grid(row=0,column=0)

        self.tracklist=tk.LabelFrame(self,text=f'Playlist -{len(self.playlist)}',
                               font=("times new roman",15,"bold"),
                               bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        self.tracklist.configure(width=190,height=400)
        self.tracklist.grid(row=0,column=1,rowspan=3,pady=5)

        self.controls=tk.LabelFrame(self,
                               font=("times new roman",15,"bold"),
                               bg="white",fg="white",bd=2,relief=tk.GROOVE)
        self.controls.configure(width=410,height=80)
        self.controls.grid(row=2,column=0,pady=5,padx=10)

    def track_widgets(self):
        self.canvas=tk.Label(self.track,image=img)
        self.canvas.configure(width=400,height=240)
        self.canvas.grid(row=0,column=0)

        self.canvas=tk.Label(self.track,font=('times new roman',15,"bold"),
        bg="white",fg="dark blue")
        self.canvas['text']="Musicxy MP3 Player"
        self.canvas.configure(width=30,height=1)
        self.canvas.grid(row=1,column=0)

    def control_widgets(self):
        self.loadsongs=tk.Button(self.controls,bg='green',fg='white',font=10)
        self.loadsongs['text']='load songs'
        self.loadsongs['command']=self.retreive_songs()
        self.loadsongs.grid(row=0,column=0,padx=10)

        self.prev=tk.Button(self.controls,image=prev)
        self.prev['command']=self.prev_songs()
        self.prev.grid(row=0,column=1)

        self.pause=tk.Button(self.controls,image=pause)
        self.pause['command']=self.pause_songs()
        self.pause.grid(row=0,column=2)

        self.next=tk.Button(self.controls,image=next)
        self.next['command']=self.next_songs()
        self.next.grid(row=0,column=3)

        self.volume=tk.DoubleVar()
        self.slider=tk.Scale(self.controls,from_=0,to=10,orient=tk.HORIZONTAL)
        self.slider['variable']=self.volume
        self.slider.set(8)
        self.slider['command']=self.change_volume()
        self.slider.grid(row=0,column=4,padx=5)

    def tracklist_widgets(self):
        self.scrollbar=tk.Scrollbar(self.tracklist,orient=tk.VERTICAL)
        self.scrollbar.grid(row=0,column=1,rowspan=5,sticky='ns')
        self.list=tk.Listbox(self.tracklist,selectmode=tk.SINGLE,
                             yscrollcommand=self.scrollbar.set,selectbackground='sky blue')
        self.enumerate_songs()
        self.list.config(height=22)

        self.scrollbar.config(command=self.list.yview)
        self.list.grid(row=0,column=0,rowspan=5)

    
    def enumerate_songs(self):
        for index, song in enumerate(self.playlist):
            self.list.insert(index,os.path.basename(song))

    def retreive_songs(self):
        self.songslist=[]
        directory=filedialog.askdirectory()
        for root_,dirs,files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1]==".mp3":
                    path=(root_ + "" +file).replace('\\','/')
                    self.songslist.append(path)

        self.playlist=self.songslist
        self.tracklist['text']=f'playList-{str(len(self.playlist))}'
        self.enumerate_songs()
    
    
    

    def pause_songs(self):
        pass

    def prev_songs(self):
        pass

    def next_songs(self):
        pass

    def change_volume(self,event=None):
        self.v=self.volume.get()
        print(self.v)


                               

root=tk.Tk()
root.geometry('600x400')
root.wm_title('Musicxy MP3 Player')

img=PhotoImage(file="c:\\Desktop\\music.gif")
next=PhotoImage(file="C:\\Desktop\\next.gif")
prev=PhotoImage(file="C:\\Desktop\\previous.gif")
play=PhotoImage(file="C:\\Desktop\\play.gif")
pause=PhotoImage(file="C:\\Desktop\\pause.gif")


app=Player(master=root)


app.mainloop()

