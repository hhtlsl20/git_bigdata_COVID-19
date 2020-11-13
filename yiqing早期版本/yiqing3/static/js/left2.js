// 折线图1模块制作
(function() {
    var yearData1 = [
      {
        year: "国内",
        days: [],
        data: [
          // 两个数组是因为有三条线
          
          [],
          [],
          [],
        ]
      },
      {
        year: "国外",
        days: [],
        data: [
          // 两个数组是因为有三条线
          
          [],
          [],
          [],
        ]
      }
    ];
    // 1. 实例化对象
    var zexian1_myChart = echarts.init(document.getElementById('l2'));
    // 2.指定配置
    var zexian1_option = {
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
        data: yearData1[0].days,
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
      "dataZoom": [{
          "show": true,
          "height": 12,
          "xAxisIndex": [0],
          bottom:'8%',
          "start": 80,
          "end": 100,
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
      series: [
        {
          name: "新增确诊",
          type: "line",
          // 是否让线条圆滑显示
          smooth: true,
          data: yearData1[0].data[0],
        },
        {
          name: "新增治愈",
          type: "line",
          smooth: true,
          data: yearData1[0].data[1],
        },
        {
          name: "新增死亡",
          type: "line",
          smooth: true,
          data: yearData1[0].data[2],
        }
      ]
    };
  
    // 3. 把配置给实例对象
    zexian1_myChart.setOption(zexian1_option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function() {
      zexian1_myChart.resize();
    });
  
    // 5.点击切换效果
    $(".line h2").on("click", "a", function() {
      // alert(1);
      // console.log($(this).index());
      // 点击 a 之后 根据当前a的索引号 找到对应的 yearData的相关对象
      // console.log(yearData[$(this).index()]);
      var obj = yearData1[$(this).index()];
      zexian1_option.xAxis.data = obj.days;
      zexian1_option.series[0].data = obj.data[0];
      zexian1_option.series[1].data = obj.data[1];
      zexian1_option.series[2].data = obj.data[2];
      // 需要重新渲染
      zexian1_myChart.setOption(zexian1_option);
    });
function get_l2_data() {
    $.ajax({
        url:"/l2",
        success: function(data) {
            yearData1[0].days=data.c_day
            yearData1[0].data[0]=data.c_confirm_add
            yearData1[0].data[1]=data.c_heal_add
            yearData1[0].data[2]=data.c_dead_add
            yearData1[1].days=data.g_day
            yearData1[1].data[0]=data.g_confirm_add
            yearData1[1].data[1]=data.g_heal_add
            yearData1[1].data[2]=data.g_dead_add

            //更新数据，
            zexian1_option.xAxis.data = yearData1[0].days;
            zexian1_option.series[0].data = yearData1[0].data[0];
            zexian1_option.series[1].data = yearData1[0].data[1];
            zexian1_option.series[2].data = yearData1[0].data[2];
            //重新渲染
            zexian1_myChart.setOption(zexian1_option)
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
get_l2_data()
setInterval(get_l2_data,10000*10)
  })();

var index = 0; //播放所在下标
				var mTime = setInterval(function() {
					zexian1_myChart.dispatchAction({
						type: 'showTip',
						seriesIndex: 0,
						dataIndex: index
					});
					index++;
					if(index > 20) {
						index = 0;
					}
				}, 1000);