import os, sys, json
from functools import partial

setting_root_directory = os.path.expanduser(os.path.join("~", "Documents"))

local_settings_folder_name = ""

settings_directory_contents = partial(os.listdir, setting_root_directory)

def make_sure_settings_folder_exists(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def make_sure_json_exists(filepath):

    if not os.path.exists(filepath):
        _dir = os.path.dirname(filepath)
        make_sure_settings_folder_exists(_dir)

        with open(filepath, "w") as file:
            file.write(json.dumps({}, index=4, sort_keys=True))



def get_setting_module(module_name):
    # if
    return

def _read_settings(filepath):
    with open(filepath, "w") as file:
        _data = json.load(file)
    return _data

def _write_settings(filepath, settings_data):
    with open(filepath, "w") as file:
        file.write(json.dumps(settings_data))

class SettingsForModule:

    def __init__(self, module_name, module_folder_name="Settings", _root_folder=setting_root_directory):
        """
        This class manages a settings json file
        Parameters
        ----------
        module_name
        module_folder_name
        _root_folder
        """
        self._root_folder = os.path.join(_root_folder, module_folder_name)

        make_sure_settings_folder_exists(self._root_folder)

        _module_file_name = f"{module_name}_Settings.json"
        self.module_path = os.path.join(self._root_folder, _module_file_name)

        make_sure_settings_folder_exists(self.module_folder_path)

        self.settings_dictionary = _read_settings(self.module_path)

    def get_setting(self, setting):
        _setting_value = _read_settings(self.module_path).get(setting, None)
        return _setting_value

    def set_setting(self, setting, value):
        self.settings_dictionary[setting] = value
        _write_settings(self.module_path, self.settings_dictionary)

    def settings_path(self):
        return self.module_path

    def settings_size(self):
        return len(_read_settings(self.module_path))

    def print_settings(self):
        print(_read_settings(self.module_path))


