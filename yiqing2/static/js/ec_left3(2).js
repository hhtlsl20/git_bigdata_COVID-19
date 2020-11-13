var ec_left32 = echarts.init(document.getElementById('l3'));
ec_left3_Option = {
    title:{
        text:'1-7月疫情新增数据概览',
        textStyle:{
            color:'white',
            fontsize:'20px'
        }
    },
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        data: ['新增确诊数', '新增治愈数','新增死亡数'],
        left: 'right',
        textStyle:{
            color:"white",
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis:  {
        type: 'value',
        axisLabel:{
            textStyle: {
                color: "white"
            }
        }
    },
    yAxis: {
        type: 'category',
        data: ["1月","2月","3月","4月","5月","6月","7月"],
         axisLabel:{
            textStyle: {
                color: "white"
            }
        }
    },
    series: [
        {
            name: '新增确诊数',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: false,
                    position: 'insideRight'
                }
            },
            itemStyle:{
                normal:{
                    color:"red"
                }
            },
            data: []
        },
        {
            name: '新增治愈数',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: false,
                    position: 'insideRight'
                }
            },
            itemStyle:{
                normal:{
                    color:"#faff72"
                }
            },
            data: []
        },
        {
            name: '新增死亡数',
            type: 'bar',
            stack: '总量',
            label: {
                normal: {
                    show: false,
                    position: 'insideRight'
                }
            },
              itemStyle:{
                normal:{
                    color:"#00e09e"
                }
            },
            data: []
        }
    ]
};
ec_left32.setOption(ec_left3_Option);
tools.loopShowTooltip(ec_left32, ec_left3_Option, {
    loopSeries: true});