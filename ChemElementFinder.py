# Importing required libraries here
from tkinter import *  # For importing everything from tkinter to make a GUI interface

from PIL import ImageTk, Image # For showing images with Tkinter

from tkinter import messagebox #For showing popup messages on errors

from tkinter import ttk #For showing different tabs in the interface

root = Tk()#Making the main window for user interaction

my_notebook=ttk.Notebook(root)#Creating a notebook to show tabs

my_notebook.grid(row=0,column=0)





root.title('ChemElement Finder')#Setting title of the window

root.geometry('1355x825')#To fix the size and geometry of the window

root.iconbitmap('flaskicon.ico')#Adding a flask shaped icon to the window


#A dictionary to hold the basic informaton about the elements
bigdict = {1: ['Hydrogen', 'H', '1.008', '1', 's', 1, 1, '1s1'],
           2: ['Helium', 'He', '4.0026', '4', 'p', 18, 1, '1s2'],
           3: ['Lithium', 'Li', '6.941', '7', 's', 1, 2, '[He]2s1'],
           4: ['Beryllium', 'Be', '9.102', '9', 's', 2, 2, '[He]2s2'],
           5: ['Boron', 'B', '10.811', '11', 'p', 13, 2, '[He] 2s2 2p1'],
           6: ['Carbon', 'C', '12.011', '12', 'p', 14, 2, '[He] 2s2 2p2'],
           7: ['Nitrogen', 'N', '14.007', '14', 'p', 15, 2, '[He] 2s2 2p3'],
           8: ['Oxygen', 'O', '15.999', '16', 'p', 16, 2, '[He] 2s2 2p4'],
           9: ['Fluorine', 'F', '18.998', '19', 'p', 17, 2, '[He] 2s2 2p5'],
           10: ['Neon', 'Ne', '20.18', '20', 'p', 18, 2, '[He] 2s2 2p6'],
           11: ['Sodium(Natrium)', 'Na', '22.990', '23', 's', 1, 3, '[Ne] 3s1'],
           12: ['Magnesium', 'Mg', '24.305', '24', 's', 2, 3, '[Ne] 3s2'],
           13: ['Aluminium', 'Al', '26.982', '27', 'p', 13, 3, '[Ne] 3s2 3p1'],
           14: ['Silicon', 'Si', '28.086', '28', 'p', 14, 3, '[Ne] 3s2 3p2'],
           15: ['Phosphorus', 'P', '30.974', '31', 'p', 15, 3, '[Ne] 3s2 3p3'],
           16: ['Sulphur', 'S', '32.066', '32', 'p', 16, 3, '[Ne] 3s2 3p4'],
           17: ['Chlorine', 'Cl', '35.453', '35.5', 'p', 17, 3, '[Ne] 3s2 3p5'],
           18: ['Argon', 'Ar', '39.948', '40', 'p', 18, 3, '[Ne] 3s2 3p6'],
           19: ['Potassium(Kalium)', 'K', '39.098', '40', 's', 1, 4, '[Ar] 4s1'],
           20: ['Calcium', 'Ca', '40.078', '40', 's', 2, 4, '[Ar] 4s2'],
           21: ['Scandium', 'Sc', '44.956', '45', 'd', 3, 4, '[Ar]3d1 4s2'],
           22: ['Titanium', 'Ti', '47.88', '48', 'd', 4, 4, '[Ar]3d2 4s2'],
           23: ['Vanadium', 'V', '50.942', '51', 'd', 5, 4, '[Ar]3d3 4s2'],
           24: ['Chromium', 'Cr', '51.996', '52', 'd', 6, 4, '[Ar]3d5 4s1'],
           25: ['Manganese', 'Mn', '54.938', '55', 'd', 7, 4, '[Ar]3d5 4s2'],
           26: ['Iron(Ferrum)', 'Fe', '55.845', '56', 'd', 8, 4, '[Ar]3d6 4s2'],
           27: ['Cobalt', 'Co', '58.933', '59', 'd', 9, 4, '[Ar]3d7 4s2'],
           28: ['Nickel', 'Ni', '58.71', '59', 'd', 10, 4, '[Ar]3d8 4s2'],
           29: ['Copper(Cuprum', 'Cu', '63.546', '63.5', 'd', 11, 4, '[Ar]3d10 4s1'],
           30: ['Zinc', 'Zn', '65.39', '65', 'd', 12, 4, '[Ar]3d10 4s2'],
           31: ['Gallium', 'Ga', '69.723', '70', 'p', 13, 4, '[Ar] 3d10 4s2 4p1'],
           32: ['Germanium', 'Ge', '72.61', '73', 'p', 14, 4, '[Ar] 3d10 4s2 4p2'],
           33: ['Arsenic', 'As', '74.922', '75', 'p', 15, 4, '[Ar] 3d10 4s2 4p3'],
           34: ['Selenium', 'Se', '78.96', '79', 'p', 16, 4, '[Ar] 3d10 4s2 4p4'],
           35: ['Bromine', 'Br', '79.904', '80', 'p', 17, 4, '[Ar] 3d10 4s2 4p5'],
           36: ['Krypton', 'Kr', '83.80', '84', 'p', 18, 4, '[Ar] 3d10 4s2 4p6'],
           37: ['Rubidium', 'Rb', '85.468', '85', 's', 1, 5, '[Kr] 5s1'],
           38: ['Strontium', 'Sr', '87.62', '88', 's', 2, 5, '[Kr] 5s2'],
           39: ['Ytterium', 'Y', '88.906', '89', 'd', 3, 5, '[Kr]4d1 5s2'],
           40: ['Zirconium', 'Zr', '91.224', '91', 'd', 4, 5, '[Kr]4d2 5s2'],
           41: ['Niobium', 'Nb', '92.906', '93', 'd', 5, 5, '[Kr]4d4 5s1'],
           42: ['Molybdenum', 'Mo', '95.94', '96', 'd', 6, 5, '[Kr]4d5 5s1'],
           43: ['Technetium', 'Tc', '98.906', '99', 'd', 7, 5, '[Kr]4d5 5s2'],
           44: ['Ruthenium', 'Ru', '101.07', '101', 'd', 8, 5, '[Kr]4d7 5s1'],
           45: ['Rhodium', 'Rh', '102.905', '103', 'd', 9, 5, '[Kr]4d8 5s1'],
           46: ['Palladium', 'Pd', '106.42', '106', 'd', 10, 5, '[Kr]4d10 5s0'],
           47: ['Silver(Argentum)', 'Ag', '107.87', '108', 'd', 11, 5, '[Kr]4d10 5s1'],
           48: ['Cadmium', 'Cd', '112.41', '112', 'd', 12, 5, '[Kr]4d10 5s1'],
           49: ['Indium', 'In', '114.82', '115', 'p', 13, 5, '[Kr] 4d10 5s2 5p1'],
           50: ['Tin(Stannum)', 'Sn', '118.71', '119', 'p', 14, 5, '[Kr] 4d10 5s2 5p2'],
           51: ['Antimony(Stibium)', 'Sb', '121.76', '122', 'p', 15, 5, '[Kr] 4d10 5s2 5p3'],
           52: ['Tellurium', 'Te', '127.60', '128', 'p', 16, 5, '[Kr] 4d10 5s2 5p4'],
           53: ['Iodine', 'I', '126.90', '127', 'p', 17, 5, '[Kr] 4d10 5s2 5p5'],
           54: ['Xenon', 'Xe', '131.29', '131', 'p', 18, 5, '[Kr] 4d10 5s2 5p6'],
           55: ['Cesium', 'Cs', '132.905', '133', 's', 1, 6, '[Xe] 6s1'],
           56: ['Barium', 'Ba', '137.33', '137', 's', 2, 6, '[Xe] 6s2'],
           57: ['Lanthanum', 'La', '138.91', '139', 'd', 3, 6, '[Rn]  5d1 6s2'],
           58: ['Cerium', 'Ce', '140.12', '140', 'f', '4f', 1, '[Xe] 4f1 5d1 6s2'],
           59: ['Praseodymium', 'Pr', '140.91', '141', 'f', '4f', 1, '[Xe] 4f3 5d0 6s2'],
           60: ['Neodymium', 'Nd', '144.24', '144', 'f', '4f', 1, '[Xe] 4f4 5d0 6s2'],
           61: ['Promethium', 'Pm', '146.92', '147', 'f', '4f', 1, '[Xe] 4f5 5d0 6s2 '],
           62: ['Samarium', 'Sm', '150.36', '150', 'f', '4f', 1, '[Xe] 4f6 5d0 6s2'],
           63: ['Europium', 'Eu', '151.96', '152', 'f', '4f', 1, '[Xe] 4f7 5d0 6s2'],
           64: ['Gadolinium', 'Gd', '157.25', '157', 'f', '4f', 1, '[Xe] 4f7 5d1 6s2'],
           65: ['Terbium', 'Tb', '158.93', '159', 'f', '4f', 1, '[Xe] 4f9 5d0 6s2'],
           66: ['Dysprosium', 'Dy', '162.50', '162', 'f', '4f', 1, '[Xe] 4f10 5d0 6s2'],
           67: ['Holmium', 'Ho', '164.93', '165', 'f', '4f', 1, '[Xe] 4f11 5d0 6s2'],
           68: ['Erbium', 'Er', '167.26', '167', 'f', '4f', 1, '[Xe] 4f12 5d0 6s2 '],
           69: ['Thulium', 'Tm', '168.90', '169', 'f', '4f', 1, '[Xe] 4f13 5d0 6s2'],
           70: ['Ytterbium', 'Yb', '173.04', '173', 'f', '4f', 1, '[Xe] 4f14 5d0 6s2'],
           71: ['Lutetium', 'Lu', '174.97', '175', 'f', '4f', 1, '[Xe] 4f14 5d1 6s2'],
           72: ['Hafnium', 'Hf', '178.49', '178', 'd', 4, 6, '[Xe] 4f14 5d2 6s2'],
           73: ['Tantalum', 'Ta', '180.95', '181', 'd', 5, 6, '[Xe] 4f14 5d3 6s2'],
           74: ['Tungsten(Wolfram)', 'W', '183.84', '184', 'd', 6, 6, '[Kr] 4f14 5d4 6s2'],
           75: ['Rhenium', 'Re', '186.21', '186', 'd', 7, 6, '[Xe] 4f14 5d5 6s2'],
           76: ['Osmium', 'Os', '190.23', '190', 'd', 8, 6, '[Xe] 4f14 5d6 6s2 '],
           77: ['Iridium', 'Ir', '192.217', '192', 'd', 9, 6, '[Xe] 4f14 5d7 6s2'],
           78: ['Platinum', 'Pt', '195.08', '195', 'd', 10, 6, '[Xe] 4f14 5d9 6s1'],
           79: ['Gold(Aurum)', 'Au', '196.97', '197', 'd', 11, 6, '[Xe] 4f14 5d10 6s1'],
           80: ['Mercury(Hydragyrum)', 'Hg', '200.59', '201', 'd', 12, 6, '[Xe] 4f14 5d10 6s1'],
           81: ['Thallium', 'Tl', 204.38, 204.0, 'p', 13, 6, '[Xe]5d106s26p1'],
           82: ['Lead(Plumbum)', 'Pb', 207.19, 207.0, 'p', 14, 6, '[Xe]5d106s26p2'],
           83: ['Bismuth', 'Bi', 208.98, 209.0, 'p', 15, 6, '[Xe]5d106s26p3'],
           84: ['Polonium', 'Po', 209.98, 210.0, 'p', 16, 6, '[Xe]5d106s26p4'],
           85: ['Astatine', 'At', 209.99, 210.0, 'p', 17, 6, '[Xe]5d106s26p5'],
           86: ['Radon', 'Rn', 222.02, 222.0, 'p', 18, 6, '[Xe]5d106s26p6'],
           87: ['Francium', 'Fr', 223.02, 223.0, 's', 1, 7, '[Rn]7s1'],
           88: ['Radium', 'Ra', 226.03, 226.0, 's', 2, 7, '[Rn]7s2'],
           89: ['Actinium', 'Ac', '227.03', '227', 'd', 3, 7, '[Rn]6d1 7s2'],
           90: ['Thorium', 'Th', '232.04', '232', 'f', '5f', 2, '[Rn] 5f0 6d2 7s2'],
           91: ['Protactinium', 'Pa', '231.04', '231', 'f', '5f', 2, '[Rn] 5f2 6d1 7s2'],
           92: ['Uranium', 'U', '238.03', '238', 'f', '5f', 2, '[Rn] 5f3 6d1 7s2'],
           93: ['Neptunium', 'Np', '237.05', '237', 'f', '5f', 2, '[Rn] 5f4 6d1 7s2'],
           94: ['Plutonium', 'Pu', '244.06', '244', 'f', '5f', 2, '[Rn] 5f6 6d0 7s2'],
           95: ['Americium', 'Am', '246.06', '246', 'f', '5f', 2, '[Rn] 5f7 6d0 7s2'],
           96: ['Curium', 'Cm', '247.07', '247', 'f', '5f', 2, '[Rn] 5f7 6d1 7s2'],
           97: ['Berkelium', 'Bk', '247.07', '247', 'f', '5f', 2, '[Rn] 5f9 6d0 7s2'],
           98: ['Californium', 'Cf', '251.08', '251', 'f', '5f', 2, '[Rn] 5d10 6d0 7s2'],
           99: ['Einsteinium', 'Es', '252.08', '252', 'f', '5f', 2, '[Rn] 5f11 6d0 7s2'],
           100: ['Fermium', 'Fm', '257.18', '257', 'f', '5f', 2, '[Rn] 5f12 6d0 7s2'],
           101: ['Mendelevium', 'Md', '258.10', '258', 'f', '5f', 2, '[Rn] 5f13 6d0 7s2'],
           102: ['Nobelium', 'No', '259.10', '259', 'f', '5f', 2, '[Rn] 5f14 6d0 7s2'],
           103: ['Lawrencium', 'Lr', '262.11', '262', 'f', '5f', 2, '[Rn] 5f14 6d1 7s2'],
           104: ['Rutherfordium', 'Rf', '261.11', '261', 'd', 4, 7, '[Rn] 5f14 6d2 7s2'],
           105: ['Dubnium', 'Db', '261.11', '261', 'd', 5, 7, '[Rn]5f14 6d3 7s2'],
           106: ['Seaborgium', 'Sg', '263.12', '263', 'd', 6, 7, '[Rn] 5f14 6d4 7s2'],
           107: ['Bohrium', 'Bh', '262.12', '262', 'd', 7, 7, '[Rn] 5f14 6d5 7s2'],
           108: ['Hassnium', 'Hs', '265', '265', 'd', 8, 7, '[Rn] 5f14 6d6 7s2'],
           109: ['Meitnerium', 'Mt', '268', '268', 'd', 9, 7, '[Rn] 5f14 6d7 7s2'],
           110: ['Darmstadtium', 'Ds', '269', '269', 'd', 10, 7, '[Rn] 5f14 6d8 7s2'],
           111: ['Roentgenium', 'Rg', '272', '272', 'd', 11, 7, '[Rn] 5f14 6d10 7s1'],
           112: ['Copernicium', 'Cn', '277', '277', 'd', 12, 7, '[Rn] 5f14 6d10 7s1'],
           113: ['Nihonium', 'Nh', '286', '286', 'p', 13, 7, '[Rn] 6d10 7s2 7p1'],
           114: ['Flerovium', 'Fl', '289', '289', 'p', 14, 7, '[Rn] 6d10 7s2 7p2'],
           115: ['Moscovium', 'Mc', '288', '288', 'p', 15, 7, '[Rn] 6d10 7s2 7p3'],
           116: ['Livermorium', 'Lv', '292', '292', 'p', 16, 7, '[Rn] 6d10 7s2 7p4'],
           117: ['Tennessine', 'Ts', '294', '294', 'p', 17, 7, '[Rn] 6d10 7s2 7p5'],
           118: ['Oganesson', 'Og', '294', '294', 'p', 18, 7, '[Rn] 6d10 7s2 7p6']
           }
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#All the functions come here
#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

