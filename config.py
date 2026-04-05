import os

# Required variables
api_id = int(os.getenv("API_ID", "0"))
api_hash = os.getenv("API_HASH", "")
bot_token = os.getenv("BOT_TOKEN", "")

# Convert string → list of int
def parse_users(env_var):
    value = os.getenv(env_var, "")
    if value:
        return list(map(int, value.split()))
    return []

auth_users = parse_users("AUTH_USERS")
sudo_users = parse_users("SUDO_USERS")
