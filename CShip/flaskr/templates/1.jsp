<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme() + "://"
			+ request.getServerName() + ":" + request.getServerPort()
			+ path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<base href="<%=basePath%>">

<title>JPWQ系统战备完好性集成演示验证系统</title>

<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="expires" content="0">
<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
<meta http-equiv="description" content="This is my page">
<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
<script type="text/javascript"
	src="build/dist/echarts.js"></script>
	<script type="text/javascript" src="echarts.js"></script>
	<script type="text/javascript" src="jquery-1.8.3.js"></script>
<script type="text/javascript" src="jquery.min.js"></script>
<script type="text/javascript">
	// 路径配置
	require.config({
		paths : {
			echarts : 'build/dist'
		}
	});
	// 使用
	require([ 'echarts', 'echarts/chart/bar' ,'echarts/chart/line'// 使用柱状图就加载bar模块，按需加载
	], 
	drewEcharts
);
	function drewEcharts(ec) {
		// 基于准备好的dom，初始化echarts图表
		var myChart = ec.init(document.getElementById('main'));

		var option = {
			    title : {
			        text: '部件',
			        subtext: '输出统计'
			    },
			    tooltip : {
			        trigger: 'axis',
			        //position:['100%','100%']
			        position:['100%',60]
			    },
			    legend: {
			        data:['故障率','维修率','','平均故障间隔时间','平均故障修复时间','平均停机时间']
			    },
			    
			    
			    dataZoom: {
			        show: true,
			        start : 0
			    },
			    
			    toolbox: {
			        show : true,
			        feature : {
			            dataView : {show: true, readOnly: false},
			            magicType : {show: true, type: ['line', 'bar']},
			            restore : {show: true},
			            saveAsImage : {show: true}
			        }
			    },
			    calculable : true,
			    
                grid: {  
               	 y2: '60px',   
               	 }, 
               	 
			    xAxis : [			    	
			    	        {        	 			            	 
			            	 splitLine:{show: false},//去除网格线
			            	 axisTick: {
			                     alignWithLabel: true
			                 },
			                 axisLabel: {
			                     interval:0 
			                    // rotate:45, //代表逆时针旋转45度
			                 },
			                 
			                 type : 'category',
			                 data : (function(){
                                 var arr=[];
                                 $.ajax({
                                 type : "post",
                                 async : false, //同步执行
                                 url : "part_output.do",
                                 data : {},
                                 dataType : "json", //返回数据形式为json
                                 success : function(result) {
                                 if (result) {
                                        for(var i=0;i<result.length;i++){
                                         // console.log("br"+result[i].If_average_br+"============="); 
                                          arr.push(result[i].device);
                   
                                        }  
                                 }
                             },
                             error : function(errorMsg) {
                                 alert("不好意思，图表请求数据失败啦!");
                                 myChart.hideLoading();
                             }
                            })
                           return arr;
			             })
			             ()
			             }
			        			         
			             ],
			                
			yAxis : [ 
				{
			    splitLine:{show: false},//去除网格线

				type : 'value'
			} ],
			series : [ 

				//******************************
				   {
						"name" : "故障率",
						"type" : "bar",
						"data" : (function(){
		                                        var arr=[];
		                                        $.ajax({
		                                        type : "post",
		                                        async : false, //同步执行
		                                        url : "part_output.do",
		                                        data : {},
		                                        dataType : "json", //返回数据形式为json
		                                        success : function(result) {
		                                        if (result) {
		                                               for(var i=0;i<result.length;i++){
		                                                  console.log(result[i].FR);
		                         
		                                                  arr.push(result[i].FR);
		                                                }  
		                                        }
		                                    },
		                                    error : function(errorMsg) {
		                                        alert("不好意思，图表请求数据失败啦!");
		                                        myChart.hideLoading();
		                                    }
		                                   })
		                                  return arr;
						 })(),
						  
						 },
						 
							//******************************
						  {
							name : '维修率',
							type : 'bar',
							"data" : (function() {
								var arr = [];
								$.ajax({
									type : "post",
									async : false, //同步执行
									url : "part_output.do",
									data : {},
									dataType : "json", //返回数据形式为json
									success : function(result) {
										if (result) {
											for (var i = 0; i < result.length; i++) {
												console.log(result[i].RR);
			                                    if(result[i].RR=="inf"){
			                                  	  result[i].RR=1;
			                                    }
												arr.push(result[i].RR);
											}
										}
									},
									error : function(errorMsg) {
										alert("不好意思，图表请求数据失败啦!");
										myChart.hideLoading();
									}
								})
								return arr;
							})(),
							
				    	   },
			//******************************
		  {
				"name" : "平均故障间隔时间",
				"type" : "bar",
				"data" : (function(){
                                        var arr=[];
                                        $.ajax({
                                        type : "post",
                                        async : false, //同步执行
                                        url : "part_output.do",
                                        data : {},
                                        dataType : "json", //返回数据形式为json
                                        success : function(result) {
                                        if (result) {
                                               for(var i=0;i<result.length;i++){
                                                  console.log(result[i].MTBF);
                                                  arr.push(result[i].MTBF);
                                                }  
                                        }
                                    },
                                    error : function(errorMsg) {
                                        alert("不好意思，图表请求数据失败啦!");
                                        myChart.hideLoading();
                                    }
                                   })
                                  return arr;
				 })(),
				  
				 },
		
			//******************************
		  {
				"name" : "平均故障修复时间",
				"type" : "bar",
				"data" : (function(){
                                        var arr=[];
                                        $.ajax({
                                        type : "post",
                                        async : false, //同步执行
                                        url : "part_output.do",
                                        data : {},
                                        dataType : "json", //返回数据形式为json
                                        success : function(result) {
                                        if (result) {
                                               for(var i=0;i<result.length;i++){
                                                  console.log(result[i].MTTR);
                     
                                                  arr.push(result[i].MTTR);
                                                }  
                                        }
                                    },
                                    error : function(errorMsg) {
                                        alert("不好意思，图表请求数据失败啦!");
                                        myChart.hideLoading();
                                    }
                                   })
                                  return arr;
				 })(),
				 
				 },
			//******************************
			 {
				"name" : "平均停机时间",
				"type" : "bar",
				"data" : (function(){
                                        var arr=[];
                                        $.ajax({
                                        type : "post",
                                        async : false, //同步执行
                                        url : "part_output.do",
                                        data : {},
                                        dataType : "json", //返回数据形式为json
                                        success : function(result) {
                                        if (result) {
                                               for(var i=0;i<result.length;i++){
                                                  console.log(result[i].MDT);
                                        
                                                  arr.push(result[i].MDT);
                                                }  
                                        }
                                    },
                                    error : function(errorMsg) {
                                        alert("不好意思，图表请求数据失败啦!");
                                        myChart.hideLoading();
                                    }
                                   })
                                  return arr;
				 })(),
				  
				 }

			]
		};

		// 为echarts对象加载数据 
		myChart.setOption(option);
	}
