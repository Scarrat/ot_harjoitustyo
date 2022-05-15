from datetime import datetime


class Note:
    def __init__(self,expression:str, time:datetime):
        self.expression=expression
        self.time=time