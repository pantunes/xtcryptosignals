function create_chart_twitter(chart_id, data, frequency) {

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
            text: `Twitter ${data.project.name} / ${data.project.coin_or_token} ${frequency}`
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
                text: `Date (${moment.tz.guess(true)})`
            }
        }],
        yAxis: {
            title: {
                text: 'Number of followers'
            }
        },
        legend: {
            enabled: false
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
            name: `Number of Followers`,
            type: 'area',
            data: data.num_followers,
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