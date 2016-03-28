import tkinter as tk

#create top level window/frame
top = tk.Tk() #what is it that I'm creating here?
F = tk.Frame(top) #create a frame with top as parent
F.pack(fill='both') #'fill' the parent with this frame?

#now the frame with text entry
fEntry = tk.Frame(F, border=1) #create a frame to hold entry widget
eHello = tk.Entry(fEntry) #create entry widget
eHello.pack(side="left") #pack the (empty) frame at the left
lHistory = tk.Label(fEntry, text='last entry appears here', foreground="steelblue")
lHistory.pack(side='bottom', fill='x') #pack at bottom?
fEntry.pack(side='top')

#create the event handler to clear the test
def evClear():
	lHistory['text'] = eHello.get()
	eHello.delete(0, tk.END)

#Finally the frame with the buttons
# sink this one for emphasis
fButtons = tk.Frame(F, relief='sunken', border='1')
bClear = tk.Button(fButtons, text='Clear Text', command=evClear)
bClear.pack(side='left', padx=5, pady=2)
bQuit = tk.Button(fButtons, text='Quit', command=F.quit)
bQuit.pack(side='right', padx=5, pady=2)
fButtons.pack(side='top', fill='x')

#run eventloop
F.mainloop()