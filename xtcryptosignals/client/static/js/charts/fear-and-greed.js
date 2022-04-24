function create_chart_fear_and_greed(data, quote, frequency) {

    return Highcharts.chart('chart', {
        chart: {
            zoomType: 'x',
            events: {
                load: function() {
                    this.showLoading();
                }
            }
        },
        title: {
            text: `Crypto Fear & Greed Index vs BTC Price - ${frequency}`
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
            categories: data.days,
            crosshair: true
        }],
        yAxis: [{
            labels: {
                style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return num_formatter.format(this.value);
                }
            },
            title: {
                text: `Price (${quote})`,
                style: {
                    color: Highcharts.getOptions().colors[0]
                },
                formatter: function() {
                    return num_formatter.format(this.value);
                }
            }
        }, {
            title: {
                text: 'Percentage',
            },
            labels: {
                format: '{value}%',
            },
            max: 100,
            opposite: true
        }],
        tooltip: {
            shared: true
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
                    radius: 1
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
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },
        series: [{
            name: 'BTC Price',
            type: 'area',
            data: data.BTC,
            tooltip: {
                pointFormatter: function() {
                    return '<span style="color:' + this.color + '">\u25CF</span> ' +
                        this.series.name + ': <b>' + num_formatter.format(this.y) + ' ' + quote + '</b><br/>';
                }
            },

        }, {
            name: 'Fear & Greed Index',
            type: 'line',
            yAxis: 1,
            data: data.cfgi,
            tooltip: {
                valueSuffix: '%'
            }
        }]
    });
}