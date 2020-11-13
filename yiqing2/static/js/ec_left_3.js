var ec_left3 = echarts.init(document.getElementById('l3'));
ec_left3_Option = {
     title: {
            text: "1-8月疫情数据对比图",
            left: "left",
            top:'5%',
            textStyle:{
                color:"#91d6e7",
                fontSize:30
            }
        },
  	grid:{
		top:'25%',
		bottom:'10%'
	},
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        },
   //     formatter: function(params){return Math.max(params.value,-params.value)}

        formatter: function (params) {
                    return params[0].name +
                        "<br>新增死亡：" + params[0].value +
                        "<br>新增治愈：" +  params[1].value;
                }
    },
    legend: {
        data:['新增死亡', '新增治愈'],
        left: "right",
        textStyle:{
            color:"white"
        }
    },
    // grid: {
    //     left: '3%',
    //     right: '4%',
    //     bottom: '3%',
    //     containLabel: true
    // },
    xAxis : [
        {
            type : 'value',
            axisLabel: {
        	color:'white',
            fontSize:15
		}
        }
    ],
    yAxis : [
        {
            type : 'category',
            axisTick : {show: false},
            data : ['1月','2月','3月','4月','5月','6月','7月','8月'],
            axisLabel: {
        	color:'white',
            fontSize: 15
		}
        }
    ],
    series : [

        {
            name:'新增死亡',
            type:'bar',
            stack: '总量',
            label: {
                normal: {
                    show: false
                }
            },
            data:[]
        },
        {
            name:'新增治愈',
            type:'bar',
            stack: '总量',
            label: {
                normal: {
                    show: false,
                    formatter: function(params){return -params.value}
                }
            },
            itemStyle:{
                normal:{
                    color:'#3876dc'
                }
            },
            data:[]
        }
    ]
};
ec_left3.setOption(ec_left3_Option);
tools.loopShowTooltip(ec_left3, ec_left3_Option, {
    loopSeries: true});