function draw_chart_fear_and_greed(data, frequency) {
    return Highcharts.chart('chart', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Fear & Greed Index vs BTC Price - ' + frequency
        },
        subtitle: {
            text: null
        },
        credits: {
            enabled: false
        },
        xAxis: [{
            categories: data.days,
            crosshair: true
        }],
        yAxis: [{ // Primary yAxis
            labels: {
                format: '${value}',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            title: {
                text: 'Price',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            }
        }, { // Secondary yAxis
            title: {
                text: 'Percentage',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            labels: {
                format: '{value}%',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
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
        series: [{
            name: 'Fear & Greed Index',
            type: 'area',
            yAxis: 1,
            data: data.cfgi,
            tooltip: {
                valueSuffix: '%'
            }

        }, {
            name: 'BTC Price',
            type: 'line',
            data: data.btc,
            tooltip: {
                valuePrefix: '$'
            }
        }]
    });
}