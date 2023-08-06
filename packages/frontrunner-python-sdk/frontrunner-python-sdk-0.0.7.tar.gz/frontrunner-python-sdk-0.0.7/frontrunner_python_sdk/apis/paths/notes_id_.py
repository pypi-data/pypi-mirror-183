from frontrunner_python_sdk.paths.notes_id_.get import ApiForget
from frontrunner_python_sdk.paths.notes_id_.put import ApiForput
from frontrunner_python_sdk.paths.notes_id_.delete import ApiFordelete
from frontrunner_python_sdk.paths.notes_id_.patch import ApiForpatch


class NotesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
