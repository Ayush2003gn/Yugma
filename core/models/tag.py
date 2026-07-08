from core.utils.color_generator import random_color
from core.utils.uid_generator import uuid_generator
from core.utils.datetime_now import datetime_now
class Tag:
    def __init__(self,tag,description = ""):
        self.tag = tag
        self.description = description
        self.color = random_color()
        self.tag_id = uuid_generator().data
        self.created_date = datetime_now()
        self.modified_date = datetime_now()


    def __str__(self):
        return self.tag
    
    def __repr__(self):
        return self.tag
    
    def update_color(self,color):
        self.color = color
        self.modified_date = datetime_now()
    
    def update_description(self,description):
        self.description = description
        self.modified_date = datetime_now()
        