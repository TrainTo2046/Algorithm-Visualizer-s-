import pygame
from rightScreenObject import Right_Screen_Object
from attributes import Screen_Type, Screen_Attributes
from utils import load_readme, load_code

pygame.init()
class Right_Screen():
    def __init__(self):
        # Right Screen
        self.x_value = Screen_Attributes.x_value.value
        self.y_value = Screen_Attributes.y_value.value
        self.width = Screen_Attributes.width.value
        self.height = Screen_Attributes.height.value

        self.top_rect = pygame.Rect((self.x_value, self.y_value), (self.width, self.height))
        self.top_color = Screen_Attributes.top_color.value
        self.border_radius = Screen_Attributes.border_radius.value

        # Text
        self.font_color = Screen_Attributes.font_color.value
        self.font_size_readme_txt = Screen_Attributes.font_size_readme_txt.value
        self.font_size_code_txt = Screen_Attributes.font_size_code_txt.value

        # ReadMe
        readMeTxt1 = Right_Screen_Object('Binary Search',  Screen_Type.ReadMe, [])
        readMeTxt2 = Right_Screen_Object('Bubble Sort',  Screen_Type.ReadMe, [])
        readMeTxt3 = Right_Screen_Object('Topological Sort',  Screen_Type.ReadMe, [])
        readMeTxt4 = Right_Screen_Object('BFS',  Screen_Type.ReadMe, [])
        readMeTxt5 = Right_Screen_Object('DFS', Screen_Type.ReadMe, [])
        readMeTxt6 = Right_Screen_Object('Floyds Algorithm', Screen_Type.ReadMe, [])
        readMeTxt7 = Right_Screen_Object('Bucket Sort', Screen_Type.ReadMe, [])
        readMeTxt8 = Right_Screen_Object('Union-Find', Screen_Type.ReadMe, [])
        readMeTxt9 = Right_Screen_Object('Dijkstra Algorithm', Screen_Type.ReadMe, [])
        readMeTxt10 = Right_Screen_Object('Prims Algorithm', Screen_Type.ReadMe, [],)
        readMeTxt11 = Right_Screen_Object('Kruskal Algorithm', Screen_Type.ReadMe, [])
        readMeTxt12 = Right_Screen_Object('Bellman-Ford', Screen_Type.ReadMe, [])

        # Code
        codeTxt1 = Right_Screen_Object('Binary Search',  Screen_Type.Code, [])
        codeTxt2 = Right_Screen_Object('Bubble Sort',  Screen_Type.Code, [])
        codeTxt3 = Right_Screen_Object('Topological Sort',  Screen_Type.Code, [])
        codeTxt4 = Right_Screen_Object('BFS',  Screen_Type.Code, [])
        codeTxt5 = Right_Screen_Object('DFS', Screen_Type.Code, [])
        codeTxt6 = Right_Screen_Object('Floyds Algorithm', Screen_Type.Code, [])
        codeTxt7 = Right_Screen_Object('Bucket Sort', Screen_Type.Code, [])
        codeTxt8 = Right_Screen_Object('Union-Find', Screen_Type.Code, [])
        codeTxt9 = Right_Screen_Object('Dijkstra Algorithm', Screen_Type.Code, [])
        codeTxt10 = Right_Screen_Object('Prims Algorithm', Screen_Type.Code, [],)
        codeTxt11 = Right_Screen_Object('Kruskal Algorithm', Screen_Type.Code, [])
        codeTxt12 = Right_Screen_Object('Bellman-Ford', Screen_Type.Code, [])
        
        self.txt_map = {    readMeTxt1.name: [readMeTxt1,    codeTxt1], readMeTxt2.name: [readMeTxt2,    codeTxt2],
                            readMeTxt3.name: [readMeTxt3,    codeTxt3], readMeTxt4.name: [readMeTxt4,    codeTxt4],
                            readMeTxt5.name: [readMeTxt5,    codeTxt5], readMeTxt6.name: [readMeTxt6,    codeTxt6],
                            readMeTxt7.name: [readMeTxt7,    codeTxt7], readMeTxt8.name: [readMeTxt8,    codeTxt8],
                            readMeTxt9.name: [readMeTxt9,    codeTxt9], readMeTxt10.name: [readMeTxt10,   codeTxt10],
                            readMeTxt11.name: [readMeTxt11,   codeTxt11], readMeTxt12.name: [readMeTxt12,   codeTxt12]}

    def drawRightScreen(self, screen):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = self.border_radius)

    def draw(self, screen):
        for key in self.txt_map.keys():
            self.txt_map[key][0].draw_text(screen)
            self.txt_map[key][1].draw_text(screen)

    def update(self, name, screen_type):
        for key in self.txt_map.keys():
            if (key == name):
                # read me txt
                if screen_type == self.txt_map[key][0].screen_type:
                    line_content = load_readme(name)
                    line_list = self.get_line_list(line_content, screen_type)
                    self.txt_map[key][0].text = line_list
                    self.txt_map[key][1].text = []

                # code txt
                else:
                    line_content = load_code(name)
                    line_list = self.get_line_list(line_content, screen_type)
                    self.txt_map[key][1].text = line_list
                    self.txt_map[key][0].text = []
            else:
                self.txt_map[key][0].text = []
                self.txt_map[key][1].text = []

    def get_line_list(self, line_content, screen_type):
        lst = []
        offset = 0
        font_size = self.font_size_code_txt
        if screen_type == Screen_Type.ReadMe:
            font_size = self.font_size_readme_txt

        gui_font = pygame.font.SysFont("marquee", font_size, bold=False)
        for line in line_content: 
            text_surf = gui_font.render(line, True, self.font_color)
            text_rect = text_surf.get_rect(topleft = (self.x_value + 10, self.y_value + 10 + offset))
            lst.append([text_surf, text_rect])
            offset += 20

        return lst
