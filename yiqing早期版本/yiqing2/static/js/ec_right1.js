var ec_right1 = echarts.init(document.getElementById('r1'));
var ec_right1_option = {
	//标题样式
	title : {
	    text : "非湖北地区城市确诊TOP5",
	    textStyle : {
	        color : '#19CAAD',
	    },
	    left : 'left'
	},
	legend:{
		textStyle: {
			color:"white"
		}
	},
	  color: ['#007FFF'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: [],
		axisLabel:{
        	color:'white'
		}
    },
    yAxis: {
        type: 'value',
		axisLabel: {
        	color:'white'
		}
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%",
		tooltip: {
        	trigger: 'axis'
		}
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
				ec_right1.setOption(ec_right1_option)