#search function
#____________________________________________________________
def search(val,type_,way='SearchBox'):

	if SearchEntry.get() not in '                                ':
		SearchEntry.delete(0, END)
	if way=='PT':

		my_notebook.select(HomeFrame)
	if type_ == 'Atomic Number':
		try:
			a = int(val)
			InfoFrame.grid_forget()
			x = bigdict[a][0]
		except:
			pass


	elif type_ == 'Symbol':
	    for i in range(1, 119):
	        if (bigdict[i][1]).lower() == val.lower():
	            a = i

	elif type_ == 'Name':
	    for i in range(1, 119):
	        if val.lower() in (bigdict[i][0]).lower():
	            a = i
	elif type_ == 'Any':
	    if len(val) <= 3:
	        try:
	            a = int(val)
	            type_ = 'Atomic Number'
	        except:
	            type_ = 'Symbol'
	            for i in range(1, 119):
	                if (bigdict[i][1]).lower() == val.lower():
	                    a = i
	                    type_ = 'Symbol'
	    else:
	        type_ = 'Name'
	        for i in range(1, 119):
	            if val.lower() in (bigdict[i][0]).lower() and len(val) >= 3:
	                a = i
	                type_ = 'Name'

	InfoFrame = LabelFrame(SearchResultsFrame, relief=SOLID)
	InfoFrame.grid(row=1, column=0, sticky=W + E)
	
	SearchLabel = Label(SearchResultsFrame, text="You searched for " + type_ + ' ' + str(SearchEntry.get()), anchor=NW,
	                    bd=3, relief=SUNKEN)
	SearchLabel.grid(row=0, column=0, sticky=W + E)

	try:
	    AtnoLabel = Label(InfoFrame, text='Atomic Number:		' + str(a), anchor=W, font=('Comic Sans Ms', 13),
	                       fg='blue')
	    NameLabel = Label(InfoFrame, text='Name:			' + bigdict[a][0], anchor=W, font=('Comic Sans Ms', 13),
	                       fg='green')
	    SymbolLabel = Label(InfoFrame, text='Symbol:			' + bigdict[a][1], anchor=W, font=('Comic Sans Ms', 13),
	                       fg='red')
	    AtmassLabel = Label(InfoFrame, text='Atomic Mass:		' + str(bigdict[a][2]), anchor=W,font=('Comic Sans Ms', 13), 
	    				   fg='violet')
	    MassnonoLabel = Label(InfoFrame, text='Mass Number:		' + str(bigdict[a][3]), anchor=W,font=('Comic Sans Ms', 13),
	                       fg='indigo')
	    BlockLabel = Label(InfoFrame, text='Block:			' + bigdict[a][4], anchor=W, font=('Comic Sans Ms', 13),
	                       fg='brown')
	    GroupLabel = Label(InfoFrame, text='Group:			' + str(bigdict[a][5]), anchor=W,font=('Comic Sans Ms', 13),
	                       fg='grey')
	    PeriodLabel = Label(InfoFrame, text='Period:			' + str(bigdict[a][6]), anchor=W,font=('Comic Sans Ms', 13),
	                       fg='purple')

	    AtnoLabel.grid(row=1, column=0, sticky=W)
	    NameLabel.grid(row=2, column=0, sticky=W)
	    SymbolLabel.grid(row=3, column=0, sticky=W)
	    AtmassLabel.grid(row=4, column=0, sticky=W)
	    MassnonoLabel.grid(row=5, column=0, sticky=W)
	    BlockLabel.grid(row=6, column=0, sticky=W)
	    GroupLabel.grid(row=7, column=0, sticky=W)
	    PeriodLabel.grid(row=8, column=0, sticky=W)
	
	except:

	    SearchLabel.grid_forget()
	    SearchLabel = Label(SearchResultsFrame, text="You gave invalid input", anchor=NW, bd=3, relief=SUNKEN, fg='red')
	    SearchLabel.grid(row=0, column=0, sticky=W + E)

	    if type_=='Atomic Number':
	    	messagebox.showwarning('ERROR', 'Invalid Search of type : '+str(type_) + '\n' +'Element with atomic number '+str(a)+' does not exist'+ '\nPlease try again')
	    else:
	    	messagebox.showwarning('ERROR', 'Invalid Search of type : '+str(type_) + '\n' + 'Please try again')
