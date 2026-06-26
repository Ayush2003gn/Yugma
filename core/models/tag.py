from core.utils.color_generator import random_color
from core.utils.uid_generator import uuid_generator
class tag:
    def __init__(self,tag,description = ""):
        self.tag = tag
        self.description = description
        self.color = random_color()
        self.tag_id = uuid_generator().data

    def __str__(self):
        return self.tag
    
    def __repr__(self):
        return self.tag
    
    def update_color(self,color):
        self.color = color
    
    def update_description(self,description):
        self.description = description
        