# lagou-spider
拉勾网数据爬虫

# 说明:
这个代码是拉勾网爬虫, 爬取拉勾网的会计岗位数据, 并且对数据做了大数据分析分析

# 依赖
pip3 install requests
pip3 install pymysql
pip3 install pyquery

# 执行方式
python3 lagou.py
	


# 建表的指令
```
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `companyId` bigint(4) DEFAULT NULL,
  `positionName` varchar(64) DEFAULT NULL,
  `workYear` varchar(16) DEFAULT NULL,
  `education` varchar(16) DEFAULT NULL,
  `jobNature` varchar(16) DEFAULT NULL,
  `positionId` bigint(4) DEFAULT NULL,
  `companyShortName` varchar(16) DEFAULT NULL,
  `createTime` varchar(38) DEFAULT NULL,
  `score` bigint(4) DEFAULT NULL,
  `city` varchar(16) DEFAULT NULL,
  `salary` varchar(16) DEFAULT NULL,
  `approve` bigint(4) DEFAULT NULL,
  `positionAdvantage` varchar(128) DEFAULT NULL,
  `financeStage` varchar(16) DEFAULT NULL,
  `industryField` varchar(16) DEFAULT NULL,
  `companySize` varchar(18) DEFAULT NULL,
  `companyLabelList` varchar(128) DEFAULT NULL,
  `publisherId` bigint(4) DEFAULT NULL,
  `district` varchar(16) DEFAULT NULL,
  `companyLogo` varchar(106) DEFAULT NULL,
  `positionLables` varchar(128) DEFAULT NULL,
  `industryLables` varchar(128) DEFAULT NULL,
  `businessZones` varchar(128) DEFAULT NULL,
  `hitags` varchar(128) DEFAULT NULL,
  `resumeProcessRate` bigint(4) DEFAULT NULL,
  `resumeProcessDay` bigint(4) DEFAULT NULL,
  `companyFullName` varchar(28) DEFAULT NULL,
  `imState` varchar(16) DEFAULT NULL,
  `lastLogin` bigint(4) DEFAULT NULL,
  `explain` varchar(128) DEFAULT NULL,
  `adWord` bigint(4) DEFAULT NULL,
  `plus` varchar(128) DEFAULT NULL,
  `pcShow` bigint(4) DEFAULT NULL,
  `appShow` bigint(4) DEFAULT NULL,
  `deliver` bigint(4) DEFAULT NULL,
  `gradeDescription` varchar(128) DEFAULT NULL,
  `promotionScoreExplain` varchar(128) DEFAULT NULL,
  `firstType` varchar(16) DEFAULT NULL,
  `secondType` varchar(16) DEFAULT NULL,
  `isSchoolJob` bigint(4) DEFAULT NULL,
  `subwayline` varchar(16) DEFAULT NULL,
  `stationname` varchar(16) DEFAULT NULL,
  `linestaion` varchar(256) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `latitude` varchar(18) DEFAULT NULL,
  `formatCreateTime` varchar(16) DEFAULT NULL,
  `advantage` text,
  `describe` text,
  `address` text,
  `lagou_src` varchar(128) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;
```