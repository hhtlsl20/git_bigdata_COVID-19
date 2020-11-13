insert OVERWRITE table global_center select sum(confirm),sum(heal),sum(dead),sum(nowConfirm) from globaldata_hive;  
insert OVERWRITE table global_coutry_top SELECT name,confirm FROM (select * from globaldata_hive order by confirm desc limit 5) aa ORDER BY name asc;  
insert OVERWRITE table global_city_top SELECT city,confirm FROM (select * from detailsusa_hive order by confirm desc limit 5) aa ORDER BY city asc;
insert OVERWRITE table china_new_out SELECT ds,confirm_add,heal_add,dead_add FROM (select * from chinahistory_hive order by ds desc limit 100) aa ORDER BY ds asc;
insert OVERWRITE table global_new_out SELECT ds,newAddConfirm,heal_add,dead_add FROM (select * from globalhistory_hive order by ds desc limit 100) aa ORDER BY ds asc;
insert OVERWRITE table china_sunconfirm_l3 select ds,confirm,heal,dead from chinahistory_hive  ORDER BY ds desc limit 1;
insert OVERWRITE table global_sunconfirm_l3 select sum(confirm),sum(heal),sum(dead) from globaldata_hive;
insert OVERWRITE table global_plate select continent,sum(confirm) as all_confirm ,sum(heal) as all_heal ,sum(dead) as all_dead from globaldata_hive group by continent;

insert overwrite table china_c1 select * from china order by ds desc limit 1;
insert overwrite table china_c2 SELECT province ,SUM(confirm) from details group by province;
insert overwrite table china_l1 select ds,confirm,heal,dead,suspect from china;
insert overwrite table china_l2 select ds,confirm_add,suspect_add from china;
insert overwrite table china_l3 select sum(confirm_add),sum(heal_add),sum(dead_add) from china group by MONTH (ds);
insert overwrite table china_r2 select content from hotsearch_hive limit 20;



