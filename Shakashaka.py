# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:02:07 2023

@author: thoidaipc
"""
import tkinter as tk
from tkinter import PhotoImage, Tk, Label, Entry, Button, messagebox, Toplevel, Canvas
import tkinter

# Tạo cửa sổ mới
window = Tk()
window.attributes('-topmost', True)

fnt = ("Comic Sans MS", 10, "bold")
window.title("Shakashaka")
def create_first_table(A, B):
    # Tạo Canvas
    canvas = Canvas(window, width=50 * len(A), height=57 * len(A))
    canvas.pack()
    def reset():
        for i in range(len(B)):
            for j in range(len(B[i])):
                if B[i][j] == "b":
                        color = "black"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                elif B[i][j] == 'w':
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] >= 0:
                    color = "black"
                    text_color = "white"
                    canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                    canvas.create_text(j * 50 + 25, i * 50 + 25, text=A[i][j], fill=text_color, font=('Helvetica','30','bold'))
    reset = Button(window, width = 4, height = 1, text = 'Reset', font = fnt, bg = 'pink', command = reset)
    reset.place(x= 28*len(A), y = 52*len(A))
    def solve():
        try:
            save_data(linear_programming(B, A),A)
        except:
            tkinter.messagebox.showerror(title="Error", message="Đầu vào có lỗi!")
    button = Button(window, width = 4, height = 1, text = 'Solve', bg = 'pink', font = fnt, command = solve)
    button.place(x= 15*len(A), y = 52*len(A))
    
    # Vẽ bảng mới
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] == "b":
                    color = "black"
                    canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
            elif B[i][j] == 'w':
                    color = "white"
                    canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] >= 0:
                color = "black"
                text_color = "white"
                canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                canvas.create_text(j * 50 + 25, i * 50 + 25, text=A[i][j], fill=text_color, font=('Helvetica','30','bold'))
    def save_data(A,B):
        n = len(A)
        # Vẽ bảng mới
        for i in range(n):
            for j in range(n):
                    if A[i][j] == "b":
                        color = "black"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                    elif A[i][j] == "w":
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                    elif A[i][j] == "lt":
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                        color = "black"
                        canvas.create_polygon(j*50,i*50,j*50+50,i*50,j*50,i*50+50,fill=color, outline="gray")
                    elif A[i][j] == "lb":
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                        color = "black"
                        canvas.create_polygon(j*50,i*50,j*50+50,i*50+50,j*50,i*50+50,fill=color, outline="gray")
                    elif A[i][j] == "rt":
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                        color = "black"
                        canvas.create_polygon(j*50,i*50,j*50+50,i*50,j*50+50,i*50+50,fill=color, outline="gray")
                    elif A[i][j]== "rb":
                        color = "white"
                        canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                        color = "black"
                        canvas.create_polygon(j*50+50,i*50,j*50+50,i*50+50,j*50,i*50+50,fill=color, outline="gray")
                        
        for i in range(len(B)):
            for j in range(len(B[i])):
                if B[i][j] >=0:
                    color = "black"
                    text_color = "white"
                    canvas.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=color, outline="gray")
                    canvas.create_text(j * 50 + 25, i * 50 + 25, text=B[i][j], fill=text_color, font=('Helvetica','30','bold'))
    window.mainloop()

def linear_programming(A, B):
    import numpy as np
    import gurobipy as gp
    from gurobipy import GRB
    from gurobipy import quicksum


    model = gp.Model("Shakashaka")   
    N = len(A)
    x = {}
    for i in range(N):
        for j in range(N):
            for k in range(5):
                x[i,j,k] = model.addVar(vtype = GRB.BINARY)
    # Constraint 1:
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'w':
                model.addConstr(quicksum(x[i,j,k] for k in range(5)) == 1)
            else:
                for k in range(5):
                    model.addConstr(x[i,j,k] == 0)
        
    # Constraint 2
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'b':
                if i == 0 and j == 0:
                    model.addConstr(x[i+1,j,2]+x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j+1,2]+x[i,j+1,3]+x[i,j+1,4] == 0)
                elif i == 0 and j == N - 1:
                    model.addConstr(x[i+1,j,1] + x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j-1,1] + x[i,j-1,3]+x[i,j-1,4] == 0)
                elif i == N - 1 and j == 0:
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2] + x [i-1,j,4] == 0)
                    model.addConstr(x[i,j+1,1] + x[i,j+1,2]+x[i,j+1,4] == 0)
                elif i == N - 1 and j == N - 1:
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2] + x[i-1,j,3] == 0)
                    model.addConstr(x[i,j-1,1]+x[i,j-1,2]+ x[i,j-1,3] == 0)
                elif i == 0 :
                    model.addConstr(x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j-1,1]+x[i,j-1,3]+x[i,j+1,2]+x[i,j+1,4] == 0)
                elif j == 0 :
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2]+x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j+1,2]+x[i,j+1,4] == 0)
                elif i == N -1:
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2]== 0)
                    model.addConstr(x[i,j-1,1]+x[i,j-1,3]+x[i,j+1,2]+x[i,j+1,4] == 0)
                elif j == N -1:
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2]+x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j-1,1]+x[i,j-1,3] == 0)
                else:   
                    model.addConstr(x[i-1,j,1]+x[i-1,j,2]+x[i+1,j,3]+x[i+1,j,4] == 0)
                    model.addConstr(x[i,j-1,1]+x[i,j-1,3]+x[i,j+1,2]+x[i,j+1,4] == 0)
            if B[i][j] != -1:
                if i == 0 and j == 0:
                    model.addConstr((x[i+1,j,1]+x[i,j+1,1]) == B[i][j])
                elif i == 0 and j == N - 1:
                    model.addConstr((x[i+1,j,2]+ x[i,j-1,2]) == B[i][j])
                elif i == N - 1 and j == 0:
                    model.addConstr((x[i-1,j,3]+x[i,j+1,3]) == B[i][j])
                elif i == N - 1 and j == N - 1:
                    model.addConstr((x[i-1,j,4]+x[i,j-1,4]) == B[i][j])
                elif i == 0 :
                    model.addConstr((x[i+1,j,1]+x[i+1,j,2]
                                    + x[i,j-1,2]+x[i,j+1,1]) == B[i][j])
                elif j == 0 :
                    model.addConstr((x[i-1,j,3]+x[i+1,j,1]
                                    + x[i,j+1,3] + x[i,j+1,1]) == B[i][j])
                elif i == N - 1 :
                    model.addConstr((x[i-1,j,3]+x[i-1,j,4]
                                    +x[i,j-1,4]+x[i,j+1,3]) == B[i][j])
                elif j == N - 1 :
                    model.addConstr((x[i-1,j,4]+x[i+1,j,2]
                                    + x[i,j-1,2]+x[i,j-1,4]) == B[i][j])
                else:   
                    model.addConstr((x[i-1,j,3]+x[i-1,j,4]+x[i+1,j,1]+x[i+1,j,2]
                                    + x[i,j-1,2]+x[i,j-1,4]+x[i,j+1,1]+x[i,j+1,3]) == B[i][j])

    # Constraint 3
    for i in range(N):
        for j in range(N):
            if A[i][j] == 'w':
                if i == 0 and j == 0:
                    model.addConstr(x[i,j,1]<=x[i,j+1,2])
                    model.addConstr(x[i,j,1]<=x[i+1,j,3])
                    model.addConstr(x[i,j,2] + x[i,j,3] + x[i,j,4] == 0)
                elif i == 0 and j == N - 1:
                    model.addConstr(x[i,j,2]<=x[i+1,j,4])
                    model.addConstr(x[i,j,2]<=x[i,j-1,1])
                    model.addConstr(x[i,j,1] + x[i,j,3] + x[i,j,4] == 0)
                elif i == N - 1 and j == 0:
                    model.addConstr(x[i,j,3]<=x[i,j+1,4])
                    model.addConstr(x[i,j,3]<=x[i-1,j,1])
                    model.addConstr(x[i,j,2] + x[i,j,1] + x[i,j,4] == 0)
                elif i == N - 1 and j == N - 1:
                    model.addConstr(x[i,j,4]<=x[i-1,j,2])
                    model.addConstr(x[i,j,4]<=x[i,j-1,3])
                    model.addConstr(x[i,j,2] + x[i,j,3] + x[i,j,1] == 0)
                elif i == 0 :
                    model.addConstr(x[i,j,1]<=x[i,j+1,2])
                    model.addConstr(x[i,j,1]<=x[i+1,j,3]+x[i+1,j-1,1])
                    model.addConstr(x[i,j,1] + x[i+1,j-1,1]<=x[i+1,j,0]+1)
                    
                    model.addConstr(x[i,j,2]<=x[i+1,j,4]+x[i+1,j+1,2])
                    model.addConstr(x[i,j,2] + x[i+1,j+1,2]<=x[i+1,j,0]+1)
                    model.addConstr(x[i,j,2]<=x[i,j-1,1])
                    
                    model.addConstr(x[i,j,3] + x[i,j,4] == 0)
                
                elif j == 0 :
                    model.addConstr(x[i,j,1]<=x[i,j+1,3]+x[i-1,j+1,1])
                    model.addConstr(x[i,j,1] + x[i-1,j+1,1]<=x[i,j+1,0]+1)
                    model.addConstr(x[i,j,1]<=x[i+1,j,3])
                                        
                    model.addConstr(x[i,j,3]<=x[i,j+1,4]+x[i+1,j+1,3])
                    model.addConstr(x[i,j,3] + x[i+1,j+1,3]<=x[i,j+1,0]+1)
                    model.addConstr(x[i,j,3]<=x[i-1,j,1])
                    
                    model.addConstr(x[i,j,2]+x[i,j,4] == 0)
                  
                elif i == N -1:
                            
                    model.addConstr(x[i,j,3]<=x[i,j+1,4])
                    model.addConstr(x[i,j,3]<=x[i-1,j,1]+x[i-1,j-1,3])
                    model.addConstr(x[i,j,3] + x[i-1,j-1,3]<=x[i-1,j,0]+1)
                    
                    model.addConstr(x[i,j,4]<=x[i-1,j,2]+x[i-1,j+1,4])
                    model.addConstr(x[i,j,4] + x[i-1,j+1,4]<=x[i-1,j,0]+1)
                    model.addConstr(x[i,j,4]<=x[i,j-1,3])
                    
                    model.addConstr(x[i,j,1]+x[i,j,2] == 0)
                    
                elif j == N -1:
                    model.addConstr(x[i,j,2]<=x[i+1,j,4])
                    model.addConstr(x[i,j,2]<=x[i-1,j-1,2]+x[i,j-1,1])
                    model.addConstr(x[i,j,2] + x[i-1,j-1,2]<=x[i,j-1,0]+1)
                            
                    model.addConstr(x[i,j,4]<=x[i-1,j,2])
                    model.addConstr(x[i,j,4]<=x[i,j-1,3]+x[i+1,j-1,4])
                    model.addConstr(x[i,j,4] + x[i+1,j-1,4]<=x[i,j-1,0]+1)
                    
                    model.addConstr(x[i,j,1]+x[i,j,3] == 0)
                
                else:           
                    model.addConstr(x[i,j,1]<=x[i,j+1,2]+x[i-1,j+1,1])
                    model.addConstr(x[i,j,1] + x[i-1,j+1,1]<=x[i,j+1,0]+1)
                    model.addConstr(x[i,j,1]<=x[i+1,j,3]+x[i+1,j-1,1])
                    model.addConstr(x[i,j,1] + x[i+1,j-1,1]<=x[i+1,j,0]+1)
                    
                    model.addConstr(x[i,j,2]<=x[i+1,j,4]+x[i+1,j+1,2])
                    model.addConstr(x[i,j,2] + x[i+1,j+1,2]<=x[i+1,j,0]+1)
                    model.addConstr(x[i,j,2]<=x[i-1,j-1,2]+x[i,j-1,1])
                    model.addConstr(x[i,j,2] + x[i-1,j-1,2]<=x[i,j-1,0]+1)
                            
                    model.addConstr(x[i,j,3]<=x[i,j+1,4]+x[i+1,j+1,3])
                    model.addConstr(x[i,j,3] + x[i+1,j+1,3]<=x[i,j+1,0]+1)
                    model.addConstr(x[i,j,3]<=x[i-1,j,1]+x[i-1,j-1,3])
                    model.addConstr(x[i,j,3] + x[i-1,j-1,3]<=x[i-1,j,0]+1)
                    
                    model.addConstr(x[i,j,4]<=x[i-1,j,2]+x[i-1,j+1,4])
                    model.addConstr(x[i,j,4] + x[i-1,j+1,4]<=x[i-1,j,0]+1)
                    model.addConstr(x[i,j,4]<=x[i,j-1,3]+x[i+1,j-1,4])
                    model.addConstr(x[i,j,4] + x[i+1,j-1,4]<=x[i,j-1,0]+1) 
    
           
    # Constraint 4
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                model.addConstr(x[i,j,1]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
            elif i == 0 and j == N - 1:
                model.addConstr(x[i,j,2]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
            elif i == N - 1 and j == 0:
                model.addConstr(x[i,j,3]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
            elif i == N - 1 and j == N - 1:
                model.addConstr(x[i,j,4]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
                
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
            elif i == 0 :
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                
                model.addConstr(x[i,j,1]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,2]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)  
            elif j == 0 :
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                
                model.addConstr(x[i,j,1]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,3]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
            elif i == N -1:                       
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
                
                model.addConstr(x[i,j,3]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                model.addConstr(x[i,j,4]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
            elif j == N -1:
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
            
                model.addConstr(x[i,j,2]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                model.addConstr(x[i,j,4]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
            else:
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,0]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                model.addConstr(x[i,j,0]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
                
                model.addConstr(x[i,j,1]+x[i,j+1,0]+x[i+1,j,0] <= x[i+1,j+1,0]+x[i+1,j+1,4]+2)
                model.addConstr(x[i,j,3]+x[i,j+1,0]+x[i-1,j,0] <= x[i-1,j+1,0]+x[i-1,j+1,2]+2)
                model.addConstr(x[i,j,2]+x[i,j-1,0]+x[i+1,j,0] <= x[i+1,j-1,0]+x[i+1,j-1,3]+2)
                model.addConstr(x[i,j,4]+x[i,j-1,0]+x[i-1,j,0] <= x[i-1,j-1,0]+x[i-1,j-1,1]+2)
   
    model.setObjective(0, sense = GRB.MINIMIZE)
    model.optimize()
    array = [i.x for i in model.getVars()]
    result = []
    for i in range(0,len(array),5):
        if array[i] == 1.0:
            result.append('w')
        elif array[i+1] == 1.0:
            result.append('lt')
        elif array[i+2] == 1.0:
            result.append('rt')
        elif array[i+3] == 1.0:
            result.append('lb')
        elif array[i+4] == 1.0:
            result.append('rb')
        else:
            result.append('b')
    result = np.array(result).reshape(N,N).tolist()
    return result

# create_main_window()
A=[[-1,1,-1,-1,-1,-1,2],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,2,-1,-1,-1],
   [2,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,2,-1,-1]]
B=[['w','b','b','w','w','w','b'], 
   ['b','w','w','b','w','w','w'],
   ['w','w','w','b','w','w','w'],
   ['b','w','w','w','w','w','b'],
   ['w','w','w','w','w','w','b'],
   ['w','w','w','w','w','w','b'],
   ['b','b','w','w','b','b','b']]

C = [['w', 'b', 'b', 'w', 'lt', 'rt', 'b'], ['b', 'lt', 'w', 'b', 'lb', 'w', 'rt'], ['w', 'w', 'w', 'b', 'lt', 'w', 'w'], ['b', 'lb', 'w', 'rt', 'w', 'w', 'b'], ['lt', 'w', 'w', 'w', 'w', 'w', 'b'], ['w', 'w', 'w', 'w', 'rb', 'w', 'b'], ['b', 'b', 'w', 'rb', 'b', 'b', 'b']]
'''
C=[['w','b','b','w','lt','rt','b'],
   ['b','lt','rt','b','lb','w','rt'],
   ['w','lb','rb','b','w','lb','rb'],
   ['b','lt','rt','lt','rt','w','b'],
   ['lt','w','rb','lb','w','rt','b'],
   ['lb','rb','lt','rt','lb','rb','b'],
   ['b','b','lb','rb','b','b','b']]
'''
A_1 = [[-1,1,-1,-1,-1,-1,2],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,2,-1,-1,-1],
   [2,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,2,-1,-1]]
B_1 = [['w','b','b','w','w','w','b'], 
   ['b','w','w','b','w','w','w'],
   ['w','w','w','b','w','w','w'],
   ['b','w','w','w','w','w','b'],
   ['w','w','w','w','w','w','b'],
   ['w','w','w','w','w','w','b'],
   ['b','b','w','w','b','b','b']]

A_2 = [[-1,-1,-1,-1,-1,-1,1],
     [0,-1,2,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,-1],
     [2,-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,3],
     [-1,-1,-1,-1,-1,-1,-1],
     [-1,-1,1,-1,-1,-1,-1]]

B_2 = [['w','b','b','w','w','w','b'], 
   ['b','w','b','w','w','w','b'],
   ['w','b','w','w','w','w','w'],
   ['b','w','w','w','w','w','w'],
   ['w','w','w','w','w','w','b'],
   ['w','w','w','w','w','w','w'],
   ['b','b','b','w','w','w','w']] 

A_3 = [[-1,-1,0,-1,-1,2,-1,-1],
       [0,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,2,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,1],
       [0,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,2,-1,-1],
       [-1,-1,-1,2,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,1]]

B_3 = [['w','b','b','w','w','b','w','w'],
       ['b','w','b','b','b','w','w','w'],
       ['w','w','w','b','w','w','w','b'],
       ['w','w','w','w','w','b','w','b'],
       ['b','w','w','w','w','w','w','w'],
       ['w','b','b','w','w','w','w','w'],
       ['b','w','w','b','w','w','w','b'],
       ['b','b','b','b','b','w','w','b']]

A_4 = [[-1,-1,1,-1,-1,-1,0,-1,-1,1],
       [1,-1,-1,1,1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,2,-1,-1,-1,5,1,1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [1,-1,-1,-1,3,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,1],
       [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
       [-1,-1,-1,-1,2,-1,0,-1,-1,-1],
       [1,-1,-1,-1,-1,-1,-1,-1,0,-1]]

B_4 = [['w','w','b','b','w','w','b','b','w','b'],
       ['b','w','w','b','b','b','w','w','w','w'],
       ['b','w','w','w','w','w','w','w','w','w'],
       ['w','b','w','b','w','w','b','b','w','b'],
       ['w','w','w','w','w','b','w','w','w','b'],
       ['b','w','w','w','b','w','w','w','w','b'],
       ['w','b','w','w','w','w','w','w','w','b'],
       ['b','w','w','w','w','w','w','w','w','b'],
       ['w','w','w','w','b','w','b','w','w','b'],
       ['b','w','w','b','b','b','b','b','b','b']]
# A_4 = [[4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4],
#        [4,4,4,4,4,4,4,4,4,4,4]]

# B_4 = [['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b'],
#        ['b','b','b','b','b','b','b','b','b','b','b']]
create_first_table(A_4, B_4)
# save_data(C,A)