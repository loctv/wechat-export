#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: dump-msg.py
# Date: Mon May 25 15:23:05 2015 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

# ./dump-msg2.py decrypted.db output resource avatar.index "💯ASM Check In"
# ./dump-msg2.py decrypted.db output resource avatar.index "💯Office Check In"
# ./dump-msg2.py decrypted.db output resource avatar.index "💯PC Check In"
# ./dump-msg2.py decrypted.db output resource avatar.index "💯Sales Check In"


from __future__ import division
from wechat.parser import WeChatDBParser
from wechat.res import Resource
from common.textutil import safe_filename
from common.textutil import ensure_unicode
import sys, os, datetime

import codecs
sys.stdout=codecs.getwriter('utf-8')(sys.stdout)

if len(sys.argv) != 6:
    sys.exit("Usage: {0} <path to decrypted_database.db> <output_dir> <res> <avt> <Group>".format(sys.argv[0]))

db_file = sys.argv[1]
output_dir = sys.argv[2]
res_dir = sys.argv[3]
avt = sys.argv[4]
group = sys.argv[5]
try:
    os.mkdir(output_dir)
except:
    pass
if not os.path.isdir(output_dir):
    sys.exit("Error creating directory {}".format(output_dir))

parser = WeChatDBParser(db_file)
res = Resource(res_dir, avt)

ten_nhom = ensure_unicode(group)
msgs = parser.msgs_by_chat[ten_nhom]

import xlsxwriter
from io import BytesIO
from PIL import Image


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('%s.xlsx' % group)
worksheet = workbook.add_worksheet()
worksheet.protect()
worksheet.write(0, 0, "Day")
worksheet.write(0, 1, "Time")
worksheet.write(0, 2, "From")
worksheet.write(0, 3, "Message")
worksheet.set_column(0, 0, 20)
worksheet.set_column(1, 1, 10)
worksheet.set_column(2, 2, 10)
worksheet.set_column(3, 3, 40)

for row, m in enumerate([m for m in msgs if (m.type == 1 or m.type == 3) and m.createTime >= datetime.datetime(2016, 6, 13)]):
    if m.type == 1:
        print m.type, m.talker, m.createTime, m.content
        worksheet.write(row+1, 0, m.createTime.strftime("%d-%m-%Y"))
        worksheet.write(row+1, 1, m.createTime.strftime("%H:%M:%S"))
        worksheet.write(row+1, 2, m.talker)
        worksheet.write(row+1, 3, m.talker + ': '+ m.content)
    if m.type == 3:
        imgpath = m.imgPath.split('_')[-1]
        bigimgpath = parser.imginfo.get(m.msgSvrId)
        fnames = [k for k in [imgpath, bigimgpath] if k]
        imgBase64 = res.get_img(fnames)
        worksheet.write(row+1, 0, m.createTime.strftime("%d-%m-%Y"))
        worksheet.write(row+1, 1, m.createTime.strftime("%H:%M:%S"))
        worksheet.write(row+1, 2, m.talker)
	worksheet.write(row+1, 3, m.talker + ': ')
        worksheet.set_row(row+1, 200)
        image_data = BytesIO(imgBase64.decode('base64'))
        w, h = Image.open(image_data).size

        worksheet.insert_image('E%s' % str(row+2), '', {'image_data': image_data, 'positioning':1, 'x_scale': 200/w, 'y_scale': 200/h})
        # print m.type, m.talker, m.createTime, img

workbook.close()
