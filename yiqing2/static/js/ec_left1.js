var ec_left1 = echarts.init(document.getElementById('l1'));

var ec_left1_Option = {
	//标题样式
	title: {
		text: "全国累计趋势",
		textStyle: {
			color: '#91d6e7',
			fontSize: 30
		},
		left: 'left',
		top:'5%'
	},
	grid:{
		top:'25%',
		bottom:'10%'
	},
	tooltip: {
		//指示器
		trigger: 'axis',
		axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
	},
	legend: {
		data: ['累计确诊', "累计治愈", "累计死亡", '现有疑似'],
		left: "right",
		textStyle: {
			color:"white"
		}
	},

	// //图形位置
	// grid: {
	// 	left: '4%',
	// 	right: '6%',
	// 	bottom: '4%',
	// 	top: 50,
	// 	containLabel: true
	// },
	xAxis: [{
		type: 'category',
		//x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,
		data: [],
		axisLabel: {
        	color:'white',
			fontSize:15
		}
		// data: ['01.20', '01.21', '01.22']
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 15,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//y轴线设置显示
		axisLine: {
			show: true
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
	}],
	series: [{
		name: "累计确诊",
		type: 'line',
		smooth: true,
		data: [],//[260, 406, 529]
	},
		{
		name: "累计治愈",
		type: 'line',
		smooth: true,
		data: [],//[25, 25, 25]
		itemStyle:{
			normal:{
				color:"#3fc1ab"
				}
			}
	},
		{
		name: "现有疑似",
		type: 'line',
		smooth: true,
		data: [],//[54, 37, 3935]
		itemStyle:{
			normal:{
				color:"#3876dc"
				}
			}
	},{
		name: "累计死亡",
		type: 'line',
		smooth: true,
		data: [],//[6, 9, 17]
		itemStyle:{
			normal:{
				color:"#65007a"
				}
			}
	}]
};
ec_left1.setOption(ec_left1_Option);
tools.loopShowTooltip(ec_left1, ec_left1_Option, {
    loopSeries: true});

