var ec_center = echarts.init(document.getElementById("c2"))
var ec_center_option ={
    legend:{
      textStyle: {
          color: "white"
      }
    },
    title: {
        text: '现有确诊人数分布',
        left:'center',
        textStyle:{
            color:'#7ED6F5',
            fontSize:60
        }
    },
    tooltip:{
        trigger:'item'
    },
    visualMap:{
        show: true,
        x:'left',
        y:'bottom',
        textStyle:{
          fontsize:8,
            color:"white"
        },
        splitList: [{start:0,end:9},
            {start: 10,end:99},
            {start: 100,end:999},
            {start: 1000,end:9999},
            {start: 10000}],
        color :['#031088','#0046E4','#1597FD','#7CD1FF','#D4F0FF']
    },
    series: [{
        // name:'现有确诊人数分布',
        type:'map',
        mapType:'china',
        roam :false,
        itemStyle:{
            normal:{
              show:true,
              borderWidth: .5,
              borderColor: '#009fe8',
              areaColor:'#fff',

            },
            emphasis: {
              borderWidth: .5,
              borderColor: '#4b0002',
              areaColor:'#fff',
              show:true,

            }
      },
        label :{
            normal:{
                show:true,
                fontSize:8,

        },
            emphasis:{
                show :true,
                fontsize: 8,
        }
      },
      data:[]

    }]
  };
ec_center.setOption(ec_center_option);
ec_center.on('click',function (params) {
     privince_name=params.name;
     ids=pinyin.getFullChars(privince_name);
    var country_id=document.getElementById('ids');
    country_id.id=ids;
});


