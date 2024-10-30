import pygame
import rightScreen
import screenAttributes

pygame.init()
class RightScreenList():
    def __init__(self):
     
        # Top Left Button
        readMe5 = rightScreen.Right_Screen('Welcome', screenAttributes.ScreenType.ReadMe)
        code5 = rightScreen.Right_Screen('Welcome', screenAttributes.ScreenType.Code)
        
        """ 
        # Left Buttons
        readMe3 = rightScreen.Right_Screen('Binary Search', rightScreen.ScreenType.ReadMe)
        code3 = rightScreen.Right_Screen('Binary Search', rightScreen.ScreenType.Code)
        
        readMe16 = rightScreen.Right_Screen('Bubble Sort', rightScreen.ScreenType.ReadMe)
        code16 = rightScreen.Right_Screen('Bubble Sort', rightScreen.ScreenType.Code)
        
        readMe4 = rightScreen.Right_Screen('Topological Sort', rightScreen.ScreenType.ReadMe)
        code4 = rightScreen.Right_Screen('Topological Sort', rightScreen.ScreenType.Code)
        
        readMe7 = rightScreen.Right_Screen('BFS', rightScreen.ScreenType.ReadMe)
        code7 = rightScreen.Right_Screen('BFS', rightScreen.ScreenType.Code)
        
        readMe8 = rightScreen.Right_Screen('DFS', rightScreen.ScreenType.ReadMe)
        code8 = rightScreen.Right_Screen('DFS', rightScreen.ScreenType.Code)
        
        readMe9 = rightScreen.Right_Screen('Floyds Algorithm', rightScreen.ScreenType.ReadMe)
        code9 = rightScreen.Right_Screen('Floyds Algorithm', rightScreen.ScreenType.Code)
        
        readMe10 = rightScreen.Right_Screen('Bucket Sort', rightScreen.ScreenType.ReadMe)
        code10 = rightScreen.Right_Screen('Bucket Sort', rightScreen.ScreenType.Code)
        
        readMe11 = rightScreen.Right_Screen('Union-Find', rightScreen.ScreenType.ReadMe)
        code11 = rightScreen.Right_Screen('Union-Find', rightScreen.ScreenType.Code)
        
        readMe12 = rightScreen.Right_Screen('Dijkstra Algorithm', rightScreen.ScreenType.ReadMe)
        code12 = rightScreen.Right_Screen('Dijkstra Algorithm', rightScreen.ScreenType.Code)
        
        readMe13 = rightScreen.Right_Screen('Prims Algorithm', rightScreen.ScreenType.ReadMe)
        code13 = rightScreen.Right_Screen('Prims Algorithm', rightScreen.ScreenType.Code)
        
        readMe14 = rightScreen.Right_Screen('Kruskal Algorithm', rightScreen.ScreenType.ReadMe)
        code14 = rightScreen.Right_Screen('Kruskal Algorithm', rightScreen.ScreenType.Code)
        
        readMe15 = rightScreen.Right_Screen('Bellman-Ford', rightScreen.ScreenType.ReadMe)
        code15 = rightScreen.Right_Screen('Bellman-Ford', rightScreen.ScreenType.Code)

        readMe_list = [readMe3, readMe4, readMe5, readMe7, 
                            readMe8, readMe9, readMe10, readMe11, 
                            readMe12, readMe13, readMe14, readMe15, 
                            readMe16]
        
        code_list = [code3, code4, code5, code7, code8, code9, 
                          code10, code11, code12, code13, code14, 
                          code15, code16]
        
        self.readMe_map = {}
        for readMe in readMe_list:
            self.readMe_map[readMe.name] = readMe

        self.code_map = {}
        for code in code_list:
            self.code_map[code.name] = code

        """
        self.readMe_map = {readMe5.name : readMe5}
        self.code_map = {code5.name : code5}

    
    def get_readMe(self):
        return self.readMe_map
    
    def get_code(self):
        return self.code_map