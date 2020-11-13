var ec_right3 = echarts.init(document.getElementById('r3'));
xData = ["新增确诊数", "新增治愈数", "新增死亡数"];
ec_right3_option = {
    title: {
		text: "今日疫情新增数据概览",
		textStyle: {
			color: '#91d6e7',
            fontSize:30
		},
		left: 'left',
        top:'5%'
	},
    grid:{
		top:'25%'
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
                    data: ['新增治愈','新增死亡','新增确诊'],
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
                        fontSize: 20
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
                        fontSize:20
                    },
                },
                series: [
                    {
                        type: 'bar',
                        barWidth:60,
                        data: [],
                        label: {
                            show: true,
                            position: 'top',
                            textStyle:{
                                color:'#ffffff',
                                fontSize:20
                            }
                        },
                        itemStyle:{
                            normal:{
                                color: function (params){
                                    var colorList = [
                                        ['#fc681b','transparent'],
                                        ['#284bd5','transparent'],
                                        ['#c233be','transparent'],
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
ec_right3.setOption(ec_right3_option);
tools.loopShowTooltip(ec_right3, ec_right3_option, {
    loopSeries: true});