//cookie检查
function fetch_cookie(){
  //如果没有用户cookie，新建游客cookie
  if ($.cookie('user_info') == null || $.cookie('user_info') === undefined){
    console.log('没有用户cookie，新建游客cookie');
    var user_info = new Object();
    user_info.username = '游客';
    user_info.password = "";
    user_info.type = 'VISITOR';

    $.cookie('user_info',JSON.stringify(user_info),{/*expires:1,*/path:'/'});
  }else {
    var user_info = JSON.parse($.cookie("user_info"));
  }
  return user_info;
}

//渲染导航栏
function render_header() {
  var user_info = fetch_cookie();
  $("#identity").text(user_info.username);
  console.log('当前用户信息:'+JSON.stringify(user_info));
  switch (user_info.type) {
    case 'VISITOR':
      $("#controller").append('<a id="login_btn" class="btn btn-primary navbar-btn btn-m" href="login.html">注册/登陆</a>');
      break;
    case 'CUSTOMER':
      $("#controller").append('<a id="logout_btn" class="btn btn-danger navbar-btn btn-m" href="logout">注销</a>');
      $("#controller").append('<a id="info_btn" class="btn btn-primary navbar-btn btn-m" href="info.html">个人信息</a>');
      $("#controller").append('<a id="search_btn" class="btn btn-primary navbar-btn btn-m" href="search.html">搜索</a>');
      $("#controller").append('<a id="cart_btn" class="btn btn-success navbar-btn" href="cart.html">购物车</a>');
      break;
    case 'DELIVERER':
      $("#controller").append('<a id="logout_btn" class="btn btn-danger navbar-btn btn-m" href="logout">注销</a>');
      $("#controller").append('<a id="search_btn" class="btn btn-primary navbar-btn btn-m" href="search.html">搜索</a>');
      $("#controller").append('<a id="deliver_btn" class="btn btn-info navbar-btn" href="order.html">我要提货</a>');
      break;
    case 'ADMIN':
      $("#controller").append('<a id="logout_btn" class="btn btn-danger navbar-btn btn-m" href="logout">注销</a>');
      $("#controller").append('<a id="search_btn" class="btn btn-primary navbar-btn btn-m" href="search.html">搜索</a>');
      $("#controller").append('<a id="user_btn" class="btn btn-warning navbar-btn" href="management.html">账户管理</a>');
      break;
    default:
      console.log('未知用户类型');
  }
}

//消息提示
function notify(msg){
  Lobibox.notify('info',{size:'mini',width:400,msg:msg});
}
function success(msg){
  Lobibox.notify('success',{size:'mini',width:400,msg:msg,position:"bottom left"});
}
function failure(msg){
  Lobibox.notify('error',{size:'mini',width:400,msg:msg,position:"bottom right"});
}

function get_error(err){
  console.error('无法连接到服务器');
}
