#!/usr/bin/env ruby
require 'rubygems'
require 'nokogiri'
require 'open-uri'
require 'csv'

host = 'https://www.viovet.co.uk'

search_link = ARGV[0]
file = ARGV[1]

products = Nokogiri::HTML(open(search_link))

CSV.open(file, "w") do |csv|
	csv << ["Title", "Price", "img_url", "ET", "Code"] #header
end

products.xpath('//ul[@class="families-list"]/li/a/@href').each do |product|

	titles = []
	prices = []
	image = ''
	et_s = []
	codes = []
 
	doc = Nokogiri::HTML(open(host + product))
	doc.xpath('//*[@id="product_family_heading"]').each do |node|

		doc.xpath('//span[@class="name"]').each do |name|
	      titles << node.text + '-' + name.text.strip
		end
	     
	end

	doc.xpath('//img[@id="category_image"]/@src').each do |node|
	      image = 'http:' + node
	end

	doc.xpath('//span[@class="price"]').each do |node|
	      prices << node.text.strip
	end

	doc.xpath('//span[@class="item-code"]').each do |node|
	      codes << node.text.strip
	end

	doc.xpath('//p[@class="notification_in-stock"]').each do |node|
	      et_s << node.text.strip
	end

	#nokogiri_object = Nokogiri::HTML(http.body_str)

	CSV.open(file, "ab") do |csv|

		for i in 0..titles.length-1
		   csv << [titles[i], prices[i], image, et_s[i], codes[0]]
		end

	end
end

puts "File " + file + " has been successfully saved"

