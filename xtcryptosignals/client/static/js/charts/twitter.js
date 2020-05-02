function create_chart_twitter(chart_id, pt, days) {
      return Highcharts.chart(chart_id, {
        chart: {
            type: 'area'
        },
        title: {
            text: pt.replace('_', ' (') + ')'
        },
        credits: {
            enabled: false
        },
        xAxis: {
            categories: days,
        },
        yAxis: {
            title: {
                text: 'Number of Followers'
            },
        },
        tooltip: {
            shared: true,
        },
        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#666666',
                lineWidth: 1,
                marker: {
                    lineWidth: 1,
                    lineColor: '#666666'
                }
            }
        },
    });
}