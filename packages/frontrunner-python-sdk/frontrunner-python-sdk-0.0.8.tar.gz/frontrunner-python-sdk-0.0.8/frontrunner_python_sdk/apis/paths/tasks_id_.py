from frontrunner_python_sdk.paths.tasks_id_.get import ApiForget
from frontrunner_python_sdk.paths.tasks_id_.put import ApiForput
from frontrunner_python_sdk.paths.tasks_id_.delete import ApiFordelete
from frontrunner_python_sdk.paths.tasks_id_.patch import ApiForpatch


class TasksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
