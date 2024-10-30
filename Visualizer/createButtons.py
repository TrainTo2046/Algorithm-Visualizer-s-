import pygame
import button
import buttonAttributes
import rightScreen

pygame.init()
class ButtonList():
    def __init__(self):
        # Play Button
        button1 = button.Button('Play', (700, 11), buttonAttributes.TopRightButton, buttonAttributes.ButtonType.PlayButton)

        # Mid Right Buttons
        button2 = button.Button('ReadMe', (690, 65), buttonAttributes.MidRightButton, buttonAttributes.ButtonType.ReadMeButton)
        button6 = button.Button('Code', (855, 65), buttonAttributes.MidRightButton, buttonAttributes.ButtonType.CodeButton)

        # Top Left Button
        button5 = button.Button('Algo Visualizer', (33, 20), buttonAttributes.TopLeftButton, buttonAttributes.ButtonType.WelcomeButton)

        # Left Buttons
        button3 = button.Button('Binary Search', (30, 85), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button16 = button.Button('Bubble Sort', (30, 135), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button4 = button.Button('Topological Sort', (30, 185), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button7 = button.Button('BFS', (30, 235), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button8 = button.Button('DFS', (30, 285), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button9 = button.Button('Floyds Algorithm', (30, 335), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button10 = button.Button('Bucket Sort', (30, 385), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button11 = button.Button('Union-Find', (30, 435), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button12 = button.Button('Dijkstra Algorithm', (30, 485), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button13 = button.Button('Prims Algorithm', (30, 535), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton,)
        button14 = button.Button('Kruskal Algorithm', (30, 585), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)
        button15 = button.Button('Bellman-Ford', (30, 635), buttonAttributes.LeftButton, buttonAttributes.ButtonType.AlgoButton)

        self.button_list = [button1, button2, button3, 
                            button4, button5, button6, 
                            button7, button8, button9, 
                            button10, button11, button12, 
                            button13, button14, button15, 
                            button16]
                
    def get_button(self):
        return self.button_list