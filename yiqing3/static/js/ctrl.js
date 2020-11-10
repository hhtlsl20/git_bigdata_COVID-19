var left_button=document.getElementById('left_button');
left_button.onclick=function () {
    document.location.href='http://192.168.198.13:6060/';
};
// var input =document.getElementById('quanping')
// input.onclick=function () {
//     document.removeChild(input)
// }

var top_country=document.getElementById('top_country');
var top_city=document.getElementById('top_city');
top_country.onclick=function () {
    top_country.style.color='#00f2f1';
    top_city.style.color='white';
};

top_city.onclick=function () {
    top_city.style.color='#00f2f1';
    top_country.style.color='white'
}
var new_con_china=document.getElementById('new_con_china');
var new_con_world=document.getElementById('new_con_world');
new_con_china.onclick=function () {
    new_con_china.style.color='#00f2f1';
    new_con_world.style.color='white';
};

new_con_world.onclick=function () {
    new_con_world.style.color='#00f2f1';
    new_con_china.style.color='white'
}
var china_con_he=document.getElementById('china_con_he');
var world_con_he=document.getElementById('world_con_he');
china_con_he.onclick=function () {
    china_con_he.style.color='#00f2f1';
    world_con_he.style.color='white';
};

world_con_he.onclick=function () {
    world_con_he.style.color='#00f2f1';
    china_con_he.style.color='white'
}
var china_con_his=document.getElementById('china_con_his');
var world_con_his=document.getElementById('world_con_his');
china_con_his.onclick=function () {
    china_con_his.style.color='#00f2f1';
    world_con_his.style.color='white';
};

world_con_his.onclick=function () {
    world_con_his.style.color='#00f2f1';
    china_con_his.style.color='white'
}