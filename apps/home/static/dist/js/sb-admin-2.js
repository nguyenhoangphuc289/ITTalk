/*!
 * Start Bootstrap - SB Admin 2 v3.3.7+1 (http://startbootstrap.com/template-overviews/sb-admin-2)
 * Copyright 2013-2016 Start Bootstrap
 * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap/blob/gh-pages/LICENSE)
 */
$(function () {
    $('#side-menu').metisMenu();
});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function () {
    $(window).bind("load resize", function () {
        var topOffset = 50;
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    // var element = $('ul.nav a').filter(function() {
    //     return this.href == url;
    // }).addClass('active').parent().parent().addClass('in').parent();
    var element = $('ul.nav a').filter(function () {
        return this.href == url;
    }).addClass('active').parent();

    while (true) {
        if (element.is('li')) {
            element = element.parent().addClass('in').parent();
        } else {
            break;
        }
    }

    $(document).on('click', '.answer', function () {
        var editor = $(this).parent().parent().find('.question_widget');
        editor.slideToggle('fast');
    });

    $('.comment').click(function () {
        var cmt = $(this).parent().parent().find('.comment-panel');
        cmt.slideToggle('fast');
    });

    $('.dimiss_widget').click(function () {
        $(this).parent().slideUp('fast');
    });

    $('.popover_profile').popover({
        html: true,
        content: function () {
            return $(this).parent().parent().find('.popover_content').html();
        }
    }).on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    }).on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide");
            }
        }, 100);
    });

    $('.rep_box').on("focus", function () {
        var _this = $(this);
        _this.css('width', '100%');
        _this.parent().find('.btn_reply').show();
        _this.parent().find('.cmt_action_links').hide();
    }).on("focusout", function () {
        var _this = $(this);
        _this.css('width', '83px');
        _this.parent().find('.btn_reply').hide();
        _this.parent().find('.cmt_action_links').show();
    });

    $('#expand_question').click(function () {
        is_expand = $('#is_expand');
        if (is_expand.val() == "0") is_expand.val("1");
        else is_expand.val("0");
        var cmt = $('#question_detail').slideToggle('fast');
    });

    var films = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: 'https://twitter.github.io/typeahead.js/data/films/post_1960.json',
        remote: {
            url: 'https://twitter.github.io/typeahead.js/data/films/queries/%QUERY.json',
            wildcard: '%QUERY'
        }
    });

    $('#question_title').typeahead(null, {
        name: 'films',
        display: 'value',
        source: films,
        templates: {
            empty: [
                '<div class="empty-message">',
                '<i>Không có gợi ý nào.</i>',
                '</div>'
            ].join('\n'),
            footer: [
                '<a href="#">More Results</a>'
            ].join('\n'),
            suggestion: Handlebars.compile("<a href='/'><strong>{{value}}</strong> – {{year}}</a>")
        }
    });

    $(document).on('click', '.read_more_link', function () {
        $(this).hide();
        $(this).parent().find('.full_content').slideDown();
        $(this).parent().find('.truncated_img').hide();
        $(this).parent().find('.truncated_content').hide();
    });


});
