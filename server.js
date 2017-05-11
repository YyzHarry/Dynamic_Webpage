/*服务器建立*/
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use(cookieParser());
app.use(express.static('html'));

/* 辅助函数*/
var assert = require('assert');
var ts = require('time-stamp');
var hasha = require('hasha');

// Combine Node.js Server & Python Server
var exec = require('child_process').exec;


// 数据库模块
var mysql = require('mysql');
var database_name = 'aqidata';
var visitor_info = {username:"visitor",password:"visitor",type:'VISITOR'};

function create_connection(user_info){
  if (user_info.type == 'VISITOR') {
    user_info.username = "root";
    user_info.password = "password";
  }
  var connection = mysql.createConnection({
    host:'localhost',
    user:user_info.username,
    password:user_info.password,
    database:database_name,
    multipleStatements:true
  });
  return connection;
}

/*服务器主逻辑*/
/*主页逻辑*/

// 主页查询地区信息
app.get('/index_fetch_district', function (req, res) {
  console.log('主页发送校内区域查询请求');
  console.log(req.cookies);

  var user_info = JSON.parse(req.cookies.user_info);
  var connection  = create_connection(user_info);
  var sqlString = 'select * from repository;';

  connection.query(sqlString,function (err,rows,fields) {
    var response = new Object();
    if(err){
      console.error('数据库查询失败:'+err.stack);
      response.error = true;
    }else{
      console.log(rows);
      response = rows;
      console.log('查询校内区域成功');
    }
    connection.end();
    res.end(JSON.stringify(response));
  });
})

app.get('/index_query_district', function (req, res) {
  console.log('主页发送区域点参数查询请求');
  console.log(req.cookies);
  console.log(req.query);

  var user_info = JSON.parse(req.cookies.user_info);
  var connection  = create_connection(user_info);
  var response = new Object();
  if (req.query.type == "now"){
    var sqlString = 'select * from aqi_now where district_id=?;';
    var escape = req.query.district_id;
  }else if (req.query.type == "average") {
    var sqlString = 'select * from aqi_average where district_id=?;';
    var escape = req.query.district_id;
  }else{
    response.error = true;
    res.end(JSON.stringify(response));
    return;
  }

  connection.query(sqlString,escape,function (err,rows,fields) {
    if(err){
      console.error('数据库查询失败:'+err.stack);
      response.error = true;
    }else{
      console.log(rows);
      response = rows;
      console.log('查询区域内AQI参数成功');
    }
    connection.end();
    res.end(JSON.stringify(response));
  });

})



// 服务器监听地图点击事件
app.get('/aqi_js.py', function(req, res){
    // lat & lng
  var arg1 = req.query.lat;
  var arg2 = req.query.lng;
  var arg3 = req.query.district;

  exec('python aqi_js.py '+ arg1+' '+arg2+' '+arg3+' ', function(error,stdout,stderr){
    // try lat and lng 
    //console.log(req.query.lat);
    //console.log(req.query.lng);
    //console.log(req.query.district);
    if(error){
        console.info('stderr : '+stderr);
    }else{
        //console.log('查询地点的经纬度和区域为 ('+req.query.lat+','+req.query.lng+','+req.query.district+')');

        //get JSON from python
        var data = JSON.parse(stdout);
        console.log(data);

        // send response to client
        res.end(JSON.stringify(data));
    }

  });

});


// 服务器监听端口8081
var server = app.listen(8081, function () {
  var host = server.address().address
  var port = server.address().port
  console.log("AQI网站已建立，访问地址为 http://%s:%s", host, port)
})
