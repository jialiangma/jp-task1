import unittest
from client import getDataPoint

class ClientTest(unittest.TestCase):
  def setUp(self):
    self.quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-12 14:38:30.873638', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.132586269847', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-12 14:38:30.873638', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.132586269847', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-13 07:36:27.588392', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.260662333526', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-13 07:36:27.588392', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.260662333526', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-14 13:56:23.563506', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.299835534501', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-14 13:56:23.563506', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.299835534501', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-15 06:15:11.311063', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.688189178017', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-15 06:15:11.311063', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.688189178017', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-16 05:35:01.321364', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.219938223848', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-16 05:35:01.321364', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.219938223848', 'stock': 'DEF'},
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-17 06:05:05.956532', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.467590198311', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-17 06:05:05.956532', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.467590198311', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 45}, 'timestamp': '2019-02-18 07:57:31.633281', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.067970864042', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-18 07:57:31.633281', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.067970864042', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 45}, 'timestamp': '2019-02-18 22:05:24.412127', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.0439955226466', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-18 22:05:24.412127', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.0439955226466', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-19 12:10:41.235646', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.496050228039', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-19 12:10:41.235646', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.496050228039', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-20 17:24:33.024286', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.264644534568', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-20 17:24:33.024286', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.264644534568', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-22 01:13:43.608841', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.0153130613218', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-22 01:13:43.608841', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.0153130613218', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-22 14:20:27.155324', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.11302813595', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-22 14:20:27.155324', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.11302813595', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-23 12:39:54.220725', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.640324504953', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-23 12:39:54.220725', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.640324504953', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-24 13:34:42.288548', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.96479359407', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-24 13:34:42.288548', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.96479359407', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-25 20:35:50.085243', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.162630417863', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-25 20:35:50.085243', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.162630417863', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-27 04:00:25.242844', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.179487940012', 'stock': 'ABC'},
      {'top_ask': {'price': 120.51, 'size': 13}, 'timestamp': '2019-02-27 04:00:25.242844', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.179487940012', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-02-28 06:35:05.465894', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.808929011786', 'stock': 'ABC'},
      {'top_ask': {'price': 119.97, 'size': 18}, 'timestamp': '2019-02-28 06:35:05.465894', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.808929011786', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-03-01 11:01:34.684037', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.671861794702', 'stock': 'ABC'},
      {'top_ask': {'price': 119.97, 'size': 18}, 'timestamp': '2019-03-01 11:01:34.684037', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.671861794702', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-03-02 18:55:54.974088', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.975695467214', 'stock': 'ABC'},
      {'top_ask': {'price': 119.97, 'size': 18}, 'timestamp': '2019-03-02 18:55:54.974088', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.975695467214', 'stock': 'DEF'},
      {'top_ask': {'price': 119.88, 'size': 93}, 'timestamp': '2019-03-03 08:26:29.171596', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.705105303921', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-03 08:26:29.171596', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.705105303921', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 51}, 'timestamp': '2019-03-04 18:02:11.087286', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.0180302923505', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-04 18:02:11.087286', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.0180302923505', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 51}, 'timestamp': '2019-03-05 23:13:54.555782', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.946019187522', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-05 23:13:54.555782', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.946019187522', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 51}, 'timestamp': '2019-03-06 12:55:25.486914', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.154107911417', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-06 12:55:25.486914', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.154107911417', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 51}, 'timestamp': '2019-03-07 12:38:17.573652', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.398511237879', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-07 12:38:17.573652', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.398511237879', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-08 09:19:54.757146', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.834265716965', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-08 09:19:54.757146', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.834265716965', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-09 15:30:23.712825', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.53228386215', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-09 15:30:23.712825', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.53228386215', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-10 06:23:47.404786', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.516561009356', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-10 06:23:47.404786', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.516561009356', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-10 23:15:14.849770', 'top_bid': {'price': 118.02, 'size': 29}, 'id': '0.630165897903', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-10 23:15:14.849770', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.630165897903', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-11 11:21:39.558672', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.0535016364364', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-11 11:21:39.558672', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.0535016364364', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-12 01:47:27.764688', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.104613534559', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-12 01:47:27.764688', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.104613534559', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-12 23:44:54.606939', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.607833610692', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-12 23:44:54.606939', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.607833610692', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-13 18:40:55.522826', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.367510390747', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-13 18:40:55.522826', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.367510390747', 'stock': 'DEF'},
      {'top_ask': {'price': 119.48, 'size': 53}, 'timestamp': '2019-03-14 15:49:51.670276', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.455105671085', 'stock': 'ABC'},
      {'top_ask': {'price': 119.19, 'size': 255}, 'timestamp': '2019-03-14 15:49:51.670276', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.455105671085', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-15 04:50:33.631264', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.448338544624', 'stock': 'ABC'},
      {'top_ask': {'price': 117.98, 'size': 8}, 'timestamp': '2019-03-15 04:50:33.631264', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.448338544624', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-16 13:53:44.594335', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.495490275826', 'stock': 'ABC'},
      {'top_ask': {'price': 117.98, 'size': 8}, 'timestamp': '2019-03-16 13:53:44.594335', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.495490275826', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-18 01:24:56.401266', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.697599952214', 'stock': 'ABC'},
      {'top_ask': {'price': 117.98, 'size': 8}, 'timestamp': '2019-03-18 01:24:56.401266', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.697599952214', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-18 22:24:09.186375', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.711364831116', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 5}, 'timestamp': '2019-03-18 22:24:09.186375', 'top_bid': {'price': 117.74, 'size': 43}, 'id': '0.711364831116', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-20 06:39:49.142820', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.279419023742', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-20 06:39:49.142820', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.279419023742', 'stock': 'DEF'},
      {'top_ask': {'price': 119.13, 'size': 36}, 'timestamp': '2019-03-20 23:38:50.041048', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.89698783788', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-20 23:38:50.041048', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.89698783788', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-21 18:37:18.169892', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.503559315266', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-21 18:37:18.169892', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.503559315266', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-22 13:48:31.380625', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.611850707619', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-22 13:48:31.380625', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.611850707619', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-23 05:32:38.485146', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.894400583899', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-23 05:32:38.485146', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.894400583899', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-24 08:16:28.133846', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.510980811321', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-24 08:16:28.133846', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.510980811321', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-25 17:24:47.294852', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.3505102974', 'stock': 'ABC'},
      {'top_ask': {'price': 117.69, 'size': 150}, 'timestamp': '2019-03-25 17:24:47.294852', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.3505102974', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-26 14:22:00.636730', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.717234231689', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 43}, 'timestamp': '2019-03-26 14:22:00.636730', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.717234231689', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-27 02:38:40.025273', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.784649145808', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 43}, 'timestamp': '2019-03-27 02:38:40.025273', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.784649145808', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-27 17:13:31.214227', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.0498349396153', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 43}, 'timestamp': '2019-03-27 17:13:31.214227', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.0498349396153', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-28 18:44:59.368940', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.0679314279004', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 43}, 'timestamp': '2019-03-28 18:44:59.368940', 'top_bid': {'price': 117.62, 'size': 58}, 'id': '0.0679314279004', 'stock': 'DEF'},
      {'top_ask': {'price': 117.96, 'size': 38}, 'timestamp': '2019-03-30 05:46:42.740252', 'top_bid': {'price': 117.8, 'size': 12}, 'id': '0.837132970213', 'stock': 'ABC'},
      {'top_ask': {'price': 117.07, 'size': 1}, 'timestamp': '2019-03-30 05:46:42.740252', 'top_bid': {'price': 116.94, 'size': 100}, 'id': '0.837132970213', 'stock': 'DEF'}
    ]

  def testCalculateFirstRecordAverage(self):
    self.assertEqual(getDataPoint(self.quotes[0]), ('ABC', 120.48, 120.48, 119.2, 119.2), 'average price should be the same as current price on first record')

if __name__ == '__main__':
    unittest.main()
