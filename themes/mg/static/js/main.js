'use strict';

$(document).ready(function() {
    $('.mg-container-social').height($('article').height());
    $('#mg-panel-social').stick_in_parent({offset_top: 35});

    $('#tipue_search_input').tipuesearch({
        'show': 10,
        'mode': 'json',
        'showURL': false,
        'descriptiveWords': 75,
        'highlightEveryTerm': true,
        'contentLocation': '/tipue_search.json'
    });

    $(".mg-header").backstretch([
      "/theme/banner.jpg",
      "/theme/banner2.jpg",
      "/theme/banner3.jpg",
      "/theme/banner4.jpg",
      "/theme/banner5.jpg",
      "/theme/banner6.jpg",
      "/theme/banner7.jpg",
    ], {duration: 6000, fade: 750}
    );

});
