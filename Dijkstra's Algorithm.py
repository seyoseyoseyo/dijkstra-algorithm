import Tkinter as tk
import os.path
from os import path
import tkMessageBox

# Different font types that can be referred to later
TNR12 = ("Times New Roman",12)
TNR16 = ("Times New Roman",16)
TNR24 = ("Times New Roman",24)
TNR28 = ("Times New Roman",28)
TNR32 = ("Times New Roman",32)


# Class for the main window
class MainWindow:
    # Initialisation
    def __init__(self, master):
        # Create feaures and place the features at desirable places
        self.master = master
        self.title = tk.Label(self.master, text="Dijkstra's Algorithm Solution Demonstrator", font=TNR32)
        self.button1 = tk.Button(self.master, text='Input New Question', font=TNR24, command=self.window_one)
        self.button2 = tk.Button(self.master, text="Load Up Existing Question", font=TNR24,command=self.window_six)
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.title.place(x=290,y=50)
        self.button1.place(x=340, y=220, width=600, height=100)
        self.button2.place(x=340, y=400, width=600, height=100)
        self.exit_button.place(x=1240, y=670, width=40, height=30)

    # Quit Function
    def exit_screen(self):
        self.master.quit()

    # Function that calls the top-level page when corresponding button is clicked
    def window_one(self):
        self.NewWindow = tk.Toplevel(self.master)
        self.app = Page1(self.NewWindow)

    # Function that calls the top-level page when corresponding button is clicked
    def window_six(self):
        self.NewWindow=tk.Toplevel(self.master)
        self.app=Page6(self.NewWindow)


# Class for Page 1
class Page1:
    #Initialisation
    def __init__(self, master):
        self.master = master
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Create features and place the features at desirable places
        self.title = tk.Label(self.master, text="Enter The Number Of Vertices", font=TNR32)
        self.BackButton = tk.Button(self.master, text='Back', width=25, command=self.close_windows)
        self.GoButton = tk.Button(self.master, text="Go",font=TNR24, command=self.window_two)
        self.StoreEntry = tk.StringVar()
        self.entry = tk.Entry(self.master, font=TNR24, textvariable=self.StoreEntry)
        self.GoButton.place(x=340, y=350, width=600, height=100)
        self.entry.place(x=340, y=200, width=600, height=100)
        self.BackButton.place(x=1240, y=620, width=40, height=30)
        self.title.place(x=375, y=50)
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.exit_button.place(x=1240, y=670, width=40, height=30)

    # Function that destroy the toplevel page(return to previous page)
    def close_windows(self):
        self.master.destroy()

    # Function that quit the program
    def exit_screen(self):
        self.master.quit()

    # Function that calls the next toplevel page
    def window_two(self):
        NumOfVertices=self.StoreEntry.get()
        # Check if the number that the user entered is inside the desirable range
        try:
            if int(NumOfVertices)>10 or int(NumOfVertices)<3:
                tkMessageBox.showerror(parent=self.master, title="Warning", message="The Number you entered is not between 3 and 10")
            else:
                self.window_two = tk.Toplevel(self.master)
                self.app = Page2(self.window_two, NumOfVertices)
        except ValueError:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Please enter an integer between 3 and 10")


# Class for Page 2
class Page2():
    # Initialisation
    def __init__(self, master, NumOfVertices):
        self.master = master
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Create features and place the features at desirable places
        self.title = tk.Label(self.master, font=TNR32, text="Please Enter the Vertex Names")
        self.BackButton = tk.Button(self.master, text="Back", command=self.exit_page2)
        self.ProceedButton = tk.Button(self.master, text="Proceed", command=self.window_three)
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.exit_button.place(x=1240, y=670, width=40, height=30)
        self.title.place(x=375, y=50)
        self.ProceedButton.place(x=1000,y=200)
        self.BackButton.place(x=1240, y=620, width=40, height=30)
        # Pre_created dictionaries that will be referred to when the user enter things
        self.entries={}
        self.labels={}
        self.NumOfVertices=int(NumOfVertices)
        counter=0
        # Draw the entries and labels at correct place by looping through
        for i in range(0,self.NumOfVertices):
            self.entries[counter] = tk.Entry(self.master, font=TNR16)
            self.labels[counter] = tk.Label(self.master, font=TNR16, text="VertexName"+str(i+1))
            self.entries[counter].place(x=600, y=200+50*i)
            self.labels[counter].place(x=450, y=200+50*i)
            counter += 1

    # Function that destroys this toplevel page(back to previous page)
    def exit_page2(self):
        self.master.destroy()

    # Function that quits this program
    def exit_screen(self):
        self.master.quit()

    # Function that calls the next toplevel page
    def window_three(self):
        # Creates states for validations and make the state false if entered data is not desirable
        LengthState=True
        for i in range(self.NumOfVertices):
            if len(self.entries[i].get())>4:
                LengthState=False
        RepeatState=True
        for i in range(self.NumOfVertices):
            for j in [x for x in range(self.NumOfVertices) if x!=i]:
                if self.entries[i].get()==self.entries[j].get():
                    RepeatState=False

        CheckingState=True
        for i in range(self.NumOfVertices):
            if self.entries[i].get()=="":
                CheckingState=False
        if CheckingState==False:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Don't leave the entries blank please")
        elif LengthState==False:
            result=tkMessageBox.askyesno(parent=self.master,title="Caution",message="The character length of one or more of your entries is too long.\n"
                                                                             "It may affect the appearance of tables and demonstrations later.\n"
                                                                             "Are you sure to continue?")
            if result is True:
                self.window_three = tk.Toplevel(self.master)
                self.app = Page3(self.window_three,self.entries)
            else:
                pass
        elif RepeatState==False:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Two or more vertices cannot share the same name")
        else:
            self.window_three = tk.Toplevel(self.master)
            self.app = Page3(self.window_three,self.entries)


# Class for the Page3
class Page3():
    # Initialisation
    def __init__(self, master, entries):
        self.master = master
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        self.BackButton = tk.Button(self.master, text="Back", command=self.exit_page3)
        self.ProceedButton = tk.Button(self.master, text="Proceed", command=self.window_four)
        self.title = tk.Label(self.master, font=TNR32, text="Please Enter the Length of Edges")
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.title.place(x=375, y=50)
        self.exit_button.place(x=1240, y=670, width=40, height=30)
        self.BackButton.place(x=1240, y=620, width=40, height=30)
        self.ProceedButton.place(x=1000, y=200)
        NumOfVertices=len(entries)
        # Make several dictonaries that can be asssigned to later
        self.LengthEntries={}
        self.NameLabelsHor={}
        self.NameLabelsVer={}
        self.NameEntries=entries
        self.UnusedLabels={}

        # Lists of positions for counter where entry will not be placed at that place
        DeleteList=[]
        if NumOfVertices==3:
            DeleteList=[0,3,4,6,7,8]
        if NumOfVertices==4:
            DeleteList=[0,4,5,8,9,10,12,13,14,15]
        if NumOfVertices==5:
            DeleteList=[0,5,6,10,11,12,15,16,17,18,20,21,22,23,24]
        if NumOfVertices==6:
            DeleteList=[0,6,7,12,13,14,18,19,20,21,24,25,26,27,28,30,31,32,33,34,35]
        if NumOfVertices==7:
            DeleteList=[0,7,8,14,15,16,21,22,23,24,28,29,30,31,32,35,36,37,38,39,40,42,43,44,45,46,47,48]
        if NumOfVertices==8:
            DeleteList=[0,8,9,16,17,18,24,25,26,27,32,33,34,35,36,40,41,42,43,44,45,48,49,50,51,52,53,54,56,57,58,59,60,61,62,63]
        if NumOfVertices==9:
            DeleteList=[0,9,10,18,19,20,27,28,29,30,36,37,38,39,40,45,46,47,48,49,50,54,55,56,57,58,59,60,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,79,80]
        if NumOfVertices==10:
            DeleteList=[0,10,11,20,21,22,30,31,32,33,40,41,42,43,44,50,51,52,53,54,55,60,61,62,63,64,65,66,70,71,72,73,74,75,76,77,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99]

        # Counters that will be referred to in the loop
        counter1=0
        counter2=0

        # Two loops where the entries will be created at positions if the counter is not in the deletelist created above
        for i in range(0,NumOfVertices):
            for j in range(0,NumOfVertices):
                self.LengthEntries[counter1] = tk.Entry(self.master,font=TNR12)
                if counter1 not in DeleteList:
                    self.LengthEntries[counter1].place(x=475+50*i, y=200+50*j, width=30)
                    counter1+=1
                else:
                    self.UnusedLabels[counter1]=tk.Label(self.master, text="--")
                    self.UnusedLabels[counter1].place(x=475+50*i, y=200+50*j, width=30)
                    counter1+=1

        # Loop to position the labels
        for i in range(NumOfVertices):
            self.NameLabelsHor[counter2] = tk.Label(self.master, font=TNR12,text=entries[i].get())
            self.NameLabelsVer[counter2] = tk.Label(self.master, font=TNR12,text=entries[i].get())
            self.NameLabelsHor[counter2].place(x=475+50*i, y=150)
            self.NameLabelsVer[counter2].place(x=375, y=200+50*i)

    # Function to destroy this toplevel page(back to previous page)
    def exit_page3(self):
        self.master.destroy()

    # Function to quit the program
    def exit_screen(self):
        self.master.quit()

    # Function to call the next toplevel page
    def window_four(self):
        CheckingState1=True
        for i in range(len(self.LengthEntries)):
            try:
                if self.LengthEntries[i].get()=="":
                    pass
                else:
                    checkvalue=int(self.LengthEntries[i].get())
            except ValueError:
                CheckingState1=False

        if CheckingState1==False:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Please Enter Integer values please")
        else:
            self.window_four = tk.Toplevel(self.master)
            self.app = Page4(self.window_four, self.NameEntries, self.LengthEntries)

# Class for Page 4
class Page4():
    # Initialisation
    def __init__(self, master,NameEntries, LengthEntries):
        self.master = master
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Create features and place those features at desirable places on the page
        self.NameEntries=NameEntries
        self.LengthEntries=LengthEntries
        self.StartOne=tk.StringVar()
        self.EndOne=tk.StringVar()
        self.title = tk.Label(self.master, font=TNR32, text="Please select the starting and ending vertex")
        self.title.place(x=300, y=50)
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.exit_button.place(x=1240, y=670, width=40, height=30)
        Drop1Label=tk.Label(self.master,text="Starting Vertex",font=TNR24)
        Drop1Label.place(x=300,y=200)
        Drop2Label=tk.Label(self.master,text="Ending Vertex",font=TNR24)
        Drop2Label.place(x=300,y=300)
        self.BackButton = tk.Button(self.master, text="Back", command=self.exit_page4)
        self.BackButton.place(x=1240, y=620, width=40, height=30)
        self.ProceedButton = tk.Button(self.master, text="Proceed", command=self.window_five)
        self.ProceedButton.place(x=1000, y=200)
        self.VerticesList=[]
        self.LengthList=[]

        NumOfVertices=len(NameEntries)
        for i in range(0,len(NameEntries)):
            self.VerticesList.append(NameEntries[i].get())
        for i in range(0, NumOfVertices*NumOfVertices):
            self.LengthList.append(LengthEntries[i].get())
        Drop1=tk.OptionMenu(self.master, self.StartOne, *self.VerticesList)
        Drop2=tk.OptionMenu(self.master, self.EndOne, *self.VerticesList)
        Drop1.place(x=520,y=200)
        Drop2.place(x=520,y=300)

    # Function to destroy this toplevel page (back to previous page)
    def exit_page4(self):
        self.master.destroy()

    # Function to quit the program
    def exit_screen(self):
        self.master.quit()

    # Function to call the page 5 instance as the toplevel page
    def window_five(self):
        self.StartingVertex=self.StartOne.get()
        self.EndingVertex=self.EndOne.get()
        if self.StartingVertex=="" or self.EndingVertex=="":
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Please Select the vertices before going into demonstration")
        elif self.StartingVertex==self.EndingVertex:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="The Starting Vertex and the Ending Vertex cannot be same!")
        else:
            self.window_five = tk.Toplevel(self.master)
            self.app = Page5(self.window_five, self.VerticesList, self.LengthList, self.StartingVertex, self.EndingVertex)