#_____________________________________________________________

#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Making the Home screen
#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________


#_____________________________________________________________________________
HomeFrame=Frame(my_notebook,padx=12,pady=10)
HomeFrame.pack(fill='both',expand=1)
my_notebook.add(HomeFrame,text='   Home   ')
#______________________________________________________________________________



# Making the BaseFrame to show credits
#_________________________________________________________________________________
BaseFrame = LabelFrame(root, text='Credits', padx=8, pady=2, bd=4, relief=SUNKEN)

BaseFrame.grid(row=1, column=0, columnspan=5, sticky=W + E)

# Creating a label to add the text in the BaseFrame
BaseLabel = Label(BaseFrame, text="Created By: Mayank,Shreyansh and Rudraansh" + 10 * (
    "	") + "Subject Teacher : Nishant Dubey (PGT Computer Science) ", font=('Calibri', 12), anchor=W, fg='black')

BaseLabel.pack() # Packing the BaseLabel in the frame
#_________________________________________________________________________________



# Making the frame to show links related to elements
#_______________________________________________________________
LinkFrame = LabelFrame(HomeFrame, text='LINKS', padx=75, pady=290)
LinkFrame.grid(row=1, column=0, columnspan=1, rowspan=2)

EmptyLabel=Label(LinkFrame,text='')#Adding an empty label into the frame to avoid puncture 
EmptyLabel.pack()# Packing the EmptyLabel 
#_______________________________________________________________


