KindEditor.ready(function(K) {
    K.create('#id_content', {
        width: "600px",
        height: "800px",
        uploadJson: "/admin/upload/kindeditor",
        imageSizeLimit : '1MB', //批量上传图片单张最大容量
        imageUploadLimit : 100 //批量上传图片同时上传最多个数
    });
});