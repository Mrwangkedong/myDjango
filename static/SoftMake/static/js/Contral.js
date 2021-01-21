function ht_num_ok() {
    var ht_num = $('input[name="ht_num"]').val();
    var ht_num_len = ht_num.length;
    ht_num_len = Number(ht_num_len);
    //判断字符长度是否为11位
    if(ht_num_len != 11){
        return 2; //不符合ok
    }

    //判断是否全为数字
    for(i=0;i<ht_num_len;i++){

            if(isNaN(ht_num[i]) == true){
                return 2
            }

    }
    return 1; //验证完成，返回 1
}

function ybs_num_ok() {
    var ybs_num = $('input[name="ybs_num"]').val();
    var ybs_num_len = ybs_num.length;
    ybs_num_len = Number(ybs_num_len);
    //判断字符长度是否为11位
    if(ybs_num_len != 11){
        return 2; //不符合ok
    }
    //判断是否全为数字
    for(i=0;i<ybs_num_len;i++){

            if(isNaN(ybs_num[i]) == true){
                return 2
            }

    }
    return 1; //验证完成，返回 1

}

function tb_num_ok() {
    var tb_num = $('input[name="tb_num"]').val();
    var tb_num_len = tb_num.length;
    tb_num_len = Number(tb_num_len);
    //判断字符长度是否为11位
    if(tb_num_len != 11){
        return 2; //不符合ok
    }
    //判断是否全为数字
    for(i=0;i<tb_num_len;i++){

            if(isNaN(tb_num[i]) == true){
                return 2
            }

    }
    return 1; //验证完成，返回 1

}

function ht_money_ok() {
    var ht_money = $('input[name="ht_money"]').val();
    //判断是否全为数字
    for(i=0;i<ht_money.length;i++){

            if(isNaN(ht_money[i]) == true){
                return 2
            }

    }
    return 1; //验证完成，返回 1
}

function jia_name_ok() {
    var jia_name = $('input[name="jia_name"]').val();
    //判断是否全为数字
    if(jia_name != ''){
        return 1; //验证完成，返回 1
    }else {
        alert('甲方姓名不能为空');
    }

}

function yi_name_ok() {
    var yi_name = $('input[name="yi_name"]').val();
    //判断是否全为数字
    if(yi_name != ''){
        return 1; //验证完成，返回 1
    }else {
        alert('乙方姓名不能为空');
    }

}

function jia_leader_ok(){
    var jia_leader= $('input[name="jia_leader"]').val();  //甲方代表

    if (jia_leader != ''){
        return 1;
    } else {
        alert('甲方代表不为空')
    }
}

function yi_leader_ok(){
    var yi_leader= $('input[name="yi_leader"]').val();  //甲方代表

    if (yi_leader != ''){
        return 1;
    } else {
        alert('乙方代表不为空')
    }
}

function ht_content_ok(){
    var ht_content= $('input[name="ht_content"]').val();  //甲方代表

    if (ht_content != ''){
        return 1;
    } else {
        alert('合同详情不为空')
    }
}

function ht_remark_ok(){
    var ht_remark= $('input[name="ht_remark"]').val();  //甲方代表

    if (ht_remark != ''){
        return 1;
    } else {
        alert('备注不为空')
    }
}

$(function () {
    var ht_num = $('input[name="ht_num"]');   //合同编号
    var ybs_num = $('input[name="ybs_num"]');   //邀标书编号
    var tb_num = $('input[name="tb_num"]');     //投标编号
    var ht_money = $('input[name="ht_money"]'); //合同金额
    var jia_name= $('input[name="jia_name"]');      //甲方姓名
    var yi_name= $('input[name="yi_name"]');        //乙方姓名
    var jia_leader= $('input[name="jia_leader"]');  //甲方代表
    var yi_leader= $('input[name="yi_leader"]');        //乙方代表
    var ht_content= $('input[name="ht_content"]');  //合同详情
    var ht_remark= $('input[name="ht_remark"]');    //合同备注

    //如果本来就有值
    if(ybs_num.val() != ''){
        ybs_num.removeAttr('disabled');
    }
    if(tb_num.val() != ''){
        tb_num.removeAttr('disabled');
    }
    if(ht_money.val() != ''){
        ht_money.removeAttr('disabled');
    }
    if(jia_name.val() != ''){
        jia_name.removeAttr('disabled');
    }
    if(yi_name.val() != ''){
        yi_name.removeAttr('disabled');
    }
    if(jia_leader.val() != ''){
        jia_leader.removeAttr('disabled');
    }
    if(yi_leader.val() != ''){
        yi_leader.removeAttr('disabled');
    }

    //合同编号 绑定事件
    ht_num.hover(function(){
        ht_num.css("background-color","yellow");
    },function(){
       if (ht_num_ok() == 1){
           ybs_num.removeAttr("disabled")
       }
    });

    //邀标书编号 绑定事件
    ybs_num.hover(function(){
        ybs_num.css("background-color","yellow");
    },function(){
       if (ybs_num_ok() == 1){
           tb_num.removeAttr("disabled")
       }
    });

    //投标编号 绑定事件
    tb_num.hover(function(){
        tb_num.css("background-color","yellow");
    },function(){
       if (tb_num_ok() == 1){
           jia_name.removeAttr("disabled")
       }
    });
//////////////////////////////////////////////////////////////
    //甲方姓名 绑定事件
    jia_name.hover(function(){
        ht_num.css("background-color","yellow");
    },function(){
       if (jia_name_ok() == 1){
           yi_name.removeAttr("disabled")
       }
    });

    //乙方姓名 绑定事件
    yi_name.hover(function(){
        yi_name.css("background-color","yellow");
    },function(){
       if (yi_name_ok() == 1){
           ht_money.removeAttr("disabled")
       }
    });

     //合同金额 绑定事件
    ht_money.hover(function(){
        ht_money.css("background-color","yellow");
    },function(){
       if (ht_money_ok() == 1){
           jia_leader.removeAttr("disabled")
       }
    });

    //甲方代表说明
    jia_leader.hover(function(){
        jia_leader.css("background-color","yellow");
    },function(){
       if (jia_leader_ok() == 1){
           yi_leader.removeAttr("disabled")
       }
    });

    //乙方代表备注
    yi_leader.hover(function(){
        yi_leader.css("background-color","yellow");
    },function(){
       if (yi_leader_ok() == 1){
           alert('开始填写内容及备注');
       }
    });


});