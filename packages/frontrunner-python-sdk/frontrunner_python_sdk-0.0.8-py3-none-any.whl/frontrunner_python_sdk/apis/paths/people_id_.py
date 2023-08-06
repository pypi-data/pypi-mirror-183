from frontrunner_python_sdk.paths.people_id_.get import ApiForget
from frontrunner_python_sdk.paths.people_id_.put import ApiForput
from frontrunner_python_sdk.paths.people_id_.delete import ApiFordelete
from frontrunner_python_sdk.paths.people_id_.patch import ApiForpatch


class PeopleId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
