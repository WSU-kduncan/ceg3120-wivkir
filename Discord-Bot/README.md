Setup
- How to get an API token
  - To get an API token, you must download it from the remote service you will be interacting with.
- Where to put it to work with the code
  - It is good practice to keep the API token within an .env variable file and never publish that file. You can still use the token by referencing the file with a variable in your code.
- Dependencies
  - In order to run this bot you will need: python 3, discord.py, python-dotenv, and an internet connection.


Usage
- What commands you can type in your Discord server
  - If anyone types "Jeremead"(a reference to my D&D group in the server I added the bot to) anywhere in a message the bot will respond with a random quote from one of the player's characters.


Research
- Research some possible solutions that would solve this, and discuss why you think it would work.
  - I have a second computer that I sometimes run a Minecraft server out of. I plan on cloning the bot onto it and running it from there. This way I have full control and it is cheap.
  - I could also rent a remote all-purpose server from AWS and leave it running permanently. However, if AWS goes down, so does my bot, and I'll have to waith for them to fix it.
  - There were a few free solutions online involving glitch.com, repl.it, uptimerobot.com, and a couple different bot websites. They seem more user friendly at the cost of having less control.
