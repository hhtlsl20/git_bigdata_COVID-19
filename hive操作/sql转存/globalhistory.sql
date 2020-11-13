/*
 Navicat Premium Data Transfer

 Source Server         : 爬虫数据库
 Source Server Type    : MySQL
 Source Server Version : 50729
 Source Host           : 47.115.148.142:3306
 Source Schema         : yq

 Target Server Type    : MySQL
 Target Server Version : 50729
 File Encoding         : 65001

 Date: 26/07/2020 12:03:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for globalhistory
-- ----------------------------
DROP TABLE IF EXISTS `globalhistory`;
CREATE TABLE `globalhistory`  (
  `ds` datetime(0) NOT NULL COMMENT '日期',
  `confirm` int(11) NULL DEFAULT NULL COMMENT '累计确诊',
  `newAddConfirm` int(11) NULL DEFAULT NULL COMMENT '当日新增确诊',
  `heal` int(11) NULL DEFAULT NULL COMMENT '累计治愈',
  `dead` int(11) NULL DEFAULT NULL COMMENT '累计死亡',
  `confirm_add` int(11) NULL DEFAULT NULL COMMENT '当日新增确诊',
  `heal_add` int(11) NULL DEFAULT NULL COMMENT '当日新增治愈',
  `dead_add` int(11) NULL DEFAULT NULL COMMENT '当日新增死亡',
  PRIMARY KEY (`ds`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
