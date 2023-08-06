import sys
from tkinter import *
from tkinter.ttk import *

class UIStack:
    def __init__(self, mylist=None):
        self.dblist = []
        self.StringStacks = {}
        # global dblist
        if mylist:
            self.initial(mylist)
    def initial(self, mylist):
        root = Tk()
        if 'title' in mylist:
            root.title(mylist['title'])
        else:
            root.title(sys.argv[0])
        flist = mylist['function']
        i = 1
        for item in flist:
            y = 1
            func = flist[item]
            db = StringVar()
            self.dblist.append(db) # 变量
            self.StringStacks[item] = db

            inputme = Entry(root, width=80, textvariable=db)
            inputme['state'] = 'write'
            inputme.grid(row=i, column=1, padx=3, pady=3, sticky=W + E)

            if func!= None:
                pushme = Button(root, text=item, command=func)
            else:
                pushme = Button(root, text=item)
            pushme.grid(row=i, column=2, sticky=W, padx=(2, 0), pady=(2, 0))
            i += 1
        root.columnconfigure(2, weight=1)
        root.mainloop()

    def getVal(self, item):
        return self.StringStacks[item].get()

if __name__ == '__main__':
    myui = UIStack()
    def func1():
        print('001')
    def func2():
        x = getattr(myui, 'getVal')("text2")
        print(x)
    mylist = {
        "function": {
            "text1": func1,
            "text2": func2
        }
    }
    myui.initial(mylist)

