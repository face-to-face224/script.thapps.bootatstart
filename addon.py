import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

class BootAtStart(xbmcaddon.Addon):
    def __init__(self):
        super().__init__()
        self.addon_name = self.getAddonInfo('name')
        self.settings = self.getSettings()
        self.selected_addon = self.settings.getSetting('selected_addon')

    def run(self):
        if self.selected_addon:
            xbmc.executebuiltin(f'RunAddon({self.selected_addon})')

    def get_addons(self):
        """Returns list of tuples containing addon ID and name."""
        addons = []
        dirs = xbmcvfs.listdir('special://home/addons')[1]
        for dir in dirs:
            if dir.startswith('plugin.') or dir.startswith('script.'):
                addon = xbmcaddon.Addon(dir)
                addons.append((dir, addon.getAddonInfo('name')))
        return addons

def main():
    boot_at_start = BootAtStart()
    if not boot_at_start.selected_addon:
        dialog = xbmcgui.Dialog()
        addons = boot_at_start.get_addons()
        addon_list = [addon[1] for addon in addons]
        selected = dialog.select('Select Addon', addon_list)
        if selected != -1:
            boot_at_start.settings.setSetting('selected_addon', addons[selected][0])
    boot_at_start.run()

if __name__ == '__main__':
    main()