</script>
<!-- ***********************************界面************************************** -->
</head>

<body>
	<div id="container" style="width:1450px">
 
		<div id="header">
			<h1 style="float:left;width:1402px;margin-bottom:0;border-style:solid;border-width:1px;border-color:#00afff;;border-bottom-color:white">
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			JPWQ系统战备完好性集成演示验证系统</h1>
		</div>
 <!-- *****************************左边界面 *************************************-->
		<div id="menu" style="height:690px;width:650px;float:left;border-style:solid;border-width:1px;border-color:#00afff">
		<table>
<div id="header1">
    <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;功能测试输入</h2>
</div>     <!-- 在文本框内输入一个数字，点击输入完毕按钮，将在本地生成一个input.txt，内容为输入的数字 -->
<div id="input1">
    <!--<input id="data1" type="text" value="" />        <p></p>-->
   <form action="txt.do" method="post">
  &nbsp;&nbsp;&nbsp;&nbsp;请输入系统名
    <select name="system" id="data1" >
        <option value="systemall">所有系统</option>
        <option value="6管30mm舰炮系统">6管30mm舰炮系统</option>
        <option value="630系统">630系统</option>
        <option value="H/PJ26型单管76mm舰炮系统">H/PJ26型单管76mm舰炮系统</option>
        <option value="H/PJ13型6管30mm舰炮系统">H/PJ13型6管30mm舰炮系统</option>
        <option value="单76系统">单76系统</option>
        <option value="单76舰炮火控系统">单76舰炮火控系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="单76炮系统">单76炮系统</option>
        <option value="单100系统">单100系统</option>
        <option value="H/PJ333B舰炮系统">H/PJ333B舰炮系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="双100系统">双100系统</option>
        <option value="双37系统">双37系统</option>
        <option value="3200火箭炮系统">3200火箭炮系统</option>
        <option value="1130舰炮武器系统">1130舰炮武器系统</option>
        <option value="单管76舰炮武器系统">单管76舰炮武器系统</option>
        <option value="万发系统">万发系统</option>
        <option value="857副炮系统">857副炮系统</option>
        <option value="单76主炮系统">单76主炮系统</option>
        <option value="单130系统">单130系统</option>
        <option value="非系统">非系统</option>
        <option value="400H2逆变电源">400H2逆变电源</option>
        <option value="11管30mm舰炮系统">11管30mm舰炮系统</option>
        <option value="360系统">360系统</option>
        <option value="69A式双30mm舰炮系统">69A式双30mm舰炮系统</option>
        <option value="76F双37㎜舰炮">76F双37㎜舰炮</option>
        <option value="7管30mm舰炮系统">7管30mm舰炮系统</option>
        <option value="857系统">857系统</option>
        <option value="H/LJQ-363A搜索雷达">H/LJQ-363A搜索雷达</option>
        <option value="H/PJ26型单管76mm舰炮">H/PJ26型单管76mm舰炮</option>
        <option value="АК-130舰炮">АК-130舰炮</option>
    </select>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;请输入舰队名
    <select name="brigade" id="data2">
        <option value="brigadeall">所有舰队</option>
        <option value="205大队">205大队</option>
        <option value="21大队">21大队</option>
        <option value="14大队">14大队</option>
        <option value="登五支队">登五支队</option>
        <option value="护13支队">护13支队</option>
        <option value="护14支队">护14支队</option>
        <option value="护15支队">护15支队</option>
        <option value="护16支队">护16支队</option>
        <option value="驱3支队">驱3支队</option>
        <option value="作2支队">作2支队</option>
    </select>
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入开始时间
    <select id="data3" name="starttime">
        <option value="start_time">请选择开始时间</option>
        <option value="2004.1.1">2004.1.1</option>
        <option value="2005.1.1">2005.1.1</option>
        <option value="2006.1.1">2006.1.1</option>
        <option value="2007.1.1">2007.1.1</option>
        <option value="2008.1.1">2008.1.1</option>
        <option value="2009.1.1">2009.1.1</option>
        <option value="2010.1.1">2010.1.1</option>
        <option value="2011.1.1">2011.1.1</option>
        <option value="2012.1.1">2012.1.1</option>
        <option value="2013.1.1">2013.1.1</option>
        <option value="2014.1.1">2014.1.1</option>
        <option value="2015.1.1">2015.1.1</option>
        <option value="2016.1.1">2016.1.1</option>
        <option value="2017.1.1">2017.1.1</option>
        <option value="2018.1.1">2018.1.1</option>
        <option value="2019.1.1">2019.1.1</option>
        <option value="2020.1.1">2020.1.1</option>
        <option value="2021.1.1">2021.1.1</option>
        <option value="2022.1.1">2022.1.1</option>
        <option value="2023.1.1">2023.1.1</option>
        <option value="2024.1.1">2024.1.1</option>
        <option value="2025.1.1">2025.1.1</option>
        <option value="2026.1.1">2026.1.1</option>
        <option value="2027.1.1">2027.1.1</option>
        <option value="2028.1.1">2028.1.1</option>
        <option value="2029.1.1">2029.1.1</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入结束时间
    <select id="data4" name="stoptime">
        <option value="end_time">请选择结束时间</option>
        <option value="2004.12.31">2004.12.31</option>
        <option value="2005.12.31">2005.12.31</option>
        <option value="2006.12.31">2006.12.31</option>
        <option value="2007.12.31">2007.12.31</option>
        <option value="2008.12.31">2008.12.31</option>
        <option value="2009.12.31">2009.12.31</option>
        <option value="2010.12.31">2010.12.31</option>
        <option value="2011.12.31">2011.12.31</option>
        <option value="2012.12.31">2012.12.31</option>
        <option value="2013.12.31">2013.12.31</option>
        <option value="2014.12.31">2014.12.31</option>
        <option value="2015.12.31">2015.12.31</option>
        <option value="2016.12.31">2016.12.31</option>
        <option value="2017.12.31">2017.12.31</option>
        <option value="2018.12.31">2018.12.31</option>
        <option value="2019.12.31">2019.12.31</option>
        <option value="2020.12.31">2020.12.31</option>
        <option value="2021.12.31">2021.12.31</option>
        <option value="2022.12.31">2022.12.31</option>
        <option value="2023.12.31">2023.12.31</option>
        <option value="2024.12.31">2024.12.31</option>
        <option value="2025.12.31">2025.12.31</option>
        <option value="2026.12.31">2026.12.31</option>
        <option value="2027.12.31">2027.12.31</option>
        <option value="2028.12.31">2028.12.31</option>
        <option value="2029.12.31">2029.12.31</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入计算方式
    <select id="data5" name="calway">
        <option value="modall">所有平均方式</option>
        <option value="mod1">混合平均</option>
        <option value="mod2">按舰队平均</option>
        <option value="mod3">按试验平均</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入试验方式
        <select id="data6" name="testway">
            <option value="experimentall">所有试验方式</option>
            <option value="4A系泊航行">4A系泊航行</option>
            <option value="4A陆试">4A陆试</option>
            <option value="54系泊航行">54系泊航行</option>
            <option value="55陆试">55陆试</option>
            <option value="052陆试">052陆试</option>
            <option value="2D陆试">2D陆试</option>
            <option value="2D系泊航行">2D系泊航行</option>
            <option value="6A系泊航行">6A系泊航行</option>
            <option value="172系泊航行">172系泊航行</option>
        </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<input value="输入完毕" type="submit" id="registerBtn"/>  
