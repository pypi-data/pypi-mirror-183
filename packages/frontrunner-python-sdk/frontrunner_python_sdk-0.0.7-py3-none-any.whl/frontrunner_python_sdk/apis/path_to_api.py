import typing_extensions

from frontrunner_python_sdk.paths import PathValues
from frontrunner_python_sdk.apis.paths.abbreviated_people_ import AbbreviatedPeople
from frontrunner_python_sdk.apis.paths.abbreviated_people_id_ import AbbreviatedPeopleId
from frontrunner_python_sdk.apis.paths.abbreviated_users_ import AbbreviatedUsers
from frontrunner_python_sdk.apis.paths.abbreviated_users_id_ import AbbreviatedUsersId
from frontrunner_python_sdk.apis.paths.api_token_ import ApiToken
from frontrunner_python_sdk.apis.paths.feed_ import Feed
from frontrunner_python_sdk.apis.paths.feed_id_ import FeedId
from frontrunner_python_sdk.apis.paths.integration_settings_facebook_ import IntegrationSettingsFacebook
from frontrunner_python_sdk.apis.paths.integration_settings_facebook_id_ import IntegrationSettingsFacebookId
from frontrunner_python_sdk.apis.paths.integration_settings_mailchimp_ import IntegrationSettingsMailchimp
from frontrunner_python_sdk.apis.paths.integration_settings_mailchimp_id_ import IntegrationSettingsMailchimpId
from frontrunner_python_sdk.apis.paths.integration_settings_prompt_ import IntegrationSettingsPrompt
from frontrunner_python_sdk.apis.paths.integration_settings_prompt_id_ import IntegrationSettingsPromptId
from frontrunner_python_sdk.apis.paths.integration_settings_revv_ import IntegrationSettingsRevv
from frontrunner_python_sdk.apis.paths.integration_settings_revv_id_ import IntegrationSettingsRevvId
from frontrunner_python_sdk.apis.paths.integration_settings_twitter_ import IntegrationSettingsTwitter
from frontrunner_python_sdk.apis.paths.integration_settings_twitter_id_ import IntegrationSettingsTwitterId
from frontrunner_python_sdk.apis.paths.integration_settings_whatsapp_ import IntegrationSettingsWhatsapp
from frontrunner_python_sdk.apis.paths.integration_settings_whatsapp_id_ import IntegrationSettingsWhatsappId
from frontrunner_python_sdk.apis.paths.integrations_mailchimp_ import IntegrationsMailchimp
from frontrunner_python_sdk.apis.paths.integrations_mailchimp_id_ import IntegrationsMailchimpId
from frontrunner_python_sdk.apis.paths.integrations_prompt_ import IntegrationsPrompt
from frontrunner_python_sdk.apis.paths.integrations_prompt_id_ import IntegrationsPromptId
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweeters_ import IntegrationsTwitterTweeters
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweeters_id_ import IntegrationsTwitterTweetersId
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweets_ import IntegrationsTwitterTweets
from frontrunner_python_sdk.apis.paths.integrations_twitter_tweets_id_ import IntegrationsTwitterTweetsId
from frontrunner_python_sdk.apis.paths.integrations_all_ import IntegrationsAll
from frontrunner_python_sdk.apis.paths.integrations_all_id_ import IntegrationsAllId
from frontrunner_python_sdk.apis.paths.notes_ import Notes
from frontrunner_python_sdk.apis.paths.notes_id_ import NotesId
from frontrunner_python_sdk.apis.paths.paginated_people_ import PaginatedPeople
from frontrunner_python_sdk.apis.paths.people_ import People
from frontrunner_python_sdk.apis.paths.people_id_ import PeopleId
from frontrunner_python_sdk.apis.paths.pull_jobs_ import PullJobs
from frontrunner_python_sdk.apis.paths.pull_jobs_id_ import PullJobsId
from frontrunner_python_sdk.apis.paths.tags_ import Tags
from frontrunner_python_sdk.apis.paths.tags_id_ import TagsId
from frontrunner_python_sdk.apis.paths.tasks_ import Tasks
from frontrunner_python_sdk.apis.paths.tasks_id_ import TasksId
from frontrunner_python_sdk.apis.paths.tenants_ import Tenants
from frontrunner_python_sdk.apis.paths.tenants_id_ import TenantsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ABBREVIATED_PEOPLE_: AbbreviatedPeople,
        PathValues.ABBREVIATED_PEOPLE_ID_: AbbreviatedPeopleId,
        PathValues.ABBREVIATED_USERS_: AbbreviatedUsers,
        PathValues.ABBREVIATED_USERS_ID_: AbbreviatedUsersId,
        PathValues.API_TOKEN_: ApiToken,
        PathValues.FEED_: Feed,
        PathValues.FEED_ID_: FeedId,
        PathValues.INTEGRATION_SETTINGS_FACEBOOK_: IntegrationSettingsFacebook,
        PathValues.INTEGRATION_SETTINGS_FACEBOOK_ID_: IntegrationSettingsFacebookId,
        PathValues.INTEGRATION_SETTINGS_MAILCHIMP_: IntegrationSettingsMailchimp,
        PathValues.INTEGRATION_SETTINGS_MAILCHIMP_ID_: IntegrationSettingsMailchimpId,
        PathValues.INTEGRATION_SETTINGS_PROMPT_: IntegrationSettingsPrompt,
        PathValues.INTEGRATION_SETTINGS_PROMPT_ID_: IntegrationSettingsPromptId,
        PathValues.INTEGRATION_SETTINGS_REVV_: IntegrationSettingsRevv,
        PathValues.INTEGRATION_SETTINGS_REVV_ID_: IntegrationSettingsRevvId,
        PathValues.INTEGRATION_SETTINGS_TWITTER_: IntegrationSettingsTwitter,
        PathValues.INTEGRATION_SETTINGS_TWITTER_ID_: IntegrationSettingsTwitterId,
        PathValues.INTEGRATION_SETTINGS_WHATSAPP_: IntegrationSettingsWhatsapp,
        PathValues.INTEGRATION_SETTINGS_WHATSAPP_ID_: IntegrationSettingsWhatsappId,
        PathValues.INTEGRATIONS_MAILCHIMP_: IntegrationsMailchimp,
        PathValues.INTEGRATIONS_MAILCHIMP_ID_: IntegrationsMailchimpId,
        PathValues.INTEGRATIONS_PROMPT_: IntegrationsPrompt,
        PathValues.INTEGRATIONS_PROMPT_ID_: IntegrationsPromptId,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_: IntegrationsTwitterTweeters,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_ID_: IntegrationsTwitterTweetersId,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_: IntegrationsTwitterTweets,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_ID_: IntegrationsTwitterTweetsId,
        PathValues.INTEGRATIONS_ALL_: IntegrationsAll,
        PathValues.INTEGRATIONS_ALL_ID_: IntegrationsAllId,
        PathValues.NOTES_: Notes,
        PathValues.NOTES_ID_: NotesId,
        PathValues.PAGINATED_PEOPLE_: PaginatedPeople,
        PathValues.PEOPLE_: People,
        PathValues.PEOPLE_ID_: PeopleId,
        PathValues.PULLJOBS_: PullJobs,
        PathValues.PULLJOBS_ID_: PullJobsId,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_ID_: TagsId,
        PathValues.TASKS_: Tasks,
        PathValues.TASKS_ID_: TasksId,
        PathValues.TENANTS_: Tenants,
        PathValues.TENANTS_ID_: TenantsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ABBREVIATED_PEOPLE_: AbbreviatedPeople,
        PathValues.ABBREVIATED_PEOPLE_ID_: AbbreviatedPeopleId,
        PathValues.ABBREVIATED_USERS_: AbbreviatedUsers,
        PathValues.ABBREVIATED_USERS_ID_: AbbreviatedUsersId,
        PathValues.API_TOKEN_: ApiToken,
        PathValues.FEED_: Feed,
        PathValues.FEED_ID_: FeedId,
        PathValues.INTEGRATION_SETTINGS_FACEBOOK_: IntegrationSettingsFacebook,
        PathValues.INTEGRATION_SETTINGS_FACEBOOK_ID_: IntegrationSettingsFacebookId,
        PathValues.INTEGRATION_SETTINGS_MAILCHIMP_: IntegrationSettingsMailchimp,
        PathValues.INTEGRATION_SETTINGS_MAILCHIMP_ID_: IntegrationSettingsMailchimpId,
        PathValues.INTEGRATION_SETTINGS_PROMPT_: IntegrationSettingsPrompt,
        PathValues.INTEGRATION_SETTINGS_PROMPT_ID_: IntegrationSettingsPromptId,
        PathValues.INTEGRATION_SETTINGS_REVV_: IntegrationSettingsRevv,
        PathValues.INTEGRATION_SETTINGS_REVV_ID_: IntegrationSettingsRevvId,
        PathValues.INTEGRATION_SETTINGS_TWITTER_: IntegrationSettingsTwitter,
        PathValues.INTEGRATION_SETTINGS_TWITTER_ID_: IntegrationSettingsTwitterId,
        PathValues.INTEGRATION_SETTINGS_WHATSAPP_: IntegrationSettingsWhatsapp,
        PathValues.INTEGRATION_SETTINGS_WHATSAPP_ID_: IntegrationSettingsWhatsappId,
        PathValues.INTEGRATIONS_MAILCHIMP_: IntegrationsMailchimp,
        PathValues.INTEGRATIONS_MAILCHIMP_ID_: IntegrationsMailchimpId,
        PathValues.INTEGRATIONS_PROMPT_: IntegrationsPrompt,
        PathValues.INTEGRATIONS_PROMPT_ID_: IntegrationsPromptId,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_: IntegrationsTwitterTweeters,
        PathValues.INTEGRATIONS_TWITTER_TWEETERS_ID_: IntegrationsTwitterTweetersId,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_: IntegrationsTwitterTweets,
        PathValues.INTEGRATIONS_TWITTER_TWEETS_ID_: IntegrationsTwitterTweetsId,
        PathValues.INTEGRATIONS_ALL_: IntegrationsAll,
        PathValues.INTEGRATIONS_ALL_ID_: IntegrationsAllId,
        PathValues.NOTES_: Notes,
        PathValues.NOTES_ID_: NotesId,
        PathValues.PAGINATED_PEOPLE_: PaginatedPeople,
        PathValues.PEOPLE_: People,
        PathValues.PEOPLE_ID_: PeopleId,
        PathValues.PULLJOBS_: PullJobs,
        PathValues.PULLJOBS_ID_: PullJobsId,
        PathValues.TAGS_: Tags,
        PathValues.TAGS_ID_: TagsId,
        PathValues.TASKS_: Tasks,
        PathValues.TASKS_ID_: TasksId,
        PathValues.TENANTS_: Tenants,
        PathValues.TENANTS_ID_: TenantsId,
    }
)
