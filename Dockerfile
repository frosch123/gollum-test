FROM ruby
RUN apt-get -y update && apt-get -y install libicu-dev cmake && rm -rf /var/lib/apt/lists/*
RUN gem install github-linguist
RUN gem install gollum
RUN gem install wikicloth
ADD config.rb /
WORKDIR /wiki
ENTRYPOINT ["gollum", "--port", "80", "--css", "--js", "--allow-uploads", "dir", "--config", "/config.rb"]
EXPOSE 80
