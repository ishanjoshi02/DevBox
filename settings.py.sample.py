from constants import EDITORS
ROOT_DEV_FOLDER = ''


codebases = {
    "voice": {
        "valid_commands": ['voice'],
        "folder": "practo-voice",
        'editor': EDITORS[1]
    },
    "communicator": {
        "valid_commands": ['communicator', 'praccomm', 'comm'],
        "folder": "practo-communicator",
        "editor": EDITORS[0]
    },
    "fabric": {
        "valid_commands" : ['fabric'],
        "folder": "fabric"
    },
    # ['book_scheduler', 'book', 'phoenix']
    "project_name": {
        "valid_commands": [""],
        "folder": "your-project-folder(inside root dev folder)",
        'editor': "editor of choice of project (optional)"
    }
}