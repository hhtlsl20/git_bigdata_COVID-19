// 饼形图1

// 数据变化
var dataAll_2 = [
    { year: "国内", data: [8, 7, 4] },
    { year: "国外",data: [3, 8, 2] }
  ];

(function() {
  // 1. 实例化对象
  var pie1_myChart = echarts.init(document.getElementById('l3'));
  // 2.指定配置
  var pie1_option = {
    color: ["#ed3f35","#00f2f1","#F8F8FF"],
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)"
    },

    legend: {
      bottom: "0%",
      // 修改小图标的大小
      itemWidth: 10,
      itemHeight: 10,
      // 修改图例组件的文字为 12px
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    series: [
      {
        name: "疫情病例分布",
        type: "pie",
        // 这个radius可以修改饼形图的大小
        // radius 第一个值是内圆的半径 第二个值是外圆的半径
        radius: ["40%", "60%"],
        center: ["50%", "45%"],
        avoidLabelOverlap: false,
        // 图形上的文字
        label: {
          show: false,
          position: "center"
        },
        // 链接文字和图形的线是否显示
        labelLine: {
          show: false
        },
        data: [
          { value: 84347, name: "累计确诊" },
          { value: 78664, name: "累计治愈" },
          { value: 4643, name: "累计死亡" },
        ]
      }
    ]
  };

  // 3. 把配置给实例对象
  pie1_myChart.setOption(pie1_option);
  // 4. 让图表跟随屏幕自动的去适应
  window.addEventListener("resize", function() {
    pie1_myChart.resize();
  });
   // 5.点击切换效果
  $(".pie h2").on("click", "a", function() {
    // alert(1);
    // console.log($(this).index());
    // 点击 a 之后 根据当前a的索引号 找到对应的 yearData的相关对象
    // console.log(yearData[$(this).index()]);
    var obj = dataAll_2[$(this).index()];
    pie1_option.series[0].data[0].value = obj.data[0];
    pie1_option.series[0].data[1].value = obj.data[1];
    pie1_option.series[0].data[2].value = obj.data[2];
    pie1_myChart.setOption(pie1_option);
    tools.loopShowTooltip(pie1_myChart, pie1_option, {
        loopSeries: true
    });
  });
  //返回病例指数
function get_l3_data() {
    $.ajax({
        url:"/l3",
        success: function(data) {
            dataAll_2[0].data[0]=data.china_confirm
            dataAll_2[0].data[1]=data.china_heal
            dataAll_2[0].data[2]=data.china_dead
            dataAll_2[1].data[0]=data.global_confirm
            dataAll_2[1].data[1]=data.global_heal
            dataAll_2[1].data[2]=data.global_dead

            //更新数据
            pie1_option.series[0].data[0].value = dataAll_2[0].data[0];
            pie1_option.series[0].data[1].value = dataAll_2[0].data[1];
            pie1_option.series[0].data[2].value = dataAll_2[0].data[2];
            //重新渲染
            pie1_myChart.setOption(pie1_option);
            tools.loopShowTooltip(pie1_myChart, pie1_option, {
                loopSeries: true
            });
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
  get_l3_data()
  setInterval(get_l3_data,10000*10)
})();