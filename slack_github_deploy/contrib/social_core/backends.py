from social_core.backends.slack import SlackOAuth2 as BaseSlackOAuth2


class SlackOAuth2(BaseSlackOAuth2):
    DEFAULT_SCOPE = ['commands', 'bot']
    EXTRA_DATA = [
        ('id', 'id'),
        ('username', 'username'),
    ]

    def get_user_details(self, response):
        username = '{}@{}'.format(response['user'], response['team_name'])
        return {
            'username': username,
            'team_id': response['team_id'],
            'team_name': response['team_name'],
            'team_url': response['url'],
            'bot': response['bot'],
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        response = self.get_json(
            'https://slack.com/api/auth.test',
            params={'token': access_token},
        )
        if not response.get('id', None):
            response['id'] = response['user_id']
        return response

    def auth_allowed(self, response, details):
        """
        Make sure we have all the scope we need.
        """
        expected_scope = set(self.DEFAULT_SCOPE)
        actual_scope = set(response['scope'].split(','))
        return actual_scope >= expected_scope
