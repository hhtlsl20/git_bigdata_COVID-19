//实现页面跳转
var right_button=document.getElementById('right_button');
right_button.onclick=function () {
    document.location.href='http://192.168.198.13:5050/';
};
//实现弹窗,
var c2=document.getElementById('c2');
var guizhou=document.getElementById('GuiZhou')
c2.onclick=function () {
   guizhou.style.display="block";
}
//ids为点击的省份拼音名字,进行动态id传递实现地图下钻
var l1=document.getElementById('l1');
var l2=document.getElementById('l2');
var l3=document.getElementById('l3');
var r1=document.getElementById('r1');
var r3=document.getElementById('r3');
var box2=document.getElementById('box2');
c2.onclick=function () {
    box2.style.display="block";
    var guizhou=document.getElementById(ids);
    guizhou.style.position="absolute";
    guizhou.style.height="80%";
    guizhou.style.width="40%";
    guizhou.style.zIndex="60";
    guizhou.style.top="10%";
    guizhou.style.left="33%";
     var gz = echarts.init(document.getElementById(ids));
     var guizhou_option = {
        visualMap:{
        show: true,
        x:'left',
        y:'bottom',
        textStyle:{
          fontsize:8,
            color:"white"
        },
        splitList: [{start:1,end:9},
            {start: 10,end:99},
            {start: 100,end:999},
            {start: 1000,end:9999},
            {start: 10000}],
        color :['#8A3310','#C64918','#E55825','#F2AD92','#F9DCD1']
    },
      series: [
        {
        name: '数据名称',
        type: 'map',
        mapType: privince_name,
        selectedMode : 'single',
        itemStyle:{
             normal:{label:{show:true,formatter:function (params) {
                    return params.name+"\n"+params.value
                     },fontSize:15}},
             emphasis:{label:{show:true}}
            },
            data:[]
        }]
      };
gz.setOption(guizhou_option);
//发送ajax请求,将身份名字传到后端sql拼接查询
var info={"privince":privince_name};
$.ajax({
        data:info,
        traditional:true,
        contentType: 'application/json; charset=UTF-8',
        url:"/guizhou",
        success: function (data) {
            guizhou_option.series[0].data=data.data
            gz.setOption(guizhou_option);
        },
        error:function (xhr,type,errorThrown) {

        }
    });
//弹窗左上角图标实现(不同省份地图,数据不一样,需要ids动态传递id和省份名字)
var div1=document.createElement("div");
document.getElementById("box2").appendChild(div1);
var new_id=ids+'_l1';
var title=ids+'title';
div1.id=new_id;
document.getElementById(new_id).style.width="30%";
document.getElementById(new_id).style.height="40%";
// document.getElementById('gz_l1').style.backgroundColor="red";
document.getElementById(new_id).style.position="absolute";
document.getElementById(new_id).style.top="5%";
document.getElementById(new_id).style.left="2%"

//弹窗左下角图表实现(此部分不变,在所有弹窗身份地图都需要现实)
var div2=document.createElement("div");
document.getElementById("box2").appendChild(div2);
div2.id='gz_all_l2';
document.getElementById('gz_all_l2').style.width="30%";
document.getElementById('gz_all_l2').style.height="40%";
// document.getElementById('gz_all_l2').style.backgroundColor="red";
document.getElementById('gz_all_l2').style.position="absolute";
document.getElementById('gz_all_l2').style.top="55%";
document.getElementById('gz_all_l2').style.left="2%";

var p = document.createElement("p");
document.getElementById("box2").appendChild(p);
p.id=title;
document.getElementById(title).innerText=privince_name+"疫情数据概览";
document.getElementById(title).style.color="white";
document.getElementById(title).style.fontSize="3rem";
document.getElementById(title).style.position="absolute";
document.getElementById(title).style.top="4%";
document.getElementById(title).style.left="45%"

var gz_l1 = echarts.init(document.getElementById(new_id));
var gz_l1_Option = {
                title:{
                    text:'省内累计确诊数据概览',
                    textStyle:{
                        color:'white',
                        fontSize:25
                    }
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
                    data: [],
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
                        fontSize: 17
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
                        show:false
                    },
                },
                series: [
                    {
                        type: 'bar',
                        barWidth:30,
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
gz_l1.setOption(gz_l1_Option);
var info={"privince":privince_name};
$.ajax({
        data:info,
        contentType: 'application/json; charset=UTF-8',
        url:"/gz_l1",
        traditional:true,
        success: function (data) {
            gz_l1_Option.series[0].data=data.confirm
            gz_l1_Option.xAxis.data=data.name
            gz_l1.setOption(gz_l1_Option)
        },
        error:function (xhr,type,errorThrown) {
        }
    });

var gz_all_l2=echarts.init(document.getElementById('gz_all_l2'));
var gz_all_l2_Option= {
    // backgroundColor: '#515151',
						title : {
						    text : "今日热搜",
						    textStyle : {
						        color : 'white',
                                fontSize:25
						    },
						    left : 'left'
						},
                        legend:{
                            textStyle: {
			                    color:"white"
		                }
                        },
                        xAxis:{
                            axisLabel: {color:'white'
		                    }
                        },
                         yAxis:{axisLabel: {
        	            color:'white'
		                }},
                        tooltip: {
                            show: false
                        },
                        series: [{
                                type: 'wordCloud',
								// drawOutOfBound:true,
                                gridSize: 1,
                                sizeRange: [12, 55],
                                rotationRange: [-45, 0, 45, 90],
                                // maskImage: maskImage,

                                //这是让词云图的颜色随机
                                textStyle: {
                                    normal: {
                                        color: function () {
                                            return 'rgb(' +
                                                    Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) +
                                                    ', ' + Math.round(Math.random() * 255) + ')'
                                        }
                                    }
                                },
                                // left: 'center',
                                // top: 'center',
                                // // width: '96%',
                                // // height: '100%',
                                right: null,
                                bottom: null,
                                // width: 300,
                                // height: 200,
                                // top: 20,
                                data:[]
                            }]
};
gz_all_l2.setOption(gz_all_l2_Option);
$.ajax({
        data:info,
        contentType: 'application/json; charset=UTF-8',
        url:"/gz_all_l2",
        success: function(data) {
            gz_all_l2_Option.series[0].data=data.data
            gz_all_l2.setOption(gz_all_l2_Option)
        },
        error: function(xhr, type, errorThrown) {
        }
    });
       l1.style.display="none";
       l2.style.display="none";
       l3.style.display="none";
       r1.style.display="none";
       r3.style.display="none";
//隐藏弹窗
box2.onclick=function () {
       document.getElementById(new_id).remove();
       box2.style.display = "none";
       var city_id = document.getElementById('box2').firstElementChild;
       gz.clear();
       city_id.id = "ids";
       l1.style.display="block";
       l2.style.display="block";
       l3.style.display="block";
       r1.style.display="block";
       r3.style.display="block";
       document.getElementById(title).remove();
   };
};