//返回大屏数据
function get_c1_data() {
    $.ajax({
        url: "/c1",
        success: function(data) {
            $(".num li").eq(0).text(data.confirm);
            $(".num li").eq(1).text(data.heal);
            $(".num li").eq(2).text(data.dead);
            $(".num li").eq(3).text(data.nowConfirm);
        },
        error: function(xhr, type, errorThrown) {
        }
    })
}
get_c1_data()
setInterval(get_c1_data,10000*10);