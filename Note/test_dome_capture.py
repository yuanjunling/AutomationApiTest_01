# coding=utf-8
import json
from Driver.base_request import request as Response
save={
  "activityName": "退货活动090",
  "activityBeginTime": "2022-02-10 00:00:00",
  "activityEndTime": "2022-02-11 00:00:00",
  "sort": "123123",
  "activityImg": "http://yjdf-oss-uat.oss-cn-shanghai.aliyuncs.com/uat/2022/2/10/1644467388967.jpg",
  "consignee": "123123",
  "consigneePhone": "123234234234234",
  "consigneeAddress": "234324234",
  "activityRules": "234234234234",
  "goodsRos": [
    {
      "goodsId": 13,
      "goodsImg": "http://oss-uat.yjdfytmall.com/qiniu//Public/Uploads/ueditor/php/upload/image/Common/20200929/1601349365204878.png",
      "goodsName": "福袋升级【团购】抽奖【1次】",
      "goodsNo": "DEV20200729001",
      "skuId": 13,
      "skuNo": "DEV20200729001",
      "num": 1,
      "freightPrice": 1,
      "mustSelect": "true",
      "goodsPrice": "11",
      "singleRefundMinNumber": "1",
      "singleRefundMultiple": "1",
      "singleRefundMaxNumber": "1",
      "goodsCode": "DEV20200729001"
    }
  ],
  "goodsVos": []
}
metadata={
  "Content-Type":"application/json",
  "Accept":"application/json, text/plain, */*",
  "X-Requested-With":"XMLHttpRequest",
  "token":"u7iu95rep0i0dbl9001fljiiv4",
  "clientType":"2",
  "version":"1.0"
}
url="http://api-test.yjdfmall.com/api-interim/mgmt/refundActivity/activity/save"
res = Response.run_main('POST', url=url, headers=metadata, json=save)
print(res)