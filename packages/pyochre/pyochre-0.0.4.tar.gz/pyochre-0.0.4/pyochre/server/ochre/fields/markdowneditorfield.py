import logging
from pyochre.server.ochre.fields import MonacoEditorField
from pyochre.server.ochre.widgets import MonacoEditorWidget


logger = logging.getLogger(__name__)


class MarkdownEditorField(MonacoEditorField):

    def __init__(self, *argv, **argd):
        retval = super(MarkdownEditorField, self).__init__(*argv, **argd)
        self.style["rendering_url"] = "markdown"
        self.style["hide_label"] = True


        
