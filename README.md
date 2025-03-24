# github-auto-commit
If you need to auto commit on Github, you can use these repo to do some auto commit for you.

### PLEASE BE AWARE THAT THIS CAN BAN YOUR GITHUB ACCOUNT SO USE IT WITH YOUR OWN RESPONSIBILITY.

## install requirements

first create a simple repo in Github.

then install python3 on your server

```bash
sudo apt install python3
sudo apt install screen
```

then clone this repo

```bash
git clone https://github.com/Theshaho/github-auto-commit && cd github-auto-commit
```

then change the username and password and repo_name in the autocommit.py file

```bash
nano autocommit.py
```
change above variables and then Ctl + X => Y => Enter.

## start auto commit

create a screen

```bash
screen -S githubautocommit
```
then start the script

```bash
python3 autocommit.py
```

then Ctl + A + D
