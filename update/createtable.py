import socket, time, os
from db.database import Database
from db.models import TDEVICEDATA5MINSERVER, TDEVICEDATA1MINSERVER
import sqlalchemy




db_session = Database.getSession()


while(True):

    SQL_param_num_1 = '''CREATE TABLE `TIME_SYNC_DATA` (
  `S_GW_ID` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `S_JOB_TYPE` char(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `D_GW_TIME` datetime DEFAULT NULL,
  `D_SEND_TIME` datetime DEFAULT NULL,
  `D_RCV_TIME` datetime DEFAULT NULL,
  `D_SERVER_TIME` datetime DEFAULT NULL,
  `D_SET_TIME` datetime DEFAULT NULL
); '''


    SQL_param_num_2 = '''CREATE TABLE `adc_archive` (
  `seq_num` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` varchar(10) NOT NULL,
  `adc_board_id` varchar(10) NOT NULL,
  `ch1_pt100` varchar(20) DEFAULT NULL,
  `ch2_pt100` varchar(20) DEFAULT NULL,
  `ch1_4_20ma` varchar(20) DEFAULT NULL,
  `ch2_4_20ma` varchar(20) DEFAULT NULL,
  `ch3_4_20ma` varchar(20) DEFAULT NULL,
  `ch4_4_20ma` varchar(20) DEFAULT NULL,
  `ch5_4_20ma` varchar(20) DEFAULT NULL,
  `voltage` varchar(20) DEFAULT NULL,
  `high_low` int(11) DEFAULT '1',
  `value_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`seq_num`,`group_id`,`adc_board_id`) USING BTREE
); '''

    SQL_param_num_3 = '''CREATE TABLE `ct_archive` (
  `seq_num` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` varchar(10) NOT NULL,
  `ct_board_id` varchar(10) NOT NULL,
  `ch1_current` varchar(20) DEFAULT NULL,
  `ch2_current` varchar(20) DEFAULT NULL,
  `ch3_current` varchar(20) DEFAULT NULL,
  `ch4_current` varchar(20) DEFAULT NULL,
  `ch5_current` varchar(20) DEFAULT NULL,
  `ch6_current` varchar(20) DEFAULT NULL,
  `ch7_current` varchar(20) DEFAULT NULL,
  `ch8_current` varchar(20) DEFAULT NULL,
  `ch9_current` varchar(20) DEFAULT NULL,
  `ch10_current` varchar(20) DEFAULT NULL,
  `value_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`seq_num`,`group_id`,`ct_board_id`) USING BTREE
);'''
    SQL_param_num_4 = '''Insert Into adc_archive (select * from adc_sensor_data) '''
    SQL_param_num_5 = '''insert into ct_archive (select * from ct_sensor_data) '''
    
    db_session.execute(SQL_param_num_1)
    db_session.execute(SQL_param_num_2)
    db_session.execute(SQL_param_num_3)
    db_session.execute(SQL_param_num_4)
    db_session.execute(SQL_param_num_5)
        db_session.commit()
        break        


