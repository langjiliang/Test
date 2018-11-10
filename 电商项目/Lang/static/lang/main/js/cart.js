$(document).ready(function () {

    $("#all_select").click(function () {

        $all_select = $(this)

        val = $all_select.text()

        color = $all_select.css('color')

        console.log(val)

        console.log(color)

        if (val == '√') {

            $all_select.text('')

            $all_select.css('background-color', 'white')

        }
        else {
            $all_select.text('√')

            $all_select.css('background-color', 'orangered')

        }


    })


    $(".add_to_cart").click(function () {

        $add_to_cart = $(this)

        only_id = $add_to_cart.attr("only_id")

        console.log(only_id)

        $.getJSON('/lang/add_to_cart', {'goods_id': only_id}, function (data) {

            console.log("数据添加成功")

            console.log(data)

            if (data['status'] == 200) {

                $add_to_cart.prev('span').html(data['goods_num']);

            }

            else if (data['status'] == 500) {
                window.open('/lang/login/', target = '_self')
            }

        })


    })

    // 在market中进行减操作

    $(".sub_from_cart").click(function () {

        $sub_from_cart = $(this)

        only_id = $sub_from_cart.attr('only_id')

        console.log(only_id)

        $.getJSON('/lang/sub_from_cart', {'goods_id': only_id}, function (data) {

            console.log("我开始进行减判断")

            if (data['status'] == 200) {
                $sub_from_cart.next('span').html(data['goods_num']);

            }
              else if(data['status']==400){
                window.open('/lang/cart/', target = '_self')
            }
            else if (data['status'] == 500) {
                window.open('/lang/login/', target = '_self')
            }


        })

    })


    // 对小圆圈中的数据进行判断
    $(".bool1").click(function () {

        var flag

        $ball = $(this)

        val = $ball.text()

        cart_id = $ball.attr('cart_id')

        console.log(cart_id)

        if (val == '√') {

            $ball.text('')

            $ball.css('background-color', 'white')

            flag=0

        }
        else {
            $ball.text('√')

            $ball.css('background-color', 'orangered')

            flag=1

        }

       $.getJSON('/lang/judge_ball',{'cart_id':cart_id,'flag':flag},function (data) {
            console.log("ajax  SUcceed")
           console.log(data['price'])
           if(data['statud']==500){
                window.open('/lang/login',target="_self")
           }
           else{
                console.log(data['price'])
                $("#total").html(data['price'])

           }

       })


    })


    // 点击之后下单

    $("#place_an_order").click(function () {

        console.log("我已经点击下单了")
        $.getJSON('/lang/place_an_order',{},function (data) {

            if(data['status']==200)
            {
                window.open('/lang/show_order/?order_id=' + data['order_id'],target='_self')
            }

            else if(data['status']==300)
            {
                console.log("用户未选择商品")
            }
            else if(data['status']==500){
                console.log("用户未登录")
                window.open('/lang/login/',target='_self')
            }

        })

    })

})