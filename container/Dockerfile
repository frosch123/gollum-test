FROM ruby
RUN apt-get -y update && apt-get -y install libicu-dev cmake && rm -rf /var/lib/apt/lists/*
RUN gem install github-linguist
RUN gem install gollum
RUN gem install wikicloth
ADD wikicloth.diff /
ADD gollum-lib.diff /
ADD config.rb /
RUN cd /usr/local/bundle/gems/wikicloth-*; patch -p 1 -i /wikicloth.diff
RUN cd /usr/local/bundle/gems/gollum-lib-*; patch -p 1 -i /gollum-lib.diff
WORKDIR /wiki
ENTRYPOINT ["gollum", "--port", "80", "--config", "/config.rb"]
EXPOSE 80
