$("#emotionIcon_Button").click(function() {
    var text = $("#emotionIcon_Area").val();
    $.ajax({
        url: '/sentiment/',
        data: {
            'text': text
        },
        dataType: 'json',
        success: function (data) {
            $("#emotionLabel").append(data.emoji);
        }
    });
});

