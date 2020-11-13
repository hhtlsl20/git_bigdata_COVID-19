var ec_right1 = echarts.init(document.getElementById('r1'));
var ec_right1_option = {
	//标题样式
	title : {
	    text : "非湖北地区城市确诊TOP5",
	    textStyle : {
	        color : '#91d6e7',
            fontSize:30
	    },
	    left : 'left',
        top:'5%'
	},
    grid:{
		top:'25%'
	},
    tooltip: {
        trigger: 'axis',
        formatter: "{b} : {c}",
        axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    xAxis: {
        data: [],
        //坐标轴
        axisLine: {
            lineStyle: {
                color: '#3eb2e8'
            },
            show:false
        },
        //坐标值标注
        axisLabel: {
            show: true,
            textStyle: {
                color: '#fff',
                fontSize: 20
            }
        }
    },
    yAxis: {
        //坐标轴
        axisLine: {
            show: false
        },
        //坐标值标注
        axisLabel: {
            show: true,
            textStyle: {
                color: '#fff',
                fontSize:15
            }
        },
        //分格线
        splitLine: {
            lineStyle: {
                color: '#4784e8'
            },
            show:false
        }
    },
    series: [{
        name: 'a',
        tooltip: {
            show: false
        },
        type: 'bar',
        barWidth: 24.5,
        itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                    offset: 0,
                    color: "#0B4EC3" // 0% 处的颜色
                }, {
                    offset: 0.6,
                    color: "#138CEB" // 60% 处的颜色
                }, {
                    offset: 1,
                    color: "#17AAFE" // 100% 处的颜色
                }], false)
            }
        },
        data: [],
        barGap: 0
    }, {
        type: 'bar',
        barWidth: 8,
        itemStyle: {
            normal: {
                color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                    offset: 0,
                    color: "#09337C" // 0% 处的颜色
                }, {
                    offset: 0.6,
                    color: "#0761C0" // 60% 处的颜色
                }, {
                    offset: 1,
                    color: "#0575DE" // 100% 处的颜色
                }], false)
            }
        },
        barGap: 0,
        data: []
    }, {
        name: 'b',
        tooltip: {
            show: false
        },
        type: 'pictorialBar',
        itemStyle: {
            borderWidth: 1,
            borderColor: '#0571D5',
            color: '#1779E0'
        },
        symbol: 'path://M 0,0 l 120,0 l -30,60 l -120,0 z',
        symbolSize: ['30', '12'],
        symbolOffset: ['0', '-11'],
        //symbolRotate: -5,
        symbolPosition: 'end',
        data: [],
        z: 3
    }]
};
				// var index = 0; //播放所在下标
				// var mTime = setInterval(function() {
				// 	ec_right1.dispatchAction({
				// 		type: 'showTip',
				// 		seriesIndex: 0,
				// 		dataIndex: index
				// 	});
				// 	index++;
				// 	if(index > data.length) {
				// 		index = 0;
				// 	}
				// }, 1000);
				ec_right1.setOption(ec_right1_option);
				tools.loopShowTooltip(ec_right1, ec_right1_option, {
    loopSeries: true});