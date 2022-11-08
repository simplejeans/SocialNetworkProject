from clients import SocialNetworkAPIClient
from services import BotService

if __name__ == "__main__":
    client = SocialNetworkAPIClient()
    bot = BotService(client)
    bot.main()

