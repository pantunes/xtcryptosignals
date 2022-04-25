function create_chart_depth(chart_id, coin_or_token, quote) {

    return Highcharts.chart(chart_id, {
        chart: {
            type: 'area',
            zoomType: 'xy',
            events: {
                load: function() {
                    this.showLoading();
                }
            }
        },
        title: {
            text: `${coin_or_token}/${quote} Market Depth`
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag an area in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        credits: {
            enabled: false
        },
        xAxis: {
            minPadding: 0,
            maxPadding: 0,
            plotLines: [{
                color: '#888',
                value: 0.1523,
                width: 1,
                label: {
                    text: 'Actual price',
                    rotation: 90
                }
            }],
            title: {
                text: `Price (${quote})`
            }
        },
        yAxis: [{
            lineWidth: 1,
            gridLineWidth: 1,
            tickWidth: 1,
            tickLength: 5,
            tickPosition: 'inside',
            labels: {
                align: 'left',
                x: 8
            },
            title: {
                text: `Number ${coin_or_token}`
            }
        }, {
            opposite: true,
            linkedTo: 0,
            lineWidth: 1,
            gridLineWidth: 0,
            title: null,
            tickWidth: 1,
            tickLength: 5,
            tickPosition: 'inside',
            labels: {
                align: 'right',
                x: -8
            }
        }],
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillOpacity: 0.2,
                lineWidth: 1,
                step: 'center'
            }
        },
        tooltip: {
            formatter: function() {
                return '<span style="color:' + this.color + '">\u25CF</span> ' +
                    this.series.name + ': <b>' + num_formatter_low_values.format(this.y) + ' ' + coin_or_token + '</b><br/>' +
                    '<span style="color:' + this.color + '">\u25CF</span> ' +
                    'Price: <b>' + num_formatter_low_values.format(this.x) + ' ' + quote + '</b><br/>';
            }
        },
        series: [{
            name: 'Bids',
            color: '#03a7a8'
        }, {
            name: 'Asks',
            color: '#fc5857'
        }]
    });
}