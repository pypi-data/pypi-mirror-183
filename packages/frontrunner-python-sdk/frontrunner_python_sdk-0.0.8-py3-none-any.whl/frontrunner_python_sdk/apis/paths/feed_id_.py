from frontrunner_python_sdk.paths.feed_id_.get import ApiForget
from frontrunner_python_sdk.paths.feed_id_.put import ApiForput
from frontrunner_python_sdk.paths.feed_id_.delete import ApiFordelete
from frontrunner_python_sdk.paths.feed_id_.patch import ApiForpatch


class FeedId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
