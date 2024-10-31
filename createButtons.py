import pygame
import button
from attributes import Button_Type, MR_Button_Attributes, TL_Button_Attributes, TR_Button_Attributes, L_Button_Attributes

pygame.init()
class ButtonList():
    def __init__(self):
        # Play Button
        button1 = button.Button('Play', (700, 11), TR_Button_Attributes, Button_Type.PlayButton)

        # Mid Right Buttons
        button2 = button.Button('ReadMe', (690, 65), MR_Button_Attributes, Button_Type.ReadMeButton)
        button6 = button.Button('Code', (855, 65), MR_Button_Attributes, Button_Type.CodeButton)

        # Top Left Button
        button5 = button.Button('Algo Visualizer', (33, 20), TL_Button_Attributes, Button_Type.WelcomeButton)

        # Left Buttons
        button3 = button.Button('Binary Search', (30, 85), L_Button_Attributes, Button_Type.AlgoButton)
        button16 = button.Button('Bubble Sort', (30, 135), L_Button_Attributes, Button_Type.AlgoButton)
        button4 = button.Button('Topological Sort', (30, 185), L_Button_Attributes, Button_Type.AlgoButton)
        button7 = button.Button('BFS', (30, 235), L_Button_Attributes, Button_Type.AlgoButton)
        button8 = button.Button('DFS', (30, 285), L_Button_Attributes, Button_Type.AlgoButton)
        button9 = button.Button('Floyds Algorithm', (30, 335), L_Button_Attributes, Button_Type.AlgoButton)
        button10 = button.Button('Bucket Sort', (30, 385), L_Button_Attributes, Button_Type.AlgoButton)
        button11 = button.Button('Union-Find', (30, 435), L_Button_Attributes, Button_Type.AlgoButton)
        button12 = button.Button('Dijkstra Algorithm', (30, 485), L_Button_Attributes, Button_Type.AlgoButton)
        button13 = button.Button('Prims Algorithm', (30, 535), L_Button_Attributes, Button_Type.AlgoButton,)
        button14 = button.Button('Kruskal Algorithm', (30, 585), L_Button_Attributes, Button_Type.AlgoButton)
        button15 = button.Button('Bellman-Ford', (30, 635), L_Button_Attributes, Button_Type.AlgoButton)

        self.button_list = [button1, button2, button3, 
                            button4, button5, button6, 
                            button7, button8, button9, 
                            button10, button11, button12, 
                            button13, button14, button15, 
                            button16]
                
    def get_button(self):
        return self.button_list