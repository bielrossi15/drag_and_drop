class RectUpdate():
    def __init__(self, pos_center, rec_color, size=[100,100]):
        self.pos_center = pos_center
        self.size = size
        self.rec_color = rec_color

    def update(self, cursor):
        cx, cy = self.pos_center
        w, h = self.size

        if (cx-w//2 < cursor[0] < cx+w//2 
        and cy-h//2 < cursor[1] < cy+h//2):
            self.pos_center = cursor
        