# The search frame to search for elements
#_____________________________________________________________________________________
SearchFrame = LabelFrame(HomeFrame, text='SEARCH BOX', )
SearchFrame.grid(row=1, column=4)

SearchEntry = Entry(SearchFrame, width=20, font=('Comic Sans Ms', 15))#Creating a text box for taking search input
SearchEntry.grid(row=0, column=0, pady=30, columnspan=2, padx=50)#Positioning the text box

urchoice = StringVar()#Making a variable to store the choice taken from below created OptionMenu
choices = OptionMenu(SearchFrame, urchoice, 'Atomic Number', 'Name', 'Symbol', 'Any')#Creating the OptionMenu
choices.grid(row=1, column=1, pady=10)#Positioning the OptionMenu
urchoice.set('Any')#Setting default option in the OptionMenu


SearchByLabel = Label(SearchFrame, text='Search By', font=('Calibri', 15))#Creating label to contain hint text
SearchByLabel.grid(row=1, column=0, pady=10)#Positioning the label


SearchButton = Button(SearchFrame, text='Search', font=('Calibri', 15),
                      command=lambda: search(SearchEntry.get(), urchoice.get()))#Button to call the search command
SearchButton.grid(row=2, column=0, columnspan=2, pady=20)#Positioning the Button
#_____________________________________________________________________________________



