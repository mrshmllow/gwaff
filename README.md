# 📈 Open source [mee6.xyz](https://mee6.xyz/) xp graphing 
![logo](https://raw.githubusercontent.com/bwac2517/gwaff/master/assets/logo.png)

![image](https://i.imgur.com/mFQKdG0.png "Demo image")

![code sytle](https://img.shields.io/badge/code%20style-black-black?style=flat-square) ![Codacy branch grade](https://img.shields.io/codacy/grade/ca5609bf92774f9ea1d6b55cbea6dfed/master?style=flat-square)

`Why is it called 'gwaff?'`  
`- asked no one ever`

A mee6 xp graphing python program using matplotlib.

Generate line plots and bar charts from mee6 xp data!  
See your xp gain over time, and keep track of your highest talkers!

---

Originally made for the Mumbo Jumbo Discord server.

## Steps to use for your own server
## For dummies (github beginners)
1. First, you will need to make a github accoun if you dont already have one, it's easy, just go to [https://github.com/signup](https://github.com/signup)
2. Once your back here, [Fork this](https://github.com/bwac2517/gwaff/fork), its okay if it doesnt make sense right now  
3. Next, edit the config.yml on your fork, you can find your fork at "https://github.com/[your-username]/gwaff"  
replace the values to what you would like:
```
server_id: 377946908783673344 # your server id
darkmode: true # dark mode or not
title: "GWAFF V2"
bottom_message: "\nCheck out the github on bwac2517/gwaff"
plot:
  range: 60 # how many users to include in the plots
  minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
  rank_range: 20 # the interval it starts a new graph
bar:
  range: 15 # how many users to include in the bar graph
data:
  range: 300 # -1 for all users. how many people to include in data collection
```
4. On your fork, press the Settings button. Now press Secrets. Press New Secret. Now on your discord server, press the cog on a channel, select Webhooks, then press Create Webhook, you can edit the name and stuff, but copy your webhook url. Now go back to your new secret, and paste it into the Value box, and call your secret "WEBHOOK_URL", press Update.
5. Now, your going to create a new file at /.github/workflows/data.yml, press Add file on your fork, then select Create New File, then paste ".github/workflows/data.yml" into the name of the file so it looks like this ![image](https://i.imgur.com/yExkeXO.png).  

Now paste
```
name: data-collection

on:
  schedule:    
  - cron: "0 0 * * *"
  
jobs:
  record:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python3 -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: store data
      run:
        python3 gwaff.py --store --save --plot --post ${{ secrets.WEBHOOK_URL }}

    - uses: EndBug/add-and-commit@v4
      with:
        message: "automated recording of xp data"
        add: "*"
        cwd: .
        force: true
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
If you did this right, your graphs will be posted into your channel every day at 00:00 UTC
