require 'sinatra'

class HelloWorldApp < Sinatra::Base
  get '/hi' do
    "Hello World"
  end
end