# Class for Page 5
class Page5():
    # Initialisation
    def __init__(self, master, VerticesList, LengthList, StartingVertex, EndingVertex):
        self.master = master
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Create features and place the features at desirable places
        self.StartingVertex=StartingVertex
        self.EndingVertex=EndingVertex
        self.VerticesList=VerticesList
        self.LengthList=LengthList
        self.title = tk.Label(self.master, font=TNR32, text="Demonstration Page")
        self.title.place(x=200, y=30)
        NumOfVertices=len(VerticesList)
        self.NumOfUnits=300
        ExplanationLabelVariable=tk.StringVar()
        ExplanationLabel=tk.Label(self.master,textvariable=ExplanationLabelVariable, justify=tk.LEFT, wraplength=self.NumOfUnits, font=TNR16)
        ExplanationLabel.place(x=900,y=200)
        self.ExitButton = tk.Button(self.master, text="Exit", command=self.exit_screen)
        self.ExitButton.place(x=1240, y=670, width=40, height=30)
        self.FileNameEntry=tk.Entry(self.master,font=TNR16)
        self.FileNameEntry.place(x=900, y=600, width=200)
        self.SaveButton = tk.Button(self.master, text="Save This Question",command=self.save)
        self.SaveButton.place(x=900, y=500, width=200, height=30)
        self.SaveLabel=tk.Label(self.master,text="Under the name",font=TNR16)
        self.SaveLabel.place(x=900,y=550)
        self.BackButton = tk.Button(self.master, text="Back", command=self.exit_page5)
        self.BackButton.place(x=1240, y=620, width=40, height=30)

        # If the user enters nothing in one entry, the program will set it to 0
        for i in range(0,len(LengthList)):
            if LengthList[i]=="":
                LengthList[i]="0"
        # Make up for the non-existent entries because they are the same so share same values
        if NumOfVertices ==3:
            LengthList[3]=LengthList[1]
            LengthList[6]=LengthList[2]
            LengthList[7]=LengthList[5]

        if NumOfVertices==4:
            LengthList[4]=LengthList[1]
            LengthList[8]=LengthList[2]
            LengthList[9]=LengthList[6]
            LengthList[12]=LengthList[3]
            LengthList[13]=LengthList[7]
            LengthList[14]=LengthList[11]
        if NumOfVertices==5:
            LengthList[5]=LengthList[1]
            LengthList[10]=LengthList[2]
            LengthList[15]=LengthList[3]
            LengthList[20]=LengthList[4]
            LengthList[11]=LengthList[7]
            LengthList[16]=LengthList[8]
            LengthList[21]=LengthList[9]
            LengthList[17]=LengthList[13]
            LengthList[22]=LengthList[14]
            LengthList[23]=LengthList[19]
        if NumOfVertices==6:
            LengthList[6]=LengthList[1]
            LengthList[12]=LengthList[2]
            LengthList[18]=LengthList[3]
            LengthList[24]=LengthList[4]
            LengthList[30]=LengthList[5]
            LengthList[13]=LengthList[8]
            LengthList[19]=LengthList[9]
            LengthList[25]=LengthList[10]
            LengthList[31]=LengthList[11]
            LengthList[20]=LengthList[15]
            LengthList[26]=LengthList[16]
            LengthList[32]=LengthList[17]
            LengthList[27]=LengthList[22]
            LengthList[33]=LengthList[23]
            LengthList[34]=LengthList[29]
        if NumOfVertices==7:
            LengthList[7]=LengthList[1]
            LengthList[14]=LengthList[2]
            LengthList[21]=LengthList[3]
            LengthList[28]=LengthList[4]
            LengthList[35]=LengthList[5]
            LengthList[42]=LengthList[6]
            LengthList[15]=LengthList[9]
            LengthList[22]=LengthList[10]
            LengthList[29]=LengthList[11]
            LengthList[36]=LengthList[12]
            LengthList[43]=LengthList[13]
            LengthList[23]=LengthList[17]
            LengthList[30]=LengthList[18]
            LengthList[37]=LengthList[19]
            LengthList[44]=LengthList[20]
            LengthList[31]=LengthList[25]
            LengthList[38]=LengthList[26]
            LengthList[45]=LengthList[27]
            LengthList[39]=LengthList[33]
            LengthList[46]=LengthList[34]
            LengthList[47]=LengthList[41]
        if NumOfVertices==8:
            LengthList[8]=LengthList[1]
            LengthList[16]=LengthList[2]
            LengthList[24]=LengthList[3]
            LengthList[32]=LengthList[4]
            LengthList[40]=LengthList[5]
            LengthList[48]=LengthList[6]
            LengthList[56]=LengthList[7]
            LengthList[17]=LengthList[10]
            LengthList[25]=LengthList[11]
            LengthList[33]=LengthList[12]
            LengthList[41]=LengthList[13]
            LengthList[49]=LengthList[14]
            LengthList[57]=LengthList[15]
            LengthList[26]=LengthList[19]
            LengthList[34]=LengthList[20]
            LengthList[42]=LengthList[21]
            LengthList[50]=LengthList[22]
            LengthList[58]=LengthList[23]
            LengthList[35]=LengthList[28]
            LengthList[43]=LengthList[29]
            LengthList[51]=LengthList[30]
            LengthList[59]=LengthList[31]
            LengthList[44]=LengthList[37]
            LengthList[52]=LengthList[38]
            LengthList[60]=LengthList[39]
            LengthList[53]=LengthList[46]
            LengthList[61]=LengthList[47]
            LengthList[62]=LengthList[55]
        if NumOfVertices==9:
            LengthList[9]=LengthList[1]
            LengthList[18]=LengthList[2]
            LengthList[27]=LengthList[3]
            LengthList[36]=LengthList[4]
            LengthList[45]=LengthList[5]
            LengthList[54]=LengthList[6]
            LengthList[63]=LengthList[7]
            LengthList[72]=LengthList[8]
            LengthList[19]=LengthList[11]
            LengthList[28]=LengthList[12]
            LengthList[37]=LengthList[13]
            LengthList[46]=LengthList[14]
            LengthList[55]=LengthList[15]
            LengthList[64]=LengthList[16]
            LengthList[73]=LengthList[17]
            LengthList[29]=LengthList[21]
            LengthList[38]=LengthList[22]
            LengthList[47]=LengthList[23]
            LengthList[56]=LengthList[24]
            LengthList[65]=LengthList[25]
            LengthList[74]=LengthList[26]
            LengthList[39]=LengthList[31]
            LengthList[48]=LengthList[32]
            LengthList[57]=LengthList[33]
            LengthList[66]=LengthList[34]
            LengthList[75]=LengthList[35]
            LengthList[49]=LengthList[41]
            LengthList[58]=LengthList[42]
            LengthList[67]=LengthList[43]
            LengthList[76]=LengthList[44]
            LengthList[59]=LengthList[51]
            LengthList[68]=LengthList[52]
            LengthList[77]=LengthList[53]
            LengthList[69]=LengthList[61]
            LengthList[78]=LengthList[62]
            LengthList[79]=LengthList[71]
        if NumOfVertices==10:
            LengthList[10]=LengthList[1]
            LengthList[20]=LengthList[2]
            LengthList[30]=LengthList[3]
            LengthList[40]=LengthList[4]
            LengthList[50]=LengthList[5]
            LengthList[60]=LengthList[6]
            LengthList[70]=LengthList[7]
            LengthList[80]=LengthList[8]
            LengthList[90]=LengthList[9]
            LengthList[21]=LengthList[12]
            LengthList[31]=LengthList[13]
            LengthList[41]=LengthList[14]
            LengthList[51]=LengthList[15]
            LengthList[61]=LengthList[16]
            LengthList[71]=LengthList[17]
            LengthList[81]=LengthList[18]
            LengthList[91]=LengthList[19]
            LengthList[32]=LengthList[23]
            LengthList[42]=LengthList[24]
            LengthList[52]=LengthList[25]
            LengthList[62]=LengthList[26]
            LengthList[72]=LengthList[27]
            LengthList[82]=LengthList[28]
            LengthList[92]=LengthList[29]
            LengthList[43]=LengthList[34]
            LengthList[53]=LengthList[35]
            LengthList[63]=LengthList[36]
            LengthList[73]=LengthList[37]
            LengthList[83]=LengthList[38]
            LengthList[93]=LengthList[39]
            LengthList[54]=LengthList[45]
            LengthList[64]=LengthList[46]
            LengthList[74]=LengthList[47]
            LengthList[84]=LengthList[48]
            LengthList[94]=LengthList[49]
            LengthList[65]=LengthList[56]
            LengthList[75]=LengthList[57]
            LengthList[85]=LengthList[58]
            LengthList[95]=LengthList[59]
            LengthList[76]=LengthList[67]
            LengthList[86]=LengthList[68]
            LengthList[96]=LengthList[69]
            LengthList[87]=LengthList[78]
            LengthList[97]=LengthList[79]
            LengthList[98]=LengthList[89]

        # Create a Dictionary that will be referred to later which is extracted from the length entries from the user#
        # Will also create keys that correspond to each sub-dictionary in this Dictionary
        # Inside this dictionary there will also keys that corresponds to each vertex

        NameList={}
        counter=0
        for i in range(0,NumOfVertices):
            NameList[VerticesList[i]]={}
            counter += 1
            for j in [x for x in range(0,NumOfVertices) if x!=i]:
                NameList[VerticesList[i]][VerticesList[j]]=LengthList[len(VerticesList)*i+j]

        # If the distance between two points is 0, delete that item in that dictionary
        for i in NameList.keys():
            for j in NameList[i].keys():
                if NameList[i][j]=="0":
                    del NameList[i][j]

        # Delete the entries with 0 value in the dictionary

        # This parts check for the connection from starting vertex to ending vertex
        FullConnection=True
        ApproachableVertices=[]

        # For every vertex that is approachable from the starting vertex, it will be added to a list
        # if the ending vertex is not in the list where the starting vertex can get to.
        # the demonstration will not begin and a label will tell the user that the question
        # that they entered is not connected
        for i in NameList[StartingVertex].keys():
            ApproachableVertices.append(i)
        print ApproachableVertices
        for i in ApproachableVertices:
            for j in NameList[i].keys():
                if j not in ApproachableVertices:
                        ApproachableVertices.append(j)
        if EndingVertex not in ApproachableVertices:
            FullConnection=False
        if FullConnection==False:
            BigLabel=tk.Label(self.master,justify=tk.LEFT,text="There is no connection from \nthe starting vertex to \nthe ending vertex.",font=TNR28)
            BigLabel.place(x=200,y=200)

        # If there is a connection from the starting vertex to the ending vertex,
        # the graph will be drawn and demonstration will begin
        else:
            # Create a canvas that will hold the shapes and stuffs
            cv=tk.Canvas(self.master, width=800, height=600,borderwidth=5, background="white")
            cv.place(x=20,y=100)
            # If the number of vertices is 3, the below part of the program will run
            if len(VerticesList)==3:
                # Draw three dots on the canvas
                dot1=cv.create_oval(400,100,402,102,activefill="black")
                dot2=cv.create_oval(200,500,202,502,activefill="black")
                dot3=cv.create_oval(600,500,602,502,activefill="black")
                # Creates value holders
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                # Draw lables for each vertex
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(390,50,width=60,height=20,window=Node1_Name)
                cv.create_window(430,50,width=20,height=20,window=Node1_O)
                cv.create_window(450,50,width=20,height=20,window=Node1_P)
                cv.create_window(440,70,width=40,height=20,window=Node1_T)
                # Creates the labels that holes the variables above
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(190,450,width=60,height=20,window=Node2_Name)
                cv.create_window(230,450,width=20,height=20,window=Node2_O)
                cv.create_window(250,450,width=20,height=20,window=Node2_P)
                cv.create_window(240,470,width=40,height=20,window=Node2_T)
                # Creates the labels that holds the variables above
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(590,450,width=60,height=20,window=Node3_Name)
                cv.create_window(630,450,width=20,height=20,window=Node3_O)
                cv.create_window(650,450,width=20,height=20,window=Node3_P)
                cv.create_window(640,470,width=40,height=20,window=Node3_T)

                # Draw lines between vertices, if the distance is 0, delete that line,
                # Label on the length of the line will also be added onto the line
                line1=cv.create_line(400.5,100.5,200.5,500.5)
                line2=cv.create_line(400.5,100.5,600.5,500.5)
                line3=cv.create_line(200.5,500.5,600.5,500.5)
                if int(LengthList[1])==0:
                    cv.delete(line1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                if int(LengthList[5])==0:
                    cv.delete(line3)
                if int(LengthList[1])!=0:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(300,300,window=Label1)
                if int(LengthList[2])!=0:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(500,300,window=Label2)
                if int(LengthList[5])!=0:
                    Label3=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(400,500,window=Label3)

                # Begin the algorithm
                ExplanationLabelVariable.set("Demonstration Begin")
                # Start by updating the labels of the starting vertex update the explanation label accordingly
                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))

                # Update the labels in the demonstration
                print NameList
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))

                # Update temporary labels to the vertices that can be get to from starting vertex
                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass


                Temporary1=[]
                for i in NameList.keys():
                    if "temporary" in NameList[i].keys():
                        Temporary1.append(i)
                if len(Temporary1)==2:
                    ExplanationLabel.after(10000, lambda s=("The distance from the starting vertex to "+Temporary1[0]+" and "+ Temporary1[1]+" are "+
                                                            NameList[Temporary1[0]]["temporary"]+" and "+ NameList[Temporary1[1]]["temporary"]+" respectively."
                                                           +" Therefore we assign "+ Temporary1[0] +" temporary label "+ NameList[Temporary1[0]]["temporary"]+" and "+
                                                           Temporary1[1]+ " temporary label "+ NameList[Temporary1[1]]["temporary"]+". "):ExplanationLabelVariable.set(s))
                elif len(Temporary1)==1:
                    ExplanationLabel.after(10000, lambda s=("The distance from the starting vertex to "+Temporary1[0]+ " is "+
                                                            NameList[Temporary1[0]]["temporary"]+"."
                                                           +" Therefore we assign "+ Temporary1[0] +" temporary label "+ NameList[Temporary1[0]]["temporary"]
                                                            +". "):ExplanationLabelVariable.set(s))


                # Delete the vertex that we finished working with
                del NameList[StartingVertex]

                # Update the labels
                try:
                    Node1_T.after(10000,Node1_T_Value.set, NameList[VerticesList[0]]["temporary"])
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,Node2_T_Value.set,NameList[VerticesList[1]]["temporary"])
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,Node3_T_Value.set,NameList[VerticesList[2]]["temporary"])
                except KeyError:
                    pass


                # The function below gets the vertex with the smallest temporary label
                # It firstly creates an dictionary and inside it it has the vertex names
                # of the vertices that has a temporary label as the key and the value of
                # the temporary label as item.
                # Then the function get the key with the smallest value assigned to it.
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1
                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"

                # Updating labels
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass

                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                # If the ending vertex has already been make a permanent label, end the demonstration
                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))

                # If not, carry on
                else:
                    # The below code update the temporary labels
                    # It updates by checking whether the existing value of temporary label is smaller
                    # than the distance if it were to go from the currently working vertex to it
                    # It gives the smaller value to the temporary label
                    for item in NameList[min_temp_1].keys():
                        try:
                            if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])<int(NameList[item]["temporary"]):
                                NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                        except KeyError:
                            pass
                    if "temporary" not in NameList[EndingVertex].keys():
                        NameList[EndingVertex]["temporary"]=str(int(NameList[min_temp_1]["permanent"])+int(NameList[EndingVertex][min_temp_1]))


                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass


                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))

                    # Update the last vertex avaliable
                    for i in NameList.keys():
                        if i!=StartingVertex and i!=min_temp_1:
                            NameList[i]["permanent"]=NameList[i]["temporary"]
                            NameList[EndingVertex]["order"]="3"


                    try:
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    except KeyError:
                        pass

                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                        + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                    ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
            # if user enters 4 vertices
            if len(VerticesList)==4:
                # Creates dots which are nodes at desirable places
                dot1=cv.create_oval(200,100,202,102,activefill="black")
                dot2=cv.create_oval(200,500,202,502,activefill="black")
                dot3=cv.create_oval(600,500,602,502,activefill="black")
                dot4=cv.create_oval(600,100,602,102,activefill="black")
                # Create variable holders
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                # Create labels around the labels
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(190,50,width=60,height=20,window=Node1_Name)
                cv.create_window(230,50,width=20,height=20,window=Node1_O)
                cv.create_window(250,50,width=20,height=20,window=Node1_P)
                cv.create_window(240,70,width=40,height=20,window=Node1_T)
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(190,530,width=60,height=20,window=Node2_Name)
                cv.create_window(230,530,width=20,height=20,window=Node2_O)
                cv.create_window(250,530,width=20,height=20,window=Node2_P)
                cv.create_window(240,550,width=40,height=20,window=Node2_T)
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(590,530,width=60,height=20,window=Node3_Name)
                cv.create_window(630,530,width=20,height=20,window=Node3_O)
                cv.create_window(650,530,width=20,height=20,window=Node3_P)
                cv.create_window(640,550,width=40,height=20,window=Node3_T)
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(590,50,width=60,height=20,window=Node4_Name)
                cv.create_window(630,50,width=20,height=20,window=Node4_O)
                cv.create_window(650,50,width=20,height=20,window=Node4_P)
                cv.create_window(640,70,width=40,height=20,window=Node4_T)

                # Creates the lines connecting all vertices, delete the one
                # where the distance is 0 and add labels
                line1=cv.create_line(201,101,201,501)
                line2=cv.create_line(201,501,601,501)
                line3=cv.create_line(601,501,601,101)
                line4=cv.create_line(601,101,201,101)
                line5=cv.create_line(201,101,601,501)
                line6=cv.create_line(201,501,601,101)

                if int(LengthList[1])==0:
                    cv.delete(line1)
                if int(LengthList[2])==0:
                    cv.delete(line5)
                if int(LengthList[3])==0:
                    cv.delete(line4)
                if int(LengthList[6])==0:
                    cv.delete(line2)
                if int(LengthList[7])==0:
                    cv.delete(line6)
                if int(LengthList[11])==0:
                    cv.delete(line3)
                if int(LengthList[1])!=0:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(200,300,window=Label1)
                if int(LengthList[2])!=0:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(350,250,window=Label2)
                if int(LengthList[3])!=0:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(400,100,window=Label3)
                if int(LengthList[6])!=0:
                    Label1=tk.Label(cv,text=LengthList[6], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(400,500,window=Label1)
                if int(LengthList[7])!=0:
                    Label2=tk.Label(cv,text=LengthList[7], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(450,250,window=Label2)
                if int(LengthList[11])!=0:
                    Label3=tk.Label(cv,text=LengthList[11], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(600,300,window=Label3)

                # Where the algorithm start

                ExplanationLabelVariable.set("Demonstration Begin")
                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))

                # Update the order and permanent labels
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))

                # Create temporary labels to the vertices that can be reached
                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass

                # Updation of all temporary labels
                Temporary1=[]
                for i in NameList.keys():
                    if "temporary" in NameList[i].keys():
                        Temporary1.append(i)

                if len(Temporary1)==3:
                    ExplanationLabel.after(10000, lambda s=("The distance from the starting vertex to "+Temporary1[0]+" , "+ Temporary1[1]+ " and "+ Temporary1[2]+ " are "+
                                                            NameList[Temporary1[0]]["temporary"]+" , "+ NameList[Temporary1[1]]["temporary"]+ " and "+ NameList[Temporary1[2]]["temporary"]+
                                                            " respectively."
                                                           +" Therefore we assign "+ Temporary1[0] +" temporary label "+ NameList[Temporary1[0]]["temporary"]+" , "+
                                                           Temporary1[1]+ " temporary label "+ NameList[Temporary1[1]]["temporary"]+" and "+Temporary1[2]+ " temporary label "+ NameList[Temporary1[2]]["temporary"]+". "):ExplanationLabelVariable.set(s))
                elif len(Temporary1)==2:
                    ExplanationLabel.after(10000, lambda s=("The distance from the starting vertex to "+Temporary1[0]+" and "+ Temporary1[1]+" are "+
                                                            NameList[Temporary1[0]]["temporary"]+" and "+ NameList[Temporary1[1]]["temporary"]+" respectively."
                                                           +" Therefore we assign "+ Temporary1[0] +" temporary label "+ NameList[Temporary1[0]]["temporary"]+" and "+
                                                           Temporary1[1]+ " temporary label "+ NameList[Temporary1[1]]["temporary"]+". "):ExplanationLabelVariable.set(s))
                elif len(Temporary1)==1:
                    ExplanationLabel.after(10000, lambda s=("The distance from the starting vertex to "+Temporary1[0]+ " is "+
                                                            NameList[Temporary1[0]]["temporary"]+"."
                                                           +" Therefore we assign "+ Temporary1[0] +" temporary label "+ NameList[Temporary1[0]]["temporary"]
                                                            +". "):ExplanationLabelVariable.set(s))
                # Delete the vertex that we finished working with
                del NameList[StartingVertex]

                # Update the temporary labels
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass

                # Find the vertex with smallest temporary label
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                min_temp_1= min(TempDict1,key=TempDict1.get)

                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"

                # Update labels
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass

                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                # If ending vertex has a permanent label, end
                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))

                # Otherwise, carry on
                else:
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item]!=0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass

                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass

                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))

                    # Delete the vertex that we finished working with and get the new working label
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    print min_temp_2
                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass


                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))

                    # If the ending vertex has a permanent label, end
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

                    # Otherwise carry on the process
                    else:
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass

                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass

                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))
                        for i in NameList.keys():
                            if i!=StartingVertex and i!=min_temp_2:
                                NameList[i]["permanent"]=NameList[i]["temporary"]
                                NameList[EndingVertex]["order"]="4"
                        try:
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        except KeyError:
                            pass

                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                        + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                        ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

            # Only when there are five vertices
            if len(VerticesList)==5:
                # Creates dots(nodes)at the vertices places
                dot1=cv.create_oval(400,100,402,102,activefill="black")
                dot2=cv.create_oval(150,250,152,252,activefill="black")
                dot3=cv.create_oval(250,500,252,502,activefill="black")
                dot4=cv.create_oval(550,500,552,502,activefill="black")
                dot5=cv.create_oval(650,250,652,252,activefill="black")
                # Create value holder
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()

                # Create labels at desirable places
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(390,50,width=60,height=20,window=Node1_Name)
                cv.create_window(430,50,width=20,height=20,window=Node1_O)
                cv.create_window(450,50,width=20,height=20,window=Node1_P)
                cv.create_window(440,70,width=40,height=20,window=Node1_T)
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(60,280,width=60,height=20,window=Node2_Name)
                cv.create_window(100,280,width=20,height=20,window=Node2_O)
                cv.create_window(120,280,width=20,height=20,window=Node2_P)
                cv.create_window(110,300,width=40,height=20,window=Node2_T)
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(240,530,width=60,height=20,window=Node3_Name)
                cv.create_window(280,530,width=20,height=20,window=Node3_O)
                cv.create_window(300,530,width=20,height=20,window=Node3_P)
                cv.create_window(290,550,width=40,height=20,window=Node3_T)
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(540,530,width=60,height=20,window=Node4_Name)
                cv.create_window(580,530,width=20,height=20,window=Node4_O)
                cv.create_window(600,530,width=20,height=20,window=Node4_P)
                cv.create_window(590,550,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(640,280,width=30,height=20,window=Node5_Name)
                cv.create_window(680,280,width=20,height=20,window=Node5_O)
                cv.create_window(700,280,width=20,height=20,window=Node5_P)
                cv.create_window(690,300,width=40,height=20,window=Node5_T)

                # Create lines and delete it if the distance is 0
                # Also put labels on it
                line1=cv.create_line(401,101,151,251)
                line2=cv.create_line(401,101,251,501)
                line3=cv.create_line(401,101,551,501)
                line4=cv.create_line(401,101,651,251)
                line5=cv.create_line(151,251,251,500)
                line6=cv.create_line(151,251,551,501)
                line7=cv.create_line(151,251,651,251)
                line8=cv.create_line(251,501,551,501)
                line9=cv.create_line(251,501,651,251)
                line10=cv.create_line(551,501,651,251)
                if int(LengthList[1])==0:
                    cv.delete(line1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                if int(LengthList[7])==0:
                    cv.delete(line5)
                if int(LengthList[8])==0:
                    cv.delete(line6)
                if int(LengthList[9])==0:
                    cv.delete(line7)
                if int(LengthList[13])==0:
                    cv.delete(line8)
                if int(LengthList[14])==0:
                    cv.delete(line9)
                if int(LengthList[19])==0:
                    cv.delete(line10)
                if int(LengthList[1])!=0:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(275,175,window=Label1)
                if int(LengthList[2])!=0:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(325,300,window=Label2)
                if int(LengthList[3])!=0:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(475,300,window=Label3)
                if int(LengthList[4])!=0:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(525,175,window=Label4)
                if int(LengthList[7])!=0:
                    Label5=tk.Label(cv,text=LengthList[7], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(200,375,window=Label5)
                if int(LengthList[8])!=0:
                    Label6=tk.Label(cv,text=LengthList[8], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(350,375,window=Label6)
                if int(LengthList[9])!=0:
                    Label7=tk.Label(cv,text=LengthList[9], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(400,250,window=Label7)
                if int(LengthList[13])!=0:
                    Label8=tk.Label(cv,text=LengthList[13], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(400,500,window=Label8)
                if int(LengthList[14])!=0:
                    Label9=tk.Label(cv,text=LengthList[14], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(450,375,window=Label9)
                if int(LengthList[19])!=0:
                    Label10=tk.Label(cv,text=LengthList[19], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(600,375,window=Label10)

                # Algorithm begin and Demonstration begin
                ExplanationLabelVariable.set("Demonstration Begin")
                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))

                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))


                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass

                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                # Update the temporary labels
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass

                # Delete the label that we finished working with
                del NameList[StartingVertex]

                # Get the new working label
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                min_temp_1= min(TempDict1,key=TempDict1.get)
                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"

                # Update all the labels
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass

                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                # If there is a permanent label in ending vertex
                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                # Otherwise, carry on
                else:
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass

                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass

                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))

                    # Delete the vertex that we finished working with
                    # and get the new working vertex
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"

                    # Update the labels
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass


                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))

                    # If the ending vertex has a permanent label, end
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                    # Otherwise, carry on
                    else:
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass

                        # Update all the temporary labels
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass

                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        # Delete the minimum working vertex and and get the new working vertex
                        del NameList[min_temp_2]
                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3
                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"

                        # Update all the labels
                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass

                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))

                        # If the ending vertex has a permanent label, end
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

                        # Otherwise, carry on
                        else:
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass

                            # Update all the labels
                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass

                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            # Give the ending vertex order and temporary labels
                            for i in NameList.keys():
                                if i!=StartingVertex and i!=min_temp_3:
                                    NameList[i]["permanent"]=NameList[i]["temporary"]
                                    NameList[EndingVertex]["order"]="5"

                            # Update the labels
                            try:
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            except KeyError:
                                pass

                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                            + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                            ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

            # Only when there are five vertices
            if len(VerticesList)==6:
                # Creates dots(nodes)at the vertices places
                dot1=cv.create_oval(250,100,252,102,activefill="black")
                dot2=cv.create_oval(150,300,152,302,activefill="black")
                dot3=cv.create_oval(250,500,252,502,activefill="black")
                dot4=cv.create_oval(550,500,552,502,activefill="black")
                dot5=cv.create_oval(650,300,652,302,activefill="black")
                dot6=cv.create_oval(550,100,552,102,activefill="black")
                # Create the variables to hold values
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()
                Node6_O_Value=tk.StringVar()
                Node6_P_Value=tk.StringVar()
                Node6_T_Value=tk.StringVar()

                # Create labels that for each vertices
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(190,50,width=60,height=20,window=Node1_Name)
                cv.create_window(230,50,width=20,height=20,window=Node1_O)
                cv.create_window(250,50,width=20,height=20,window=Node1_P)
                cv.create_window(240,70,width=40,height=20,window=Node1_T)
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(60,330,width=60,height=20,window=Node2_Name)
                cv.create_window(100,330,width=20,height=20,window=Node2_O)
                cv.create_window(120,330,width=20,height=20,window=Node2_P)
                cv.create_window(110,350,width=40,height=20,window=Node2_T)
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(190,530,width=60,height=20,window=Node3_Name)
                cv.create_window(230,530,width=20,height=20,window=Node3_O)
                cv.create_window(250,530,width=20,height=20,window=Node3_P)
                cv.create_window(240,550,width=40,height=20,window=Node3_T)
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(540,530,width=60,height=20,window=Node4_Name)
                cv.create_window(580,530,width=20,height=20,window=Node4_O)
                cv.create_window(600,530,width=20,height=20,window=Node4_P)
                cv.create_window(590,550,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(660,330,width=30,height=20,window=Node5_Name)
                cv.create_window(700,330,width=20,height=20,window=Node5_O)
                cv.create_window(720,330,width=20,height=20,window=Node5_P)
                cv.create_window(710,350,width=40,height=20,window=Node5_T)
                Node6_Name=tk.Label(cv, text=VerticesList[5], bg="white", justify=tk.RIGHT)
                Node6_O=tk.Label(cv, textvariable=Node6_O_Value, relief=tk.GROOVE )
                Node6_P=tk.Label(cv, textvariable=Node6_P_Value, relief=tk.GROOVE )
                Node6_T=tk.Label(cv, textvariable=Node6_T_Value, relief=tk.GROOVE )
                cv.create_window(540,50,width=30,height=20,window=Node6_Name)
                cv.create_window(580,50,width=20,height=20,window=Node6_O)
                cv.create_window(600,50,width=20,height=20,window=Node6_P)
                cv.create_window(590,70,width=40,height=20,window=Node6_T)

                # Create lines and delete the lines where the distance is 0
                # add labels on the edges
                line1=cv.create_line(251,101,151,301)
                line2=cv.create_line(250,101,251,501)
                line3=cv.create_line(250,101,551,501)
                line4=cv.create_line(250,101,651,301)
                line5=cv.create_line(250,101,551,101)
                line6=cv.create_line(151,301,251,501)
                line7=cv.create_line(151,301,551,501)
                line8=cv.create_line(151,301,651,301)
                line9=cv.create_line(151,301,551,101)
                line10=cv.create_line(251,501,551,501)
                line11=cv.create_line(251,501,651,301)
                line12=cv.create_line(251,501,551,101)
                line13=cv.create_line(551,501,651,301)
                line14=cv.create_line(551,501,551,101)
                line15=cv.create_line(650,301,551,101)
                if int(LengthList[1])==0:
                    cv.delete(line1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                if int(LengthList[5])==0:
                    cv.delete(line5)
                if int(LengthList[8])==0:
                    cv.delete(line6)
                if int(LengthList[9])==0:
                    cv.delete(line7)
                if int(LengthList[10])==0:
                    cv.delete(line8)
                if int(LengthList[11])==0:
                    cv.delete(line9)
                if int(LengthList[15])==0:
                    cv.delete(line10)
                if int(LengthList[16])==0:
                    cv.delete(line11)
                if int(LengthList[17])==0:
                    cv.delete(line12)
                if int(LengthList[22])==0:
                    cv.delete(line13)
                if int(LengthList[23])==0:
                    cv.delete(line14)
                if int(LengthList[29])==0:
                    cv.delete(line15)
                if int(LengthList[1])!=0:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(200,200,window=Label1)
                if int(LengthList[2])!=0:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(250,280,window=Label2)
                if int(LengthList[3])!=0:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(380,280,window=Label3)
                if int(LengthList[4])!=0:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(450,200,window=Label4)
                if int(LengthList[5])!=0:
                    Label5=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(400,100,window=Label5)
                if int(LengthList[8])!=0:
                    Label6=tk.Label(cv,text=LengthList[8], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(200,400,window=Label6)
                if int(LengthList[9])!=0:
                    Label7=tk.Label(cv,text=LengthList[9], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(350,400,window=Label7)
                if int(LengthList[10])!=0:
                    Label8=tk.Label(cv,text=LengthList[10], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(400,300,window=Label8)
                if int(LengthList[11])!=0:
                    Label9=tk.Label(cv,text=LengthList[11], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(350,200,window=Label9)
                if int(LengthList[15])!=0:
                    Label10=tk.Label(cv,text=LengthList[15], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(400,500,window=Label10)
                if int(LengthList[16])!=0:
                    Label11=tk.Label(cv,text=LengthList[16], fg="black",bg="white")
                    Label11.pack()
                    cv.create_window(450,400,window=Label11)
                if int(LengthList[17])!=0:
                    Label12=tk.Label(cv,text=LengthList[17], fg="black",bg="white")
                    Label12.pack()
                    cv.create_window(420,280,window=Label12)
                if int(LengthList[22])!=0:
                    Label13=tk.Label(cv,text=LengthList[22], fg="black",bg="white")
                    Label13.pack()
                    cv.create_window(600,400,window=Label13)
                if int(LengthList[23])!=0:
                    Label14=tk.Label(cv,text=LengthList[23], fg="black",bg="white")
                    Label14.pack()
                    cv.create_window(550,320,window=Label14)
                if int(LengthList[29])!=0:
                    Label15=tk.Label(cv,text=LengthList[29], fg="black",bg="white")
                    Label15.pack()
                    cv.create_window(600,200,window=Label15)

                # Algorithm start and demonstration begin
                ExplanationLabelVariable.set("Demonstration Begin")

                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))
                if StartingVertex==VerticesList[5]:
                    Node6_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node6_O_Value. set(s))
                    Node6_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node6_P_Value.set(s))

                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))

                # Assign vertices temporary labels
                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass
                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node6_T.after(10000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                except KeyError:
                    pass

                # Delete the vertex that we are currently working with and get a new temporary working vertex
                del NameList[StartingVertex]
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                print TempDict1
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1

                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"
                # Update labels
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node6_O.after(15000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                    Node6_P.after(15000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                except Exception:
                    pass

                # Update all the order and permanent labels
                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))
                # If the ending vertex has a permanent label, end
                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                # Otherwise, carry on
                else:
                    # Update the values for the temporary labels
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass
                    # Update the temporary labels
                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node6_T.after(20000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                    except KeyError:
                        pass

                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))
                    # Delete the vertex that we finished working with and get a new working vertex
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    print min_temp_2

                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"

                    # Update the labels
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node6_O.after(25000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                        Node6_P.after(25000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                    except Exception:
                        pass

                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))
                    # If there is a permanent label in the ending vertex, end
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

                    # Otherwise, carry on
                    else:
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass

                        # Update all the temporary labels
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass

                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        # Delete the vertex that we finished working with and get a new working vertex
                        del NameList[min_temp_2]
                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3
                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"

                        # Update all the labels
                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node6_O.after(35000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                            Node6_P.after(35000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                        except Exception:
                            pass

                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))
                        # If the ending vertex has a permanent label, end
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                        # Otherwise, carry on
                        else:
                            # Update the values for the temporary labels
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass

                            # Update the temporary labels
                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node6_T.after(40000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                            except KeyError:
                                pass

                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            # Delete the vertex that we finished working with and get a new working vertex
                            del NameList[min_temp_3]
                            TempDict4={}
                            for i in NameList.keys():
                                for j in NameList[i].keys():
                                    if j=="temporary":
                                        TempDict4[i]=int(NameList[i][j])

                            min_temp_4= min(TempDict4,key=TempDict4.get)

                            NameList[min_temp_4]["permanent"]=NameList[min_temp_4]["temporary"]
                            NameList[min_temp_4]["order"]="5"

                            # Update the labels
                            try:
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node6_O.after(45000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                Node6_P.after(45000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                            except Exception:
                                pass

                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +min_temp_4+ " is assigned permanent label "+ NameList[min_temp_4]["permanent"]+ " and order label "
                                                            + NameList[min_temp_4]["order"]+"."):ExplanationLabelVariable.set(s))
                            if "permanent" in NameList[EndingVertex].keys():
                                ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                            # Otherwise, carry on
                            else:
                                # Update all the values for the temporary labels
                                for item in NameList.keys():
                                    if item!=min_temp_4:
                                        try:
                                            if NameList[min_temp_4][item]!=0:
                                                try:
                                                    if int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])> int(NameList[item]["temporary"]):
                                                        pass
                                                    elif int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])< int(NameList[item]["temporary"]):
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                                except KeyError:
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                        except KeyError:
                                            pass
                                # Update the temporary labels
                                try:
                                    Node1_T.after(50000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_T.after(50000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_T.after(50000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_T.after(50000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_T.after(50000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_T.after(50000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                except KeyError:
                                    pass

                                ExplanationLabel.after(50000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                    "working vertex "+ min_temp_4+"."):ExplanationLabelVariable.set(s))

                                # Give the eding vertex labels
                                for i in NameList.keys():
                                    if i!=StartingVertex and i!=min_temp_4:
                                        NameList[i]["permanent"]=NameList[i]["temporary"]
                                        NameList[EndingVertex]["order"]="6"


                                # Update all the labels
                                try:
                                    Node1_P.after(55000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                    Node1_O.after(55000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_P.after(55000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                    Node2_O.after(55000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_P.after(55000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                    Node3_O.after(55000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_P.after(55000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                    Node4_O.after(55000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_P.after(55000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                    Node5_O.after(55000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_P.after(55000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                    Node6_O.after(55000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                except KeyError:
                                    pass
                                # Update all the permanent and order labels
                                ExplanationLabel.after(55000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                                + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                                ExplanationLabel.after(60000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                # Update the explanation label a couple of times before ending too
            # Only when there are five vertices
            if len(VerticesList)==7:
                # Creates dots at desirable places
                dot1=cv.create_oval(400,100,402,102,activefill="black")
                dot2=cv.create_oval(200,200,202,202,activefill="black")
                dot3=cv.create_oval(150,350,152,352,activefill="black")
                dot4=cv.create_oval(300,500,302,502,activefill="black")
                dot5=cv.create_oval(500,500,502,502,activefill="black")
                dot6=cv.create_oval(650,350,652,352,activefill="black")
                dot7=cv.create_oval(600,200,602,202,activefill="black")
                # Creates variables holders
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()
                Node6_O_Value=tk.StringVar()
                Node6_P_Value=tk.StringVar()
                Node6_T_Value=tk.StringVar()
                Node7_O_Value=tk.StringVar()
                Node7_P_Value=tk.StringVar()
                Node7_T_Value=tk.StringVar()
                # Create labels around vertices
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(340,50,width=60,height=20,window=Node1_Name)
                cv.create_window(380,50,width=20,height=20,window=Node1_O)
                cv.create_window(400,50,width=20,height=20,window=Node1_P)
                cv.create_window(390,70,width=40,height=20,window=Node1_T)
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(110,180,width=60,height=20,window=Node2_Name)
                cv.create_window(150,180,width=20,height=20,window=Node2_O)
                cv.create_window(170,180,width=20,height=20,window=Node2_P)
                cv.create_window(160,200,width=40,height=20,window=Node2_T)
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(60,380,width=60,height=20,window=Node3_Name)
                cv.create_window(100,380,width=20,height=20,window=Node3_O)
                cv.create_window(120,380,width=20,height=20,window=Node3_P)
                cv.create_window(110,400,width=40,height=20,window=Node3_T)
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(240,530,width=60,height=20,window=Node4_Name)
                cv.create_window(280,530,width=20,height=20,window=Node4_O)
                cv.create_window(300,530,width=20,height=20,window=Node4_P)
                cv.create_window(290,550,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(490,530,width=30,height=20,window=Node5_Name)
                cv.create_window(530,530,width=20,height=20,window=Node5_O)
                cv.create_window(550,530,width=20,height=20,window=Node5_P)
                cv.create_window(540,550,width=40,height=20,window=Node5_T)
                Node6_Name=tk.Label(cv, text=VerticesList[5], bg="white", justify=tk.RIGHT)
                Node6_O=tk.Label(cv, textvariable=Node6_O_Value, relief=tk.GROOVE )
                Node6_P=tk.Label(cv, textvariable=Node6_P_Value, relief=tk.GROOVE )
                Node6_T=tk.Label(cv, textvariable=Node6_T_Value, relief=tk.GROOVE )
                cv.create_window(655,380,width=30,height=20,window=Node6_Name)
                cv.create_window(680,380,width=20,height=20,window=Node6_O)
                cv.create_window(700,380,width=20,height=20,window=Node6_P)
                cv.create_window(690,400,width=40,height=20,window=Node6_T)
                Node7_Name=tk.Label(cv, text=VerticesList[6], bg="white", justify=tk.RIGHT)
                Node7_O=tk.Label(cv, textvariable=Node7_O_Value, relief=tk.GROOVE )
                Node7_P=tk.Label(cv, textvariable=Node7_P_Value, relief=tk.GROOVE )
                Node7_T=tk.Label(cv, textvariable=Node7_T_Value, relief=tk.GROOVE )
                cv.create_window(605,180,width=30,height=20,window=Node7_Name)
                cv.create_window(630,180,width=20,height=20,window=Node7_O)
                cv.create_window(650,180,width=20,height=20,window=Node7_P)
                cv.create_window(640,200,width=40,height=20,window=Node7_T)
                # Creates lines and delete it if the distance is 0, add labels of edges
                line1=cv.create_line(401,101,201,201)
                line2=cv.create_line(400,101,151,351)
                line3=cv.create_line(400,101,301,501)
                line4=cv.create_line(400,101,501,501)
                line5=cv.create_line(400,101,651,351)
                line6=cv.create_line(400,101,601,201)
                line7=cv.create_line(201,201,151,351)
                line8=cv.create_line(201,201,301,501)
                line9=cv.create_line(201,201,501,501)
                line10=cv.create_line(201,201,651,351)
                line11=cv.create_line(201,201,601,201)
                line12=cv.create_line(151,351,301,501)
                line13=cv.create_line(151,351,501,501)
                line14=cv.create_line(151,351,651,351)
                line15=cv.create_line(151,351,601,201)
                line16=cv.create_line(301,501,501,501)
                line17=cv.create_line(301,501,651,351)
                line18=cv.create_line(301,501,601,201)
                line19=cv.create_line(501,501,651,351)
                line20=cv.create_line(501,501,601,201)
                line21=cv.create_line(650,351,601,201)
                if int(LengthList[1])==0:
                    cv.delete(line1)
                else:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(300,150,window=Label1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                else:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(290,215,window=Label2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                else:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(350,300,window=Label3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                else:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(450,300,window=Label4)
                if int(LengthList[5])==0:
                    cv.delete(line5)
                else:
                    Label5=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(510,215,window=Label5)
                if int(LengthList[6])==0:
                    cv.delete(line6)
                else:
                    Label6=tk.Label(cv,text=LengthList[6], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(500,150,window=Label6)
                if int(LengthList[9])==0:
                    cv.delete(line7)
                else:
                    Label7=tk.Label(cv,text=LengthList[9], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(175,275,window=Label7)
                if int(LengthList[10])==0:
                    cv.delete(line8)
                else:
                    Label8=tk.Label(cv,text=LengthList[10], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(260,365,window=Label8)
                if int(LengthList[11])==0:
                    cv.delete(line9)
                else:
                    Label9=tk.Label(cv,text=LengthList[11], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(365,365,window=Label9)
                if int(LengthList[12])==0:
                    cv.delete(line10)
                else:
                    Label10=tk.Label(cv,text=LengthList[12], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(425,275,window=Label10)
                if int(LengthList[13])==0:
                    cv.delete(line11)
                else:
                    Label11=tk.Label(cv,text=LengthList[13], fg="black",bg="white")
                    Label11.pack()
                    cv.create_window(400,200,window=Label11)
                if int(LengthList[17])==0:
                    cv.delete(line12)
                else:
                    Label12=tk.Label(cv,text=LengthList[17], fg="black",bg="white")
                    Label12.pack()
                    cv.create_window(225,425,window=Label12)
                if int(LengthList[18])==0:
                    cv.delete(line13)
                else:
                    Label13=tk.Label(cv,text=LengthList[18], fg="black",bg="white")
                    Label13.pack()
                    cv.create_window(310,420,window=Label13)
                if int(LengthList[19])==0:
                    cv.delete(line14)
                else:
                    Label14=tk.Label(cv,text=LengthList[19], fg="black",bg="white")
                    Label14.pack()
                    cv.create_window(400,350,window=Label14)
                if int(LengthList[20])==0:
                    cv.delete(line15)
                else:
                    Label15=tk.Label(cv,text=LengthList[20], fg="black",bg="white")
                    Label15.pack()
                    cv.create_window(375,275,window=Label15)
                if int(LengthList[25])==0:
                    cv.delete(line16)
                else:
                    Label16=tk.Label(cv,text=LengthList[25], fg="black",bg="white")
                    Label16.pack()
                    cv.create_window(400,500,window=Label16)
                if int(LengthList[26])==0:
                    cv.delete(line17)
                else:
                    Label17=tk.Label(cv,text=LengthList[26], fg="black",bg="white")
                    Label17.pack()
                    cv.create_window(490,420,window=Label17)
                if int(LengthList[27])==0:
                    cv.delete(line18)
                else:
                    Label18=tk.Label(cv,text=LengthList[27], fg="black",bg="white")
                    Label18.pack()
                    cv.create_window(435,365,window=Label18)
                if int(LengthList[33])==0:
                    cv.delete(line19)
                else:
                    Label19=tk.Label(cv,text=LengthList[33], fg="black",bg="white")
                    Label19.pack()
                    cv.create_window(575,425,window=Label19)
                if int(LengthList[34])==0:
                    cv.delete(line20)
                else:
                    Label20=tk.Label(cv,text=LengthList[34], fg="black",bg="white")
                    Label20.pack()
                    cv.create_window(560,335,window=Label20)
                if int(LengthList[41])==0:
                    cv.delete(line21)
                else:
                    Label21=tk.Label(cv,text=LengthList[41], fg="black",bg="white")
                    Label21.pack()
                    cv.create_window(625,275,window=Label21)

                # Demonstration begin and algorithm start
                ExplanationLabelVariable.set("Demonstration Begin")

                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"

                # Update all the labels
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))
                if StartingVertex==VerticesList[5]:
                    Node6_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node6_O_Value. set(s))
                    Node6_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node6_P_Value.set(s))
                if StartingVertex==VerticesList[6]:
                    Node7_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node7_O_Value. set(s))
                    Node7_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node7_P_Value.set(s))


                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))

                # Assign temporary labels where eligible
                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass
                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                # Update all the temporary labels
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node6_T.after(10000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node7_T.after(10000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                except KeyError:
                    pass

                # Delete the vertex that we finished working with and get the new working vertex
                del NameList[StartingVertex]
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                print TempDict1
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1

                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"

                # Update all the labels
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node6_O.after(15000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                    Node6_P.after(15000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node7_O.after(15000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                    Node7_P.after(15000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                except Exception:
                    pass

                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                # If there is a permanent label in the ending vertex, end
                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                # Otherwise, carry on
                else:
                    # Update the values for the temporary labels
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass

                    # Update the temporary labels
                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node6_T.after(20000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node7_T.after(20000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                    except KeyError:
                        pass

                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))
                    # Delete the vertex that we finished working with and ge the new working vertex
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)


                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"

                    # Update the labels
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node6_O.after(25000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                        Node6_P.after(25000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node7_O.after(25000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                        Node7_P.after(25000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                    except Exception:
                        pass

                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))

                    # If the ending vertex has a permanent label, end
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                    # Otherwise, carry on
                    else:
                    # Update the values for the temporary labels
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass
                        # Update the temporary labels
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node7_T.after(30000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                        except KeyError:
                            pass

                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        # Delete the vertex that we finished working with and get a new working vertex
                        del NameList[min_temp_2]
                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3

                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"

                        # Update all the labels
                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node6_O.after(35000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                            Node6_P.after(35000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node7_O.after(35000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                            Node7_P.after(35000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                        except Exception:
                            pass

                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))

                        # If there is a permanent label in the ending vertex,end
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                        # Otherwise, carry on
                        else:
                            # Update the vaues for the temporary labels
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass

                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node6_T.after(40000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node7_T.after(40000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                            except KeyError:
                                pass

                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            # Delete the vertex that we fininshed working with and get a new one
                            del NameList[min_temp_3]
                            TempDict4={}
                            for i in NameList.keys():
                                for j in NameList[i].keys():
                                    if j=="temporary":
                                        TempDict4[i]=int(NameList[i][j])

                            min_temp_4= min(TempDict4,key=TempDict4.get)
                            print min_temp_4
                            NameList[min_temp_4]["permanent"]=NameList[min_temp_4]["temporary"]
                            NameList[min_temp_4]["order"]="5"


                            # Update all the labels
                            try:
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node6_O.after(45000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                Node6_P.after(45000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node7_O.after(45000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                Node7_P.after(45000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                            except Exception:
                                pass

                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +min_temp_4+ " is assigned permanent label "+ NameList[min_temp_4]["permanent"]+ " and order label "
                                                            + NameList[min_temp_4]["order"]+"."):ExplanationLabelVariable.set(s))

                            # If there is a permanent lable in the ending vertex,end
                            if "permanent" in NameList[EndingVertex].keys():
                                ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                            # Otherwise, carry on
                            else:
                            # Update all the temporary label values
                                for item in NameList.keys():
                                    if item!=min_temp_4:
                                        try:
                                            if NameList[min_temp_4][item]!=0:
                                                try:
                                                    if int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])> int(NameList[item]["temporary"]):
                                                        pass
                                                    elif int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])< int(NameList[item]["temporary"]):
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                                except KeyError:
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                        except KeyError:
                                            pass

                                # Update all the temporary labels
                                try:
                                    Node1_T.after(50000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_T.after(50000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_T.after(50000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_T.after(50000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_T.after(50000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_T.after(50000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node7_T.after(50000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                except KeyError:
                                    pass

                                ExplanationLabel.after(50000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                    "working vertex "+ min_temp_4+"."):ExplanationLabelVariable.set(s))

                                # Delete the vertex that we finished working with and get a new one
                                del NameList[min_temp_4]
                                TempDict5={}
                                for i in NameList.keys():
                                    for j in NameList[i].keys():
                                        if j=="temporary":
                                            TempDict5[i]=int(NameList[i][j])

                                min_temp_5= min(TempDict5,key=TempDict5.get)
                                print min_temp_5
                                NameList[min_temp_5]["permanent"]=NameList[min_temp_5]["temporary"]
                                NameList[min_temp_5]["order"]="6"


                                # Update the labels
                                try:
                                    Node1_O.after(55000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                    Node1_P.after(55000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node2_O.after(55000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                    Node2_P.after(55000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node3_O.after(55000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                    Node3_P.after(55000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node4_O.after(55000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                    Node4_P.after(55000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node5_O.after(55000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                    Node5_P.after(55000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node6_O.after(55000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                    Node6_P.after(55000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node7_O.after(55000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                    Node7_P.after(55000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                except Exception:
                                    pass

                                ExplanationLabel.after(55000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                "Therefore Vertex " +min_temp_5+ " is assigned permanent label "+ NameList[min_temp_5]["permanent"]+ " and order label "
                                                                + NameList[min_temp_5]["order"]+"."):ExplanationLabelVariable.set(s))

                                # If the ending vertex has a permanent label, end
                                if "permanent" in NameList[EndingVertex].keys():
                                    ExplanationLabel.after(60000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                        StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                        +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

                                # Otherwise, carry on
                                else:
                                    # Update the values for the temporary labels
                                    for item in NameList.keys():
                                        if item!=min_temp_5:
                                            try:
                                                if NameList[min_temp_5][item]!=0:
                                                    try:
                                                        if int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])> int(NameList[item]["temporary"]):
                                                            pass
                                                        elif int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])< int(NameList[item]["temporary"]):
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                                    except KeyError:
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                            except KeyError:
                                                pass

                                    # Update the labels
                                    try:
                                        Node1_T.after(60000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node2_T.after(60000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node3_T.after(60000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node4_T.after(60000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node5_T.after(60000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node6_T.after(60000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node7_T.after(60000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                    except KeyError:
                                        pass

                                    ExplanationLabel.after(60000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                        "working vertex "+ min_temp_5+"."):ExplanationLabelVariable.set(s))

                                    # Assign the ending vertex labels
                                    for i in NameList.keys():
                                        if i!=StartingVertex and i!=min_temp_5:
                                            NameList[i]["permanent"]=NameList[i]["temporary"]
                                            NameList[EndingVertex]["order"]="7"

                                    # Update the labels
                                    try:
                                        Node1_P.after(65000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                        Node1_O.after(65000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node2_P.after(65000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                        Node2_O.after(65000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node3_P.after(65000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                        Node3_O.after(65000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node4_P.after(65000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                        Node4_O.after(65000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node5_P.after(65000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                        Node5_O.after(65000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node6_P.after(65000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                        Node6_O.after(65000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node7_P.after(65000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                        Node7_O.after(65000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                    except KeyError:
                                        pass

                                    ExplanationLabel.after(65000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                    "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                                    + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                                    ExplanationLabel.after(70000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                        StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                        +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
             



            if len(VerticesList)==8:
            # Only when there are five vertices
                dot1=cv.create_oval(300,100,302,102,activefill="black")
                dot2=cv.create_oval(200,200,202,202,activefill="black")
                dot3=cv.create_oval(200,400,202,402,activefill="black")
                dot4=cv.create_oval(300,500,302,502,activefill="black")
                dot5=cv.create_oval(500,500,502,502,activefill="black")
                dot6=cv.create_oval(600,400,602,402,activefill="black")
                dot7=cv.create_oval(600,200,602,202,activefill="black")
                dot8=cv.create_oval(500,100,502,102,activefill="black")

                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()
                Node6_O_Value=tk.StringVar()
                Node6_P_Value=tk.StringVar()
                Node6_T_Value=tk.StringVar()
                Node7_O_Value=tk.StringVar()
                Node7_P_Value=tk.StringVar()
                Node7_T_Value=tk.StringVar()
                Node8_O_Value=tk.StringVar()
                Node8_P_Value=tk.StringVar()
                Node8_T_Value=tk.StringVar()
                # Three variables that will be changed throughout the program that will appear at the different labels
                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(240,50,width=60,height=20,window=Node1_Name)
                cv.create_window(280,50,width=20,height=20,window=Node1_O)
                cv.create_window(300,50,width=20,height=20,window=Node1_P)
                cv.create_window(290,70,width=40,height=20,window=Node1_T)
                # Creates the labels that holes the variables above
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(120,150,width=60,height=20,window=Node2_Name)
                cv.create_window(160,150,width=20,height=20,window=Node2_O)
                cv.create_window(180,150,width=20,height=20,window=Node2_P)
                cv.create_window(170,170,width=40,height=20,window=Node2_T)
                # Creates the labels that holds the variables above
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(120,350,width=60,height=20,window=Node3_Name)
                cv.create_window(160,350,width=20,height=20,window=Node3_O)
                cv.create_window(180,350,width=20,height=20,window=Node3_P)
                cv.create_window(170,370,width=40,height=20,window=Node3_T)
                # Creates the labels that hold the variables above
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(240,530,width=60,height=20,window=Node4_Name)
                cv.create_window(280,530,width=20,height=20,window=Node4_O)
                cv.create_window(300,530,width=20,height=20,window=Node4_P)
                cv.create_window(290,550,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(460,530,width=30,height=20,window=Node5_Name)
                cv.create_window(500,530,width=20,height=20,window=Node5_O)
                cv.create_window(520,530,width=20,height=20,window=Node5_P)
                cv.create_window(510,550,width=40,height=20,window=Node5_T)
                Node6_Name=tk.Label(cv, text=VerticesList[5], bg="white", justify=tk.RIGHT)
                Node6_O=tk.Label(cv, textvariable=Node6_O_Value, relief=tk.GROOVE )
                Node6_P=tk.Label(cv, textvariable=Node6_P_Value, relief=tk.GROOVE )
                Node6_T=tk.Label(cv, textvariable=Node6_T_Value, relief=tk.GROOVE )
                cv.create_window(625,350,width=30,height=20,window=Node6_Name)
                cv.create_window(640,350,width=20,height=20,window=Node6_O)
                cv.create_window(660,350,width=20,height=20,window=Node6_P)
                cv.create_window(650,370,width=40,height=20,window=Node6_T)
                Node7_Name=tk.Label(cv, text=VerticesList[6], bg="white", justify=tk.RIGHT)
                Node7_O=tk.Label(cv, textvariable=Node7_O_Value, relief=tk.GROOVE )
                Node7_P=tk.Label(cv, textvariable=Node7_P_Value, relief=tk.GROOVE )
                Node7_T=tk.Label(cv, textvariable=Node7_T_Value, relief=tk.GROOVE )
                cv.create_window(590,150,width=30,height=20,window=Node7_Name)
                cv.create_window(630,150,width=20,height=20,window=Node7_O)
                cv.create_window(650,150,width=20,height=20,window=Node7_P)
                cv.create_window(640,170,width=40,height=20,window=Node7_T)
                Node8_Name=tk.Label(cv, text=VerticesList[7], bg="white", justify=tk.RIGHT)
                Node8_O=tk.Label(cv, textvariable=Node8_O_Value, relief=tk.GROOVE )
                Node8_P=tk.Label(cv, textvariable=Node8_P_Value, relief=tk.GROOVE )
                Node8_T=tk.Label(cv, textvariable=Node8_T_Value, relief=tk.GROOVE )
                cv.create_window(460,50,width=30,height=20,window=Node8_Name)
                cv.create_window(500,50,width=20,height=20,window=Node8_O)
                cv.create_window(520,50,width=20,height=20,window=Node8_P)
                cv.create_window(510,70,width=40,height=20,window=Node8_T)
                # Creates the labels that holds the variables above
                line1=cv.create_line(301,101,201,201)
                line2=cv.create_line(301,101,201,401)
                line3=cv.create_line(301,101,301,501)
                line4=cv.create_line(301,101,501,501)
                line5=cv.create_line(301,101,601,401)
                line6=cv.create_line(301,101,601,201)
                line7=cv.create_line(301,101,501,101)
                line8=cv.create_line(201,201,201,401)
                line9=cv.create_line(201,201,301,501)
                line10=cv.create_line(201,201,501,501)
                line11=cv.create_line(201,201,601,401)
                line12=cv.create_line(201,201,601,201)
                line13=cv.create_line(201,201,501,101)
                line14=cv.create_line(201,401,301,501)
                line15=cv.create_line(201,401,501,501)
                line16=cv.create_line(201,401,601,401)
                line17=cv.create_line(201,401,601,201)
                line18=cv.create_line(201,401,501,101)
                line19=cv.create_line(301,501,501,501)
                line20=cv.create_line(301,501,601,401)
                line21=cv.create_line(301,501,601,201)
                line22=cv.create_line(301,501,501,101)
                line23=cv.create_line(501,501,601,401)
                line24=cv.create_line(501,501,601,201)
                line25=cv.create_line(501,501,501,101)
                line26=cv.create_line(601,401,601,201)
                line27=cv.create_line(601,401,501,101)
                line28=cv.create_line(601,201,501,101)
                # Create lines for each edge possible
                if int(LengthList[1])==0:
                    cv.delete(line1)
                else:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(250,150,window=Label1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                else:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(255,240,window=Label2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                else:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(300,280,window=Label3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                else:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(385,270,window=Label4)
                if int(LengthList[5])==0:
                    cv.delete(line5)
                else:
                    Label5=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(450,250,window=Label5)
                if int(LengthList[6])==0:
                    cv.delete(line6)
                else:
                    Label6=tk.Label(cv,text=LengthList[6], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(430,140,window=Label6)
                if int(LengthList[7])==0:
                    cv.delete(line7)
                else:
                    Label7=tk.Label(cv,text=LengthList[7], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(400,100,window=Label7)
                if int(LengthList[10])==0:
                    cv.delete(line8)
                else:
                    Label8=tk.Label(cv,text=LengthList[10], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(200,300,window=Label8)
                if int(LengthList[11])==0:
                    cv.delete(line9)
                else:
                    Label9=tk.Label(cv,text=LengthList[11], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(240,330,window=Label9)
                if int(LengthList[12])==0:
                    cv.delete(line10)
                else:
                    Label10=tk.Label(cv,text=LengthList[12], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(350,350,window=Label10)
                if int(LengthList[13])==0:
                    cv.delete(line11)
                else:
                    Label11=tk.Label(cv,text=LengthList[13], fg="black",bg="white")
                    Label11.pack()
                    cv.create_window(430,315,window=Label11)
                if int(LengthList[14])==0:
                    cv.delete(line12)
                else:
                    Label12=tk.Label(cv,text=LengthList[14], fg="black",bg="white")
                    Label12.pack()
                    cv.create_window(380,200,window=Label12)
                if int(LengthList[15])==0:
                    cv.delete(line13)
                else:
                    Label13=tk.Label(cv,text=LengthList[15], fg="black",bg="white")
                    Label13.pack()
                    cv.create_window(370,142,window=Label13)
                if int(LengthList[19])==0:
                    cv.delete(line14)
                else:
                    Label14=tk.Label(cv,text=LengthList[19], fg="black",bg="white")
                    Label14.pack()
                    cv.create_window(250,450,window=Label14)
                if int(LengthList[20])==0:
                    cv.delete(line15)
                else:
                    Label15=tk.Label(cv,text=LengthList[20], fg="black",bg="white")
                    Label15.pack()
                    cv.create_window(370,460,window=Label15)
                if int(LengthList[21])==0:
                    cv.delete(line16)
                else:
                    Label16=tk.Label(cv,text=LengthList[21], fg="black",bg="white")
                    Label16.pack()
                    cv.create_window(420,400,window=Label16)
                if int(LengthList[22])==0:
                    cv.delete(line17)
                else:
                    Label17=tk.Label(cv,text=LengthList[22], fg="black",bg="white")
                    Label17.pack()
                    cv.create_window(430,285,window=Label17)
                if int(LengthList[23])==0:
                    cv.delete(line18)
                else:
                    Label18=tk.Label(cv,text=LengthList[23], fg="black",bg="white")
                    Label18.pack()
                    cv.create_window(350,250,window=Label18)
                if int(LengthList[28])==0:
                    cv.delete(line19)
                else:
                    Label19=tk.Label(cv,text=LengthList[28], fg="black",bg="white")
                    Label19.pack()
                    cv.create_window(400,500,window=Label19)
                if int(LengthList[29])==0:
                    cv.delete(line20)
                else:
                    Label20=tk.Label(cv,text=LengthList[29], fg="black",bg="white")
                    Label20.pack()
                    cv.create_window(430,460,window=Label20)
                if int(LengthList[30])==0:
                    cv.delete(line21)
                else:
                    Label21=tk.Label(cv,text=LengthList[30], fg="black",bg="white")
                    Label21.pack()
                    cv.create_window(450,350,window=Label21)
                if int(LengthList[31])==0:
                    cv.delete(line22)
                else:
                    Label22=tk.Label(cv,text=LengthList[31], fg="black",bg="white")
                    Label22.pack()
                    cv.create_window(415,270,window=Label22)
                if int(LengthList[37])==0:
                    cv.delete(line23)
                else:
                    Label23=tk.Label(cv,text=LengthList[37], fg="black",bg="white")
                    Label23.pack()
                    cv.create_window(550,450,window=Label23)
                if int(LengthList[38])==0:
                    cv.delete(line24)
                else:
                    Label24=tk.Label(cv,text=LengthList[38], fg="black",bg="white")
                    Label24.pack()
                    cv.create_window(560,330,window=Label24)
                if int(LengthList[39])==0:
                    cv.delete(line25)
                else:
                    Label25=tk.Label(cv,text=LengthList[39], fg="black",bg="white")
                    Label25.pack()
                    cv.create_window(500,280,window=Label25)
                if int(LengthList[46])==0:
                    cv.delete(line26)
                else:
                    Label26=tk.Label(cv,text=LengthList[46], fg="black",bg="white")
                    Label26.pack()
                    cv.create_window(600,300,window=Label26)
                if int(LengthList[47])==0:
                    cv.delete(line27)
                else:
                    Label27=tk.Label(cv,text=LengthList[47], fg="black",bg="white")
                    Label27.pack()
                    cv.create_window(560,270,window=Label27)
                if int(LengthList[55])==0:
                    cv.delete(line28)
                else:
                    Label28=tk.Label(cv,text=LengthList[55], fg="black",bg="white")
                    Label28.pack()
                    cv.create_window(550,150,window=Label28)

                ExplanationLabelVariable.set("Demonstration Begin")

                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                # Assign permanent and order labels
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))
                if StartingVertex==VerticesList[5]:
                    Node6_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node6_O_Value. set(s))
                    Node6_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node6_P_Value.set(s))
                if StartingVertex==VerticesList[6]:
                    Node7_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node7_O_Value. set(s))
                    Node7_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node7_P_Value.set(s))
                if StartingVertex==VerticesList[7]:
                    Node8_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node8_O_Value. set(s))
                    Node8_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node8_P_Value.set(s))

                # Update the order and permanent labels of the starting vertex
                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))


                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass
                # Assign temporary labels to the ones eligible
                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node6_T.after(10000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node7_T.after(10000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node8_T.after(10000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                except KeyError:
                    pass
                # Update all the temporary labels
                del NameList[StartingVertex]
                # Delete the label that we finished working with
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                print TempDict1
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1
                # Get the vertex which has the smallest temporary label
                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"
                # Make that label permanent and give it order 2
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node6_O.after(15000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                    Node6_P.after(15000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node7_O.after(15000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                    Node7_P.after(15000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node8_O.after(15000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                    Node8_P.after(15000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                except Exception:
                    pass
                # Update all the order and permanent labels
                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                else:
                # Otherwise, carry on
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass
                    # Update the values for the temporary labels if possible
                    print NameList
                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node6_T.after(20000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node7_T.after(20000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node8_T.after(20000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                    except KeyError:
                        pass
                    # Update all the temporary labels
                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    print min_temp_2
                    # Get the vertex which has the smallest temporary label
                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"
                    # Make that label permanent and give it order 3
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node6_O.after(25000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                        Node6_P.after(25000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node7_O.after(25000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                        Node7_P.after(25000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node8_O.after(25000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                        Node8_P.after(25000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                    except Exception:
                        pass
                    # Update all the order and temporary labels
                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                    # If the permanent lable is made to the ending vertex, end everything
                    else:
                    # Otherwise, carry on
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass
                        # Update the values of the temporary labels if eligible
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node7_T.after(30000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node8_T.after(30000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                        except KeyError:
                            pass
                        # Update all the temporary labels
                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        del NameList[min_temp_2]
                        # Delete the vertex that we finished working with

                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3
                        # Get the vertex which has the smallest temporary label
                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"
                        # Make that label permanent and give it order 2

                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node6_O.after(35000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                            Node6_P.after(35000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node7_O.after(35000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                            Node7_P.after(35000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node8_O.after(35000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                            Node8_P.after(35000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                        except Exception:
                            pass
                        # Update all the order and permanent labels
                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                        else:
                        # Otherwise, carry on
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass
                            #Update the temporary label values if eligible
                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node6_T.after(40000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node7_T.after(40000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node8_T.after(40000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                            except KeyError:
                                pass
                            # Update all the temporary labels
                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            del NameList[min_temp_3]
                            # Delete the vertex that we finished working with

                            TempDict4={}
                            for i in NameList.keys():
                                for j in NameList[i].keys():
                                    if j=="temporary":
                                        TempDict4[i]=int(NameList[i][j])

                            min_temp_4= min(TempDict4,key=TempDict4.get)
                            print min_temp_4
                            # Get the vertex which has the smallest temporary label
                            NameList[min_temp_4]["permanent"]=NameList[min_temp_4]["temporary"]
                            NameList[min_temp_4]["order"]="5"
                            # Make that label permanent and give it order 2

                            try:
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node6_O.after(45000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                Node6_P.after(45000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node7_O.after(45000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                Node7_P.after(45000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node8_O.after(45000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                Node8_P.after(45000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                            except Exception:
                                pass
                            # Update all the order and permanent labels
                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +min_temp_4+ " is assigned permanent label "+ NameList[min_temp_4]["permanent"]+ " and order label "
                                                            + NameList[min_temp_4]["order"]+"."):ExplanationLabelVariable.set(s))
                            if "permanent" in NameList[EndingVertex].keys():
                                ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                            else:
                            # Otherwise, carry on
                                for item in NameList.keys():
                                    if item!=min_temp_4:
                                        try:
                                            if NameList[min_temp_4][item]!=0:
                                                try:
                                                    if int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])> int(NameList[item]["temporary"]):
                                                        pass
                                                    elif int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])< int(NameList[item]["temporary"]):
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                                except KeyError:
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                        except KeyError:
                                            pass
                                #Update the temporary label values if eligible
                                try:
                                    Node1_T.after(50000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_T.after(50000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_T.after(50000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_T.after(50000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_T.after(50000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_T.after(50000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node7_T.after(50000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node8_T.after(50000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                except KeyError:
                                    pass
                                # Update all the temporary labels
                                ExplanationLabel.after(50000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                    "working vertex "+ min_temp_4+"."):ExplanationLabelVariable.set(s))

                                del NameList[min_temp_4]
                                # Delete the vertex that we finished working with

                                TempDict5={}
                                for i in NameList.keys():
                                    for j in NameList[i].keys():
                                        if j=="temporary":
                                            TempDict5[i]=int(NameList[i][j])

                                min_temp_5= min(TempDict5,key=TempDict5.get)
                                print min_temp_5
                                # Get the vertex which has the smallest temporary label
                                NameList[min_temp_5]["permanent"]=NameList[min_temp_5]["temporary"]
                                NameList[min_temp_5]["order"]="6"
                                # Make that label permanent and give it order 2

                                try:
                                    Node1_O.after(55000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                    Node1_P.after(55000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node2_O.after(55000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                    Node2_P.after(55000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node3_O.after(55000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                    Node3_P.after(55000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node4_O.after(55000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                    Node4_P.after(55000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node5_O.after(55000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                    Node5_P.after(55000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node6_O.after(55000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                    Node6_P.after(55000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node7_O.after(55000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                    Node7_P.after(55000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node8_O.after(55000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                    Node8_P.after(55000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                except Exception:
                                    pass
                                # Update all the order and permanent labels
                                ExplanationLabel.after(55000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                "Therefore Vertex " +min_temp_5+ " is assigned permanent label "+ NameList[min_temp_5]["permanent"]+ " and order label "
                                                                + NameList[min_temp_5]["order"]+"."):ExplanationLabelVariable.set(s))
                                if "permanent" in NameList[EndingVertex].keys():
                                    ExplanationLabel.after(60000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                        StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                        +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                else:
                                    for item in NameList.keys():
                                        if item!=min_temp_5:
                                            try:
                                                if NameList[min_temp_5][item]!=0:
                                                    try:
                                                        if int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])> int(NameList[item]["temporary"]):
                                                            pass
                                                        elif int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])< int(NameList[item]["temporary"]):
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                                    except KeyError:
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                            except KeyError:
                                                pass
                                    #Update the temporary label values if eligible
                                    try:
                                        Node1_T.after(60000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node2_T.after(60000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node3_T.after(60000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node4_T.after(60000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node5_T.after(60000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node6_T.after(60000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node7_T.after(60000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node8_T.after(60000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    # Update all the temporary labels
                                    ExplanationLabel.after(60000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                        "working vertex "+ min_temp_5+"."):ExplanationLabelVariable.set(s))
                                    del NameList[min_temp_5]
                                    # Delete the vertex that we finished working with

                                    TempDict6={}
                                    for i in NameList.keys():
                                        for j in NameList[i].keys():
                                            if j=="temporary":
                                                TempDict6[i]=int(NameList[i][j])

                                    min_temp_6= min(TempDict6,key=TempDict6.get)
                                    print min_temp_6
                                    # Get the vertex which has the smallest temporary label
                                    NameList[min_temp_6]["permanent"]=NameList[min_temp_6]["temporary"]
                                    NameList[min_temp_6]["order"]="7"
                                    # Make that label permanent and give it order 2

                                    try:
                                        Node1_O.after(65000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                        Node1_P.after(65000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node2_O.after(65000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                        Node2_P.after(65000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node3_O.after(65000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                        Node3_P.after(65000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node4_O.after(65000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                        Node4_P.after(65000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node5_O.after(65000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                        Node5_P.after(65000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node6_O.after(65000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                        Node6_P.after(65000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node7_O.after(65000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                        Node7_P.after(65000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node8_O.after(65000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                        Node8_P.after(65000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                    except Exception:
                                        pass
                                    # Update all the order and permanent labels
                                    ExplanationLabel.after(65000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                    "Therefore Vertex " +min_temp_6+ " is assigned permanent label "+ NameList[min_temp_6]["permanent"]+ " and order label "
                                                                    + NameList[min_temp_6]["order"]+"."):ExplanationLabelVariable.set(s))
                                    if "permanent" in NameList[EndingVertex].keys():
                                        ExplanationLabel.after(70000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                    else:
                                        for item in NameList.keys():
                                            if item!=min_temp_6:
                                                try:
                                                    if NameList[min_temp_6][item]!=0:
                                                        try:
                                                            if int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])> int(NameList[item]["temporary"]):
                                                                pass
                                                            elif int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])< int(NameList[item]["temporary"]):
                                                                NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                        except KeyError:
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                except KeyError:
                                                    pass
                                        #Update the temporary label values if eligible
                                        try:
                                            Node1_T.after(70000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node2_T.after(70000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node3_T.after(70000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node4_T.after(70000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node5_T.after(70000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node6_T.after(70000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node7_T.after(70000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node8_T.after(70000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        # Update all the temporary labels
                                        ExplanationLabel.after(70000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                            "working vertex "+ min_temp_6+"."):ExplanationLabelVariable.set(s))

                                        for i in NameList.keys():
                                            if i!=StartingVertex and i!=min_temp_6:
                                                NameList[i]["permanent"]=NameList[i]["temporary"]
                                                NameList[EndingVertex]["order"]="8"
                                        # Give the ending vertex order and temporary labels
                                        try:
                                            Node1_P.after(75000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                            Node1_O.after(75000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node2_P.after(75000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                            Node2_O.after(75000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node3_P.after(75000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                            Node3_O.after(75000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node4_P.after(75000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                            Node4_O.after(75000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node5_P.after(75000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                            Node5_O.after(75000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node6_P.after(75000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                            Node6_O.after(75000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node7_P.after(75000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                            Node7_O.after(75000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node8_P.after(75000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                            Node8_O.after(75000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                        except KeyError:
                                            pass
                                        # Update all the permanent and order labels
                                        ExplanationLabel.after(75000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                        "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                                        + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                                        ExplanationLabel.after(80000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))



            if len(VerticesList)==9:
                # Only when there are five vertices
                dot1=cv.create_oval(400,100,402,102,activefill="black")
                dot2=cv.create_oval(250,150,252,152,activefill="black")
                dot3=cv.create_oval(200,300,202,302,activefill="black")
                dot4=cv.create_oval(240,425,242,427,activefill="black")
                dot5=cv.create_oval(325,500,327,502,activefill="black")
                dot6=cv.create_oval(475,500,477,502,activefill="black")
                dot7=cv.create_oval(560,425,562,427,activefill="black")
                dot8=cv.create_oval(600,300,602,302,activefill="black")
                dot9=cv.create_oval(550,150,552,152,activefill="black")

                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()
                Node6_O_Value=tk.StringVar()
                Node6_P_Value=tk.StringVar()
                Node6_T_Value=tk.StringVar()
                Node7_O_Value=tk.StringVar()
                Node7_P_Value=tk.StringVar()
                Node7_T_Value=tk.StringVar()
                Node8_O_Value=tk.StringVar()
                Node8_P_Value=tk.StringVar()
                Node8_T_Value=tk.StringVar()
                Node9_O_Value=tk.StringVar()
                Node9_P_Value=tk.StringVar()
                Node9_T_Value=tk.StringVar()
                # Three variables that will be changed throughout the program that will appear at the different labels

                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(340,50,width=60,height=20,window=Node1_Name)
                cv.create_window(380,50,width=20,height=20,window=Node1_O)
                cv.create_window(400,50,width=20,height=20,window=Node1_P)
                cv.create_window(390,70,width=40,height=20,window=Node1_T)
                # Creates the labels that holes the variables above
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(160,130,width=60,height=20,window=Node2_Name)
                cv.create_window(200,130,width=20,height=20,window=Node2_O)
                cv.create_window(220,130,width=20,height=20,window=Node2_P)
                cv.create_window(210,150,width=40,height=20,window=Node2_T)
                # Creates the labels that holds the variables above
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(110,280,width=60,height=20,window=Node3_Name)
                cv.create_window(150,280,width=20,height=20,window=Node3_O)
                cv.create_window(170,280,width=20,height=20,window=Node3_P)
                cv.create_window(160,300,width=40,height=20,window=Node3_T)
                # Creates the labels that hold the variables above
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(150,405,width=60,height=20,window=Node4_Name)
                cv.create_window(190,405,width=20,height=20,window=Node4_O)
                cv.create_window(210,405,width=20,height=20,window=Node4_P)
                cv.create_window(200,425,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(240,530,width=30,height=20,window=Node5_Name)
                cv.create_window(280,530,width=20,height=20,window=Node5_O)
                cv.create_window(300,530,width=20,height=20,window=Node5_P)
                cv.create_window(290,550,width=40,height=20,window=Node5_T)
                Node6_Name=tk.Label(cv, text=VerticesList[5], bg="white", justify=tk.RIGHT)
                Node6_O=tk.Label(cv, textvariable=Node6_O_Value, relief=tk.GROOVE )
                Node6_P=tk.Label(cv, textvariable=Node6_P_Value, relief=tk.GROOVE )
                Node6_T=tk.Label(cv, textvariable=Node6_T_Value, relief=tk.GROOVE )
                cv.create_window(485,530,width=30,height=20,window=Node6_Name)
                cv.create_window(510,530,width=20,height=20,window=Node6_O)
                cv.create_window(530,530,width=20,height=20,window=Node6_P)
                cv.create_window(520,550,width=40,height=20,window=Node6_T)
                Node7_Name=tk.Label(cv, text=VerticesList[6], bg="white", justify=tk.RIGHT)
                Node7_O=tk.Label(cv, textvariable=Node7_O_Value, relief=tk.GROOVE )
                Node7_P=tk.Label(cv, textvariable=Node7_P_Value, relief=tk.GROOVE )
                Node7_T=tk.Label(cv, textvariable=Node7_T_Value, relief=tk.GROOVE )
                cv.create_window(605,405,width=30,height=20,window=Node7_Name)
                cv.create_window(630,405,width=20,height=20,window=Node7_O)
                cv.create_window(650,405,width=20,height=20,window=Node7_P)
                cv.create_window(640,425,width=40,height=20,window=Node7_T)
                Node8_Name=tk.Label(cv, text=VerticesList[7], bg="white", justify=tk.RIGHT)
                Node8_O=tk.Label(cv, textvariable=Node8_O_Value, relief=tk.GROOVE )
                Node8_P=tk.Label(cv, textvariable=Node8_P_Value, relief=tk.GROOVE )
                Node8_T=tk.Label(cv, textvariable=Node8_T_Value, relief=tk.GROOVE )
                cv.create_window(635,280,width=30,height=20,window=Node8_Name)
                cv.create_window(660,280,width=20,height=20,window=Node8_O)
                cv.create_window(680,280,width=20,height=20,window=Node8_P)
                cv.create_window(670,300,width=40,height=20,window=Node8_T)
                Node9_Name=tk.Label(cv, text=VerticesList[8], bg="white", justify=tk.RIGHT)
                Node9_O=tk.Label(cv, textvariable=Node9_O_Value, relief=tk.GROOVE )
                Node9_P=tk.Label(cv, textvariable=Node9_P_Value, relief=tk.GROOVE )
                Node9_T=tk.Label(cv, textvariable=Node9_T_Value, relief=tk.GROOVE )
                cv.create_window(555,130,width=30,height=20,window=Node9_Name)
                cv.create_window(580,130,width=20,height=20,window=Node9_O)
                cv.create_window(600,130,width=20,height=20,window=Node9_P)
                cv.create_window(590,150,width=40,height=20,window=Node9_T)
                # Creates the labels that holds the variables above
                line1=cv.create_line(401,101,251,151)
                line2=cv.create_line(401,101,201,301)
                line3=cv.create_line(401,101,241,426)
                line4=cv.create_line(401,101,326,501)
                line5=cv.create_line(401,101,476,501)
                line6=cv.create_line(401,101,561,426)
                line7=cv.create_line(401,101,601,301)
                line8=cv.create_line(401,101,551,151)
                line9=cv.create_line(251,151,201,301)
                line10=cv.create_line(251,151,241,426)
                line11=cv.create_line(251,151,326,501)
                line12=cv.create_line(251,151,476,501)
                line13=cv.create_line(251,151,561,426)
                line14=cv.create_line(251,151,601,301)
                line15=cv.create_line(251,151,551,151)
                line16=cv.create_line(201,301,241,426)
                line17=cv.create_line(201,301,326,501)
                line18=cv.create_line(201,301,476,501)
                line19=cv.create_line(201,301,561,426)
                line20=cv.create_line(201,301,601,301)
                line21=cv.create_line(201,301,551,151)
                line22=cv.create_line(241,426,326,501)
                line23=cv.create_line(241,426,476,501)
                line24=cv.create_line(241,426,561,426)
                line25=cv.create_line(241,426,601,301)
                line26=cv.create_line(241,426,551,151)
                line27=cv.create_line(326,501,476,501)
                line28=cv.create_line(326,501,561,426)
                line29=cv.create_line(326,501,601,301)
                line30=cv.create_line(326,501,551,151)
                line31=cv.create_line(476,501,561,426)
                line32=cv.create_line(476,501,601,301)
                line33=cv.create_line(476,501,551,151)
                line34=cv.create_line(561,426,601,301)
                line35=cv.create_line(561,426,551,151)
                line36=cv.create_line(601,301,551,151)
                # Create lines for each edge possible

                if int(LengthList[1])==0:
                    cv.delete(line1)
                else:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(325,125,window=Label1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                else:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(295,203,window=Label2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                else:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(315,272,window=Label3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                else:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(365,285,window=Label4)
                if int(LengthList[5])==0:
                    cv.delete(line5)
                else:
                    Label5=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(440,285,window=Label5)
                if int(LengthList[6])==0:
                    cv.delete(line6)
                else:
                    Label6=tk.Label(cv,text=LengthList[6], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(490,277,window=Label6)
                if int(LengthList[7])==0:
                    cv.delete(line7)
                else:
                    Label7=tk.Label(cv,text=LengthList[7], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(490,190,window=Label7)
                if int(LengthList[8])==0:
                    cv.delete(line8)
                else:
                    Label8=tk.Label(cv,text=LengthList[8], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(475,125,window=Label8)
                if int(LengthList[11])==0:
                    cv.delete(line9)
                else:
                    Label9=tk.Label(cv,text=LengthList[11], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(225,225,window=Label9)
                if int(LengthList[12])==0:
                    cv.delete(line10)
                else:
                    Label10=tk.Label(cv,text=LengthList[12], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(245,292,window=Label10)
                if int(LengthList[13])==0:
                    cv.delete(line11)
                else:
                    Label11=tk.Label(cv,text=LengthList[13], fg="black",bg="white")
                    Label11.pack()
                    cv.create_window(297,355,window=Label11)
                if int(LengthList[14])==0:
                    cv.delete(line12)
                else:
                    Label12=tk.Label(cv,text=LengthList[14], fg="black",bg="white")
                    Label12.pack()
                    cv.create_window(372,335,window=Label12)
                if int(LengthList[15])==0:
                    cv.delete(line13)
                else:
                    Label13=tk.Label(cv,text=LengthList[15], fg="black",bg="white")
                    Label13.pack()
                    cv.create_window(385,267,window=Label13)
                if int(LengthList[16])==0:
                    cv.delete(line14)
                else:
                    Label14=tk.Label(cv,text=LengthList[16], fg="black",bg="white")
                    Label14.pack()
                    cv.create_window(435,230,window=Label14)
                if int(LengthList[17])==0:
                    cv.delete(line15)
                else:
                    Label15=tk.Label(cv,text=LengthList[17], fg="black",bg="white")
                    Label15.pack()
                    cv.create_window(400,150,window=Label15)
                if int(LengthList[21])==0:
                    cv.delete(line16)
                else:
                    Label16=tk.Label(cv,text=LengthList[21], fg="black",bg="white")
                    Label16.pack()
                    cv.create_window(220,362,window=Label16)
                if int(LengthList[22])==0:
                    cv.delete(line17)
                else:
                    Label17=tk.Label(cv,text=LengthList[22], fg="black",bg="white")
                    Label17.pack()
                    cv.create_window(252,380,window=Label17)
                if int(LengthList[23])==0:
                    cv.delete(line18)
                else:
                    Label18=tk.Label(cv,text=LengthList[23], fg="black",bg="white")
                    Label18.pack()
                    cv.create_window(315,385,window=Label18)
                if int(LengthList[24])==0:
                    cv.delete(line19)
                else:
                    Label19=tk.Label(cv,text=LengthList[24], fg="black",bg="white")
                    Label19.pack()
                    cv.create_window(370,357,window=Label19)
                if int(LengthList[25])==0:
                    cv.delete(line20)
                else:
                    Label20=tk.Label(cv,text=LengthList[25], fg="black",bg="white")
                    Label20.pack()
                    cv.create_window(400,300,window=Label20)
                if int(LengthList[26])==0:
                    cv.delete(line21)
                else:
                    Label21=tk.Label(cv,text=LengthList[26], fg="black",bg="white")
                    Label21.pack()
                    cv.create_window(365,230,window=Label21)
                if int(LengthList[31])==0:
                    cv.delete(line22)
                else:
                    Label22=tk.Label(cv,text=LengthList[31], fg="black",bg="white")
                    Label22.pack()
                    cv.create_window(282,462,window=Label22)
                if int(LengthList[32])==0:
                    cv.delete(line23)
                else:
                    Label23=tk.Label(cv,text=LengthList[32], fg="black",bg="white")
                    Label23.pack()
                    cv.create_window(360,467,window=Label23)
                if int(LengthList[33])==0:
                    cv.delete(line24)
                else:
                    Label24=tk.Label(cv,text=LengthList[33], fg="black",bg="white")
                    Label24.pack()
                    cv.create_window(400,425,window=Label24)
                if int(LengthList[34])==0:
                    cv.delete(line25)
                else:
                    Label25=tk.Label(cv,text=LengthList[34], fg="black",bg="white")
                    Label25.pack()
                    cv.create_window(432,357,window=Label25)
                if int(LengthList[35])==0:
                    cv.delete(line26)
                else:
                    Label26=tk.Label(cv,text=LengthList[35], fg="black",bg="white")
                    Label26.pack()
                    cv.create_window(415,267,window=Label26)
                if int(LengthList[41])==0:
                    cv.delete(line27)
                else:
                    Label27=tk.Label(cv,text=LengthList[41], fg="black",bg="white")
                    Label27.pack()
                    cv.create_window(400,500,window=Label27)
                if int(LengthList[42])==0:
                    cv.delete(line28)
                else:
                    Label28=tk.Label(cv,text=LengthList[42], fg="black",bg="white")
                    Label28.pack()
                    cv.create_window(440,462,window=Label28)
                if int(LengthList[43])==0:
                    cv.delete(line29)
                else:
                    Label29=tk.Label(cv,text=LengthList[43], fg="black",bg="white")
                    Label29.pack()
                    cv.create_window(482,385,window=Label29)
                if int(LengthList[44])==0:
                    cv.delete(line30)
                else:
                    Label30=tk.Label(cv,text=LengthList[44], fg="black",bg="white")
                    Label30.pack()
                    cv.create_window(430,335,window=Label30)
                if int(LengthList[51])==0:
                    cv.delete(line31)
                else:
                    Label31=tk.Label(cv,text=LengthList[51], fg="black",bg="white")
                    Label31.pack()
                    cv.create_window(517,462,window=Label31)
                if int(LengthList[52])==0:
                    cv.delete(line32)
                else:
                    Label32=tk.Label(cv,text=LengthList[52], fg="black",bg="white")
                    Label32.pack()
                    cv.create_window(552,380,window=Label32)
                if int(LengthList[53])==0:
                    cv.delete(line33)
                else:
                    Label33=tk.Label(cv,text=LengthList[53], fg="black",bg="white")
                    Label33.pack()
                    cv.create_window(507,348,window=Label33)
                if int(LengthList[61])==0:
                    cv.delete(line34)
                else:
                    Label34=tk.Label(cv,text=LengthList[61], fg="black",bg="white")
                    Label34.pack()
                    cv.create_window(580,362,window=Label34)
                if int(LengthList[62])==0:
                    cv.delete(line35)
                else:
                    Label35=tk.Label(cv,text=LengthList[62], fg="black",bg="white")
                    Label35.pack()
                    cv.create_window(555,292,window=Label35)
                if int(LengthList[71])==0:
                    cv.delete(line36)
                else:
                    Label36=tk.Label(cv,text=LengthList[71], fg="black",bg="white")
                    Label36.pack()
                    cv.create_window(575,225,window=Label36)

                ExplanationLabelVariable.set("Demonstration Begin")

                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                # Assign permanent and order labels
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))
                if StartingVertex==VerticesList[5]:
                    Node6_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node6_O_Value. set(s))
                    Node6_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node6_P_Value.set(s))
                if StartingVertex==VerticesList[6]:
                    Node7_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node7_O_Value. set(s))
                    Node7_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node7_P_Value.set(s))
                if StartingVertex==VerticesList[7]:
                    Node8_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node8_O_Value. set(s))
                    Node8_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node8_P_Value.set(s))
                if StartingVertex==VerticesList[8]:
                    Node9_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node9_O_Value. set(s))
                    Node9_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node9_P_Value.set(s))


                # Update the order and permanent labels of the starting vertex
                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))


                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass
                # Assign temporary labels to the ones eligible
                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node6_T.after(10000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node7_T.after(10000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node8_T.after(10000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node9_T.after(10000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                except KeyError:
                    pass
                # Update all the temporary labels
                del NameList[StartingVertex]
                # Delete the label that we finished working with
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                print TempDict1
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1
                # Get the vertex which has the smallest temporary label
                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"
                # Make that label permanent and give it order 2
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node6_O.after(15000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                    Node6_P.after(15000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node7_O.after(15000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                    Node7_P.after(15000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node8_O.after(15000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                    Node8_P.after(15000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node9_O.after(15000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                    Node9_P.after(15000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                except Exception:
                    pass
                # Update all the order and permanent labels
                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                else:
                # Otherwise, carry on
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass
                    # Update the values for the temporary labels if possible
                    print NameList
                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node6_T.after(20000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node7_T.after(20000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node8_T.after(20000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node9_T.after(20000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                    except KeyError:
                        pass
                    # Update all the temporary labels
                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    print min_temp_2
                    # Get the vertex which has the smallest temporary label
                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"
                    # Make that label permanent and give it order 3
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node6_O.after(25000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                        Node6_P.after(25000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node7_O.after(25000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                        Node7_P.after(25000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node8_O.after(25000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                        Node8_P.after(25000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node9_O.after(25000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                        Node9_P.after(25000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                    except Exception:
                        pass
                    # Update all the order and temporary labels
                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                    # If the permanent lable is made to the ending vertex, end everything
                    else:
                    # Otherwise, carry on
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass
                        # Update the values of the temporary labels if eligible
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node7_T.after(30000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node8_T.after(30000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node9_T.after(30000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                        except KeyError:
                            pass
                        # Update all the temporary labels
                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        del NameList[min_temp_2]
                        # Delete the vertex that we finished working with

                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3
                        # Get the vertex which has the smallest temporary label
                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"
                        # Make that label permanent and give it order 2

                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node6_O.after(35000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                            Node6_P.after(35000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node7_O.after(35000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                            Node7_P.after(35000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node8_O.after(35000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                            Node8_P.after(35000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node9_O.after(35000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                            Node9_P.after(35000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                        except Exception:
                            pass
                        # Update all the order and permanent labels
                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                        else:
                        # Otherwise, carry on
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass
                            #Update the temporary label values if eligible
                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node6_T.after(40000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node7_T.after(40000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node8_T.after(40000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node9_T.after(40000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                            except KeyError:
                                pass
                            # Update all the temporary labels
                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            del NameList[min_temp_3]
                            # Delete the vertex that we finished working with

                            TempDict4={}
                            for i in NameList.keys():
                                for j in NameList[i].keys():
                                    if j=="temporary":
                                        TempDict4[i]=int(NameList[i][j])

                            min_temp_4= min(TempDict4,key=TempDict4.get)
                            print min_temp_4
                            # Get the vertex which has the smallest temporary label
                            NameList[min_temp_4]["permanent"]=NameList[min_temp_4]["temporary"]
                            NameList[min_temp_4]["order"]="5"
                            # Make that label permanent and give it order 2

                            try:
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node6_O.after(45000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                Node6_P.after(45000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node7_O.after(45000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                Node7_P.after(45000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node8_O.after(45000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                Node8_P.after(45000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node9_O.after(45000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                Node9_P.after(45000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                            except Exception:
                                pass
                            # Update all the order and permanent labels
                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +min_temp_4+ " is assigned permanent label "+ NameList[min_temp_4]["permanent"]+ " and order label "
                                                            + NameList[min_temp_4]["order"]+"."):ExplanationLabelVariable.set(s))
                            if "permanent" in NameList[EndingVertex].keys():
                                ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                            else:
                            # Otherwise, carry on
                                for item in NameList.keys():
                                    if item!=min_temp_4:
                                        try:
                                            if NameList[min_temp_4][item]!=0:
                                                try:
                                                    if int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])> int(NameList[item]["temporary"]):
                                                        pass
                                                    elif int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])< int(NameList[item]["temporary"]):
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                                except KeyError:
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                        except KeyError:
                                            pass
                                #Update the temporary label values if eligible
                                try:
                                    Node1_T.after(50000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_T.after(50000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_T.after(50000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_T.after(50000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_T.after(50000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_T.after(50000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node7_T.after(50000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node8_T.after(50000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node9_T.after(50000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                except KeyError:
                                    pass
                                # Update all the temporary labels
                                ExplanationLabel.after(50000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                    "working vertex "+ min_temp_4+"."):ExplanationLabelVariable.set(s))

                                del NameList[min_temp_4]
                                # Delete the vertex that we finished working with

                                TempDict5={}
                                for i in NameList.keys():
                                    for j in NameList[i].keys():
                                        if j=="temporary":
                                            TempDict5[i]=int(NameList[i][j])

                                min_temp_5= min(TempDict5,key=TempDict5.get)
                                print min_temp_5
                                # Get the vertex which has the smallest temporary label
                                NameList[min_temp_5]["permanent"]=NameList[min_temp_5]["temporary"]
                                NameList[min_temp_5]["order"]="6"
                                # Make that label permanent and give it order 2

                                try:
                                    Node1_O.after(55000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                    Node1_P.after(55000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node2_O.after(55000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                    Node2_P.after(55000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node3_O.after(55000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                    Node3_P.after(55000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node4_O.after(55000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                    Node4_P.after(55000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node5_O.after(55000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                    Node5_P.after(55000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node6_O.after(55000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                    Node6_P.after(55000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node7_O.after(55000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                    Node7_P.after(55000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node8_O.after(55000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                    Node8_P.after(55000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node9_O.after(55000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                    Node9_P.after(55000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                except Exception:
                                    pass

                                # Update all the order and permanent labels
                                ExplanationLabel.after(55000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                "Therefore Vertex " +min_temp_5+ " is assigned permanent label "+ NameList[min_temp_5]["permanent"]+ " and order label "
                                                                + NameList[min_temp_5]["order"]+"."):ExplanationLabelVariable.set(s))
                                if "permanent" in NameList[EndingVertex].keys():
                                    ExplanationLabel.after(60000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                        StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                        +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                else:
                                    for item in NameList.keys():
                                        if item!=min_temp_5:
                                            try:
                                                if NameList[min_temp_5][item]!=0:
                                                    try:
                                                        if int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])> int(NameList[item]["temporary"]):
                                                            pass
                                                        elif int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])< int(NameList[item]["temporary"]):
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                                    except KeyError:
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                            except KeyError:
                                                pass
                                    #Update the temporary label values if eligible
                                    try:
                                        Node1_T.after(60000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node2_T.after(60000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node3_T.after(60000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node4_T.after(60000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node5_T.after(60000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node6_T.after(60000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node7_T.after(60000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node8_T.after(60000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node9_T.after(60000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    # Update all the temporary labels
                                    ExplanationLabel.after(60000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                        "working vertex "+ min_temp_5+"."):ExplanationLabelVariable.set(s))
                                    del NameList[min_temp_5]
                                    # Delete the vertex that we finished working with

                                    TempDict6={}
                                    for i in NameList.keys():
                                        for j in NameList[i].keys():
                                            if j=="temporary":
                                                TempDict6[i]=int(NameList[i][j])

                                    min_temp_6= min(TempDict6,key=TempDict6.get)
                                    print min_temp_6
                                    # Get the vertex which has the smallest temporary label
                                    NameList[min_temp_6]["permanent"]=NameList[min_temp_6]["temporary"]
                                    NameList[min_temp_6]["order"]="7"
                                    # Make that label permanent and give it order 2

                                    try:
                                        Node1_O.after(65000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                        Node1_P.after(65000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node2_O.after(65000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                        Node2_P.after(65000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node3_O.after(65000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                        Node3_P.after(65000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node4_O.after(65000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                        Node4_P.after(65000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node5_O.after(65000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                        Node5_P.after(65000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node6_O.after(65000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                        Node6_P.after(65000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node7_O.after(65000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                        Node7_P.after(65000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node8_O.after(65000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                        Node8_P.after(65000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node9_O.after(65000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                        Node9_P.after(65000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                    except Exception:
                                        pass
                                    # Update all the order and permanent labels
                                    ExplanationLabel.after(65000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                    "Therefore Vertex " +min_temp_6+ " is assigned permanent label "+ NameList[min_temp_6]["permanent"]+ " and order label "
                                                                    + NameList[min_temp_6]["order"]+"."):ExplanationLabelVariable.set(s))
                                    if "permanent" in NameList[EndingVertex].keys():
                                        ExplanationLabel.after(70000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                    else:
                                        for item in NameList.keys():
                                            if item!=min_temp_6:
                                                try:
                                                    if NameList[min_temp_6][item]!=0:
                                                        try:
                                                            if int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])> int(NameList[item]["temporary"]):
                                                                pass
                                                            elif int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])< int(NameList[item]["temporary"]):
                                                                NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                        except KeyError:
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                except KeyError:
                                                    pass
                                        #Update the temporary label values if eligible
                                        try:
                                            Node1_T.after(70000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node2_T.after(70000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node3_T.after(70000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node4_T.after(70000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node5_T.after(70000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node6_T.after(70000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node7_T.after(70000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node8_T.after(70000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node9_T.after(70000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        # Update all the temporary labels
                                        ExplanationLabel.after(70000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                            "working vertex "+ min_temp_6+"."):ExplanationLabelVariable.set(s))
                                        del NameList[min_temp_6]
                                        # Delete the vertex that we finished working with

                                        TempDict7={}
                                        for i in NameList.keys():
                                            for j in NameList[i].keys():
                                                if j=="temporary":
                                                    TempDict7[i]=int(NameList[i][j])

                                        min_temp_7= min(TempDict7,key=TempDict7.get)
                                        print min_temp_7
                                        # Get the vertex which has the smallest temporary label
                                        NameList[min_temp_7]["permanent"]=NameList[min_temp_7]["temporary"]
                                        NameList[min_temp_7]["order"]="8"
                                        # Make that label permanent and give it order 2

                                        try:
                                            Node1_O.after(75000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                            Node1_P.after(75000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node2_O.after(75000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                            Node2_P.after(75000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node3_O.after(75000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                            Node3_P.after(75000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node4_O.after(75000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                            Node4_P.after(75000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node5_O.after(75000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                            Node5_P.after(75000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node6_O.after(75000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                            Node6_P.after(75000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node7_O.after(75000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                            Node7_P.after(75000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node8_O.after(75000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                            Node8_P.after(75000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node9_O.after(75000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                            Node9_P.after(75000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                        except Exception:
                                            pass
                                        # Update all the order and permanent labels
                                        ExplanationLabel.after(75000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                        "Therefore Vertex " +min_temp_7+ " is assigned permanent label "+ NameList[min_temp_7]["permanent"]+ " and order label "
                                                                        + NameList[min_temp_7]["order"]+"."):ExplanationLabelVariable.set(s))
                                        if "permanent" in NameList[EndingVertex].keys():
                                            ExplanationLabel.after(80000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                        else:
                                            for item in NameList.keys():
                                                if item!=min_temp_7:
                                                    try:
                                                        if NameList[min_temp_7][item]!=0:
                                                            try:
                                                                if int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"])> int(NameList[item]["temporary"]):
                                                                    pass
                                                                elif int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"])< int(NameList[item]["temporary"]):
                                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"]))
                                                            except KeyError:
                                                                NameList[item]["temporary"]=str(int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"]))
                                                    except KeyError:
                                                        pass
                                            #Update the temporary label values if eligible
                                            try:
                                                Node1_T.after(80000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node2_T.after(80000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node3_T.after(80000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node4_T.after(80000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node5_T.after(80000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node6_T.after(80000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node7_T.after(80000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node8_T.after(80000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node9_T.after(80000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            # Update all the temporary labels
                                            ExplanationLabel.after(80000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                                "working vertex "+ min_temp_7+"."):ExplanationLabelVariable.set(s))

                                            for i in NameList.keys():
                                                if i!=StartingVertex and i!=min_temp_7:
                                                    NameList[i]["permanent"]=NameList[i]["temporary"]
                                                    NameList[EndingVertex]["order"]="9"
                                            # Give the ending vertex order and temporary labels
                                            try:
                                                Node1_P.after(85000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                                Node1_O.after(85000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node2_P.after(85000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                                Node2_O.after(85000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node3_P.after(85000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                                Node3_O.after(85000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node4_P.after(85000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                                Node4_O.after(85000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node5_P.after(85000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                                Node5_O.after(85000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node6_P.after(85000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                                Node6_O.after(85000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node7_P.after(85000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                                Node7_O.after(85000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node8_P.after(85000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                                Node8_O.after(85000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node9_P.after(85000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                                Node9_O.after(85000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                            except KeyError:
                                                pass
                                            # Update all the permanent and order labels
                                            ExplanationLabel.after(85000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                            "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                                            + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                                            ExplanationLabel.after(90000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))

            if len(VerticesList)==10:
                # Only when there are five vertices
                dot1=cv.create_oval(400,100,402,102,activefill="black")
                dot2=cv.create_oval(200,150,202,152,activefill="black")
                dot3=cv.create_oval(100,250,102,252,activefill="black")
                dot4=cv.create_oval(100,350,102,352,activefill="black")
                dot5=cv.create_oval(200,450,202,452,activefill="black")
                dot6=cv.create_oval(400,500,402,502,activefill="black")
                dot7=cv.create_oval(600,450,602,452,activefill="black")
                dot8=cv.create_oval(700,350,702,352,activefill="black")
                dot9=cv.create_oval(700,250,702,252,activefill="black")
                dot10=cv.create_oval(600,150,602,152,activefill="black")
                Node1_O_Value=tk.StringVar()
                Node1_P_Value=tk.StringVar()
                Node1_T_Value=tk.StringVar()
                Node2_O_Value=tk.StringVar()
                Node2_P_Value=tk.StringVar()
                Node2_T_Value=tk.StringVar()
                Node3_O_Value=tk.StringVar()
                Node3_P_Value=tk.StringVar()
                Node3_T_Value=tk.StringVar()
                Node4_O_Value=tk.StringVar()
                Node4_P_Value=tk.StringVar()
                Node4_T_Value=tk.StringVar()
                Node5_O_Value=tk.StringVar()
                Node5_P_Value=tk.StringVar()
                Node5_T_Value=tk.StringVar()
                Node6_O_Value=tk.StringVar()
                Node6_P_Value=tk.StringVar()
                Node6_T_Value=tk.StringVar()
                Node7_O_Value=tk.StringVar()
                Node7_P_Value=tk.StringVar()
                Node7_T_Value=tk.StringVar()
                Node8_O_Value=tk.StringVar()
                Node8_P_Value=tk.StringVar()
                Node8_T_Value=tk.StringVar()
                Node9_O_Value=tk.StringVar()
                Node9_P_Value=tk.StringVar()
                Node9_T_Value=tk.StringVar()
                Node10_O_Value=tk.StringVar()
                Node10_P_Value=tk.StringVar()
                Node10_T_Value=tk.StringVar()
                # Three variables that will be changed throughout the program that will appear at the different labels

                Node1_Name=tk.Label(cv, text=VerticesList[0], bg="white", justify=tk.RIGHT)
                Node1_O=tk.Label(cv, textvariable=Node1_O_Value, relief=tk.GROOVE )
                Node1_P=tk.Label(cv, textvariable=Node1_P_Value, relief=tk.GROOVE )
                Node1_T=tk.Label(cv, textvariable=Node1_T_Value, relief=tk.GROOVE )
                cv.create_window(340,50,width=60,height=20,window=Node1_Name)
                cv.create_window(380,50,width=20,height=20,window=Node1_O)
                cv.create_window(400,50,width=20,height=20,window=Node1_P)
                cv.create_window(390,70,width=40,height=20,window=Node1_T)
                # Creates the labels that holes the variables above
                Node2_Name=tk.Label(cv, text=VerticesList[1], bg="white", justify=tk.RIGHT)
                Node2_O=tk.Label(cv, textvariable=Node2_O_Value, relief=tk.GROOVE )
                Node2_P=tk.Label(cv, textvariable=Node2_P_Value, relief=tk.GROOVE )
                Node2_T=tk.Label(cv, textvariable=Node2_T_Value, relief=tk.GROOVE )
                cv.create_window(110,130,width=60,height=20,window=Node2_Name)
                cv.create_window(150,130,width=20,height=20,window=Node2_O)
                cv.create_window(170,130,width=20,height=20,window=Node2_P)
                cv.create_window(160,150,width=40,height=20,window=Node2_T)
                # Creates the labels that holds the variables above
                Node3_Name=tk.Label(cv, text=VerticesList[2], bg="white", justify=tk.RIGHT)
                Node3_O=tk.Label(cv, textvariable=Node3_O_Value, relief=tk.GROOVE )
                Node3_P=tk.Label(cv, textvariable=Node3_P_Value, relief=tk.GROOVE )
                Node3_T=tk.Label(cv, textvariable=Node3_T_Value, relief=tk.GROOVE )
                cv.create_window(10,230,width=60,height=20,window=Node3_Name)
                cv.create_window(50,230,width=20,height=20,window=Node3_O)
                cv.create_window(70,230,width=20,height=20,window=Node3_P)
                cv.create_window(60,250,width=40,height=20,window=Node3_T)
                # Creates the labels that hold the variables above
                Node4_Name=tk.Label(cv, text=VerticesList[3], bg="white", justify=tk.RIGHT)
                Node4_O=tk.Label(cv, textvariable=Node4_O_Value, relief=tk.GROOVE )
                Node4_P=tk.Label(cv, textvariable=Node4_P_Value, relief=tk.GROOVE )
                Node4_T=tk.Label(cv, textvariable=Node4_T_Value, relief=tk.GROOVE )
                cv.create_window(10,330,width=60,height=20,window=Node4_Name)
                cv.create_window(50,330,width=20,height=20,window=Node4_O)
                cv.create_window(70,330,width=20,height=20,window=Node4_P)
                cv.create_window(60,350,width=40,height=20,window=Node4_T)
                Node5_Name=tk.Label(cv, text=VerticesList[4], bg="white", justify=tk.RIGHT)
                Node5_O=tk.Label(cv, textvariable=Node5_O_Value, relief=tk.GROOVE )
                Node5_P=tk.Label(cv, textvariable=Node5_P_Value, relief=tk.GROOVE )
                Node5_T=tk.Label(cv, textvariable=Node5_T_Value, relief=tk.GROOVE )
                cv.create_window(110,430,width=30,height=20,window=Node5_Name)
                cv.create_window(150,430,width=20,height=20,window=Node5_O)
                cv.create_window(170,430,width=20,height=20,window=Node5_P)
                cv.create_window(160,450,width=40,height=20,window=Node5_T)
                Node6_Name=tk.Label(cv, text=VerticesList[5], bg="white", justify=tk.RIGHT)
                Node6_O=tk.Label(cv, textvariable=Node6_O_Value, relief=tk.GROOVE )
                Node6_P=tk.Label(cv, textvariable=Node6_P_Value, relief=tk.GROOVE )
                Node6_T=tk.Label(cv, textvariable=Node6_T_Value, relief=tk.GROOVE )
                cv.create_window(340,530,width=30,height=20,window=Node6_Name)
                cv.create_window(380,530,width=20,height=20,window=Node6_O)
                cv.create_window(400,530,width=20,height=20,window=Node6_P)
                cv.create_window(390,550,width=40,height=20,window=Node6_T)
                Node7_Name=tk.Label(cv, text=VerticesList[6], bg="white", justify=tk.RIGHT)
                Node7_O=tk.Label(cv, textvariable=Node7_O_Value, relief=tk.GROOVE )
                Node7_P=tk.Label(cv, textvariable=Node7_P_Value, relief=tk.GROOVE )
                Node7_T=tk.Label(cv, textvariable=Node7_T_Value, relief=tk.GROOVE )
                cv.create_window(650,430,width=30,height=20,window=Node7_Name)
                cv.create_window(690,430,width=20,height=20,window=Node7_O)
                cv.create_window(710,430,width=20,height=20,window=Node7_P)
                cv.create_window(700,450,width=40,height=20,window=Node7_T)
                Node8_Name=tk.Label(cv, text=VerticesList[7], bg="white", justify=tk.RIGHT)
                Node8_O=tk.Label(cv, textvariable=Node8_O_Value, relief=tk.GROOVE )
                Node8_P=tk.Label(cv, textvariable=Node8_P_Value, relief=tk.GROOVE )
                Node8_T=tk.Label(cv, textvariable=Node8_T_Value, relief=tk.GROOVE )
                cv.create_window(730,330,width=30,height=20,window=Node8_Name)
                cv.create_window(770,330,width=20,height=20,window=Node8_O)
                cv.create_window(790,330,width=20,height=20,window=Node8_P)
                cv.create_window(780,350,width=40,height=20,window=Node8_T)
                Node9_Name=tk.Label(cv, text=VerticesList[8], bg="white", justify=tk.RIGHT)
                Node9_O=tk.Label(cv, textvariable=Node9_O_Value, relief=tk.GROOVE )
                Node9_P=tk.Label(cv, textvariable=Node9_P_Value, relief=tk.GROOVE )
                Node9_T=tk.Label(cv, textvariable=Node9_T_Value, relief=tk.GROOVE )
                cv.create_window(730,230,width=30,height=20,window=Node9_Name)
                cv.create_window(770,230,width=20,height=20,window=Node9_O)
                cv.create_window(790,230,width=20,height=20,window=Node9_P)
                cv.create_window(780,250,width=40,height=20,window=Node9_T)
                Node10_Name=tk.Label(cv, text=VerticesList[9], bg="white", justify=tk.RIGHT)
                Node10_O=tk.Label(cv, textvariable=Node10_O_Value, relief=tk.GROOVE )
                Node10_P=tk.Label(cv, textvariable=Node10_P_Value, relief=tk.GROOVE )
                Node10_T=tk.Label(cv, textvariable=Node10_T_Value, relief=tk.GROOVE )
                cv.create_window(600,130,width=30,height=20,window=Node10_Name)
                cv.create_window(640,130,width=20,height=20,window=Node10_O)
                cv.create_window(660,130,width=20,height=20,window=Node10_P)
                cv.create_window(650,150,width=40,height=20,window=Node10_T)
                # Creates the labels that holds the variables above

                line1=cv.create_line(401,101,200,151)
                line2=cv.create_line(401,101,101,251)
                line3=cv.create_line(401,101,101,351)
                line4=cv.create_line(401,101,201,451)
                line5=cv.create_line(401,101,401,501)
                line6=cv.create_line(401,101,601,451)
                line7=cv.create_line(401,101,701,351)
                line8=cv.create_line(401,101,701,251)
                line9=cv.create_line(401,101,601,151)
                line10=cv.create_line(201,151,101,251)
                line11=cv.create_line(201,151,101,351)
                line12=cv.create_line(201,151,201,451)
                line13=cv.create_line(201,151,401,501)
                line14=cv.create_line(201,151,601,451)
                line15=cv.create_line(201,151,701,351)
                line16=cv.create_line(201,151,701,251)
                line17=cv.create_line(201,151,601,151)
                line18=cv.create_line(101,251,100,351)
                line19=cv.create_line(101,251,200,451)
                line20=cv.create_line(101,251,401,501)
                line21=cv.create_line(101,251,601,451)
                line22=cv.create_line(101,251,701,351)
                line23=cv.create_line(101,251,701,251)
                line24=cv.create_line(101,251,601,151)
                line25=cv.create_line(101,351,201,451)
                line26=cv.create_line(101,351,401,501)
                line27=cv.create_line(101,351,601,451)
                line28=cv.create_line(101,351,701,351)
                line29=cv.create_line(101,351,701,251)
                line30=cv.create_line(101,351,601,151)
                line31=cv.create_line(201,451,401,501)
                line32=cv.create_line(201,451,601,451)
                line33=cv.create_line(201,451,701,351)
                line34=cv.create_line(201,451,701,251)
                line35=cv.create_line(201,451,601,151)
                line36=cv.create_line(401,501,601,451)
                line37=cv.create_line(401,501,701,351)
                line38=cv.create_line(401,501,701,251)
                line39=cv.create_line(401,501,601,151)
                line40=cv.create_line(601,451,701,351)
                line41=cv.create_line(601,451,701,251)
                line42=cv.create_line(601,451,601,151)
                line43=cv.create_line(701,351,701,251)
                line44=cv.create_line(701,351,601,151)
                line45=cv.create_line(701,251,601,151)
                # Create lines for each edge possible
                if int(LengthList[1])==0:
                    cv.delete(line1)
                else:
                    Label1=tk.Label(cv,text=LengthList[1], fg="black",bg="white")
                    Label1.pack()
                    cv.create_window(300,125,window=Label1)
                if int(LengthList[2])==0:
                    cv.delete(line2)
                else:
                    Label2=tk.Label(cv,text=LengthList[2], fg="black",bg="white")
                    Label2.pack()
                    cv.create_window(315,140,window=Label2)
                if int(LengthList[3])==0:
                    cv.delete(line3)
                else:
                    Label3=tk.Label(cv,text=LengthList[3], fg="black",bg="white")
                    Label3.pack()
                    cv.create_window(230,240,window=Label3)
                if int(LengthList[4])==0:
                    cv.delete(line4)
                else:
                    Label4=tk.Label(cv,text=LengthList[4], fg="black",bg="white")
                    Label4.pack()
                    cv.create_window(330,225,window=Label4)
                if int(LengthList[5])==0:
                    cv.delete(line5)
                else:
                    Label5=tk.Label(cv,text=LengthList[5], fg="black",bg="white")
                    Label5.pack()
                    cv.create_window(400,275,window=Label5)
                if int(LengthList[6])==0:
                    cv.delete(line6)
                else:
                    Label6=tk.Label(cv,text=LengthList[6], fg="black",bg="white")
                    Label6.pack()
                    cv.create_window(470,225,window=Label6)
                if int(LengthList[7])==0:
                    cv.delete(line7)
                else:
                    Label7=tk.Label(cv,text=LengthList[7], fg="black",bg="white")
                    Label7.pack()
                    cv.create_window(570,240,window=Label7)
                if int(LengthList[8])==0:
                    cv.delete(line8)
                else:
                    Label8=tk.Label(cv,text=LengthList[8], fg="black",bg="white")
                    Label8.pack()
                    cv.create_window(485,140,window=Label8)
                if int(LengthList[9])==0:
                    cv.delete(line9)
                else:
                    Label9=tk.Label(cv,text=LengthList[9], fg="black",bg="white")
                    Label9.pack()
                    cv.create_window(500,125,window=Label9)
                if int(LengthList[12])==0:
                    cv.delete(line10)
                else:
                    Label10=tk.Label(cv,text=LengthList[12], fg="black",bg="white")
                    Label10.pack()
                    cv.create_window(150,200,window=Label10)
                if int(LengthList[13])==0:
                    cv.delete(line11)
                else:
                    Label11=tk.Label(cv,text=LengthList[13], fg="black",bg="white")
                    Label11.pack()
                    cv.create_window(180,195,window=Label11)
                if int(LengthList[14])==0:
                    cv.delete(line12)
                else:
                    Label12=tk.Label(cv,text=LengthList[14], fg="black",bg="white")
                    Label12.pack()
                    cv.create_window(200,300,window=Label12)
                if int(LengthList[15])==0:
                    cv.delete(line13)
                else:
                    Label13=tk.Label(cv,text=LengthList[15], fg="black",bg="white")
                    Label13.pack()
                    cv.create_window(265,265,window=Label13)
                if int(LengthList[16])==0:
                    cv.delete(line14)
                else:
                    Label14=tk.Label(cv,text=LengthList[16], fg="black",bg="white")
                    Label14.pack()
                    cv.create_window(375,280,window=Label14)
                if int(LengthList[17])==0:
                    cv.delete(line15)
                else:
                    Label15=tk.Label(cv,text=LengthList[17], fg="black",bg="white")
                    Label15.pack()
                    cv.create_window(425,240,window=Label15)
                if int(LengthList[18])==0:
                    cv.delete(line16)
                else:
                    Label16=tk.Label(cv,text=LengthList[18], fg="black",bg="white")
                    Label16.pack()
                    cv.create_window(435,200,window=Label16)
                if int(LengthList[19])==0:
                    cv.delete(line17)
                else:
                    Label17=tk.Label(cv,text=LengthList[19], fg="black",bg="white")
                    Label17.pack()
                    cv.create_window(390,150,window=Label17)
                if int(LengthList[23])==0:
                    cv.delete(line18)
                else:
                    Label18=tk.Label(cv,text=LengthList[23], fg="black",bg="white")
                    Label18.pack()
                    cv.create_window(100,300,window=Label18)
                if int(LengthList[24])==0:
                    cv.delete(line19)
                else:
                    Label19=tk.Label(cv,text=LengthList[24], fg="black",bg="white")
                    Label19.pack()
                    cv.create_window(133,312,window=Label19)
                if int(LengthList[25])==0:
                    cv.delete(line20)
                else:
                    Label20=tk.Label(cv,text=LengthList[25], fg="black",bg="white")
                    Label20.pack()
                    cv.create_window(235,365,window=Label20)
                if int(LengthList[26])==0:
                    cv.delete(line21)
                else:
                    Label21=tk.Label(cv,text=LengthList[26], fg="black",bg="white")
                    Label21.pack()
                    cv.create_window(378,363,window=Label21)
                if int(LengthList[27])==0:
                    cv.delete(line22)
                else:
                    Label22=tk.Label(cv,text=LengthList[27], fg="black",bg="white")
                    Label22.pack()
                    cv.create_window(360,293,window=Label22)
                if int(LengthList[28])==0:
                    cv.delete(line23)
                else:
                    Label23=tk.Label(cv,text=LengthList[28], fg="black",bg="white")
                    Label23.pack()
                    cv.create_window(388,250,window=Label23)
                if int(LengthList[29])==0:
                    cv.delete(line24)
                else:
                    Label24=tk.Label(cv,text=LengthList[29], fg="black",bg="white")
                    Label24.pack()
                    cv.create_window(370,197,window=Label24)
                if int(LengthList[34])==0:
                    cv.delete(line25)
                else:
                    Label25=tk.Label(cv,text=LengthList[34], fg="black",bg="white")
                    Label25.pack()
                    cv.create_window(150,400,window=Label25)
                if int(LengthList[35])==0:
                    cv.delete(line26)
                else:
                    Label26=tk.Label(cv,text=LengthList[35], fg="black",bg="white")
                    Label26.pack()
                    cv.create_window(192,397,window=Label26)
                if int(LengthList[36])==0:
                    cv.delete(line27)
                else:
                    Label27=tk.Label(cv,text=LengthList[36], fg="black",bg="white")
                    Label27.pack()
                    cv.create_window(370,405,window=Label27)
                if int(LengthList[37])==0:
                    cv.delete(line28)
                else:
                    Label28=tk.Label(cv,text=LengthList[37], fg="black",bg="white")
                    Label28.pack()
                    cv.create_window(420,350,window=Label28)
                if int(LengthList[38])==0:
                    cv.delete(line29)
                else:
                    Label29=tk.Label(cv,text=LengthList[38], fg="black",bg="white")
                    Label29.pack()
                    cv.create_window(450,290,window=Label29)
                if int(LengthList[39])==0:
                    cv.delete(line30)
                else:
                    Label30=tk.Label(cv,text=LengthList[39], fg="black",bg="white")
                    Label30.pack()
                    cv.create_window(372,240,window=Label30)
                if int(LengthList[45])==0:
                    cv.delete(line31)
                else:
                    Label31=tk.Label(cv,text=LengthList[45], fg="black",bg="white")
                    Label31.pack()
                    cv.create_window(300,475,window=Label31)
                if int(LengthList[46])==0:
                    cv.delete(line32)
                else:
                    Label32=tk.Label(cv,text=LengthList[46], fg="black",bg="white")
                    Label32.pack()
                    cv.create_window(390,450,window=Label32)
                if int(LengthList[47])==0:
                    cv.delete(line33)
                else:
                    Label33=tk.Label(cv,text=LengthList[47], fg="black",bg="white")
                    Label33.pack()
                    cv.create_window(440,405,window=Label33)
                if int(LengthList[48])==0:
                    cv.delete(line34)
                else:
                    Label34=tk.Label(cv,text=LengthList[48], fg="black",bg="white")
                    Label34.pack()
                    cv.create_window(480,337,window=Label34)
                if int(LengthList[49])==0:
                    cv.delete(line35)
                else:
                    Label35=tk.Label(cv,text=LengthList[49], fg="black",bg="white")
                    Label35.pack()
                    cv.create_window(430,275,window=Label35)
                if int(LengthList[56])==0:
                    cv.delete(line36)
                else:
                    Label36=tk.Label(cv,text=LengthList[56], fg="black",bg="white")
                    Label36.pack()
                    cv.create_window(500,475,window=Label36)
                if int(LengthList[57])==0:
                    cv.delete(line37)
                else:
                    Label37=tk.Label(cv,text=LengthList[57], fg="black",bg="white")
                    Label37.pack()
                    cv.create_window(468,470,window=Label37)
                if int(LengthList[58])==0:
                    cv.delete(line38)
                else:
                    Label38=tk.Label(cv,text=LengthList[58], fg="black",bg="white")
                    Label38.pack()
                    cv.create_window(567,365,window=Label38)
                if int(LengthList[59])==0:
                    cv.delete(line39)
                else:
                    Label39=tk.Label(cv,text=LengthList[59], fg="black",bg="white")
                    Label39.pack()
                    cv.create_window(473,375,window=Label39)
                if int(LengthList[67])==0:
                    cv.delete(line40)
                else:
                    Label40=tk.Label(cv,text=LengthList[67], fg="black",bg="white")
                    Label40.pack()
                    cv.create_window(650,400,window=Label40)
                if int(LengthList[68])==0:
                    cv.delete(line41)
                else:
                    Label41=tk.Label(cv,text=LengthList[68], fg="black",bg="white")
                    Label41.pack()
                    cv.create_window(630,400,window=Label41)
                if int(LengthList[69])==0:
                    cv.delete(line42)
                else:
                    Label42=tk.Label(cv,text=LengthList[69], fg="black",bg="white")
                    Label42.pack()
                    cv.create_window(600,300,window=Label42)
                if int(LengthList[78])==0:
                    cv.delete(line43)
                else:
                    Label43=tk.Label(cv,text=LengthList[78], fg="black",bg="white")
                    Label43.pack()
                    cv.create_window(700,300,window=Label43)
                if int(LengthList[79])==0:
                    cv.delete(line44)
                else:
                    Label44=tk.Label(cv,text=LengthList[79], fg="black",bg="white")
                    Label44.pack()
                    cv.create_window(628,200,window=Label44)
                if int(LengthList[89])==0:
                    cv.delete(line45)
                else:
                    Label45=tk.Label(cv,text=LengthList[89], fg="black",bg="white")
                    Label45.pack()
                    cv.create_window(650,200,window=Label45)

                ExplanationLabelVariable.set("Demonstration Begin")

                NameList[StartingVertex]["permanent"]="0"
                NameList[StartingVertex]["order"]="1"
                # Assign permanent and order labels
                if StartingVertex==VerticesList[0]:
                    Node1_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node1_O_Value. set(s))
                    Node1_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node1_P_Value.set(s))
                if StartingVertex==VerticesList[1]:
                    Node2_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node2_O_Value. set(s))
                    Node2_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node2_P_Value.set(s))
                if StartingVertex==VerticesList[2]:
                    Node3_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node3_O_Value. set(s))
                    Node3_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node3_P_Value.set(s))
                if StartingVertex==VerticesList[3]:
                    Node4_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node4_O_Value. set(s))
                    Node4_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node4_P_Value.set(s))
                if StartingVertex==VerticesList[4]:
                    Node5_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node5_O_Value. set(s))
                    Node5_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node5_P_Value.set(s))
                if StartingVertex==VerticesList[5]:
                    Node6_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node6_O_Value. set(s))
                    Node6_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node6_P_Value.set(s))
                if StartingVertex==VerticesList[6]:
                    Node7_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node7_O_Value. set(s))
                    Node7_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node7_P_Value.set(s))
                if StartingVertex==VerticesList[7]:
                    Node8_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node8_O_Value. set(s))
                    Node8_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node8_P_Value.set(s))
                if StartingVertex==VerticesList[8]:
                    Node9_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node9_O_Value. set(s))
                    Node9_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node9_P_Value.set(s))
                if StartingVertex==VerticesList[9]:
                    Node10_O.after(5000,lambda s=NameList[StartingVertex]["order"]: Node10_O_Value. set(s))
                    Node10_P.after(5000,lambda s=NameList[StartingVertex]["permanent"]: Node10_P_Value.set(s))

                # Update the order and permanent labels of the starting vertex
                ExplanationLabel.after(5000, lambda s=("The Starting Vertex is "+StartingVertex+", Therefore we assign it order label "+NameList[StartingVertex]["order"]+
                " and permanent label "+NameList[StartingVertex]["permanent"]+"."): ExplanationLabelVariable.set(s))


                for item in NameList[StartingVertex].keys():
                    try:
                        if NameList[StartingVertex][item]!=0:
                            NameList[item]["temporary"]=NameList[StartingVertex][item]
                    except KeyError:
                        pass
                # Assign temporary labels to the ones eligible
                ExplanationLabel.after(10000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ StartingVertex+". "):ExplanationLabelVariable.set(s))
                try:
                    Node1_T.after(10000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node2_T.after(10000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node3_T.after(10000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node4_T.after(10000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node5_T.after(10000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node6_T.after(10000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node7_T.after(10000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node8_T.after(10000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node9_T.after(10000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                except KeyError:
                    pass
                try:
                    Node10_T.after(10000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                except KeyError:
                    pass
                # Update all the temporary labels
                del NameList[StartingVertex]
                # Delete the label that we finished working with
                TempDict1={}
                for i in NameList.keys():
                    for j in NameList[i].keys():
                        if j=="temporary":
                            TempDict1[i]=int(NameList[i][j])
                print TempDict1
                min_temp_1= min(TempDict1,key=TempDict1.get)
                print min_temp_1
                # Get the vertex which has the smallest temporary label
                NameList[min_temp_1]["permanent"]=NameList[min_temp_1]["temporary"]
                NameList[min_temp_1]["order"]="2"
                # Make that label permanent and give it order 2
                try:
                    Node1_O.after(15000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                    Node1_P.after(15000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node2_O.after(15000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                    Node2_P.after(15000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node3_O.after(15000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                    Node3_P.after(15000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node4_O.after(15000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                    Node4_P.after(15000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node5_O.after(15000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                    Node5_P.after(15000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node6_O.after(15000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                    Node6_P.after(15000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node7_O.after(15000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                    Node7_P.after(15000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node8_O.after(15000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                    Node8_P.after(15000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node9_O.after(15000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                    Node9_P.after(15000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                except Exception:
                    pass
                try:
                    Node10_O.after(15000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                    Node10_P.after(15000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                except Exception:
                    pass
                # Update all the order and permanent labels
                ExplanationLabel.after(15000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_1+ " is assigned permanent label "+ NameList[min_temp_1]["permanent"]+ " and order label "
                                                        + NameList[min_temp_1]["order"]+"."):ExplanationLabelVariable.set(s))

                if "permanent" in NameList[EndingVertex].keys():
                    ExplanationLabel.after(20000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +" and the route is " + StartingVertex+" to "+EndingVertex+". " ):ExplanationLabelVariable.set(s))
                else:
                # Otherwise, carry on
                    for item in NameList.keys():
                        if item!=min_temp_1:
                            try:
                                if NameList[min_temp_1][item] != 0:
                                    try:
                                        if int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])> int(NameList[item]["temporary"]):
                                            pass
                                        elif int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"])< int(NameList[item]["temporary"]):
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                                    except KeyError:
                                        NameList[item]["temporary"]=str(int(NameList[min_temp_1][item])+int(NameList[min_temp_1]["permanent"]))
                            except KeyError:
                                pass
                    # Update the values for the temporary labels if possible
                    print NameList
                    try:
                        Node1_T.after(20000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node2_T.after(20000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node3_T.after(20000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node4_T.after(20000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node5_T.after(20000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node6_T.after(20000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node7_T.after(20000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node8_T.after(20000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node9_T.after(20000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                    except KeyError:
                        pass
                    try:
                        Node10_T.after(20000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                    except KeyError:
                        pass
                    # Update all the temporary labels
                    ExplanationLabel.after(20000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                            "working vertex "+ min_temp_1+"."):ExplanationLabelVariable.set(s))
                    del NameList[min_temp_1]
                    TempDict2={}
                    for i in NameList.keys():
                        for j in NameList[i].keys():
                            if j=="temporary":
                                TempDict2[i]=int(NameList[i][j])

                    min_temp_2= min(TempDict2,key=TempDict2.get)
                    print min_temp_2
                    # Get the vertex which has the smallest temporary label
                    NameList[min_temp_2]["permanent"]=NameList[min_temp_2]["temporary"]
                    NameList[min_temp_2]["order"]="3"
                    # Make that label permanent and give it order 3
                    try:
                        Node1_O.after(25000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                        Node1_P.after(25000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node2_O.after(25000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                        Node2_P.after(25000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node3_O.after(25000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                        Node3_P.after(25000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node4_O.after(25000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                        Node4_P.after(25000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node5_O.after(25000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                        Node5_P.after(25000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node6_O.after(25000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                        Node6_P.after(25000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node7_O.after(25000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                        Node7_P.after(25000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node8_O.after(25000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                        Node8_P.after(25000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node9_O.after(25000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                        Node9_P.after(25000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                    except Exception:
                        pass
                    try:
                        Node10_O.after(25000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                        Node10_P.after(25000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                    except Exception:
                        pass
                    # Update all the order and temporary labels
                    ExplanationLabel.after(25000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_2+ " is assigned permanent label "+ NameList[min_temp_2]["permanent"]+ " and order label "
                                                        + NameList[min_temp_2]["order"]+"."):ExplanationLabelVariable.set(s))
                    if "permanent" in NameList[EndingVertex].keys():
                        ExplanationLabel.after(30000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                    # If the permanent lable is made to the ending vertex, end everything
                    else:
                    # Otherwise, carry on
                        for item in NameList.keys():
                            if item!=min_temp_2:
                                try:
                                    if NameList[min_temp_2][item]!=0:
                                        try:
                                            if int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])> int(NameList[item]["temporary"]):
                                                pass
                                            elif int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"])< int(NameList[item]["temporary"]):
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                        except KeyError:
                                            NameList[item]["temporary"]=str(int(NameList[min_temp_2][item])+int(NameList[min_temp_2]["permanent"]))
                                except KeyError:
                                    pass
                        # Update the values of the temporary labels if eligible
                        try:
                            Node1_T.after(30000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node2_T.after(30000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node3_T.after(30000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node4_T.after(30000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node5_T.after(30000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node6_T.after(30000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node7_T.after(30000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node8_T.after(30000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node9_T.after(30000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                        except KeyError:
                            pass
                        try:
                            Node10_T.after(30000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                        except KeyError:
                            pass
                        # Update all the temporary labels
                        ExplanationLabel.after(30000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_2+"."):ExplanationLabelVariable.set(s))

                        del NameList[min_temp_2]
                        # Delete the vertex that we finished working with

                        TempDict3={}
                        for i in NameList.keys():
                            for j in NameList[i].keys():
                                if j=="temporary":
                                    TempDict3[i]=int(NameList[i][j])

                        min_temp_3= min(TempDict3,key=TempDict3.get)
                        print min_temp_3
                        # Get the vertex which has the smallest temporary label
                        NameList[min_temp_3]["permanent"]=NameList[min_temp_3]["temporary"]
                        NameList[min_temp_3]["order"]="4"
                        # Make that label permanent and give it order 2

                        try:
                            Node1_O.after(35000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                            Node1_P.after(35000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node2_O.after(35000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                            Node2_P.after(35000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node3_O.after(35000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                            Node3_P.after(35000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node4_O.after(35000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                            Node4_P.after(35000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node5_O.after(35000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                            Node5_P.after(35000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node6_O.after(35000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                            Node6_P.after(35000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node7_O.after(35000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                            Node7_P.after(35000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node8_O.after(35000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                            Node8_P.after(35000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node9_O.after(35000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                            Node9_P.after(35000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                        except Exception:
                            pass
                        try:
                            Node10_O.after(35000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                            Node10_P.after(35000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                        except Exception:
                            pass
                        # Update all the order and permanent labels
                        ExplanationLabel.after(35000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                        "Therefore Vertex " +min_temp_3+ " is assigned permanent label "+ NameList[min_temp_3]["permanent"]+ " and order label "
                                                        + NameList[min_temp_3]["order"]+"."):ExplanationLabelVariable.set(s))
                        if "permanent" in NameList[EndingVertex].keys():
                            ExplanationLabel.after(40000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                        else:
                        # Otherwise, carry on
                            for item in NameList.keys():
                                if item!=min_temp_3:
                                    try:
                                        if NameList[min_temp_3][item]!=0:
                                            try:
                                                if int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])> int(NameList[item]["temporary"]):
                                                    pass
                                                elif int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"])< int(NameList[item]["temporary"]):
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                            except KeyError:
                                                NameList[item]["temporary"]=str(int(NameList[min_temp_3][item])+int(NameList[min_temp_3]["permanent"]))
                                    except KeyError:
                                        pass
                            #Update the temporary label values if eligible
                            try:
                                Node1_T.after(40000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node2_T.after(40000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node3_T.after(40000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node4_T.after(40000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node5_T.after(40000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node6_T.after(40000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node7_T.after(40000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node8_T.after(40000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node9_T.after(40000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                            except KeyError:
                                pass
                            try:
                                Node10_T.after(40000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                            except KeyError:
                                pass
                            # Update all the temporary labels
                            ExplanationLabel.after(40000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                "working vertex "+ min_temp_3+"."):ExplanationLabelVariable.set(s))

                            del NameList[min_temp_3]
                            # Delete the vertex that we finished working with

                            TempDict4={}
                            for i in NameList.keys():
                                for j in NameList[i].keys():
                                    if j=="temporary":
                                        TempDict4[i]=int(NameList[i][j])

                            min_temp_4= min(TempDict4,key=TempDict4.get)
                            print min_temp_4
                            # Get the vertex which has the smallest temporary label
                            NameList[min_temp_4]["permanent"]=NameList[min_temp_4]["temporary"]
                            NameList[min_temp_4]["order"]="5"
                            # Make that label permanent and give it order 2

                            try:
                                Node1_O.after(45000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                Node1_P.after(45000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node2_O.after(45000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                Node2_P.after(45000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node3_O.after(45000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                Node3_P.after(45000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node4_O.after(45000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                Node4_P.after(45000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node5_O.after(45000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                Node5_P.after(45000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node6_O.after(45000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                Node6_P.after(45000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node7_O.after(45000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                Node7_P.after(45000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node8_O.after(45000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                Node8_P.after(45000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node9_O.after(45000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                Node9_P.after(45000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                            except Exception:
                                pass
                            try:
                                Node10_O.after(45000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                Node10_P.after(45000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                            except Exception:
                                pass
                            # Update all the order and permanent labels
                            ExplanationLabel.after(45000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                            "Therefore Vertex " +min_temp_4+ " is assigned permanent label "+ NameList[min_temp_4]["permanent"]+ " and order label "
                                                            + NameList[min_temp_4]["order"]+"."):ExplanationLabelVariable.set(s))
                            if "permanent" in NameList[EndingVertex].keys():
                                ExplanationLabel.after(50000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                            else:
                            # Otherwise, carry on
                                for item in NameList.keys():
                                    if item!=min_temp_4:
                                        try:
                                            if NameList[min_temp_4][item]!=0:
                                                try:
                                                    if int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])> int(NameList[item]["temporary"]):
                                                        pass
                                                    elif int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"])< int(NameList[item]["temporary"]):
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                                except KeyError:
                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_4][item])+int(NameList[min_temp_4]["permanent"]))
                                        except KeyError:
                                            pass
                                #Update the temporary label values if eligible
                                try:
                                    Node1_T.after(50000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node2_T.after(50000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node3_T.after(50000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node4_T.after(50000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node5_T.after(50000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node6_T.after(50000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node7_T.after(50000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node8_T.after(50000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node9_T.after(50000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                except KeyError:
                                    pass
                                try:
                                    Node10_T.after(50000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                                except KeyError:
                                    pass
                                # Update all the temporary labels
                                ExplanationLabel.after(50000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                    "working vertex "+ min_temp_4+"."):ExplanationLabelVariable.set(s))

                                del NameList[min_temp_4]
                                # Delete the vertex that we finished working with

                                TempDict5={}
                                for i in NameList.keys():
                                    for j in NameList[i].keys():
                                        if j=="temporary":
                                            TempDict5[i]=int(NameList[i][j])

                                min_temp_5= min(TempDict5,key=TempDict5.get)
                                print min_temp_5
                                # Get the vertex which has the smallest temporary label
                                NameList[min_temp_5]["permanent"]=NameList[min_temp_5]["temporary"]
                                NameList[min_temp_5]["order"]="6"
                                # Make that label permanent and give it order 2

                                try:
                                    Node1_O.after(55000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                    Node1_P.after(55000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node2_O.after(55000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                    Node2_P.after(55000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node3_O.after(55000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                    Node3_P.after(55000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node4_O.after(55000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                    Node4_P.after(55000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node5_O.after(55000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                    Node5_P.after(55000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node6_O.after(55000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                    Node6_P.after(55000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node7_O.after(55000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                    Node7_P.after(55000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node8_O.after(55000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                    Node8_P.after(55000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node9_O.after(55000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                    Node9_P.after(55000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                except Exception:
                                    pass
                                try:
                                    Node10_O.after(55000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                    Node10_P.after(55000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                                except Exception:
                                    pass

                                # Update all the order and permanent labels
                                ExplanationLabel.after(55000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                "Therefore Vertex " +min_temp_5+ " is assigned permanent label "+ NameList[min_temp_5]["permanent"]+ " and order label "
                                                                + NameList[min_temp_5]["order"]+"."):ExplanationLabelVariable.set(s))
                                if "permanent" in NameList[EndingVertex].keys():
                                    ExplanationLabel.after(60000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                        StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                        +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                else:
                                    for item in NameList.keys():
                                        if item!=min_temp_5:
                                            try:
                                                if NameList[min_temp_5][item]!=0:
                                                    try:
                                                        if int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])> int(NameList[item]["temporary"]):
                                                            pass
                                                        elif int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"])< int(NameList[item]["temporary"]):
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                                    except KeyError:
                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_5][item])+int(NameList[min_temp_5]["permanent"]))
                                            except KeyError:
                                                pass
                                    #Update the temporary label values if eligible
                                    try:
                                        Node1_T.after(60000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node2_T.after(60000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node3_T.after(60000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node4_T.after(60000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node5_T.after(60000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node6_T.after(60000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node7_T.after(60000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node8_T.after(60000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node9_T.after(60000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    try:
                                        Node10_T.after(60000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                                    except KeyError:
                                        pass
                                    # Update all the temporary labels
                                    ExplanationLabel.after(60000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                        "working vertex "+ min_temp_5+"."):ExplanationLabelVariable.set(s))
                                    del NameList[min_temp_5]
                                    # Delete the vertex that we finished working with

                                    TempDict6={}
                                    for i in NameList.keys():
                                        for j in NameList[i].keys():
                                            if j=="temporary":
                                                TempDict6[i]=int(NameList[i][j])

                                    min_temp_6= min(TempDict6,key=TempDict6.get)
                                    print min_temp_6
                                    # Get the vertex which has the smallest temporary label
                                    NameList[min_temp_6]["permanent"]=NameList[min_temp_6]["temporary"]
                                    NameList[min_temp_6]["order"]="7"
                                    # Make that label permanent and give it order 2

                                    try:
                                        Node1_O.after(65000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                        Node1_P.after(65000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node2_O.after(65000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                        Node2_P.after(65000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node3_O.after(65000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                        Node3_P.after(65000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node4_O.after(65000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                        Node4_P.after(65000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node5_O.after(65000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                        Node5_P.after(65000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node6_O.after(65000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                        Node6_P.after(65000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node7_O.after(65000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                        Node7_P.after(65000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node8_O.after(65000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                        Node8_P.after(65000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node9_O.after(65000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                        Node9_P.after(65000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                    except Exception:
                                        pass
                                    try:
                                        Node10_O.after(65000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                        Node10_P.after(65000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                                    except Exception:
                                        pass
                                    # Update all the order and permanent labels
                                    ExplanationLabel.after(65000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                    "Therefore Vertex " +min_temp_6+ " is assigned permanent label "+ NameList[min_temp_6]["permanent"]+ " and order label "
                                                                    + NameList[min_temp_6]["order"]+"."):ExplanationLabelVariable.set(s))
                                    if "permanent" in NameList[EndingVertex].keys():
                                        ExplanationLabel.after(70000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                            StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                            +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                    else:
                                        for item in NameList.keys():
                                            if item!=min_temp_6:
                                                try:
                                                    if NameList[min_temp_6][item]!=0:
                                                        try:
                                                            if int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])> int(NameList[item]["temporary"]):
                                                                pass
                                                            elif int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"])< int(NameList[item]["temporary"]):
                                                                NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                        except KeyError:
                                                            NameList[item]["temporary"]=str(int(NameList[min_temp_6][item])+int(NameList[min_temp_6]["permanent"]))
                                                except KeyError:
                                                    pass
                                        #Update the temporary label values if eligible
                                        try:
                                            Node1_T.after(70000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node2_T.after(70000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node3_T.after(70000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node4_T.after(70000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node5_T.after(70000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node6_T.after(70000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node7_T.after(70000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node8_T.after(70000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node9_T.after(70000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        try:
                                            Node10_T.after(70000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                                        except KeyError:
                                            pass
                                        # Update all the temporary labels
                                        ExplanationLabel.after(70000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                            "working vertex "+ min_temp_6+"."):ExplanationLabelVariable.set(s))
                                        del NameList[min_temp_6]
                                        # Delete the vertex that we finished working with

                                        TempDict7={}
                                        for i in NameList.keys():
                                            for j in NameList[i].keys():
                                                if j=="temporary":
                                                    TempDict7[i]=int(NameList[i][j])

                                        min_temp_7= min(TempDict7,key=TempDict7.get)
                                        print min_temp_7
                                        # Get the vertex which has the smallest temporary label
                                        NameList[min_temp_7]["permanent"]=NameList[min_temp_7]["temporary"]
                                        NameList[min_temp_7]["order"]="8"
                                        # Make that label permanent and give it order 2

                                        try:
                                            Node1_O.after(75000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                            Node1_P.after(75000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node2_O.after(75000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                            Node2_P.after(75000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node3_O.after(75000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                            Node3_P.after(75000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node4_O.after(75000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                            Node4_P.after(75000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node5_O.after(75000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                            Node5_P.after(75000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node6_O.after(75000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                            Node6_P.after(75000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node7_O.after(75000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                            Node7_P.after(75000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node8_O.after(75000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                            Node8_P.after(75000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node9_O.after(75000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                            Node9_P.after(75000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                        except Exception:
                                            pass
                                        try:
                                            Node10_O.after(75000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                            Node10_P.after(75000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                                        except Exception:
                                            pass
                                        # Update all the order and permanent labels
                                        ExplanationLabel.after(75000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                        "Therefore Vertex " +min_temp_7+ " is assigned permanent label "+ NameList[min_temp_7]["permanent"]+ " and order label "
                                                                        + NameList[min_temp_7]["order"]+"."):ExplanationLabelVariable.set(s))
                                        if "permanent" in NameList[EndingVertex].keys():
                                            ExplanationLabel.after(80000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                                StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                                +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                        else:
                                            for item in NameList.keys():
                                                if item!=min_temp_7:
                                                    try:
                                                        if NameList[min_temp_7][item]!=0:
                                                            try:
                                                                if int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"])> int(NameList[item]["temporary"]):
                                                                    pass
                                                                elif int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"])< int(NameList[item]["temporary"]):
                                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"]))
                                                            except KeyError:
                                                                NameList[item]["temporary"]=str(int(NameList[min_temp_7][item])+int(NameList[min_temp_7]["permanent"]))
                                                    except KeyError:
                                                        pass
                                            #Update the temporary label values if eligible
                                            try:
                                                Node1_T.after(80000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node2_T.after(80000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node3_T.after(80000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node4_T.after(80000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node5_T.after(80000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node6_T.after(80000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node7_T.after(80000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node8_T.after(80000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node9_T.after(80000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            try:
                                                Node10_T.after(80000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                                            except KeyError:
                                                pass
                                            # Update all the temporary labels
                                            ExplanationLabel.after(80000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                                "working vertex "+ min_temp_7+"."):ExplanationLabelVariable.set(s))

                                            del NameList[min_temp_7]
                                            # Delete the vertex that we finished working with

                                            TempDict8={}
                                            for i in NameList.keys():
                                                for j in NameList[i].keys():
                                                    if j=="temporary":
                                                        TempDict8[i]=int(NameList[i][j])

                                            min_temp_8= min(TempDict8,key=TempDict8.get)
                                            print min_temp_8
                                            # Get the vertex which has the smallest temporary label
                                            NameList[min_temp_8]["permanent"]=NameList[min_temp_8]["temporary"]
                                            NameList[min_temp_8]["order"]="9"
                                            # Make that label permanent and give it order 2

                                            try:
                                                Node1_O.after(85000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                                Node1_P.after(85000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node2_O.after(85000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                                Node2_P.after(85000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node3_O.after(85000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                                Node3_P.after(85000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node4_O.after(85000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                                Node4_P.after(85000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node5_O.after(85000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                                Node5_P.after(85000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node6_O.after(85000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                                Node6_P.after(85000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node7_O.after(85000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                                Node7_P.after(85000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node8_O.after(85000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                                Node8_P.after(85000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node9_O.after(85000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                                Node9_P.after(85000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                            except Exception:
                                                pass
                                            try:
                                                Node10_O.after(85000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                                Node10_P.after(85000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                                            except Exception:
                                                pass

                                            # Update all the order and permanent labels
                                            ExplanationLabel.after(85000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                            "Therefore Vertex " +min_temp_8+ " is assigned permanent label "+ NameList[min_temp_8]["permanent"]+ " and order label "
                                                                            + NameList[min_temp_8]["order"]+"."):ExplanationLabelVariable.set(s))
                                            if "permanent" in NameList[EndingVertex].keys():
                                                ExplanationLabel.after(90000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))
                                            else:
                                                for item in NameList.keys():
                                                    if item!=min_temp_8:
                                                        try:
                                                            if NameList[min_temp_8][item]!=0:
                                                                try:
                                                                    if int(NameList[min_temp_8][item])+int(NameList[min_temp_8]["permanent"])> int(NameList[item]["temporary"]):
                                                                        pass
                                                                    elif int(NameList[min_temp_8][item])+int(NameList[min_temp_8]["permanent"])< int(NameList[item]["temporary"]):
                                                                        NameList[item]["temporary"]=str(int(NameList[min_temp_8][item])+int(NameList[min_temp_8]["permanent"]))
                                                                except KeyError:
                                                                    NameList[item]["temporary"]=str(int(NameList[min_temp_8][item])+int(NameList[min_temp_8]["permanent"]))
                                                        except KeyError:
                                                            pass
                                                #Update the temporary label values if eligible
                                                try:
                                                    Node1_T.after(90000,lambda s=NameList[VerticesList[0]]["temporary"]: Node1_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node2_T.after(90000,lambda s=NameList[VerticesList[1]]["temporary"]: Node2_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node3_T.after(90000,lambda s=NameList[VerticesList[2]]["temporary"]: Node3_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node4_T.after(90000,lambda s=NameList[VerticesList[3]]["temporary"]: Node4_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node5_T.after(90000,lambda s=NameList[VerticesList[4]]["temporary"]: Node5_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node6_T.after(90000,lambda s=NameList[VerticesList[5]]["temporary"]: Node6_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node7_T.after(90000,lambda s=NameList[VerticesList[6]]["temporary"]: Node7_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node8_T.after(90000,lambda s=NameList[VerticesList[7]]["temporary"]: Node8_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node9_T.after(90000,lambda s=NameList[VerticesList[8]]["temporary"]: Node9_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node10_T.after(90000,lambda s=NameList[VerticesList[9]]["temporary"]: Node10_T_Value.set(s))
                                                except KeyError:
                                                    pass
                                                # Update all the temporary labels
                                                ExplanationLabel.after(90000, lambda s=("We update the temporary labels of the vertices that can be reached directly from our currently "
                                                                                    "working vertex "+ min_temp_8+"."):ExplanationLabelVariable.set(s))

                                                for i in NameList.keys():
                                                    if i!=StartingVertex and i!=min_temp_8:
                                                        NameList[i]["permanent"]=NameList[i]["temporary"]
                                                        NameList[EndingVertex]["order"]="10"
                                                # Give the ending vertex order and temporary labels
                                                try:
                                                    Node1_P.after(95000,lambda s=NameList[VerticesList[0]]["permanent"]: Node1_P_Value.set(s))
                                                    Node1_O.after(95000,lambda s=NameList[VerticesList[0]]["order"]: Node1_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node2_P.after(95000,lambda s=NameList[VerticesList[1]]["permanent"]: Node2_P_Value.set(s))
                                                    Node2_O.after(95000,lambda s=NameList[VerticesList[1]]["order"]: Node2_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node3_P.after(95000,lambda s=NameList[VerticesList[2]]["permanent"]: Node3_P_Value.set(s))
                                                    Node3_O.after(95000,lambda s=NameList[VerticesList[2]]["order"]: Node3_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node4_P.after(95000,lambda s=NameList[VerticesList[3]]["permanent"]: Node4_P_Value.set(s))
                                                    Node4_O.after(95000,lambda s=NameList[VerticesList[3]]["order"]: Node4_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node5_P.after(95000,lambda s=NameList[VerticesList[4]]["permanent"]: Node5_P_Value.set(s))
                                                    Node5_O.after(95000,lambda s=NameList[VerticesList[4]]["order"]: Node5_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node6_P.after(95000,lambda s=NameList[VerticesList[5]]["permanent"]: Node6_P_Value.set(s))
                                                    Node6_O.after(95000,lambda s=NameList[VerticesList[5]]["order"]: Node6_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node7_P.after(95000,lambda s=NameList[VerticesList[6]]["permanent"]: Node7_P_Value.set(s))
                                                    Node7_O.after(95000,lambda s=NameList[VerticesList[6]]["order"]: Node7_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node8_P.after(95000,lambda s=NameList[VerticesList[7]]["permanent"]: Node8_P_Value.set(s))
                                                    Node8_O.after(95000,lambda s=NameList[VerticesList[7]]["order"]: Node8_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node9_P.after(95000,lambda s=NameList[VerticesList[8]]["permanent"]: Node9_P_Value.set(s))
                                                    Node9_O.after(95000,lambda s=NameList[VerticesList[8]]["order"]: Node9_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                try:
                                                    Node10_P.after(95000,lambda s=NameList[VerticesList[9]]["permanent"]: Node10_P_Value.set(s))
                                                    Node10_O.after(95000,lambda s=NameList[VerticesList[9]]["order"]: Node10_O_Value.set(s))
                                                except KeyError:
                                                    pass
                                                # Update all the permanent and order labels
                                                ExplanationLabel.after(95000, lambda s=("We assign a permanent label to the vertex with smallest temporary label that does not have a permanent label yet." +
                                                                                "Therefore Vertex " +EndingVertex+ " is assigned permanent label "+ NameList[EndingVertex]["permanent"]+ " and order label "
                                                                                + NameList[EndingVertex]["order"]+"."):ExplanationLabelVariable.set(s))

                                                ExplanationLabel.after(100000, lambda s=("The ending vertex has a permanent label! Therefore the shortest distance from "+
                                                                                    StartingVertex+" to "+ EndingVertex+" is " + NameList[EndingVertex]["permanent"]
                                                                                    +". Now work out the route using the graph on the left!"):ExplanationLabelVariable.set(s))


    def exit_page5(self):
        self.master.destroy()
    def exit_screen(self):
        self.master.quit()

    def save(self):
        if self.FileNameEntry.get()=="":
            tkMessageBox.showerror(parent=self.master, title="Warning", message="Please enter a name for the file")
        else:
            newpath = r'C:\Users\Public\Dijkstra Demonstrator'
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            save_path = 'C:\Users\Public\Dijkstra Demonstrator'

            name_of_file = self.FileNameEntry.get()

            completeName = os.path.join(save_path, name_of_file+".txt")

            file1 = open(completeName, "w")

            toFile = "StartingVertex="+self.StartingVertex+"\nEndingVertex="+self.EndingVertex+\
                     "\nVerticesList="+str(self.VerticesList)+"\nLengthList="+str(self.LengthList)

            file1.write(toFile)

            file1.close()

class Page6:
    def __init__(self, master):
        self.master = master
        # Initialisation
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        self.FileName=tk.StringVar()
        self.FileNameEntry=tk.Entry(self.master, font=TNR24, textvariable=self.FileName)
        self.FileNameEntry.place(x=340, y=200, width=600, height=100)
        self.ProceedButton=tk.Button(self.master,font=TNR24,text="Proceed",command=self.Proceed)
        self.ProceedButton.place(x=340, y=350, width=600, height=100)
        self.BackButton = tk.Button(self.master, text="Back", command=self.exit_page6)
        self.BackButton.place(x=1240, y=620, width=40, height=30)
        self.title = tk.Label(self.master, font=TNR32, text="Please Enter the Name of the Question")
        self.title.place(x=320, y=50)
        self.exit_button = tk.Button(self.master, text="EXIT", command=self.exit_screen)
        self.exit_button.place(x=1240, y=670, width=40, height=30)
    def exit_page6(self):
        self.master.destroy()
    def exit_screen(self):
        self.master.quit()
    def Proceed(self):
        NameVariable=self.FileName.get()
        SavePath='C:\Users\Public\Dijkstra Demonstrator'
        CompleteName = os.path.join(SavePath, NameVariable+".txt")
        file_path = path.relpath(CompleteName)
        if os.path.exists(file_path)==True:
            vars = dict()
            with open(file_path) as f:
                for line in f:
                    eq_index = line.find('=')
                    var_name = line[:eq_index].strip()
                    number = line[eq_index + 1:].strip()
                    vars[var_name] = number
            self.StartingVertex=vars["StartingVertex"]
            self.EndingVertex=vars["EndingVertex"]
            self.VerticesList=eval(vars["VerticesList"])
            self.LengthList=eval(vars["LengthList"])
            self.window_five = tk.Toplevel(self.master)
            self.app = Page5(self.window_five, self.VerticesList, self.LengthList, self.StartingVertex, self.EndingVertex)
        else:
            tkMessageBox.showerror(parent=self.master, title="Warning", message="You sure that you entered the correct name?")





def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
    #Main Function

if __name__ == '__main__':
    main()