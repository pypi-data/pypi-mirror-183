from frontrunner_python_sdk.paths.tenants_id_.get import ApiForget
from frontrunner_python_sdk.paths.tenants_id_.put import ApiForput
from frontrunner_python_sdk.paths.tenants_id_.delete import ApiFordelete
from frontrunner_python_sdk.paths.tenants_id_.patch import ApiForpatch


class TenantsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
