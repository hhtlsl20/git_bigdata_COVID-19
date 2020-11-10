// 柱状图1模块

// 数据变化
    var dataAll = [
      { year: "全球", city:[],data: [] },
      { year: "美国", city:[],data: [] }
    ];

(function() {

    // 实例化对象
    var bar1_myChart = echarts.init(document.getElementById('l1'));
    // 指定配置和数据
    var bar1_option = {
      color: ["#2f89cf"],
      tooltip: {
        trigger: "axis",
        axisPointer: {
          // 坐标轴指示器，坐标轴触发有效
          type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
        }
      },
      grid: {
        left: "0%",
        top: "10px",
        right: "0%",
        bottom: "4%",
        containLabel: true
      },
      xAxis: [
        {
          type: "category",
          data: dataAll[0].city,
          axisTick: {
            alignWithLabel: true
          },
          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255,.6)",
              fontSize: "0.20rem"
            }
          },
          axisLine: {
            show: false
          }
        }
      ],
      yAxis: [
        {
          type: "value",
          axisLabel: {
            textStyle: {
              color: "rgba(255,255,255,.6)",
              fontSize: "12"
            }
          },
          axisLine: {
            lineStyle: {
              color: "rgba(255,255,255,.1)"
              // width: 1,
              // type: "solid"
            }
          },
          splitLine: {
            lineStyle: {
              color: "rgba(255,255,255,.1)"
            }
          }
        }
      ],
      series: [
        {
          name: "",
          type: "bar",
          barWidth: "35%",
          data: dataAll[0].data,
          itemStyle: {
            barBorderRadius: 5
          }
        }
      ]
    };


    // 把配置给实例对象
    bar1_myChart.setOption(bar1_option);
    window.addEventListener("resize", function() {
      bar1_myChart.resize();
    });
    //数据获取操作
    function get_l1_data() {
    $.ajax({
        url:"/l1",
        success: function(data) {
            dataAll[0].city=data.name
            dataAll[0].data=data.name_confirm
            dataAll[1].city=data.city
            dataAll[1].data=data.city_confirm

            bar1_option.xAxis[0].data=dataAll[0].city
            bar1_option.series[0].data = dataAll[0].data;
            bar1_myChart.setOption(bar1_option);
             tools.loopShowTooltip(bar1_myChart, bar1_option, {
    loopSeries: true
  });
        },
        error: function(xhr, type, errorThrown) {

        }
    })
    };
    get_l1_data();
    setInterval(get_l1_data,100000*10);
    //触发点击选项
    $(".bar h2 ").on("click", "a", function() {
      bar1_option.xAxis[0].data = dataAll[$(this).index()].city;
      bar1_option.series[0].data = dataAll[$(this).index()].data;
      bar1_myChart.setOption(bar1_option);
    });
  })();