</form>


<p></p>    <!-- 点击运行Python按钮，将本地执行test4.py程序 -->
<form action="yunxing.do" method="post">
    &nbsp;&nbsp;&nbsp;&nbsp;<input value="运行程序" type="submit" id="yunxing"/>
</form>     <!-- 点击结果, 将在框内显示出计算的结果-->
<!--<div id="result">-->
    <!--<p><a href="result.txt" target="result">显示结果</a></p>-->
    <!--<iframe name="result" width="100" height="30" scrolling="no" frameborder="3"></iframe>-->
<!--</div>     <p></p>-->
<div id="result">    &nbsp;&nbsp;  使用说明：文本框输入按照要求对应的输入，然后依次点击 [输入完毕] [运行程序]
</div>
<br>
<div>
   <form action="chaxun.do" method="post">
  &nbsp;&nbsp;&nbsp;&nbsp;请输入部件名
    <select name="device" id="data0" >
        <option value="deviceall">所有部件</option>
        <option value="H/PJ13型6管30mm舰炮">H/PJ13型6管30mm舰炮</option>
        <option value="ZGJ-1C光电跟踪仪">ZGJ-1C光电跟踪仪</option>
        <option value="触摸屏">触摸屏</option>
        <option value="630舰炮">630舰炮</option>
        <option value="监控柜">监控柜</option>
        <option value="光电跟踪仪">光电跟踪仪</option>
        <option value="随动系统">随动系统</option>
        <option value="630舰炮">630舰炮</option>
        <option value="上软导引">上软导引</option>
        <option value="下软导引">下软导引</option>
        <option value="随动部分">随动部分</option>
        <option value="机械部分">机械部分</option>
        <option value="导气设备">导气设备</option>
        <option value="冷却系统">冷却系统</option>
        <option value="双联装57mm舰炮">双联装57mm舰炮</option>
        <option value="双联装37mm舰炮">双联装37mm舰炮</option>
        <option value="66式双57mm舰炮">66式双57mm舰炮</option>
        <option value="61式双37mm舰炮（一）">61式双37mm舰炮（一）</option>
        <option value="61式双38mm舰炮（二）">61式双38mm舰炮（二）</option>
        <option value="61式双39mm舰炮（三）">61式双39mm舰炮（三）</option>
        <option value="H/PJ17单管30毫米舰炮">H/PJ17单管30毫米舰炮</option>
        <option value="单76毫米舰炮">单76毫米舰炮</option>
        <option value="630舰炮火控设备">630舰炮火控设备</option>
        <option value="H/PJ13型6管30mm舰炮">H/PJ13型6管30mm舰炮</option>
        <option value="630舰炮">630舰炮</option>
        <option value="H/ZGJ-1C光电跟踪仪">H/ZGJ-1C光电跟踪仪</option>
        <option value="H/PJ130401监控柜">H/PJ130401监控柜</option>
        <option value="H/PJ130402监控柜">H/PJ130402监控柜</option>
        <option value="H/PJ130403监控柜">H/PJ130403监控柜</option>
        <option value="1C光电跟踪仪">1C光电跟踪仪</option>
        <option value="单管30毫米舰炮">单管30毫米舰炮</option>
        <option value="卡什坦导弹火炮系统">卡什坦导弹火炮系统</option>
        <option value="61F双37炮">61F双37炮</option>
        <option value="61F双25炮">61F双25炮</option>
        <option value="火控设备">火控设备</option>
        <option value="349A跟踪雷达">349A跟踪雷达</option>
        <option value="火控设备">火控设备</option>
        <option value="347B跟踪雷达">347B跟踪雷达</option>
        <option value="单76毫米舰炮">单76毫米舰炮</option>
        <option value="349A雷达">349A雷达</option>
        <option value="扬弹机">扬弹机</option>
        <option value="76监控台">76监控台</option>
        <option value="枪炮长显控台">枪炮长显控台</option>
        <option value="H/ZPJ-2C指挥仪">H/ZPJ-2C指挥仪</option>
        <option value="主炮雷达">主炮雷达</option>
        <option value="跟踪雷达">跟踪雷达</option>
        <option value="弹药装载机">弹药装载机</option>
        <option value="左前副炮随动">左前副炮随动</option>
        <option value="右前副炮随动">右前副炮随动</option>
        <option value="左后副炮随动">左后副炮随动</option>
        <option value="右后副炮随动">右后副炮随动</option>
        <option value="前主炮随动">前主炮随动</option>
        <option value="后主炮随动">后主炮随动</option>
        <option value="主炮指挥仪">主炮指挥仪</option>
        <option value="副炮指挥仪">副炮指挥仪</option>
        <option value="副枪炮长显控台">副枪炮长显控台</option>
        <option value="枪炮长显控台">枪炮长显控台</option>
        <option value="JM-90瞄准仪">JM-90瞄准仪</option>
        <option value="H/ZPJ-4C指挥仪">H/ZPJ-4C指挥仪</option>
        <option value="副炮雷达">副炮雷达</option>
        <option value="随动控制柜">随动控制柜</option>
        <option value="反潜指挥仪">反潜指挥仪</option>
        <option value="单76毫米舰炮">单76毫米舰炮</option>
        <option value="火控系统">火控系统</option>
        <option value="H/ZFJ-1型近程反导火控设备">H/ZFJ-1型近程反导火控设备</option>
        <option value="H/LJP-349跟踪雷达">H/LJP-349跟踪雷达</option>
        <option value="H/ZGJ-4光电跟踪仪">H/ZGJ-4光电跟踪仪</option>
        <option value="H/JWJ-1捷联垂直参考基准">H/JWJ-1捷联垂直参考基准</option>
        <option value="H/PJ12型7管30mm舰炮">H/PJ12型7管30mm舰炮</option>
        <option value="H/PJ13型6管30mm舰炮">H/PJ13型6管30mm舰炮</option>
        <option value="ZGJ-1C光电跟踪仪">ZGJ-1C光电跟踪仪</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<input value="查看部件输出统计" type="submit" id="registerBtn"/>  
