// 复学复课模块
(function() {
    var pie2_myChart = echarts.init(document.getElementById('r3'));
    var colorList = [[
      '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
      '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
      '#1e90ff', '#ff6347', '#7b68ee', '#d0648a', '#ffd700',
      '#6b8e23', '#4ea397', '#3cb371', '#b8860b', '#7bd9a5'
      ],
      [
      '#ff7f50', '#87cefa', '#da70d6', '#32cd32', '#6495ed',
      '#ff69b4', '#ba55d3', '#cd5c5c', '#ffa500', '#40e0d0',
      '#1e90ff', '#ff6347', '#7b68ee', '#00fa9a', '#ffd700',
      '#6b8e23', '#ff00ff', '#3cb371', '#b8860b', '#30e0e0'
      ],
      [
      '#929fff', '#9de0ff', '#ffa897', '#af87fe', '#7dc3fe',
      '#bb60b2', '#433e7c', '#f47a75', '#009db2', '#024b51', 
      '#0780cf', '#765005', '#e75840', '#26ccd8', '#3685fe', 
      '#9977ef', '#f5616f', '#f7b13f', '#f9e264', '#50c48f'
      ]][2];

    var ALLdata = [];
  pie2_option = {
      // 图表标题
      title: {
          show:false,//显示策略，默认值true,可选为：true（显示） | false（隐藏）
          text: '热搜榜话题图谱',//主标题文本，'\n'指定换行
          x: 'center',        // 水平安放位置，默认为左对齐，可选为：
                            // 'center' ¦ 'left' ¦ 'right'
                            // ¦ {number}（x坐标，单位px）
          y: 'bottom',             // 垂直安放位置，默认为全图顶端，可选为：
                            // 'top' ¦ 'bottom' ¦ 'center'
                            // ¦ {number}（y坐标，单位px）
          //textAlign: null          // 水平对齐方式，默认根据x设置自动调整
          backgroundColor: 'rgba(0,0,0,0)',
          borderColor: '#ccc',    // 标题边框颜色
          borderWidth: 0,         // 标题边框线宽，单位px，默认为0（无边框）
          padding: 5,             // 标题内边距，单位px，默认各方向内边距为5，
                                  // 接受数组分别设定上右下左边距，同css
          itemGap: 10,            // 主副标题纵向间隔，单位px，默认为10，
          textStyle: {
              fontSize: 18,
              fontWeight: 'bolder',
              color: '#333'        // 主标题文字颜色
          },
          subtextStyle: {
              color: '#aaa'        // 副标题文字颜色
          }
      },
      backgroundColor: '',
      tooltip: {},
      animationDurationUpdate: function(idx) {
          // 越往后的数据延迟越大
          return idx * 100;
      },
      animationEasingUpdate: 'bounceIn',
      color: ['#fff', '#fff', '#fff'],
      series: [{
          type: 'graph',
          layout: 'force',
          force: {
              repulsion: 250,
              edgeLength: 10
          },
          roam: true,
          label: {
              normal: {
                  show: true
              }
          },
          data: [
              
              {"name": '武汉重启满月', "value": 11718475, "symbolSize": 149, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[0], "color": colorList[0] } } },
              {"name": '多所大学部分年级本学期不返校', "value": 8842381, "symbolSize": 131, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[1], "color": colorList[1] } } },
              {"name": '又一批学校叫停开学', "value": 7551764, "symbolSize": 123, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[2], "color": colorList[2] } } },
              {"name": '杭州5月18日幼儿园大班开学', "value": 2397216, "symbolSize": 123, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[3], "color": colorList[3] } } },
              {"name": '景区要求护士出示原件才能免费', "value": 847720, "symbolSize": 118, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[4], "color": colorList[4] } } },
              {"name": '武汉国际班轮开航', "value": 979565, "symbolSize": 115, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[5], "color": colorList[5] } } },
              {"name": '香港影院复工', "value": 5563521, "symbolSize": 111, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[6], "color": colorList[6] } } },
              {"name": '全国高校5月开学时间表', "value": 116802, "symbolSize": 106, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[7], "color": colorList[7] } } },
              {"name": ALLdata[8], "value": 2468532, "symbolSize": 106, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[7], "color": colorList[8] } } },
              {"name": ALLdata[9], "value": 5421639, "symbolSize": 103, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[9], "color": colorList[9] } } },
              {"name": ALLdata[10], "value": 2549782, "symbolSize": 95, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[10], "color": colorList[10] } } },
              {"name": ALLdata[11], "value": 872461, "symbolSize": 95, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[11], "color": colorList[11] } } },
              {"name": ALLdata[12], "value": 643169, "symbolSize": 92, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[12], "color": colorList[12] } } },
              {"name": ALLdata[13], "value": 973461, "symbolSize": 44, "draggable": true, "itemStyle": {"normal": { "shadowBlur": 100, "shadowColor": colorList[9], "color": colorList[9] } } },
          ]
      }]
  }
    pie2_myChart.setOption(pie2_option);
    // 监听浏览器缩放，图表对象调用缩放resize函数
    window.addEventListener("resize", function() {
      pie2_myChart.resize();
    });

    function get_r3_data() {
    $.ajax({
        url:"/r3",
        success: function(data) {
            ALLdata = data.d
            pie2_myChart.setOption(pie2_option)
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
get_r3_data()
setInterval(get_r3_data,10000*10)

  })();