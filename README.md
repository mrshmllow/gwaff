# gwaff

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bwac2517/gwaff/record-xp-data?label=Xp%20Data%20Recording%20Status&style=flat-square)

![Codacy grade](https://img.shields.io/codacy/grade/ca5609bf92774f9ea1d6b55cbea6dfed?style=flat-square)


A mee6 xp graphing python program using matplotlib

To use it for your own server, use this ![as a template repo](https://github.com/bwac2517/gwaff/generate) OR download it and use it locally.
Next, edit the ![config.yml](https://github.com/bwac2517/gwaff/blob/master/config.yml)

```
server_id: 377946908783673344 # your server id
plot_range: 60 # how many uses to include in the plots
data_range: 300 # -1 for all users. how many people to include in data collection
minium_xp: 500 # anyone with a xp gain below this will not be included in the plots
darkmode: true # dark mode or not
```

You have to run store.py at the same time, every day.
![(we use a github action for this)](https://github.com/bwac2517/gwaff/blob/master/.github/workflows/main.yml)