</form>
<br>
<br>
        <form action="chaxun2.do" method="post">
  &nbsp;&nbsp;&nbsp;&nbsp;请输入型号名
    <select name="system" id="data1" >
        <option value="systemall">所有型号</option>
        <option value="6管30mm舰炮系统">6管30mm舰炮系统</option>
        <option value="630系统">630系统</option>
        <option value="H/PJ26型单管76mm舰炮系统">H/PJ26型单管76mm舰炮系统</option>
        <option value="H/PJ13型6管30mm舰炮系统">H/PJ13型6管30mm舰炮系统</option>
        <option value="单76系统">单76系统</option>
        <option value="单76舰炮火控系统">单76舰炮火控系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="单76炮系统">单76炮系统</option>
        <option value="单100系统">单100系统</option>
        <option value="H/PJ333B舰炮系统">H/PJ333B舰炮系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="双100系统">双100系统</option>
        <option value="双37系统">双37系统</option>
        <option value="3200火箭炮系统">3200火箭炮系统</option>
        <option value="1130舰炮武器系统">1130舰炮武器系统</option>
        <option value="单管76舰炮武器系统">单管76舰炮武器系统</option>
        <option value="万发系统">万发系统</option>
        <option value="857副炮系统">857副炮系统</option>
        <option value="单76主炮系统">单76主炮系统</option>
        <option value="单130系统">单130系统</option>
        <option value="非系统">非系统</option>
        <option value="400H2逆变电源">400H2逆变电源</option>
        <option value="11管30mm舰炮系统">11管30mm舰炮系统</option>
        <option value="360系统">360系统</option>
        <option value="69A式双30mm舰炮系统">69A式双30mm舰炮系统</option>
        <option value="76F双37㎜舰炮">76F双37㎜舰炮</option>
        <option value="7管30mm舰炮系统">7管30mm舰炮系统</option>
        <option value="857系统">857系统</option>
        <option value="H/LJQ-363A搜索雷达">H/LJQ-363A搜索雷达</option>
        <option value="H/PJ26型单管76mm舰炮">H/PJ26型单管76mm舰炮</option>
        <option value="АК-130舰炮">АК-130舰炮</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入舰队名
    <select name="brigade" id="data2">
        <option value="brigadeall">所有舰队</option>
        <option value="205大队">205大队</option>
        <option value="21大队">21大队</option>
        <option value="14大队">14大队</option>
        <option value="登五支队">登五支队</option>
        <option value="护13支队">护13支队</option>
        <option value="护14支队">护14支队</option>
        <option value="护15支队">护15支队</option>
        <option value="护16支队">护16支队</option>
        <option value="驱3支队">驱3支队</option>
        <option value="作2支队">作2支队</option>
    </select>
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入试验方式
        <select id="data6" name="testway">
            <option value="experimentall">所有试验方式</option>
            <option value="4A系泊航行">4A系泊航行</option>
            <option value="4A陆试">4A陆试</option>
            <option value="54系泊航行">54系泊航行</option>
            <option value="55陆试">55陆试</option>
            <option value="052陆试">052陆试</option>
            <option value="2D陆试">2D陆试</option>
            <option value="2D系泊航行">2D系泊航行</option>
            <option value="6A系泊航行">6A系泊航行</option>
            <option value="172系泊航行">172系泊航行</option>
        </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<input value="查看系统稳态可用度输出统计" type="submit" id="registerBtn"/>  
