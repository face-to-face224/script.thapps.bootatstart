import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

class BootAtStart(xbmcaddon.Addon):
    def __init__(self):
        self.addon = xbmcaddon.Addon()
        self.addon_name = self.addon.getAddonInfo('name')
        self.settings = self.addon.getSettings()
        self.selected_addon = self.settings.getSetting('selected_addon')

    def run(self):
        if self.selected_addon:
            xbmc.executebuiltin(f'RunAddon({self.selected_addon})')

    def get_addons(self):
        addons = []
        for dir in xbmcvfs.listdir('special://home/addons')[1]:
            if dir.startswith('plugin.') or dir.startswith('script.'):
                addons.append((dir, xbmcaddon.Addon(dir).getAddonInfo('name')))
        return addons

def main():
    boot_at_start = BootAtStart()
    if boot_at_start.settings.getSetting('selected_addon') == '':
        dialog = xbmcgui.Dialog()
        addons = boot_at_start.get_addons()
        addon_list = [addon[1] for addon in addons]
        selected = dialog.select('Select Addon', addon_list)
        if selected != -1:
            boot_at_start.settings.setSetting('selected_addon', addons[selected][0])
    boot_at_start.run()

if __name__ == '__main__':
    main()
