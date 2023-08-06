import os
import json

def create_app(name):
    # Create the app folder
    app_folder = name
    os.makedirs(app_folder, exist_ok=True)
    
    # Create the views.py file
    views_path = os.path.join(app_folder, "views.py")
    with open(views_path, "w") as f:
        f.write("# views for the {} app".format(name))
    
    # Create the urls.py file
    urls_path = os.path.join(app_folder, "urls.py")
    with open(urls_path, "w") as f:
        f.write("# urls for the {} app".format(name))
    
    meta_path = os.path.join(os.getcwd(), "meta.json")
    with open(meta_path, "w") as f:
        data = {"project": name}
        json.dump(data, f)