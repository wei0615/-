$(function () {
    var uploadBtn = $("#upload-btn");
    uploadBtn.change(function (event) {
        var file = this.files[0];
        var formData = new FormData();
        formData.append('upfile',file);

        xfzajax.post({
            'url':'/cms/upload_file/',
            'data':formData ,
            'processData':false,
            'contentType':false,
            'success':function (result) {
                if (result['code'] === 200){
                    var url = result['data']['url'];
                    console.log(url);
                    var thumbnailInput = $("input[name='thumbnail']");
                    thumbnailInput.val(url);
                }
            }
        });
    });
});

$(function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight':400,
        'serverUrl':'/ueditor/upload/'
    })
})