#Making the frame to show the results of the search
#_______________________________________________________
SearchResultsFrame = LabelFrame(HomeFrame, text='Search results')# Making a frame to contain InfoFrame and DInfoFrame
SearchResultsFrame.grid(row=1, column=1, columnspan=3, rowspan=2)# Positioning the Frame
SearchLabel = Label(SearchResultsFrame, text='Active', bd=2, anchor=NW, relief=SOLID)#To show the status of the SearchResultsFrame
SearchLabel.grid(row=0, column=0, sticky=W + E)#Positioning the Label

InfoFrame = LabelFrame(SearchResultsFrame, relief=SOLID)#Making a frame to contain the basic info
InfoFrame.grid(row=1, column=0, sticky=W + E)#Positioning the Frame
InfoFrameLabel = Label(InfoFrame, text='General Info here')#Adding label to the frame to avoid puncture 
InfoFrameLabel.grid(row=0, column=0, padx=325, pady=110)

DInfoFrame = LabelFrame(SearchResultsFrame, relief=SOLID)#Making a frame to contain the detailed info
DInfoFrame.grid(row=2, column=0, sticky=W + E)#Positioning the Frame
DInfoFrameLabel = Label(DInfoFrame, text='Detailed Info Here')#Adding label to the frame to avoid puncture 
DInfoFrameLabel.grid(row=0, column=0, padx=325, pady=150)
#___________________________________________________________



