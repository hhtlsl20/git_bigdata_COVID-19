window.onload = () => {
        let EC = echarts.init(document.getElementById('mp1'));
        let canvas = document.createElement('canvas');
        // 地球皮肤
        let mapChart = echarts.init(canvas, null, {
            width: 4096,
            height: 2048
        });
        mapChart.setOption({
            "series": [
        {
            "type": "map",
            "name": "World",
            "label": {
                "show": false,
                "position": "top",
                "margin": 8
            },
            "mapType": "world",
            "data": [{"name": "United States", "value": 5251446}, {"name": "Brazil", "value": 3057470}, {"name": "India", "value": 2215074}, {"name": "Russia", "value": 890799}, {"name": "South Africa", "value": 563598}, {"name": "Mexico", "value": 485836}, {"name": "Peru", "value": 478024}, {"name": "Colombia", "value": 387481}, {"name": "Chile", "value": 375044}, {"name": "Spain", "value": 370060}, {"name": "Iran", "value": 328844}, {"name": "United Kingdom", "value": 313392}, {"name": "Saudi Arabia", "value": 289947}, {"name": "Pakistan", "value": 284660}, {"name": "Argentina", "value": 253868}, {"name": "Italy", "value": 250825}, {"name": "Turkey", "value": 241997}, {"name": "France", "value": 239306}, {"name": "Germany", "value": 218508}, {"name": "Iraq", "value": 153599}, {"name": "Philippines", "value": 136638}, {"name": "Indonesia", "value": 127083}, {"name": "Canada", "value": 122053}, {"name": "Qatar", "value": 113262}, {"name": "Kazakhstan", "value": 99442}, {"name": "Egypt", "value": 95666}, {"name": "Ecuador", "value": 94701}, {"name": "Bolivia", "value": 89999}, {"name": "Israel", "value": 84722}, {"name": "Ukraine", "value": 83812}, {"name": "Sweden", "value": 82972}, {"name": "Oman", "value": 81787}, {"name": "Dominican Rep.", "value": 80499}, {"name": "Panama", "value": 75394}, {"name": "Belgium", "value": 74152}, {"name": "Kuwait", "value": 72400}, {"name": "Belarus", "value": 68947}, {"name": "United Arab Emirates", "value": 62704}, {"name": "Romania", "value": 62547}, {"name": "Netherlands", "value": 60058}, {"name": "Guatemala", "value": 56987}, {"name": "Singapore Rep.", "value": 55292}, {"name": "Portugal", "value": 52825}, {"name": "Poland", "value": 52410}, {"name": "Honduras", "value": 47454}, {"name": "Nigeria", "value": 46867}, {"name": "Ghana", "value": 41212}, {"name": "Armenia", "value": 40433}, {"name": "Kyrgyzstan", "value": 40085}, {"name": "Afghanistan", "value": 37162}, {"name": "Switzerland", "value": 36708}, {"name": "Algeria", "value": 35712}, {"name": "Morocco", "value": 34063}, {"name": "Azerbaijan", "value": 33647}, {"name": "Uzbekistan", "value": 31304}, {"name": "Serbia", "value": 28262}, {"name": "Moldova", "value": 27841}, {"name": "Kenya", "value": 26928}, {"name": "Ireland", "value": 26768}, {"name": "Venezuela", "value": 25805}, {"name": "Costa Rica", "value": 23872}, {"name": "Ethiopia", "value": 23591}, {"name": "Nepal", "value": 23310}, {"name": "Austria", "value": 22106}, {"name": "Australia", "value": 21750}, {"name": "El Salvador", "value": 20872}, {"name": "Czech Rep.", "value": 18494}, {"name": "Cameroon", "value": 18042}, {"name": "Côte d\'Ivoire", "value": 16798}, {"name": "Denmark", "value": 15135}, {"name": "Korea", "value": 14660}, {"name": "Palestine", "value": 14510}, {"name": "Bulgaria", "value": 13512}, {"name": "Madagascar", "value": 13202}, {"name": "Sudan", "value": 11956}, {"name": "Senegal", "value": 11312}, {"name": "Norway", "value": 9684}, {"name": "Malaysia", "value": 9094}, {"name": "Zambia", "value": 8210}, {"name": "Gabon", "value": 8006}, {"name": "Guinea", "value": 7930}, {"name": "Tajikistan", "value": 7827}, {"name": "Haiti", "value": 7634}, {"name": "Finland", "value": 7601}, {"name": "Luxembourg", "value": 7216}, {"name": "Paraguay", "value": 6907}, {"name": "Lebanon", "value": 6812}, {"name": "Mauritania", "value": 6555}, {"name": "Albania", "value": 6536}, {"name": "Libya", "value": 5929}, {"name": "Greece", "value": 5749}, {"name": "Croatia", "value": 5649}, {"name": "Djibouti", "value": 5347}, {"name": "Eq. Guinea", "value": 4821}, {"name": "Zimbabwe", "value": 4748}, {"name": "Hungary", "value": 4731}, {"name": "Malawi", "value": 4674}, {"name": "Nicaragua", "value": 3902}, {"name": "Montenegro", "value": 3696}, {"name": "Thailand", "value": 3351}, {"name": "Swaziland", "value": 3309}, {"name": "Somalia", "value": 3227}, {"name": "Namibia", "value": 3101}, {"name": "Cuba", "value": 3046}, {"name": "Sri Lanka", "value": 2871}, {"name": "Slovakia", "value": 2599}, {"name": "Mali", "value": 2573}, {"name": "Suriname", "value": 2489}, {"name": "Mozambique", "value": 2411}, {"name": "Lithuania", "value": 2265}, {"name": "Slovenia", "value": 2255}, {"name": "Estonia", "value": 2158}, {"name": "Rwanda", "value": 2152}, {"name": "Guinea Bissau", "value": 2052}, {"name": "Iceland", "value": 1962}, {"name": "Benin", "value": 1936}, {"name": "Sierra Leone", "value": 1917}, {"name": "Yemen", "value": 1832}, {"name": "Tunisia", "value": 1717}, {"name": "Angola", "value": 1679}, {"name": "New Zealand", "value": 1570}, {"name": "Uruguay", "value": 1364}, {"name": "Uganda", "value": 1297}, {"name": "Latvia", "value": 1290}, {"name": "Jordan", "value": 1268}, {"name": "Syria", "value": 1255}, {"name": "Cyprus", "value": 1252}, {"name": "Georgia", "value": 1250}, {"name": "Liberia", "value": 1240}, {"name": "Gambia", "value": 1235}, {"name": "Burkina Faso", "value": 1204}, {"name": "Niger", "value": 1158}, {"name": "Togo", "value": 1067}, {"name": "Botswana", "value": 1066}, {"name": "Jamaica", "value": 1031}, {"name": "Chad", "value": 945}, {"name": "The Bahamas", "value": 945}, {"name": "Vietnam", "value": 847}, {"name": "Lesotho", "value": 781}, {"name": "Guyana", "value": 568}, {"name": "Tanzania", "value": 509}, {"name": "Burundi", "value": 408}, {"name": "Myanmar", "value": 360}, {"name": "Mongolia", "value": 293}, {"name": "Eritrea", "value": 285}, {"name": "Cambodia", "value": 251}, {"name": "Papua New Guinea", "value": 214}, {"name": "Belize", "value": 154}, {"name": "Brunei", "value": 142}, {"name": "Bhutan", "value": 110}, {"name": "East Timor", "value": 25}, {"name": "Lao PDR", "value": 20}],
            "roam": true,
            "zoom": 1,
            "showLegendSymbol": true,
            "emphasis": {},
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                "World"
            ],
            "selected": {
                "World": true
            },
            "show": false,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "visualMap": {
        "show": true,
        "type": "piecewise",
        "min": 0,
        "max": 100,
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 5,
        "orient": "vertical",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 14,
        "borderWidth": 0,
        "pieces": [
            {
                "min": 1000000,
                "color": "#540d0d"
            },
            {
                "max": 999999,
                "min": 100000,
                "color": "#9c1414"
            },
            {
                "max": 99999,
                "min": 50000,
                "color": "#d92727"
            },
            {
                "max": 49999,
                "min": 10000,
                "color": "#ed3232"
            },
            {
                "max": 9999,
                "min": 1000,
                "color": "#f27777"
            },
            {
                "max": 999,
                "min": 100,
                "color": "#f7adad"
            },
            {
                "max": 99,
                "min": 0,
                "color": "#f7e4e4"
            }
        ]
    },
        });
        let option = {
            title: {
                textStyle: {
                    color: '#fff'
                }
            },
            backgroundColor: '#7bc3ef',
            tooltip: {
                show: true
            },
            visualMap: [{
                // show: false,
                type: 'continuous',
                seriesIndex: 0,
                text: ['scatter3D'],
                textStyle: {
                    color: '#fff'
                },
                calculable: true,
                max: 3000,
                inRange: {
                    color: ['#87aa66', '#eba438', '#d94d4c']
                }
            }, {
                show: false,
                type: 'continuous',
                seriesIndex: 1,
                calculable: true,
                max: 3000,
                inRange: {
                    color: ['#87aa66', '#eba438', '#d94d4c']
                }
            }],
            globe: {
                baseTexture: mapChart,
                environment: '../static/images/bg.jpg',
                // shading: 'lambert',
                light: { // 光照阴影
                    main: {
                        color: '#fff', // 光照颜色
                        intensity: 1.1, // 光照强度
                        // shadowQuality: 'high', //阴影亮度
                        shadow: false, // 是否显示阴影
                        alpha: 40,
                        beta: -30
                    },
                    ambient: {
                        intensity: 0.5
                    }
                },
                viewControl: {
                    alpha: 30,
                    beta: 160,
                    // targetCoord: [116.46, 39.92],
                    autoRotate: true,
                    autoRotateAfterStill: 10,
                    distance: 240
                }
            },
            series: [{
                name: 'lines3D',
                type: 'lines3D',
                zlevel: 2,
                coordinateSystem: 'globe',
                effect: {
                    show: true
                },
                blendMode: 'lighter',
                lineStyle: {
                    width: 2
                },
                data: [],
                silent: false
            },
            {
                name: '地域详情',
                type: 'map',
                map: '',
                zlevel: 1,
                zoom: 1,
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                data: []
            }]
        }

        EC.setOption(option);
         window.addEventListener("resize", function() {
      EC.resize();
    });
        mapChart.on('click', params => {
            let con_name = params.name
            let mapJson = '../static/json/' + con_name + '.json'
            EC.showLoading()
            $.getJSON(mapJson, geoJson => {
                option.title.text = '双击地图返回上级'
                option.series[1].map = con_name
                option.series[1].zlevel = 3
                echarts.registerMap(con_name, geoJson)
                /*  // 第二层随机数据
                let data = []
                geoJson.features.forEach(d => {
                    data.push({
                        name: d.properties.name,
                        value: (Math.random() * 3000).toFixed(2)
                    })
                })
                option.series[1].data = data
                EC.setOption(option)
                EC.hideLoading()  */

    var info={"country":con_name};
    //数据获取操作
    function get_c2_data() {
    $.ajax({
        data:info,
        contentType: 'application/json; charset=UTF-8',
        url:"/l1",
        traditional:true,
        success: function(data) {

            option.series[1].data = data.data
                EC.setOption(option)
                EC.hideLoading()
        },
        error: function(xhr, type, errorThrown) {

        }
    })
    };
    get_c2_data();
    setInterval(get_c2_data,100000*10);
            })
        })

        EC.on('dblclick', () => {
            option.series[1].map = ''
            option.series[1].zlevel = 1
            EC.setOption(option)
        })

    //数据获取操作
    function get_map_data() {
    $.ajax({
        url:"/map",
        success: function(data) {
                mapChart.setOption.series[0].data = data.datas
                EC.setOption(option)
                EC.hideLoading()
        },
        error: function(xhr, type, errorThrown) {

        }
    })
    };
    get_map_data();
    setInterval(get_map_data,100000*10);

    }
