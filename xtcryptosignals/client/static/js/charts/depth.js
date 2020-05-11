function create_chart_depth(chart_id, coin_or_token) {
    return Highcharts.chart(chart_id, {
        chart: {
            type: 'area',
            zoomType: 'xy'
        },
        title: {
            text: `${coin_or_token} Market Depth`
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click in the plot area to zoom in' : 'Pinch the chart to zoom in'
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
                text: 'Price (USDT)'
            }
        },
        yAxis: [{
            lineWidth: 1,
            gridLineWidth: 1,
            title: null,
            tickWidth: 1,
            tickLength: 5,
            tickPosition: 'inside',
            labels: {
                align: 'left',
                x: 8
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
            headerFormat: '<span style="font-size=10px;">Price: {point.key} USDT</span><br/>',
            valueDecimals: 2
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