# The image frame
#_____________________________________________________________________________________
ImageFrame = LabelFrame(HomeFrame, text='Image Box')#Creating frame to contain Images
ImageFrame.grid(row=2, column=4)#Positioning the Frames

ImageLabel = Label(ImageFrame, text='Images come here', padx=20, pady=20)#Adding label to the frame to avoid puncture 
ImageLabel.grid(row=0, column=0, padx=130, pady=155)#Positioning the label
#_____________________________________________________________________________________

#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Making the periodic table screen
#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

PeriodicTableFrame=Frame(my_notebook,padx=12,pady=10)
PeriodicTableFrame.pack(fill='both',expand=1)
my_notebook.add(PeriodicTableFrame,text='   Periodic Table   ')

pt_notebook=ttk.Notebook(PeriodicTableFrame)
pt_notebook.grid(row=0, column=0)


ptFrame = LabelFrame(pt_notebook,padx=115)
ptFrame.grid(row=1, column=1, columnspan=3, rowspan=2,sticky=W+E)
pt_notebook.add(ptFrame,text='   Button Periodic Table   ')

pt_label=Label(ptFrame,text='Click on any of the symbol given here to\n see information about it', font=('Comic Sans Ms', 20))
pt_label.grid(row=2,column=3,columnspan=10,rowspan=2)


