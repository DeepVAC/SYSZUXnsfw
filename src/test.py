# -*- coding:utf-8 -*-
import sys
sys.path.append("path to deepvac")

import time
import json
import uuid

from syszux_log import LOG
from aliyunsdkcore import client
from syszux_loader import OsWalkerLoader
from syszux_report import ClassifierReport
from aliyunsdkgreen.request.v20180509 import ImageSyncScanRequest
from aliyunsdkgreenextension.request.extension import ClientUploader
from aliyunsdkgreenextension.request.extension import HttpContentHelper


class NSFWTestDataset(OsWalkerLoader):
    def __init__(self, nsfw_config):
        super(NSFWTestDataset, self).__init__(nsfw_config)

class AliyunTest:
    def __init__(self, config):
        self.conf = config
        self.Location = config.Location
        self.AccessKeyId = config.AccessKeyId
        self.AccessKeySecret = config.AccessKeySecret

        self.initClient()
        self.initReport()
        self.initDataset()
        self.initRequest()

    def initClient(self):
        self.clt = client.AcsClient(self.AccessKeyId, self.AccessKeySecret, self.Location)

    def initReport(self):
        self.report = ClassifierReport(ds_name=config.ds_name, cls_num=config.cls_num)

    def initDataset(self):
        self.dataset = NSFWTestDataset(self.conf)

    def initRequest(self):
        self.request = ImageSyncScanRequest.ImageSyncScanRequest()
        self.request.set_accept_format('JSON')

    def getTask(self, image_path):
        uploader = ClientUploader.getImageClientUploader(self.clt)
        url = uploader.uploadFile(image_path)
        self.task = {"dataId": str(uuid.uuid1()), "url": url}

    def process(self):
        label_list = config.label_list
        for image_path in self.dataset():
            self.getTask(image_path)
            self.request.set_content(HttpContentHelper.toValue({"tasks": [self.task], "scenes": [config.scenes]}))
            response = self.clt.do_action_with_exception(self.request)
            result = json.loads(response)
            if result['code'] != 200:
                LOG.logE(f"got request error! please checkout your AccessKeyId and Secret")
                continue
            if result['data'][0]['code'] != 200:
                LOG.logE(f"got error! [file: {image_path}, msg: {result['data'][0]['msg']}]")
                continue
            pred = result['data'][0]['results'][0]['label']
            label = image_path.split('/')[-2]
            if label not in label_list:
                LOG.logE(f"got error! test file structure not standard")
                continue
            LOG.logI(f"got Success! [file: {image_path}, label: {label}, pred: {pred}]")
            self.report.add(label_list.index(label), label_list.index(pred))

    def __call__(self):
        self.process()
        self.report()


if __name__ == '__main__':
    from config import config

    api = AliyunTest(config)
    api()
