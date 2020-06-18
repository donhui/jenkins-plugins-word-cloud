# -*- coding: UTF-8 -*-
import json

if __name__ == "__main__":
    json_obj = json.load(open("update-center.json", "r"))
    plugins_obj = json_obj["plugins"]
    with open("jenkins-plugins.txt", "w") as fw:
        for plugin_name in plugins_obj:
            plugin_obj = plugins_obj[plugin_name]
            print plugin_obj["title"]
            fw.write(plugin_obj["title"].encode('utf-8') + "\n")

