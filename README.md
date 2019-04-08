# DiscordAuth

DiscordAuth provides OAuth-based identity verification services for MUN-affiliated people.

## Usage

Simply redirect a user to `https://auth.muncompsci.ca`.
They will be taken to a Google OAuth consent screen, after which the account they signed in to will be checked to see if it is a MUN email address.
If it is, they will be given a token that can be used to retrieve their MUN username.