</form>
<br>
<br>
        <form action="chaxun3.do" method="post">
  &nbsp;&nbsp;&nbsp;&nbsp;请输入型号名
    <select name="system" id="data1" >
        <option value="systemall">所有型号</option>
        <option value="6管30mm舰炮系统">6管30mm舰炮系统</option>
        <option value="630系统">630系统</option>
        <option value="H/PJ26型单管76mm舰炮系统">H/PJ26型单管76mm舰炮系统</option>
        <option value="H/PJ13型6管30mm舰炮系统">H/PJ13型6管30mm舰炮系统</option>
        <option value="单76系统">单76系统</option>
        <option value="单76舰炮火控系统">单76舰炮火控系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="单76炮系统">单76炮系统</option>
        <option value="单100系统">单100系统</option>
        <option value="H/PJ333B舰炮系统">H/PJ333B舰炮系统</option>
        <option value="双100炮系统">双100炮系统</option>
        <option value="双100系统">双100系统</option>
        <option value="双37系统">双37系统</option>
        <option value="3200火箭炮系统">3200火箭炮系统</option>
        <option value="1130舰炮武器系统">1130舰炮武器系统</option>
        <option value="单管76舰炮武器系统">单管76舰炮武器系统</option>
        <option value="万发系统">万发系统</option>
        <option value="857副炮系统">857副炮系统</option>
        <option value="单76主炮系统">单76主炮系统</option>
        <option value="单130系统">单130系统</option>
        <option value="非系统">非系统</option>
        <option value="400H2逆变电源">400H2逆变电源</option>
        <option value="11管30mm舰炮系统">11管30mm舰炮系统</option>
        <option value="360系统">360系统</option>
        <option value="69A式双30mm舰炮系统">69A式双30mm舰炮系统</option>
        <option value="76F双37㎜舰炮">76F双37㎜舰炮</option>
        <option value="7管30mm舰炮系统">7管30mm舰炮系统</option>
        <option value="857系统">857系统</option>
        <option value="H/LJQ-363A搜索雷达">H/LJQ-363A搜索雷达</option>
        <option value="H/PJ26型单管76mm舰炮">H/PJ26型单管76mm舰炮</option>
        <option value="АК-130舰炮">АК-130舰炮</option>
    </select>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入舰队名
    <select name="brigade" id="data2">
        <option value="brigadeall">所有舰队</option>
        <option value="205大队">205大队</option>
        <option value="21大队">21大队</option>
        <option value="14大队">14大队</option>
        <option value="登五支队">登五支队</option>
        <option value="护13支队">护13支队</option>
        <option value="护14支队">护14支队</option>
        <option value="护15支队">护15支队</option>
        <option value="护16支队">护16支队</option>
        <option value="驱3支队">驱3支队</option>
        <option value="作2支队">作2支队</option>
    </select>
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;请输入试验方式
        <select id="data6" name="testway">
            <option value="experimentall">所有试验方式</option>
            <option value="4A系泊航行">4A系泊航行</option>
            <option value="4A陆试">4A陆试</option>
            <option value="54系泊航行">54系泊航行</option>
            <option value="55陆试">55陆试</option>
            <option value="052陆试">052陆试</option>
            <option value="2D陆试">2D陆试</option>
            <option value="2D系泊航行">2D系泊航行</option>
            <option value="6A系泊航行">6A系泊航行</option>
            <option value="172系泊航行">172系泊航行</option>
        </select>
        <br>
&nbsp;&nbsp;&nbsp;&nbsp;<input value="查看系统瞬时可用度输出统计" type="submit" id="registerBtn"/>  
</form>
<!--
     <input type="button" value="查看部件输出统计" onclick="window.open('http://localhost:8080/echartsdemo/1.jsp')"> &nbsp;
	 <input type="button" value="查看系统稳态可用度输出统计" onclick="window.open('http://localhost:8080/echartsdemo/2.jsp')"> &nbsp;
	 <input type="button" value="查看系统瞬时可用度输出统计" onclick="window.open('http://localhost:8080/echartsdemo/3.jsp')">
-->
</div> 
</table>
		</div>
		
 <!-- ************************************************右边界面*************************************** -->
		<br>
		<div id="main" style="height:690px;width:750px;float:left;border-style:solid;border-width:1px;border-color:#00afff;border-left-color:white">
		</div>
	</div>
</body>
</html>