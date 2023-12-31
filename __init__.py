import os, sys, json
from functools import partial
import file_management

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
            file.write(json.dumps({}))


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

        _module_file_name = f"{module_name}.json"
        self.module_path = os.path.join(self._root_folder, _module_file_name)

        make_sure_json_exists(self.module_path)

    def get_setting(self, setting):
        _setting_value = file_management.read_json(self.module_path).get(setting, None)
        return _setting_value

    def set_setting(self, setting, value):
        _write_dict = self.settings_dictionary()
        _write_dict[setting] = value
        file_management.write_json(self.settings_path(), _write_dict)

    def remove_setting(self, setting):
        _write_dict = self.settings_dictionary()
        if setting in _write_dict:
            del _write_dict[setting]
            file_management.write_json(self.settings_path(), _write_dict)

    def settings_dictionary(self):
        return file_management.read_json(self.module_path)

    def overwrite_with_dictionary(self, dictionary):
        if isinstance(dictionary, dict):
            file_management.write_json(self.module_path, dictionary)

    def settings_path(self):
        return self.module_path

    def settings_size(self):
        return len(file_management.read_json(self.module_path))

    def print_settings(self):
        print(file_management.read_json(self.module_path))


