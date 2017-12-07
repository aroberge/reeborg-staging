''' Updates the staging repo from the main development site'''

import shutil

def update_dir(name):
    reeborg = "../reeborg/"
    print("Updating directory", name)
    try:
        shutil.rmtree(name)
    except FileNotFoundError:
        print("Warning:", name, "could not be found and removed")

    try:
        shutil.copytree(reeborg + name, name)
    except FileExistsError:
        print("Error:", name, "already exists and could not be copied.")


shutil.copy2("../reeborg/reeborg_offline.html", "index.html")

shutil.copy2("../reeborg/build/reeborg.js", "build/reeborg.js")

update_dir("offline/")
update_dir("src/blockly/")
update_dir("src/blockly_msg/")
update_dir("src/css/")
update_dir("src/images/")
update_dir("src/libraries/")
update_dir("src/python/")
update_dir("src/sounds/")
update_dir("worlds/")
