// 柱状图2
(function() {
    var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#F57474","#8B78F6"];
    var yearData4= [
      {
        city:["非洲", "欧洲", "大洋洲", "南美洲", "北美洲", "其他", "亚洲"],
        data: [
          [414660, 2494139, 9477, 2285854, 3233777, 712, 2263416],
          [10319, 192092, 126, 86906, 170365, 13, 52840],
          [196846, 1383009, 8573, 1331559, 1452773, 651, 1467653],
        ]
      }];
    // 1. 实例化对象
    var bar2_myChart = echarts.init(document.getElementById('r1'));
    // 2. 指定配置和数据
    var bar2_option = {

        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '2%',
          right: '4%',
          bottom: '14%',
          top:'16%',
          containLabel: true
        },
         legend: {
        data: ['累计确诊', '累计治愈', '累计死亡'],
        right: 10,
        top:12,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 12,
        itemHeight: 10,
        // itemGap: 35
    },
        xAxis: {
          type: 'category',
          data: yearData4[0].city,
          axisLine: {
            lineStyle: {
              color: 'white'

            }
          },
          axisLabel: {
            // interval: 0,
            // rotate: 40,
            textStyle: {
              fontFamily: 'Microsoft YaHei'
            }
          },
        },

        yAxis: {
          type: 'value',
          axisLine: {
            show: false,
            lineStyle: {
              color: 'white'
            }
          },
          splitLine: {
            show: true,
            lineStyle: {
              color: 'rgba(255,255,255,0.3)'
            }
          },
          axisLabel: {}
        },
        "dataZoom": [{
          "show": true,
          "height": 12,
          "xAxisIndex": [
            0
          ],
          bottom:'8%',
          "start": 20,
          "end": 90,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle:{
            color:"#d3dee5",

          },
          textStyle:{
            color:"#fff"},
          borderColor:"#90979c"
        }, {
          "type": "inside",
          "show": true,
          "height": 15,
          "start": 1,
          "end": 35
        }],
        series: [{
          name: '累计确诊',
          type: 'bar',
          barWidth: '25%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#ed3f35'
                }, {
                    offset: 1,
                    color: '#ed3f35'
                }]),

            },
          },
          data: yearData4[0].data[0]
        },
        {
          name: '累计治愈',
          type: 'bar',
          barWidth: '25%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#00f2f1'
                }, {
                    offset: 1,
                    color: '#00f2f1'
                }]),

            }

          },
          data: yearData4[0].data[1]
        },
        {
          name: '累计死亡',
          type: 'bar',
          barWidth: '25%',
          itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#F8F8FF'
                }, {
                    offset: 1,
                    color: '#F8F8FF'
                }]),

            }
          },
          data: yearData4[0].data[2]
        }]
      };

      var app = {
        currentIndex: -1,
      };
      setInterval(function () {
        var dataLen = option.series[0].data.length;

        // 取消之前高亮的图形
        myChart.dispatchAction({
          type: 'downplay',
          seriesIndex: 0,
          dataIndex: app.currentIndex
        });
        app.currentIndex = (app.currentIndex + 1) % dataLen;
        //console.log(app.currentIndex);
        // 高亮当前图形
        myChart.dispatchAction({
          type: 'highlight',
          seriesIndex: 0,
          dataIndex: app.currentIndex,
        });
        // 显示 tooltip
        myChart.dispatchAction({
          type: 'showTip',
          seriesIndex: 0,
          dataIndex: app.currentIndex
        });


      }, 1000);
  
    // 3. 把配置给实例对象
    bar2_myChart.setOption(bar2_option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
      bar2_myChart.resize();
    });

    function get_r1_data() {
    $.ajax({
        url:"/r1",
        success: function(data) {
            yearData4[0].city=data.city_r1
            yearData4[0].data[0]=data.confirm_r1
            yearData4[0].data[1]=data.heal_r1
            yearData4[0].data[2]=data.head_r1
            //更新数据
            bar2_myChart.xAxis[0].data=yearData4[0].city
            bar2_myChart.series[0].data = yearData4[0].data[0]
            bar2_myChart.series[1].data = yearData4[0].data[1]
            bar2_myChart.series[2].data = yearData4[0].data[2]
            //重新渲染
            bar2_myChart.setOption(bar2_option);
        },
        error: function(xhr, type, errorThrown) {
        }
    })
};
get_r1_data()
setInterval(get_r1_data,10000*10);

  })();




