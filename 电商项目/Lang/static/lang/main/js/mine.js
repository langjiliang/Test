$(document).ready(function () {

    $("#denglu").click(function () {

        console.log("点击")

        window.open('/lang/login',target='_self')

    })

    $("#sign_out").click(function () {

        console.log("点击退出")

        $.getJSON('/lang/sign_out',{'flag':1},function () {
            console.log("退出成功")
        })
    })

})
