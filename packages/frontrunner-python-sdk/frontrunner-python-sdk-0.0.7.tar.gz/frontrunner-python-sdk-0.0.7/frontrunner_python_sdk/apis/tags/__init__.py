# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from frontrunner_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ABBREVIATED_PEOPLE = "abbreviated_people"
    ABBREVIATED_USERS = "abbreviated_users"
    API = "api"
    FEED = "feed"
    INTEGRATION_SETTINGS = "integration_settings"
    INTEGRATIONS = "integrations"
    INTEGRATIONS_ALL = "integrations_all"
    NOTES = "notes"
    PAGINATED_PEOPLE = "paginated_people"
    PEOPLE = "people"
    PULLJOBS = "pull-jobs"
    TAGS = "tags"
    TASKS = "tasks"
    TENANTS = "tenants"