for i in range(1, 58):
	if bigdict[i][4]=='s':
		colour='red'
	if bigdict[i][4]=='p':
		colour='yellow'
	if bigdict[i][4]=='d':
		colour='purple'

	Button(ptFrame, text=bigdict[i][1], font=('Comic Sans Ms', 19),
    	command=lambda i=i: search(i, 'Atomic Number',way='PT'), fg=colour).grid(row=bigdict[i][6],
                                                                                            column=bigdict[i][5])
for i in range(72, 90):  # f block interruption
	if bigdict[i][4]=='s':
		colour='red'
	if bigdict[i][4]=='p':
		colour='yellow'
	if bigdict[i][4]=='d':
		colour='purple'
	Button(ptFrame, text=bigdict[i][1], font=('Comic Sans Ms', 19),
	       command=lambda i=i: search(i, 'Atomic Number',way='PT'), fg=colour).grid(row=bigdict[i][6],
                                                                                            column=bigdict[i][5])
for i in range(104, 119):  # f block interruption
	if bigdict[i][4]=='s':
		colour='red'
	if bigdict[i][4]=='p':
		colour='yellow'
	if bigdict[i][4]=='d':
		colour='purple'
	Button(ptFrame, text=bigdict[i][1], font=('Comic Sans Ms', 19),
		command=lambda i=i: search(i, 'Atomic Number',way='PT'), fg=colour).grid(row=bigdict[i][6],
                                                                                            column=bigdict[i][5])
GapLabel=Label(ptFrame,text='').grid(row=8,column=0,columnspan=19)

for i in range(58, 72):# f block
	start=58
	Button(ptFrame, text=bigdict[i][1], font=('Comic Sans Ms', 19),
	               command=lambda i=i: search(i, 'Atomic Number',way='PT'), fg='blue').grid(row=9,
                                                                                                column=i-57+2)
for i in range(90, 104):  # f block 
	    Button(ptFrame, text=bigdict[i][1], font=('Comic Sans Ms', 19),
	           command=lambda i=i: search(i, 'Atomic Number',way='PT'), fg='blue').grid(row=10,
                                                                                                column=i-89+2)

#To show the periodic table image
#__________________________________________________________________________

imgFrame = LabelFrame(pt_notebook)#Creating the main frame for adding the image
imgFrame.grid(row=1, column=1, columnspan=3, rowspan=2,sticky=W+E)
pt_notebook.add(imgFrame,text='  Periodic Table Image   ')

#Creating a canvas
ptCanvas=Canvas(imgFrame,width=1300,height=584)
ptCanvas.grid(row=0,column=0,sticky=W+E)

#Add a scrollbar to the canvas
pt_scrollbarY=ttk.Scrollbar(imgFrame,orient=VERTICAL,command=ptCanvas.yview)
pt_scrollbarY.grid(row=0,column=1,sticky=N+S)

pt_scrollbarX=ttk.Scrollbar(imgFrame,orient=HORIZONTAL,command=ptCanvas.xview)
pt_scrollbarX.grid(row=1,column=0,sticky=W+E)

#Configure the canvas
ptCanvas.configure(yscrollcommand=pt_scrollbarY.set)
ptCanvas.bind('<Configure>',lambda e:ptCanvas.configure(scrollregion=ptCanvas.bbox('all')))

ptCanvas.configure(xscrollcommand=pt_scrollbarX.set)
ptCanvas.bind('<Configure>',lambda e:ptCanvas.configure(scrollregion=ptCanvas.bbox('all')))


#Create another frame inside the canvas
periodictableimage=ImageTk.PhotoImage(Image.open('periodictable.png'))
periodictableFrame=Frame(ptCanvas)

#Add that New frame to a window in the canvas
ptCanvas.create_window((3,3),window=periodictableFrame,anchor=NW)

#Opening the image
ptimg=(Image.open('periodictable.png'))

#Resizing the image

ptimg=ImageTk.PhotoImage(ptimg)
ptimgLabel=Label(periodictableFrame,image=ptimg)
ptimgLabel.grid(row=0,column=0)
#	_______________________________________________________________________




#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Making the the help screen
#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

HelpFrame=Frame(my_notebook,padx=12,pady=10)
HelpFrame.pack(fill='both',expand=1)
my_notebook.add(HelpFrame,text='   Help   ')




#____________________________________________________________________________________________________________
#------------------------------------------------------------------------------------------------------------
#____________________________________________________________________________________________________________

mainloop()