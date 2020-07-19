# DiscordAuth

[![Build Status](https://drone.rileyflynn.me/api/badges/MUNComputerScienceSociety/DiscordAuth/status.svg)](https://drone.rileyflynn.me/MUNComputerScienceSociety/DiscordAuth)
[![](https://images.microbadger.com/badges/image/muncs/discordauth.svg)](https://microbadger.com/images/muncs/discordauth "Get your own image badge on microbadger.com")

DiscordAuth provides OAuth-based identity verification services for MUN-affiliated people.

## Usage

Simply redirect a user to `https://discord.muncompsci.ca/auth`.
They will be taken to a Google OAuth consent screen, after which the account they signed in to will be checked to see if it is a MUN email address.
If it is, they will be given a token that can be used to retrieve their MUN username.
