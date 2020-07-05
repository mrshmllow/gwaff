# gwaff

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bwac2517/gwaff/record-xp-data?label=Xp%20Data%20Recording&style=for-the-badge) ![Codacy grade](https://img.shields.io/codacy/grade/ca5609bf92774f9ea1d6b55cbea6dfed?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/bwac2517/gwaff?style=for-the-badge) ![code sytle](https://img.shields.io/badge/code%20style-black-black?style=for-the-badge)

A mee6 xp graphing python program using matplotlib.

Originally made for the mumbo jumbo discord server

To use it for your own server, follow these steps:

1. ![fork](https://github.com/bwac2517/gwaff/fork) or ![download it](https://github.com/bwac2517/gwaff/archive/master.zip) and use it locally.

2. Edit the ![config.yml](https://github.com/bwac2517/gwaff/blob/master/config.yml)
```server_id: 377946908783673344 # your server id
plot_range: 60 # how many uses to include in the plots
bar_range: 15 # how many users to include in the bars
data_range: 300 # -1 for all users. how many people to include in data collection
minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
rank_range: 20 # the interval it starts a new graph
darkmode: true # dark mode or not
title: "GWAFF V2\nxp gain overtime"
bottom_message: "\n\nJoin cremes server for dedicated gwaff channel.\nCheck out the github on bwac2517/gwaff"
```  
3. You have to run `python3 gwaff.py -s` everyday, at the same time (to keep it consistent)
![(we use a github action for this)](https://github.com/bwac2517/gwaff/blob/master/.github/workflows/main.yml)

4. Every two days, you can generate with `python3 gwaff.py -p`, hack in any changes you want (open a PR :p)  
**you can do `python3 gwaff.py -p -s` to do both at once**
