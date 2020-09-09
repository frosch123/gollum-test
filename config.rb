mediawiki = Gollum::Markup.formats[:mediawiki]

puts mediawiki.inspect

Gollum::Markup.formats.clear
Gollum::Markup.formats[:mediawiki] = mediawiki
Precious::App.set(:default_markup, :mediawiki)
