// //
// {#    <script type="text/javascript">#}
//     {#        var myChart = echarts.init(document.getElementById('main1'));#}
//     {##}
//     {#var data = document.getElementById('main').getAttribute('d');#}
//     {#console.log(data)#}
//     {#var data1 = {"categor": ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],#}
//     {#            "dat": [5, 20, 36, 10, 10, 20]}#}
//     {#            console.log(data1.categor)#}
//     {#var data = {"衬衫":5,"羊毛衫":20,"雪纺衫":36,"裤子":10,"高跟鞋":10,"袜子":20}#}
//     {##}
//     {#//类别数组（实际用来盛放X轴坐标值）#}
//     {#var x_names = [];#}
//     {#var y_datas = [];#}
//     {#//挨个取出类别并填入类别数组#}
//     {# $.each(data, function (index, item) {#}
//     {#                x_names.push(item);#}
//     {#                y_datas.push(item);#}
//     {#            });#}
//     {##}
//     {#        // 显示标题，图例和空的坐标轴#}
//     {#        myChart.setOption({#}
//     {#            title: {#}
//     {#                text: '异步数据加载示例2'#}
//     {#            },#}
//     {#            tooltip: {},#}
//     {#            legend: {#}
//     {#                data: ['销量'],#}
//     {#                show: false#}
//     {#            },#}
//     {#            xAxis: {#}
//     {#                data: []#}
//     {#            },#}
//     {#            yAxis: {},#}
//     {#            series: [{#}
//     {#                name: '销量',#}
//     {#                type: 'bar',#}
//     {#                data: []#}
//     {#            }]#}
//     {#        });#}
//     {#        myChart.showLoading();#}
//     {#        // 异步加载数据#}
//     {#        $.get('static/js/data1.json').done(function (data) {#}
//     {#            myChart.hideLoading();#}
//     {#            // 填入数据#}
//     {#            myChart.setOption({#}
//     {#                xAxis: {#}
//     {#                    data: data.categor //不要用categore，data命名#}
//     {#                },#}
//     {#                series: [{#}
//     {#                    // 根据名字对应到相应的系列#}
//     {#                    name: '销量',#}
//     {#                    data: data.dat#}
//     {#                }]#}
//     {#            });#}
//     {#        });#}
//     {#    </script>#}
//     {#    <script type="text/javascript">#}
//     {#        var myChart = echarts.init(document.getElementById('main2'));#}
//     {##}
//     {#var data = document.getElementById('main').getAttribute('d');#}
//     {#console.log(data)#}
//     {#var data1 = {"categor": ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],#}
//     {#            "dat": [5, 20, 36, 10, 10, 20]}#}
//     {#            console.log(data1.categor)#}
//     {#var data = {"衬衫":5,"羊毛衫":20,"雪纺衫":36,"裤子":10,"高跟鞋":10,"袜子":20}#}
//     {##}
//     {#//类别数组（实际用来盛放X轴坐标值）#}
//     {#var x_names = [];#}
//     {#var y_datas = [];#}
//     {#//挨个取出类别并填入类别数组#}
//     {# $.each(data, function (index, item) {#}
//     {#                x_names.push(item);#}
//     {#                y_datas.push(item);#}
//     {#            });#}
//     {##}
//     {#        // 显示标题，图例和空的坐标轴#}
//     {#        myChart.setOption({#}
//     {#            title: {#}
//     {#                text: '异步数据加载示例3'#}
//     {#            },#}
//     {#            tooltip: {},#}
//     {#            legend: {#}
//     {#                data: ['销量'],#}
//     {#                show: false#}
//     {#            },#}
//     {#            xAxis: {#}
//     {#                data: []#}
//     {#            },#}
//     {#            yAxis: {},#}
//     {#            series: [{#}
//     {#                name: '销量',#}
//     {#                type: 'bar',#}
//     {#                data: []#}
//     {#            }]#}
//     {#        });#}
//     {#        myChart.showLoading();#}
//     {#        // 异步加载数据#}
//     {#        $.get('static/js/data2.json').done(function (data) {#}
//     {#            myChart.hideLoading();#}
//     {#            // 填入数据#}
//     {#            myChart.setOption({#}
//     {#                xAxis: {#}
//     {#                    data: data.categor //不要用categore，data命名#}
//     {#                },#}
//     {#                series: [{#}
//     {#                    // 根据名字对应到相应的系列#}
//     {#                    name: '销量',#}
//     {#                    data: data.dat#}
//     {#                }]#}
//     {#            });#}
//     {#        });#}
//     {#    </script>#}
//
//
//
// // 指定图表的配置项和数据
// var bar_option = {
//     backgroundColor: '#00265f',
//     title: {
//         text: '所有试验固有可用度',
//         y: "4%",
//         textStyle: {
//             color: '#fff',
//             fontSize: '22'
//         },
//         subtextStyle: {
//             color: '#90979c',
//             fontSize: '16',
//
//         },
//     },
//     tooltip: {
//         trigger: 'axis',
//         axisPointer: {
//             type: 'shadow'
//         }
//     },
//     grid: {
//         top: '15%',
//         right: '3%',
//         left: '5%',
//         bottom: '12%'
//     },
//     legend: {
//         data: ['销量'],
//         show: false
//     },
//     xAxis: {
//         data: [],
//         axisLine: {
//             lineStyle: {
//                 color: 'rgba(255,255,255,0.12)'
//             },
//         },
//         axisLabel: {
//             margin: 10,
//             color: '#e2e9ff',
//             textStyle: {
//                 fontSize: 14
//             },
//         },
//     },
//     yAxis: {
//         axisLabel: {
//             formatter: '{value}',
//             color: '#e2e9ff',
//         },
//         axisLine: {
//             show: false,
//             lineStyle: {
//                 color: 'rgba(255,255,255,1)'
//             }
//         },
//         splitLine: {
//             lineStyle: {
//                 color: 'rgba(255,255,255,0.12)'
//             }
//         }
//     },
//     series: [{
//         name: '销量',
//         type: 'bar',
//         data: [],
//         barWidth: '20px',
//         itemStyle: {
//             normal: {
//                 color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
//                     offset: 0,
//                     color: 'rgba(0,244,255,1)' // 0% 处的颜色
//                 }, {
//                     offset: 1,
//                     color: 'rgba(0,77,167,1)' // 100% 处的颜色
//                 }], false),
//                 barBorderRadius: [30, 30, 30, 30],
//                 shadowColor: 'rgba(0,160,221,1)',
//                 shadowBlur: 4,
//             }
//         },
//         label: {
//             normal: {
//                 show: true,
//                 lineHeight: 30,
//                 width: 80,
//                 height: 30,
//                 backgroundColor: 'rgba(0,160,221,0.1)',
//                 borderRadius: 200,
//                 position: ['-8', '-60'],
//                 distance: 1,
//                 formatter: [
//                     '    {d|●}',
//                     ' {a|{c}}     \n',
//                     '    {b|}'
//                 ].join(','),
//                 rich: {
//                     d: {
//                         color: '#3CDDCF',
//                     },
//                     a: {
//                         color: '#fff',
//                         align: 'center',
//                     },
//                     b: {
//                         width: 1,
//                         height: 30,
//                         borderWidth: 1,
//                         borderColor: '#234e6c',
//                         align: 'left'
//                     },
//                 }
//             }
//         }
//     }]
// };
