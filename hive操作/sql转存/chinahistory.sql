
DROP TABLE IF EXISTS `chinahistory`;
CREATE TABLE `chinahistory`  (
  `ds` datetime(0) NOT NULL COMMENT '日期',
  `confirm` int(11) NULL DEFAULT NULL COMMENT '累计确诊',
  `confirm_add` int(11) NULL DEFAULT NULL COMMENT '当日新增确诊',
  `suspect` int(11) NULL DEFAULT NULL COMMENT '剩余疑似',
  `suspect_add` int(11) NULL DEFAULT NULL COMMENT '当日新增疑似',
  `heal` int(11) NULL DEFAULT NULL COMMENT '累计治愈',
  `heal_add` int(11) NULL DEFAULT NULL COMMENT '当日新增治愈',
  `dead` int(11) NULL DEFAULT NULL COMMENT '累计死亡',
  `dead_add` int(11) NULL DEFAULT NULL COMMENT '当日新增死亡',
  PRIMARY KEY (`ds`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
