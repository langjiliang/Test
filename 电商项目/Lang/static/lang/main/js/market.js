$(document).ready(function () {

    // 返回主页面
    $(".backHome").click(function () {
        window.open('/lang/home', target = "_self")
    })


    // 点击加号将数据信息加一，并将数据加到购物车里，判断购物车是否已经存在这条数据，如果存在
    // 只是将购物车中的数量加一，如果不存在，将这条数据加到里面

    $(".add_to_cart").click(function () {

        $add_to_cart = $(this)

        only_id = $add_to_cart.attr("only_id")

        console.log(only_id)

        $.getJSON('/lang/add_to_cart', {'goods_id': only_id}, function (data) {

            console.log("数据添加成功")

            console.log(data)

            if (data['status'] == 200) {

                num = parseInt($add_to_cart.prev('span').html())
                num = num + 1
                $add_to_cart.prev('span').html(num)

            }
            else if (data['status'] == 500) {
                window.open('/lang/login', target = '_self')
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

            if (data['status'] == 200||data['status']==500) {
                num = parseInt($sub_from_cart.next('span').html())

                if(num>=1){
                       num = num - 1
                       $sub_from_cart.next('span').html(num)

                }


            }


        })

    })

})