# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:32:43 2021

@author: aisha
"""

def calculate_square_area(side: float): 
    return side * side

def calculate_rectangle_area(length: float, width: float):
    return length * width

def calculate_circle_area(radius: float):
    pi= 3.14
    return pi * radius ** 2
def calculate_rhombus_area(side1: float, side2: float):
    return (side1 * side2)/2

print("""
      ------------
      Area calculator
      ---------------
      Select a shape: 
          """)
    
selection = input("""\t'S' - Square
                      \t'R' - Rectangle
                      \t'C' - Circle
                      \t'B' - Rhombus
                      """)
def calculate_area(selection):
    area = 0
    
    if selection == 'S':
        side = input("Enter the side: ")
        area = calculate_square_area(float(side))
    elif selection == 'R':
        length = input("Enter the length: ")
        width = input("Enter the width: ")
        area = calculate_rectangle_area(float(length), float(width))
    elif selection == 'C':
        radius = input("Enter the radius: ")
        area = calculate_circle_area(float(radius))
        #Add logic to calculate rhombus area
    elif selection == 'B':
        side1 = input("Enter the diagonal 1: ")
        side2 = input("Enter the diagonal 2: ")
        area = calculate_rhombus_area(float(side1), float(side2))
    else:
        print("Invalid selection. Choose 'S', 'R', 'C', or 'B'")
    return area
       

def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == 'C':
        shape = "circle"
    elif tag == 'B':
        shape = "rhombus"
        #add option for rhombus
    return shape

area = calculate_area(selection)

print(f"The area of the {get_shape_name(selection)} is {area}")