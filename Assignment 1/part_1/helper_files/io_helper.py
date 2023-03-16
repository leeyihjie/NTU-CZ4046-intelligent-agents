import os


def get_project_path():
    proj_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../..'))
    return proj_path