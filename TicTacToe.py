# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:32:21 2020

@author: Janani
"""

game = [[1,0,2],
        [2,2,2],
        [1,2,1]]


def win(game):
    # Horizontal
    for row in game:
        #print(row)
        if row.count(row[0]) == len(row) and row[0] !=0:
            print(f"Player {row[0]} is the winner horizontally!")
            
    # Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
           
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")
            
    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
        if diags.count(diags[0]) == len(diags) and diags[0] !=0:
            print(f"Player {diags[0]} is the winner diagonally(/)!")
    
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] !=0:
            print(f"Player {diags[0]} is the winner diagonally(\\)!")
            
            
win(game)
        
    