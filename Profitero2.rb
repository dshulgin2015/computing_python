#!/usr/bin/env ruby
require 'nokogiri'
require 'open-uri'
require 'csv'
require 'curb'
require 'mechanize'

host = 'http://www.sammccauley.com/'

search_link = ARGV[0]
file = ARGV[1]

products = Nokogiri::HTML(Curl.get(search_link).body_str)

titles = []
prices = []
images = []
codes = []


CSV.open(file, "w") do |csv|
	csv << ["Title", "Price", "img_url", "Code"] #header
end

products.xpath('//ul[@class="inlinelist productList noDeco bold"]/li/a/@href').each do |product|


	doc = Nokogiri::HTML(Curl.get(product.text).body_str)

	head_title =  doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__detailCnt"]/h2').text



	types = doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__productFamilySelectorsView_ddlSelector1"]/option/@value')

	#puts types.length

	if types.length-1 > 0
		for i in 1..types.length-1

	    # choosing options
	    url = product.text
	    agent = Mechanize.new
		page = agent.get(url)
		form = agent.page.forms.first
		form.field_with(:id => 'ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__productFamilySelectorsView_ddlSelector1').options[i].click
		home_page = form.submit
		doc = Nokogiri::HTML(home_page.body)
	    #titles << head_title + ' ' + node.text
		image_url = doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__productFamilyImagesView__mainImage"]/@src')

		images << image_url.text 
		titles << head_title + ' ' + types[i]
		prices << doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__hasPriceItemView__priceValueLabel"]').text.strip
		codes  << doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__itemCode"]')


		end
	else
		titles << head_title
		image_url = doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__productFamilyImagesView__mainImage"]/@src')
		images << image_url.text 
		prices << doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__hasPriceItemView__priceValueLabel"]').text.strip
		codes  << doc.xpath('//*[@id="ctl00_ctl00__nestedContent__mainpageContent_ProductFamilyDetailsView1__itemCode"]').text.strip
	end

end


CSV.open(file, "ab") do |csv|
	for i in 0..titles.length-1
	   csv << [titles[i], prices[i], images[i], codes[i]]
	end

end

puts "File " + file + " has been successfully saved"