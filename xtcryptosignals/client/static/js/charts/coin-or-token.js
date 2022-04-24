function create_chart_coin_or_token(chart_id, dyn_formatter, data, coin_or_token, quote, frequency) {

      let titleTxt = `Price (${data["quote"]})`
      if (data["quote"] !== quote) {
          titleTxt = `Price (converted to ${data["quote"]})`
      }

      return Highcharts.chart(chart_id, {
        chart: {
            zoomType: 'x',
            events: {
                load: function() {
                    this.showLoading();
                }
            }
        },
        title: {
            text: `${coin_or_token} Price - ${frequency}`
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        credits: {
            enabled: false
        },
        time: {
            timezone: moment.tz.guess(true)
        },
        xAxis: [{
            type: 'datetime',
            title: {
                text: `Datetime (${moment.tz.guess(true)})`
            }
        }],
        yAxis: [{
            labels: {
                 style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return dyn_formatter.format(this.value);
                }
            },
            title: {
                text: titleTxt,
                style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return dyn_formatter.format(this.value);
                }
            }
        }, {
            labels: {
                format: '{value}' + data["quote"],
                style: {
                    color: Highcharts.getOptions().colors[1]
                },
                formatter: function() {
                    return dyn_formatter.format(this.value);
                }
            },
            title: {
                text: `${coin_or_token} Volume (${quote})`,
            },
            opposite: true
        }, {
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[3]
                },
                formatter: function() {
                    return num_formatter.format(this.value);
                }
            },
            title: {
                text: coin_or_token + ' Number of Trades',
                style: {
                    color: Highcharts.getOptions().colors[3]
                }
            },
            opposite: true
        }],
        tooltip: {
            shared: true,
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 120,
            verticalAlign: 'top',
            y: 100,
            floating: true,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || // theme
                'rgba(255,255,255,0.25)'
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    enable: false
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            },
            line: {
                marker: {
                    enable: false
                },
            }
        },
        series: [{
            name: coin_or_token + ' Price',
            type: 'area',
            data: data.prices,
            tooltip: {
                pointFormatter: function() {
                    return '<span style="color:' + this.color + '">\u25CF</span> ' +
                        this.series.name + ': <b>' + dyn_formatter.format(this.y)  + ' ' + data["quote"] + '</b><br/>';
                }
            },
            marker: {
                enabled: false,
            },
        }, {
            name: coin_or_token + ' Volume',
            type: 'line',
            yAxis: 1,
            data: data.volumes,
            tooltip: {
                pointFormatter: function() {
                    return '<span style="color:' + this.color + '">\u25CF</span> ' +
                        this.series.name + ': <b>' + num_formatter.format(this.y) + ' ' + quote + '</b><br/>';
                }
            },
            marker: {
                enabled: false,
            },
        }, {
            name: coin_or_token + ' Number of Trades',
            type: 'line',
            color: Highcharts.getOptions().colors[3],
            yAxis: 2,
            data: data.num_trades,
            tooltip: {
                pointFormatter: function() {
                    return '<span style="color:' + this.color + '">\u25CF</span> ' +
                        this.series.name + ': <b>' + num_formatter.format(this.y) + '</b><br/>';
                }
            },
            marker: {
                enabled: false,
            },
        }]
    });
}