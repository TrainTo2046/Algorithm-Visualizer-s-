import pygame
from button import Button
from attributes import Button_Type, MR_Button_Attributes, TL_Button_Attributes, TR_Button_Attributes, L_Button_Attributes

pygame.init()
class ButtonList():
    def __init__(self, program):
        self.program = program
        # Play Button
        playButton = Button(self.program, 'Play', (700, 11), TR_Button_Attributes, Button_Type.PlayButton)

        # Mid Right Buttons
        readMeButton = Button(self.program, 'ReadMe', (690, 65), MR_Button_Attributes, Button_Type.ReadMeButton)
        codeButton = Button(self.program, 'Code', (855, 65), MR_Button_Attributes, Button_Type.CodeButton)

        # Top Left Button
        homeButton = Button(self.program, 'Algo Visualizer', (33, 20), TL_Button_Attributes, Button_Type.HomeButton)

        # Left Buttons
        algoButton1 = Button(self.program, 'Binary Search', (30, 85), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton2 = Button(self.program, 'Bubble Sort', (30, 135), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton3 = Button(self.program, 'Topological Sort', (30, 185), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton4 = Button(self.program, 'BFS', (30, 235), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton5 = Button(self.program, 'DFS', (30, 285), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton6 = Button(self.program, 'Floyds Algorithm', (30, 335), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton7 = Button(self.program, 'Bucket Sort', (30, 385), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton8 = Button(self.program, 'Union-Find', (30, 435), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton9 = Button(self.program, 'Dijkstra Algorithm', (30, 485), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton10 = Button(self.program, 'Prims Algorithm', (30, 535), L_Button_Attributes, Button_Type.AlgoButton,)
        algoButton11 = Button(self.program, 'Kruskal Algorithm', (30, 585), L_Button_Attributes, Button_Type.AlgoButton)
        algoButton12 = Button(self.program, 'Bellman-Ford', (30, 635), L_Button_Attributes, Button_Type.AlgoButton)

        self.button_list = [playButton, readMeButton, algoButton1, 
                            algoButton3, homeButton, codeButton, 
                            algoButton4, algoButton5, algoButton6, 
                            algoButton7, algoButton8, algoButton9, 
                            algoButton10, algoButton11, algoButton12, 
                            algoButton2]

    def get_button(self):
        return self.button_list