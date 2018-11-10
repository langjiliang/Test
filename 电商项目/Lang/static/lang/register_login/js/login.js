// $(document).ready(function () {
//
//     // 对登陆数据进行判断
//     $username=$("#name")
//     $password=$("#password")
//
//     username=$username.val()
//     password=$password.val()
//     console.log(password)
//     $.getJSON('/lang/judge_login/',{"username":username,"password":password},function (data) {
//         console.log("我的状态码是")
//
//         console.log(data['status'])
//
//         if(data['status']==200){
//             // 登陆成功
//             window.open('/lang/mine/',target='_self')
//         }
//         else if(data['status']==300){
//             console.log("密码输入错误")
//         }
//         else if(data['status']==400){
//             console.log("用户不存在")
//         }
//
//     })
//
// })