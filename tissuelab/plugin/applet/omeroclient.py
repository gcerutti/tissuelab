
from openalea.oalab.plugins.applets import PluginApplet

class OmeroClient(PluginApplet):

    name = 'OmeroClient'
    alias = 'Omero DB'

    def __call__(self, mainwindow):
        from tissuelab.omero.client import OmeroClient

        self._applet = self.new(self.name, OmeroClient)
        mainwindow.add_applet(self._applet, self.alias, area='inputs')
        self._fill_menu(mainwindow, self._applet)
        mainwindow.menu_classic['Project'].addMenu(self._applet.menu)
