import sublime, sublime_plugin, os.path

class OpenNextFileInFolderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current = os.path.abspath(self.view.file_name())
        curName = os.path.basename(current)
        path = os.path.dirname(current)
        files = list((file for file in os.listdir(path) 
            if os.path.isfile(os.path.join(path, file))))
        if (len(files) > 1):
            targetIndex = files.index(curName) + 1
            if targetIndex >= len(files):
                targetIndex = 0
            target = os.path.join(path, files[targetIndex])
            self.view.window().open_file(target)
