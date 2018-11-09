$(document).ready(function () {

      $(".add_to_cart").click(function () {

        $add_to_cart=$(this)

        only_id=$add_to_cart.attr("only_id")

        console.log(only_id)

        $.getJSON('/lang/add_to_cart',{'goods_id':only_id},function (data) {

            console.log("数据添加成功")

            console.log(data)

            if(data['status']==200){

                $add_to_cart.prev('span').html(data['goods_num']);

            }
            else if(data['status']==500)
            {
                window.open('/lang/login',target='_self')
            }

        })





    })

    // 在market中进行减操作

    $(".sub_from_cart").click(function () {

        $sub_from_cart=$(this)

        only_id=$sub_from_cart.attr('only_id')

        console.log(only_id)

        $.getJSON('/lang/sub_from_cart',{'goods_id':only_id},function (data) {

                console.log("我开始进行减判断")

            if(data['status']==200){
                    $sub_from_cart.next('span').html(data['goods_num']);

            }
            else if(data['status']==500)
            {
                window.open('/lang/login/',target='_self')
            }


        })

    })


})