// 折线图2模块制作

var yearData3= [
      {
        year: "国内",
        days:[],
        data: [
          // 两个数组是因为有三条线

          [],
          [],
          [],
        ]
      },
      {
        year: "国外",
        days:[],
        data: [
          // 两个数组是因为有三条线
          [],
          [],
          []
        ]
      }
    ];

(function() {
    // 1. 实例化对象
    var zexian2_myChart = echarts.init(document.getElementById('r2'));
    // 2.指定配置
    var zexian2_option = {
      // 通过这个color修改两条线的颜色
      color: ["#ed3f35","#00f2f1","#F8F8FF"],
      tooltip: {
        trigger: "axis"
      },
      legend: {
        // 如果series 对象有name 值，则 legend可以不用写data
        // 修改图例组件 文字颜色
        textStyle: {
          color: "#4c9bfd"
        },
        // 这个10% 必须加引号
        right: "10%"
      },
      grid: {
        top: "20%",
        left: "3%",
        right: "4%",
        bottom: "3%",
        show: true, // 显示边框
        borderColor: "#012f4a", // 边框颜色
        containLabel: true // 包含刻度文字在内
      },
  
      xAxis: {
        type: "category",
        boundaryGap: false,
        data: yearData3[0].days,
        axisTick: {
          show: false // 去除刻度线
        },
        axisLabel: {
          color: "#4c9bfd" // 文本颜色
        },
        axisLine: {
          show: false // 去除轴线
        }
      },
      yAxis: {
        type: "value",
        axisTick: {
          show: false // 去除刻度线
        },
        axisLabel: {
          color: "#4c9bfd" // 文本颜色
        },
        axisLine: {
          show: false // 去除轴线
        },
        splitLine: {
          lineStyle: {
            color: "#012f4a" // 分割线颜色
          }
        }
      },

      series: [
        {
          name: "现存确诊",
          type: "line",
          // 是否让线条圆滑显示
          smooth: true,
          data: yearData3[0].data[0]
        },
        {
          name: "累计治愈",
          type: "line",
          smooth: true,
          data: yearData3[0].data[1]
        },
        {
          name: "累计死亡",
          type: "line",
          smooth: true,
          data: yearData3[0].data[2]
        }
      ]
    };
  
    // 3. 把配置给实例对象
    zexian2_myChart.setOption(zexian2_option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
      zexian2_myChart.resize();
    });

    // 5.点击切换效果
    $(".line2 h2").on("click", "a", function() {
      // alert(1);
      // console.log($(this).index());
      // 点击 a 之后 根据当前a的索引号 找到对应的 yearData的相关对象
      // console.log(yearData[$(this).index()]);
      var obj = yearData3[$(this).index()]
      zexian2_option.xAxis.data = obj.days;
      zexian2_option.series[0].data = obj.data[0];
      zexian2_option.series[1].data = obj.data[1];
      zexian2_option.series[2].data = obj.data[2];
      // 需要重新渲染
      zexian2_myChart.setOption(zexian2_option);
    });

function get_r2_data() {
    $.ajax({
        url:"/r2",
        success: function(data) {
            yearData3[0].days=data.c_day
            yearData3[0].data[0]=data.c_confirm_add
            yearData3[0].data[1]=data.c_heal_add
            yearData3[0].data[2]=data.c_dead_add
            yearData3[1].days=data.g_day
            yearData3[1].data[0]=data.g_confirm_add
            yearData3[1].data[1]=data.g_heal_add
            yearData3[1].data[2]=data.g_dead_add

            //更新数据
            zexian2_option.xAxis.data = yearData3[0].days;
            zexian2_option.series[0].data = yearData3[0].data[0]
            zexian2_option.series[1].data = yearData3[0].data[1]
            zexian2_option.series[2].data = yearData3[0].data[2]
            //重新渲染
            zexian2_myChart.setOption(zexian2_option);
            tools.loopShowTooltip(zexian2_myChart, zexian2_option, {
                loopSeries: true
            });
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
get_r2_data()
setInterval(get_r2_data,10000*10)

  })();