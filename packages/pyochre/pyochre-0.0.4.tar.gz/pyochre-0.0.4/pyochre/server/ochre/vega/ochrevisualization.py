import logging


logger = logging.getLogger(__name__)


class OchreVisualization(object):

    @property
    def json(self):
        retval = {
            "$schema": "https://vega.github.io/schema/vega/v5.json",
            "description": self.description,
            "background": self.background,
            "width": self.width,
            "height": self.height,
            "padding": self.padding,
            "autosize": self.autosize,
            "config" : self.config,
            "signals": self.signals,
            "data": self.data,
            "scales": self.scales,
            "projections": self.projections,
            "axes": self.axes,
            "legends": self.legends,
            "title" : self.title,
            "marks": self.marks,
            "encode": self.encode,
            "usermeta": self.usermeta,
        }
        return retval

    @property
    def description(self):
        return "A Vega visualization."

    @property
    def width(self):
        return None

    @property
    def height(self):
        return None

    @property
    def padding(self):
        return None

    @property
    def autosize(self):
        return None

    @property
    def background(self):
        return None

    @property
    def legends(self):
        return []

    @property
    def projections(self):
        return []

    @property
    def other_data(self):
        return []

    @property
    def signals(self):
        return []

    @property
    def config(self):
        return []

    @property
    def title(self):
        return None

    @property
    def transforms(self):
       return []

    @property
    def marks(self):
        return []

    @property
    def axes(self):
        return []

    @property
    def scales(self):
        return []

    @property
    def data(self):
        return []

    @property
    def scales(self):
        return []

    @property
    def encode(self):
        return []

    @property
    def usermeta(self):
        return []
