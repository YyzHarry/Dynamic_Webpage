/*界面渲染*/
//渲染查询地区选项表
function render_district(district_item) {
  var $option = $('<option></option>');
  $option.attr('value',district_item.district_id);
  $option.text(district_item.district_name);
  $('#district_select').append($option);
}

//渲染AQI参数表
function render_aqi(dp) {
  var $div = $('<div></div>');

  $div.addClass('container');

  //var content = '<div class="container page-header">' + '<h2 class="text-center">' + dp.district_name + '的AQI参数值' + '</h2></div>';
  var content = '<h2 class="text-center">' + dp.district_name + '的AQI参数值' + '</h2>';

  var img = '<img class="img-responsive center-block" src="img/' + dp.district_name + '.jpg" align="middle" width="450px" height="300px" alt="' + dp.district_name + '"/>';

  //var form = '<table class="container table-bordered">' + '<thead class="bg-danger">' + '<tr>' + '<th>一氧化碳/CO</th> <th>二氧化硫/SO2</th> <th>臭氧/O3</th> <th>一氧化氮/NO</th> <th>PM1.0</th> <th>PM2.5</th> <th>PM10</th></tr></thead>'
  //           + '<tbody> <tr class="success"> <td>' + dp.CO + '</td><td>' + dp.SO2 +'</td><td>' + dp.O3 + '</td><td>' + dp.NO + '</td><td>' + dp.PM1 + '</td><td>' + dp.PM2 + '</td><td>' + dp.PM10 + '</td></tr></tbody></table>';
  var form = '<table class="table table-bordered">' + '<thead>' + '<tr>' + '<th>一氧化碳/CO</th> <th>二氧化硫/SO2</th> <th>臭氧/O3</th> <th>一氧化氮/NO</th> <th>PM1.0</th> <th>PM2.5</th> <th>PM10</th></tr></thead>'
             + '<tbody> <tr class="success"> <td>' + dp.CO + '</td><td>' + dp.SO2 +'</td><td>' + dp.O3 + '</td><td>' + dp.NO + '</td><td>' + dp.PM1 + '</td><td>' + dp.PM2 + '</td><td>' + dp.PM10 + '</td></tr></tbody></table>';

  var link = '<div class="form-group col-sm-offset-5 col-sm-2 col-md-offset-5 col-md-2"><a href="./index.html"><button class="btn btn-warning form-control" type="button">返回</button></a></div>';
  
  $div.append(content,img,form,link);

  $('#display').append($div);
}

/*
function render_product(product) {
  var $div = $('<div></div>');
  $div.attr('style',"width:20%;height:350px;");
  $div.addClass('thumbnail col-sm-6 col-md-3');

  var img = '<img class="img-responsive" src="img/' + product.product_name + '.jpg" alt="' + product.product_name + '"/>';

  var content = '<div class="caption">' + '<h3>'+product.product_name+'</h3>' + '<p>类别：'+product.type+'</p>' + '<p>单价：'+product.price+'/'+product.unit+'</p>';

  var $form = $('<div></div>');
  $form.attr('product_name',product.product_name);
  $form.attr('price',product.price);
  $form.addClass('form-inline');
  $form.append('<input class="form-control" min="1" style="width:40%" type="number" name="quantity" value="1">');
  $form.append('<button class="btn btn-primary form-control" type="button">加入购物车</button>');
  $div.append(img,content,$form);
  $('#display').append($div);
}
*/

/*查询业务逻辑*/
//获取校内地区信息
function fetch_district(){
  $.get('index_fetch_district',function (data,status) {
    if(status=="success"){
      console.log('获得校内地区信息');
      var district_list = JSON.parse(data);
      for (var i in district_list) {
        render_district(district_list[i]);
      }
    }else{
      console.error('无法连接到服务器');
    }
  });
}

//查询指定区域内的参数
function query_district(){
  var district_id = $('#query_form [name=district]').val();
  var type = $('#query_form [name=type]').val();
  var options = {
    url:'/index_query_district',
    type:'get',
    data:{'district_id':district_id,'type':type},
    dataType:'json',
    success:function(dp_list) {
      console.log('获得地点参数信息答复');
      // dp_list = JSON.parse(dp_list);
      if (dp_list.err){
        console.error('查询地点参数信息错误');
        return;
      }
      //音效提示
      success('成功查询到地点AQI');
      //成功查询到地点AQI
      $('#display').empty();
      $('#display').attr('district_id',district_id);

      for (var i in dp_list) {
        render_aqi(dp_list[i]);
      }
      //$('#display div h4').addClass('list-group-item-heading');
      //$('#display div address').addClass('list-group-item-text');
      //$('#display div p').addClass('list-group-item-text');
    },
    error:get_error
  };
  $.ajax(options);
}

// 页面初始化
function init(){
  render_header();  //导航栏
  fetch_district();  //获取校园内地区信息
  $('#query_btn').click(query_district);  //绑定查询按钮
  console.log('主页');
}

$(document).ready(init);
