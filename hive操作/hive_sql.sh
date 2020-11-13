#!/bin/sh
/opt/apache-hive-2.3.6-bin/bin/hive -f //opt/shell_code/insert.sql

sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table global_center --num-mappers 1 --export-dir /user/hive/warehouse/global_center --input-fields-terminated-by "\t"
sqoop export --connect "jdbc:mysql://47.115.148.142:3306/datafrom_hive?useUnicode=true&characterEncoding=utf-8" --username root --password hht*LSL520 --table global_coutry_top --num-mappers 1 --export-dir "/user/hive/warehouse/global_coutry_top" --input-fields-terminated-by "\t" -- --default-character-set=utf-8 --update-mode allowinsert
sqoop export --connect "jdbc:mysql://47.115.148.142:3306/datafrom_hive?useUnicode=true&characterEncoding=utf-8" --username root --password hht*LSL520 --table global_city_top --num-mappers 1 --export-dir "/user/hive/warehouse/global_city_top" --input-fields-terminated-by "\t" -- --default-character-set=utf-8
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_new_out --num-mappers 1 --export-dir /user/hive/warehouse/china_new_out --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table global_new_out --num-mappers 1 --export-dir /user/hive/warehouse/global_new_out --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_sunconfirm_l3 --num-mappers 1 --export-dir /user/hive/warehouse/china_sunconfirm_l3 --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table global_sunconfirm_l3 --num-mappers 1 --export-dir /user/hive/warehouse/global_sunconfirm_l3 --input-fields-terminated-by "\t"
sqoop export --connect "jdbc:mysql://47.115.148.142:3306/datafrom_hive?useUnicode=true&characterEncoding=utf-8" --username root --password hht*LSL520 --table global_plate --num-mappers 1 --export-dir /user/hive/warehouse/global_plate --input-fields-terminated-by "\t"

sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_c1 --num-mappers 1 --export-dir /user/hive/warehouse/china_c1 --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_c2 --num-mappers 1 --export-dir /user/hive/warehouse/china_c2 --input-fields-terminated-by ","
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_l1 --num-mappers 1 --export-dir /user/hive/warehouse/china_l1 --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_l2 --num-mappers 1 --export-dir /user/hive/warehouse/china_l2 --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_l3 --num-mappers 1 --export-dir /user/hive/warehouse/china_l3 --input-fields-terminated-by "\t"
sqoop export --connect jdbc:mysql://47.115.148.142:3306/datafrom_hive --username root --password hht*LSL520 --table china_r2 --num-mappers 1 --export-dir /user/hive/warehouse/china_r2 --input-fields-terminated-by "\t"
