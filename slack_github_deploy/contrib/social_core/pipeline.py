from slack_github_deploy import models


def create_slack_entities(backend, details, social, *args, **kwargs):
    if backend.name != 'slack':
        return

    slack_team, __ = models.SlackTeam.objects.update_or_create(
        team_id=details['team_id'],
        defaults=dict(
            name=details['team_name'],
            url=details['team_url'],
        ),
    )

    slack_team.social_users.add(social)

    slack_bot, __ = models.SlackBot.objects.update_or_create(
        user_id=details['bot']['bot_user_id'],
        defaults=dict(
            access_token=details['bot']['bot_access_token'],
            team=slack_team,
        ),
    )

    return {
        'slack_team': slack_team,
        'slack_bot': slack_bot,
    }
