from tkinter import *

tk=Tk()

text=StringVar()
name=StringVar()
name.set('Alex')
text.set('')
tk.title('Chat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

def loopproc():
	log.insert (END,'Hello '+ name.get() + '!\n')
	tk.after(1000,loopproc)

def sendproc(event):
	log.insert (END,name.get()+':'+text.get()+'\n')
	text.set('')

msg.bind('<Return>',sendproc)
tk.after(1000,loopproc)
tk.mainloop()

