mediawiki = Gollum::Markup.formats[:mediawiki]
Gollum::Markup.formats.clear
Gollum::Markup.formats[:mediawiki] = mediawiki
Precious::App.set(:default_markup, :mediawiki)

Precious::App.set(:wiki_options, {
    :index_page => "Main/en/Main%20Page",
    :css => true,
    :js => true,
    :allow_uploads => true,
    :per_page_uploads => false,
})
