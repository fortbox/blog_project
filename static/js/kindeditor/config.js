/*******************************************************************************
* Henry Xiao's blog
* Copyright (C) HenryXiao.com
*
* @author Henry Xiao<HenryXiao@henryxiao.com>
* @website http://www.HenryXiao.net/
* @version 1.0 (2018-02-12)
*******************************************************************************/
KindEditor.options.filterMode = false;
KindEditor.ready(function(K){
                K.create('textarea[name="content"]',{
                    width:800,
                    height:200,
                    uploadJson:'/admin/upload/kindeditor',
                });
        });