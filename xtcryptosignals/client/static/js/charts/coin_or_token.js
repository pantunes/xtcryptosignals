function create_chart_coin_or_token(formatter, num_formatter, data, coin_or_token, frequency) {
      return Highcharts.chart('chart_' + coin_or_token + frequency, {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: coin_or_token + ' Price - ' + frequency
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        credits: {
            enabled: false
        },
        xAxis: [{
            type: 'datetime',
            title: {
                text: 'Datetime (UTC)'
            }
        }],
        yAxis: [{
            labels: {
                format: '${value}',
                 style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return formatter.format(this.value);
                }
            },
            title: {
                text: 'Price (USD)',
                style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return formatter.format(this.value);
                }
            }
        }, {
            labels: {
                format: '${value}',
                style: {
                    color: Highcharts.getOptions().colors[1]
                },
                formatter: function() {
                    return formatter.format(this.value);
                }
            },
            title: {
                text: 'Volume (USD)',
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
                text: 'Number of Trades',
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
                valuePrefix: '$'
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
                valueSuffix: '$'
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
            marker: {
                enabled: false,
            },
        }]
    });
}