from .devoud_data import *


class BrowserContextMenu(QMenu):
    def __init__(self, parent):
        super().__init__()
        self.radius = 6
        self.setStyleSheet(parent.theme.context_menu())

    def resizeEvent(self, event):
        paint_path = QPainterPath()
        rect = QtCore.QRectF(self.rect()).adjusted(.5, .5, -1.5, -1.5)
        paint_path.addRoundedRect(rect, self.radius, self.radius)
        region = QRegion(paint_path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)
