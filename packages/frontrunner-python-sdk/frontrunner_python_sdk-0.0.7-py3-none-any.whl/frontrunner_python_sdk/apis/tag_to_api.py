import typing_extensions

from frontrunner_python_sdk.apis.tags import TagValues
from frontrunner_python_sdk.apis.tags.abbreviated_people_api import AbbreviatedPeopleApi
from frontrunner_python_sdk.apis.tags.abbreviated_users_api import AbbreviatedUsersApi
from frontrunner_python_sdk.apis.tags.api_api import ApiApi
from frontrunner_python_sdk.apis.tags.feed_api import FeedApi
from frontrunner_python_sdk.apis.tags.integration_settings_api import IntegrationSettingsApi
from frontrunner_python_sdk.apis.tags.integrations_api import IntegrationsApi
from frontrunner_python_sdk.apis.tags.integrations_all_api import IntegrationsAllApi
from frontrunner_python_sdk.apis.tags.notes_api import NotesApi
from frontrunner_python_sdk.apis.tags.paginated_people_api import PaginatedPeopleApi
from frontrunner_python_sdk.apis.tags.people_api import PeopleApi
from frontrunner_python_sdk.apis.tags.pull_jobs_api import PullJobsApi
from frontrunner_python_sdk.apis.tags.tags_api import TagsApi
from frontrunner_python_sdk.apis.tags.tasks_api import TasksApi
from frontrunner_python_sdk.apis.tags.tenants_api import TenantsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ABBREVIATED_PEOPLE: AbbreviatedPeopleApi,
        TagValues.ABBREVIATED_USERS: AbbreviatedUsersApi,
        TagValues.API: ApiApi,
        TagValues.FEED: FeedApi,
        TagValues.INTEGRATION_SETTINGS: IntegrationSettingsApi,
        TagValues.INTEGRATIONS: IntegrationsApi,
        TagValues.INTEGRATIONS_ALL: IntegrationsAllApi,
        TagValues.NOTES: NotesApi,
        TagValues.PAGINATED_PEOPLE: PaginatedPeopleApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.PULLJOBS: PullJobsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TENANTS: TenantsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ABBREVIATED_PEOPLE: AbbreviatedPeopleApi,
        TagValues.ABBREVIATED_USERS: AbbreviatedUsersApi,
        TagValues.API: ApiApi,
        TagValues.FEED: FeedApi,
        TagValues.INTEGRATION_SETTINGS: IntegrationSettingsApi,
        TagValues.INTEGRATIONS: IntegrationsApi,
        TagValues.INTEGRATIONS_ALL: IntegrationsAllApi,
        TagValues.NOTES: NotesApi,
        TagValues.PAGINATED_PEOPLE: PaginatedPeopleApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.PULLJOBS: PullJobsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TENANTS: TenantsApi,
    }
)
