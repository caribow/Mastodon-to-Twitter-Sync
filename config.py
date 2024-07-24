import os

# Twitter API Config
twitter_config = {
    'consumer_key': os.environ.get('TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.environ.get('TWITTER_CONSUMER_SECRET'),
    'access_token': os.environ.get('TWITTER_ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'),
    'bearer_token': os.environ.get('TWITTER_BEARER_TOKEN')
}

# Mastodon Config
mastodon_config = {
    'client_id': os.environ.get('MASTODON_CLIENT_ID'),
    'client_secret': os.environ.get('MASTODON_CLIENT_SECRET'),
    'access_token': os.environ.get('MASTODON_ACCESS_TOKEN'),
    'api_base_url': os.environ.get('MASTODON_API_BASE_URL')
}

main_config = {
    'sync_time' : int(os.environ.get('SYNC_TIME', '60')),  # 从环境变量读取，默认为60秒
    'log_to_file' : os.environ.get('LOG_TO_FILE', 'True').lower() == 'true',  # 从环境变量读取，默认为True
    'limit_retry_attempt' : int(os.environ.get('LIMIT_RETRY_ATTEMPT', '13')),  # 从环境变量读取，默认为13次
    'wait_exponential_max': int(os.environ.get('WAIT_EXPONENTIAL_MAX', str(1000*60*30))),  # 从环境变量读取，默认为30分钟
    'wait_exponential_multiplier': int(os.environ.get('WAIT_EXPONENTIAL_MULTIPLIER', '800'))  # 从环境变量读取，默认为800毫秒
}
