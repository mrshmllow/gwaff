# 📈 Open source [mee6.xyz](https://mee6.xyz/) xp graphing 
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
1. ["Fork this"](https://github.com/bwac2517/gwaff/fork) or [download it](https://github.com/bwac2517/gwaff/archive/master.zip) and use it locally.
2. Next, edit the [config.yml](https://github.com/bwac2517/gwaff/blob/master/config.yml)
```server_id: 377946908783673344 # your server id
darkmode: true # dark mode or not
title: "GWAFF V2"
bottom_message: "\nCheck out the github on bwac2517/gwaff"
plot:
  range: 60 # how many users to include in the plots
  minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
  rank_range: 20 # the interval it starts a new graph
bar:
  range: 15 # how many users to include in the bar graph
versus:
  - 298294667219435521
  - 387259938977742849
  - 477148794861912084
  - 724378805728313395
data:
  range: 300
```
3. You should [make a venv](https://docs.python.org/3/library/venv.html).  
Install dependencies with `pip install -r requirements.txt`
4. Run `python3 gwaff.py --store` every day to collect xp data (at the same time of day to keep consistency) (Use a github action for this to automate it)  
This is saved in `gwaff.json` **strongly recommended you use git incase you want to roll back any unwanted saves**

5. You can generate a graphs with `python3 gwaff.py --store --plot --save`  
**you can use `python3 gwaff.py --store --plot --save --post {A discord webhook url}` to post to discord at the same time**. 

6. Make any changes you want! (make a pull request :p)
