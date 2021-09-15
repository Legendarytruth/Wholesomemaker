## Wholesome Series Videos Discord Server Bots

[![build](https://github.com/GNZTMPZ/Wholesomemaker-1/actions/workflows/build.yml/badge.svg)](https://github.com/GNZTMPZ/Wholesomemaker-1/actions/workflows/build.yml)

Wholesomemaker is a Discord Bot that have all tools you need from managing a server, engage with server members, and more...

![Wholesomemaker](Wholesomemaker.png)

## Development

This project is open to anyone who wants to contribute, large or small! Whether you noticed a typo or want to add a
whole new feature, go for it!

Large additions should be discussed in issues or on Discord first. If you're new to Python, ask me on [discord](https://discordapp.com/users/351147060956889088) for where to start and you can use Wholesomemaker as a starting point for a contribution.

## Testing/Workflow

To run the app, you need:

- A Discord Bot, with `server member intent` and `presence intent`.. obviously.. [click here](https://discord.com/developers/applications)
- A Discord server to test - you can't use the Wholesome Series Videos Discord Server to do tests
- [Python version 3.8.6](https://www.python.org/downloads/release/python-386/)
- A MongoDB Server for levelling and warning system (Pick one)
  - [MongoDB Community Server (Offline)](https://www.mongodb.com/try/download/community)
  - [MongoDB Atlas (Online)](https://www.mongodb.com/cloud/atlas)
- A Good Code IDE, obviously.. I recommend you [Visual Studio Code](https://code.visualstudio.com)

If you don't own/admin a Discord server, creating one is simple, you can do it from the same menu you join discord servers from.

## .env systems

We're starting to implement the `.env` files.

We don't provide the examples, yet.

Feel free to use these as your starting guide! :v:

```bash
VERSION="master"
BOT_TOKEN="https://discord.com/developers/applications"
MONGODB_URL="your mongodb uri's"
GITHUB_TOKEN="your github token"
GIST_ID="provide your github gist id for readme commands!"
```

## Docker

Thanks to [🐧 rsetiawan7](https://github.com/rsetiawan7), Wholesomemaker Supports running on Docker. but.. the Active Docker Images has been used for Production Purposes as a Private Repository.

You "could" technically run it on Docker, I have provide you the essence of it (Dockerfile and github actions settings).

I assume you already know how to do it, Please Refer to `Docker` folder to Getting Started. Thanks. 😉

## Leaderboards Website! 👀

Wholesomemaker using [Flask](https://flask.palletsprojects.com/) as Website Framework. 

I want to using Next.js as Framework, but.. I still don't know how to do it, so.. i made this leaderboard website using Flask.

Enough bologna, here's the thing..

These website is consist of : 

- Flask Framework in Python, obviously.. `app.py`
- Web templates in HTML `/templates` 
- and web assets (css, js, and image) in `/assets`

I'm merging the leaderboards website because of some reasons and also cutting off some unused repos or branch.

Feel free to check out or customize your own leaderboard website. Cheers!

## Installation

- first, you need to install the Python and MongoDB (Optional)
  you can see the docs for [python](https://docs.python.org/3/using/windows.html) and [mongodb](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)
- after that, you can install the required files, with pip (python package manager thingy)

  `pip install -r "requirements.txt"`

- Don't forget to fill your `.env` using example format up there!

##### Levelling Systems (Optional)

- if you want the levelling systems.

  - after that, you need to make a database on mongodb, refer to this [guide](https://www.mongodb.com/basics/create-database).
    the database name should be `discord` and the collation name is `levelling`

- if you don't want the levelling systems.

  - If you're didn't want levelling system, just delete this file `cogs/levelsys.py`

##### Warning Systems (Important, well.. sort of)

So, basically.. Warning systems are connected with `cogs/mute.py` and `cogs/kick.py`. so in order to use those two commands, you need to use warning systems, otherwise.. it will erroring all over the place.

- To use the Warning systems (assuming you already create a database named `discord`), just create another collation, the name is `muted`, `kicks`, and `warning`

- if you don't use the levelling systems.

  - you need to make a database on mongodb, refer to this [guide](https://www.mongodb.com/basics/create-database). the database name should be `discord` and the collation name is `muted`, `kicks`, and `warning`


##### Finalize things...

- Whenever you're ready, You can start the bot with this commands.

  - `py main.py` = for windows
  - `python3 main.py` = for linux

and, Voila! You've setup the bot!

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://github.com/ZappiestSet81"><img src="https://avatars.githubusercontent.com/u/80011834?v=4" width="100px;" alt="ZappiestSet81"/><br /><sub><b>ZappiestSet81</b></sub></a><br /><a href="https://github.com/GNZTMPZ/Wholesomemaker-1/blob/master/cogs/wheelspin.py" title="Code">💻</a> <a href="#" title="Ideas, Planning, & Feedback">🤔</a> </td><td align="center"><a href="https://github.com/rsetiawan7"><img src="https://avatars.githubusercontent.com/u/7775372?v=4" width="100px;" alt="rsetiawan7"/><br /><sub><b>rsetiawan7</b></sub></a><br /><a href="https://github.com/GNZTMPZ/Wholesomemaker-1/blob/master/Dockerfile" title="Code">💻</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.
Contributions of any kind welcome!

