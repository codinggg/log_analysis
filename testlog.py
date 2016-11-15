#!/usr/bin/python
# coding: utf-8

# "E:\log\py\\roms.log"

import os,sys

reload(sys)
sys.setdefaultencoding("utf-8")

source_filename = "F:\log\\12341234123412341234\\r20161115032951.log"

save_exist_name = "_exist.log"
save_not_exist_name = "_not_exist.log"

save_object_exist = open(source_filename[:-4] + save_exist_name, 'a')

save_object_not_exist = open(source_filename[:-4] + save_not_exist_name, 'a')

find_str = "157db3c015157df28dc0003"

file_object = open(source_filename, 'r')
for line in file_object:
    list_of_all_line = line

    # find have
    if (list_of_all_line.find(find_str) != -1):
        save_object_exist.write(line)

    # find not have
    elif (list_of_all_line.find(find_str) == -1):
        save_object_not_exist.write(line)
        print "---------------------"
    else:
        print list_of_all_line

file_object.close()
save_object_exist.close()
save_object_not_exist.close()

















