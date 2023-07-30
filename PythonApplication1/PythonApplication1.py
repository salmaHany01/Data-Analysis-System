from tkinter import *
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as stat
from scipy.stats import iqr
from sklearn import linear_model



root = Tk()
root.title('statistical analysis')
root.geometry('1000x700')
root.resizable(False, False)


notebook = ttk.Notebook(root)
myFrame = ttk.Frame(notebook, width=900, height=680)
myFrame.grid(pady=50, padx=5)
 #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2

notebook.add(tab1,text="Numerical Data")
notebook.add(tab2,text="Categorical Data")
'''notebook.pack(expand=True,fill="both")'''  #expand = expand to fill any space not otherwise used
notebook.pack()                                     #fill = fill space on x and y axis
data_panel=ttk.LabelFrame(tab1, text="Dataset Display", width=1000, height=300)
data_panel.pack(pady=10, padx=3)
data_panel.pack_propagate(False)

data= pd.read_csv(r'C:\Users\Salma\Downloads\StudentsPerformance.csv')
tv1 = ttk.Treeview(data_panel)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(data_panel, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(data_panel, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y")

tv1["column"] = list(data.columns)
tv1["show"] = "headings"
for column in tv1["columns"]:
        tv1.heading(column, text=column)
df_rows = data.to_numpy().tolist()
for row in df_rows:
        tv1.insert("", "end", values=row)

#Saved to get the text of the button to access a column
textOfBtn = str()
textOfBtn2= str()

#Takes the text of  button
def getColumnName(btn):
   global textOfBtn
   textOfBtn = btn['text']
   label_select.config(text = textOfBtn) 
 

def getColumnName2(btn):
   global textOfBtn2
   textOfBtn2 = btn['text']
   label_select2.config(text= textOfBtn2)

#Function check if the user pressed a column
def isPressed(columnName):
    if columnName == '':
        messagebox.showinfo("Warning", "Please Select a Column First")
        return False
    else:
        return True

#Function Mean
def getMean(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     print("Mean of column " + columnName + " " + str(np.mean(columnData)) + "\n")
     label_answer.config(text = "Mean of column " + columnName + " " + str(np.mean(columnData))) 
   

#Function Median
def getMedian(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     print("Median of column " + columnName + " " + str(np.median(columnData)) + "\n")
     label_answer.config(text= "Median of column " + columnName + " " + str(np.median(columnData)))

#Function Mode
def getMode(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     label_answer.config(text =str(stat.mode(columnData)))
    

#Function Mode Categorical
def getMode2(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     label_answer2.config(text =str(stat.mode(columnData)))


   #Function Range
def getRange(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     range = max(columnData) - min(columnData)
     label_answer.config(text= "Range of column " + columnName + " " + str(range))
     


#Function SD
def getSD(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     standD = np.std(columnData)
     label_answer.config(text= "Standard Diviation of column "  + columnName + " "  + str(standD))

#Function Variance
def getVariance(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     standD = np.std(columnData)
     var = standD * standD
     label_answer.config(text= "Variance of column "  + columnName + " "  + str(var))

#Function IQR
def getIQR(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     iqr1 = iqr(columnData)
     label_answer.config(text= "IQR of Column " + columnName + " " + str(iqr1))

#Function boxplot
def getBox(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     sns.boxplot(x=columnName, data= data)
     plt.show()

#Function outliers
treshold = 3

def detect_outliers(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     outliers = []
     mean = np.mean(columnData)
     std = np.std(columnData)
     for i in columnData:
         z_score = (i - mean)/std
         if np.abs(z_score) > treshold:
             outliers.append(i)
     print(outliers)
     label_answer.config(text= str(outliers))
     


#Function Histogram
def showHist(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     sns.displot(columnData)
     plt.show()

#Function Scatter
def showScatter():
    label_relation.config(text= "positive strong relationship")
    plt.xlabel("math score")
    plt.ylabel("reading score")
    plt.scatter(data[['math score']], data[['reading score']])
    reg = linear_model.LinearRegression()
    reg.fit(data[['math score']], data[['reading score']])
    plt.plot(data[['math score']], reg.predict(data[['math score']]), color = 'red')
    plt.show()
    plt.show()
    reg = linear_model.LinearRegression()
    reg.fit(data[['math score']], data[['reading score']])
    

#Function Correlation
def showCorrelation():
    correlation = data.corr()
    sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns
            , annot=True)
    plt.show()

#Function piechart
def showPieChar(columnName):
    if isPressed(columnName):
     print(columnName)
     columnData = data[columnName]
     columnData.value_counts().plot(kind='pie')
     plt.show()



#1st panel

columns_panel=ttk.LabelFrame(tab1, text="Columns", width=300, height=500)
columns_panel.pack(side="left")
columns_panel.grid_propagate(False)
columns_panel.grid_columnconfigure(0, weight=1)


operation_panel=ttk.LabelFrame(tab1, text="Calculate", width=300, height=500)
operation_panel.pack(side="left")
operation_panel.grid_propagate(False)
operation_panel.grid_columnconfigure(0, weight=1)
operation_panel.grid_columnconfigure(1, weight=1)



graph_panel=ttk.LabelFrame(tab1, text="Graph", width=310, height=500)
graph_panel.pack(side="left")
graph_panel.grid_propagate(False)
graph_panel.grid_columnconfigure(0, weight=1)

label_col=Label(columns_panel, text="you have selected:")
label_col.pack()
label_col.grid(row=0, columnspan=2, pady=(15,0))
label_select=Label(columns_panel, text='', pady=3)
label_select.pack()
label_select.grid(row=1, columnspan=2)

button2= tk.Button(columns_panel, text="math score", width=20, height=2, command = lambda:getColumnName(button2))
button2.pack()
button2.grid(row=2, columnspan=2, pady=(7,4))
button3= tk.Button(columns_panel, text="reading score", width=20, height=2, command = lambda:getColumnName(button3))
button3.pack()
button3.grid(row=3, columnspan=2, pady=4)
button4= tk.Button(columns_panel, text="writing score", width=20, height=2, command = lambda:getColumnName(button4))
button4.pack()
button4.grid(row=4, columnspan=2, pady=4)

label_val=Label(operation_panel, text="Calculated Value = ")
label_val.pack()
label_val.grid(row=0, columnspan=2, pady=(15,0))
label_answer=Label(operation_panel, text='', wraplength= 310, justify= "center", pady=3)
label_answer.pack()
label_answer.grid(rows=1, columnspan=2)
button5= tk.Button(operation_panel, text="Mean", width=15, height=2, command =lambda:getMean(textOfBtn))
button5.pack()
button5.grid(row=3, column=0, pady=(6,4))
button6= tk.Button(operation_panel, text="Mode", width=15, height=2, command =lambda:getMode(textOfBtn))
button6.pack()
button6.grid(row=3, column=1, pady=(6,4))
button7= tk.Button(operation_panel, text="Median", width=15, height=2, command =lambda:getMedian(textOfBtn))
button7.pack()
button7.grid(row=4, column=0, pady=4)
button8= tk.Button(operation_panel, text="IQR", width=15, height=2, command =lambda:getIQR(textOfBtn))
button8.pack()
button8.grid(row=4, column=1, pady=4)
button9= tk.Button(operation_panel, text="Range", width=15, height=2, command =lambda:getRange(textOfBtn))
button9.pack()
button9.grid(row=5, column=0, pady=4)
button10= tk.Button(operation_panel, text="Variance", width=15, height=2, command =lambda:getVariance(textOfBtn))
button10.pack()
button10.grid(row=5, column=1, pady=4)
button11= tk.Button(operation_panel, text="Standard Deviation", width=15, height=2, command =lambda:getSD(textOfBtn))
button11.pack()
button11.grid(row=6, column=0, pady=4)
button12= tk.Button(operation_panel, text="Outliers", width=15, height=2, command =lambda:detect_outliers(textOfBtn))
button12.pack()
button12.grid(row=6, column=1, pady=4)

button13= tk.Button(graph_panel, text="Histogram", width=20, height=2, command =lambda:showHist(textOfBtn))
button13.pack()
button13.grid(row=0, columnspan=2, pady=(25,4))
button14= tk.Button(graph_panel, text="Pie Chart", width=20, height=2, command =lambda:showPieChar(textOfBtn))
button14.pack()
button14.grid(row=1, pady=4)
button15= tk.Button(graph_panel, text="Box Plot", width=20, height=2, command =lambda:getBox(textOfBtn))
button15.pack()
button15.grid(row=2, pady=4)

button21= tk.Button(graph_panel, text ="Correlation" ,width=20, height=2, command =showCorrelation)
button21.pack()
button21.grid(row=3, pady=4)
label_relation=Label(graph_panel, text='-relationship type-', wraplength= 310, justify= "center", pady=3)
label_relation.pack()
label_relation.grid(row=4, columnspan=2)

button16 = tk.Button(graph_panel, text = 'Scatter Plot*',width=20, height=2, command = showScatter)
button16.pack()
button16.grid(row=5, pady=4)
label_sp=Label(graph_panel, text="*for Math and Reading Score only", font="arial 8 italic")
label_sp.pack()
label_sp.grid(row=6)

#panel 2

#data set display 2
data_panel2=ttk.LabelFrame(tab2, text="Dataset Display", width=900, height=300)
data_panel2.pack(pady=10, padx=5)
data_panel2.pack_propagate(False)

data= pd.read_csv(r'C:\Users\DELL\Downloads\StudentsPerformance.csv - Sheet1.csv')
tv2 = ttk.Treeview(data_panel2)
tv2.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly2 = tk.Scrollbar(data_panel2, orient="vertical", command=tv2.yview) 
treescrollx2 = tk.Scrollbar(data_panel2, orient="horizontal", command=tv2.xview) 
tv1.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) 
treescrollx2.pack(side="bottom", fill="x") 
treescrolly2.pack(side="right", fill="y")

tv2["column"] = list(data.columns)
tv2["show"] = "headings"
for column in tv2["columns"]:
        tv2.heading(column, text=column)
df_rows = data.to_numpy().tolist()
for row in df_rows:
        tv2.insert("", "end", values=row)

#2nd columns display
columns_panel2=ttk.LabelFrame(tab2, text="Columns", width=300, height=500)
columns_panel2.pack(side="left")
columns_panel2.grid_propagate(False)
columns_panel2.grid_columnconfigure(0, weight=1)

label_col2=Label(columns_panel2, text="you have selected:")
label_col2.pack()
label_col2.grid(row=0, columnspan=2, pady=(15,0))
label_select2=Label(columns_panel2, text='', pady=3)
label_select2.pack()
label_select2.grid(row=1, columnspan=2)

'''label_col2=Label(columns_panel2, text="you have selected:", pady=5)
label_col2.pack()
label_select2=Label(columns_panel2, text='', pady=10)
label_select2.pack()'''

button17= tk.Button(columns_panel2, text="gender", width=20, height=2, command = lambda:getColumnName2(button17))
button17.pack()
button17.grid(row=2, columnspan=2, pady=(6,4))
button18= tk.Button(columns_panel2, text="race/ethnicity", width=20, height=2, command = lambda:getColumnName2(button18))
button18.pack()
button18.grid(row=3, columnspan=2, pady=4)
button19= tk.Button(columns_panel2, text="parental level of education", width=20, height=2, command = lambda:getColumnName2(button19))
button19.pack()
button19.grid(row=4, columnspan=2, pady=4)
button20= tk.Button(columns_panel2, text="lunch", width=20, height=2, command = lambda:getColumnName2(button20))
button20.pack()
button20.grid(row=5, columnspan=2, pady=4)
button24= tk.Button(columns_panel2, text="test preparation course", width=20, height=2, command = lambda:getColumnName2(button24))
button24.pack()
button24.grid(row=6, columnspan=2, pady=4)


operation_panel2=ttk.LabelFrame(tab2, text="Calculate", width=300, height=500)
operation_panel2.pack(side="left")
operation_panel2.grid_propagate(False)
operation_panel2.grid_columnconfigure(0, weight=1)

label_val2=Label(operation_panel2, text="Calculated Value = ")
label_val2.pack()
label_val2.grid(row=0, columnspan=2, pady=(15,0))
label_answer2=Label(operation_panel2, text='', wraplength= 310, justify= "center", pady=3)
label_answer2.pack()
label_answer2.grid(rows=1, columnspan=2)


button26= tk.Button(operation_panel2, text="Mode", width=15, height=2, command =lambda:getMode2(textOfBtn2))
button26.pack()
button26.grid(row=2, columnspan=2, pady=(6,4))


#2nd graphs options display
graph_panel2=ttk.LabelFrame(tab2, text="Graph", width=300, height=500)
graph_panel2.pack(side="left")
graph_panel2.grid_propagate(False)
graph_panel2.grid_columnconfigure(0, weight=1)

button22= tk.Button(graph_panel2, text="Histogram", width=20, height=2, command =lambda:showHist(textOfBtn2))
button22.pack()
button22.grid(row=0, columnspan=2, pady=(65,10))
button23= tk.Button(graph_panel2, text="Pie Chart", width=20, height=2, command =lambda:showPieChar(textOfBtn2))
button23.grid(row=1, columnspan=2, pady=10)






root.mainloop()