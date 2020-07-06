# 📈 gwaff
![image](https://i.imgur.com/KLeOwEM.png "Demo image") ![image 2](https://i.imgur.com/u4zb68g.png "Demo image 2")

![code sytle](https://img.shields.io/badge/code%20style-black-black?style=flat-square) ![Codacy branch grade](https://img.shields.io/codacy/grade/ca5609bf92774f9ea1d6b55cbea6dfed/master?style=flat-square)

`Why is it called 'gwaff?'`  
`- asked no one ever`

A mee6 xp graphing python program using matplotlib.

Generate line plots and bar charts from mee6 xp data!  
See your xp gain over time, and keep track of your highest talkers!

---

Originally made for the Mumbo Jumbo Discord server.

## Steps to use for your own server
1. **Recommended:** [Fork this](https://github.com/bwac2517/gwaff/fork)  
Alternatively: [download it](https://github.com/bwac2517/gwaff/archive/master.zip) and use it locally.
2. Next, edit the [config.yml](https://github.com/bwac2517/gwaff/blob/master/config.yml)
```
server_id: 377946908783673344 # your server id
darkmode: true # dark mode or not
title: "GWAFF V2"
bottom_message: "\n\ntemplate text.\nCheck out the github on bwac2517/gwaff" # example text
plot:
  range: 60 # how many users to include in the plots
  minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
  rank_range: 20 # the interval it starts a new graph
bar:
  range: 15 # how many users to include in the bar graph
data:
  range: 300 # -1 for all users. how many people to include in data collection
```
3. You should ![make a venv](https://docs.python.org/3/library/venv.html).  
Install dependencies with `pip install -r requirements.txt`
4. Run `python3 gwaff.py -s` every day to collect xp data (at the same time of day to keep consistency)  
(Use a github action for this to automate it in the next section!)  
This is saved in `gwaff.json`  
**It's strongly recommended you use git incase you want to roll back any unwanted saves**

5. After 2 days of data, you can generate graphs with `python3 gwaff.py -p`  
**you can use `python3 gwaff.py -s -p` to do both at once**. 

6. Make any changes you want! (make a pull request :p)

***Note:*** There is github action called `black.yml` which automatically blackens python files, delete if you don't want to blacken.

## Automatically save data using github actions
Use github actions to automate the data collection process, it's easier than setting up your own server, plus it's free (and easy!).

All you have to do is make a file called `xp-collection.yml` in `/.github/workflows/` with the contents:

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
        python3 gwaff.py -s

    - uses: EndBug/add-and-commit@v4
      with:
        message: "automated recording of xp data"
        add: "*"
        cwd: .
        force: true
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
This will generate the xp data on `gwaff.json`, and push it to master, every 00:00 UTC.  
Once you save and commit that file, you dont have to do anything, just check back after 00:00 UTC and you should see a new commit!

Read more about github actions: [https://github.com/features/actions](https://github.com/features/actions)
