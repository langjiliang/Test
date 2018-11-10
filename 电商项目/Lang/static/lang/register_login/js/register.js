var flag = 1
$(document).ready(function () {


    $is_used = $("#name")

    $span_is_used = $("#is_used")
    // 一旦输入框数据改变则判断该用户名是否存在
    username = $is_used.val()

    $is_used.change(function () {

            console.log(username)


            $.getJSON("/lang/judge_name/", {"username": username}, function (data) {
                console.log("我已经进入ajax")
                if (data['status'] == 200) {
                    flaf = 1
                    $span_is_used.html("该用户名可用").css('color', 'green')
                }
                else if (data['status'] == 300) {
                    flag = 0
                    $span_is_used.html("该用户名已经存在").css('color', 'red')

                }
            })
        }
    )

// 对邮箱进行判断是否已经存在该数据
    $email_is_used = $("#email")

    $span_email = $("#email_is_used")

    email = $email_is_used.val()

    $email_is_used.change(function () {

        $.getJSON('/lang/judge_email', {'email': email}, function (data) {

            if (data['status'] == 201) {
                flag = 1
                $span_email.html("该邮箱可用").css("color", "green")
            }
            else if (data['status'] == 301) {
                flag = 0
                $span_email.html("该邮箱已经存在").css("color", "red")

            }

        })

    })

    // 对密码的长度和数据进行判断
    $password = $("#password")

    $span_password = $("#password_is_six")

    $password.change(function () {

        if ($password.val().length != 6) {
            flag = 0

            $span_password.html("请输入六位数密码").css("color", "red")

        }
        else {
            flag = 1
            $span_password.html("密码格式正确").css("color", "green")

        }
    })


    $passwordagain = $("#passwordagain")

    $span_passwordagain = $("#passwordagain_is_same")

    $passwordagain.change(function () {

        if ($password.val() != $passwordagain.val()) {
            flag = 0

            $span_passwordagain.html("两次密码输入不一致").css("color", "red")
        }
        else {
            flag = 1
            $span_passwordagain.html()

        }

    })


    // 对提交进行判断


    if ($is_used.val().length == 0 || $email_is_used.val().length == 0 || $password.val().length == 0 || $passwordagain.val().length == 0) {
        flag = 0
    }


})

function check() {

    if (flag == 0)
        return false
    else if (flag == 1)
        return true
}