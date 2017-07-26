(function (superlist) {
    superlist.list = {
        init : function() {
            $("input[name=text]").keypress(function() {
                $(".has-error").hide();
            });
        }
    }

    superlist.list.init();
})((superlist == undefined ? {} : superlist));