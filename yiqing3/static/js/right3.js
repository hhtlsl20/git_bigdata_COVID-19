// 复学复课模块
(function() {
    var pie2_myChart = echarts.init(document.getElementById('r3'));

var data = [
    {
        name: '国内治愈率',
        value: 92.09
    },{
        name: '全球治愈率',
        value: 64.59
    },{
        name: '国内死亡率',
        value: 5.28
    },{
        name: '全球死亡率',
        value: 3.75
    }]
'#dfeaff'
    var titleArr= [], seriesArr=[];
    colors=[['#00f2f1', '#dfeaff'],['#00f2f1', '#dfeaff'],['#ed3f35', '#dfeaff'], ['#ed3f35', '#fed4e0']]
    data.forEach(function(item, index){
        titleArr.push(
            {
                text:item.name,
                left: index * 20 + 10 +'%',
                top: '65%',
                textAlign: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    fontSize: '16',
                    color: colors[index][0],
                    textAlign: 'center',
                },
            }
        );
        seriesArr.push(
            {
                name: item.name,
                type: 'pie',
                clockWise: false,
                radius: [60, 70],
                itemStyle:  {
                    normal: {
                        color: colors[index][0],
                        shadowColor: colors[index][0],
                        shadowBlur: 0,
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        },
                    }
                },
                hoverAnimation: false,
                center: [index * 20 + 10 +'%', '50%'],
                data: [{
                    value: item.value,
                    label: {
                        normal: {
                            formatter: function(params){
                                return params.value+'%';
                            },
                            position: 'center',
                            show: true,
                            textStyle: {
                                fontSize: '20',
                                fontWeight: 'bold',
                                color: colors[index][0]
                            }
                        }
                    },
                }, {
                    value: 100-item.value,
                    name: 'invisible',
                    itemStyle: {
                        normal: {
                            color: colors[index][1]
                        },
                        emphasis: {
                            color: colors[index][1]
                        }
                    }
                }]
            }
        )
    });
pie2_option = {
    title:titleArr,
    series: seriesArr
}

    pie2_myChart.setOption(pie2_option);
    // 监听浏览器缩放，图表对象调用缩放resize函数
    window.addEventListener("resize", function() {
      pie2_myChart.resize();
      tools.loopShowTooltip(zexian1_myChart, zexian1_option, {
          loopSeries: true
      });
    });

    function get_r3_data() {
    $.ajax({
        url:"/r3",
        success: function(data) {
            ALLdata = data.d

        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
get_r3_data()
setInterval(get_r3_data,10000*10)

  })();