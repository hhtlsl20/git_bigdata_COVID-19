var ec_right3 = echarts.init(document.getElementById('r3'));
xData = ["新增确诊数", "新增治愈数", "新增死亡数"];
ec_right3_option = {
    title: {
		text: "今日疫情数据概览",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
    color:['#1C86F1'],
                legend: {
                    textStyle:{
                        color:'#9B9B9B'
                    },
                    right:37,
                    top: 22,
                },
                tooltip: {},
                xAxis: {
                    type: 'category',
                    data: ['新增确诊','新增治愈','新增死亡'],
                    axisLine:{
                        lineStyle:{
                            color:'#657CA8'
                        }
                    },
                    axisTick:{
                        show:false
                    },
                    axisLabel:{
                        color:'#eeeeee',
                        rotate:45,
                    },
                },
                yAxis: {
                    axisLine:{
                        lineStyle:{
                            color:'#657CA8'
                        }
                    },
                    axisTick:{
                        show:false
                    },
                    splitLine:{
                        show:false
                    },
                    axisLabel:{
                        color:'#eee',
                    },
                },
                series: [
                    {
                        type: 'bar',
                        barWidth:20,
                        data: [],
                        label: {
                            show: true,
                            position: 'top',
                            textStyle:{
                                color:'#ffffff'
                            }
                        },
                        itemStyle:{
                            normal:{
                                color: function (params){
                                    var colorList = [
                                        ['#f56868','transparent'],
                                        ['#41ccba','transparent'],
                                        ['#a582ea','transparent'],
                                        ['#f5c379','transparent'],
                                        ['#b4c6cc','transparent'],
                                        ['#74d28c','transparent'],
                                        ['#f4966e','transparent'],
                                        ['#64b2ef','transparent'],
                                    ];
                                    var index=params.dataIndex;
                                    if(params.dataIndex >= colorList.length){
                                            index=params.dataIndex-colorList.length;
                                    }
                                    return new echarts.graphic.LinearGradient(0, 0, 0, 1,
                                        [
                                            {offset: 0, color: colorList[index][0]},
                                            {offset: 0.5, color: colorList[index][0]},
                                            {offset: 1, color: colorList[index][1]},
                                        ]);
                                }
                            }
                        }
                    }
                ]
            };
ec_right3.setOption(ec_right3_option)