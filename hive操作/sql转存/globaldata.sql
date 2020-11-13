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

 Date: 26/07/2020 12:03:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for globaldata
-- ----------------------------
DROP TABLE IF EXISTS `globaldata`;
CREATE TABLE `globaldata`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime(0) NULL DEFAULT NULL COMMENT '数据最后更新时间',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '国家',
  `continent` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '州名',
  `confirmAdd` int(11) NULL DEFAULT NULL COMMENT '新增治愈',
  `confirm` int(11) NULL DEFAULT NULL COMMENT '累计确诊',
  `suspect` int(11) NULL DEFAULT NULL COMMENT '治愈',
  `heal` int(11) NULL DEFAULT NULL COMMENT '累计治愈',
  `dead` int(11) NULL DEFAULT NULL COMMENT '累计死亡',
  `nowConfirm` int(11) NULL DEFAULT NULL COMMENT '现存确诊',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 183 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
