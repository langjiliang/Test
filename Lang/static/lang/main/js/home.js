$(function () {

    initTopSwiper();

    initSwiperMenu();

    initTouTiao()

    initTouMenu()

})

function initTopSwiper() {
    var swiper = new Swiper("#topSwiper",{
        loop: true,
        autoplay: 3000,
        pagination: '.swiper-pagination'
    });
}

function initSwiperMenu() {
    var swiper = new Swiper("#swiperMenu",{
       slidesPerView: 3
    });
}

// 头条轮播
function initTouTiao() {
    var swiper = new Swiper("#touTiao",{
        loop: true,
        autoplay: 3000,
        pagination: '.swiper-pagination',
        direction: "vertical"
    });
}

function initTouMenu() {
    var swiper = new Swiper("#swiperMenu",{
       slidesPerView: 3
    });
}

// 搜索框
$(document).ready(function () {

    $search = $("#search")

    search_info = $search.val()

    $search_submit = $("#search_submit")

    $search_submit.click(function () {

        $.getJSON('/lang/search',{"search_info":search_info},function (data) {

        })

    })



})