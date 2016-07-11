#! /usr/bin/python2.7
# -*- coding: UTF-8 -*-

##############################
# http://rashapay.com
# https://github.com/pouya-abbassi/rashapay-py
# By Pouya Abbassi
# This source code is built for easy-pay service.
# No database and no callback url. Best to use for donation (that you don't want to restore user data and how much they pay) and learning cases.
##############################

__author__ = "Pouya Abbassi"
__copyright__ = "Copyright 2016, http://RashaPay.com"
__credits__ = ["Nima Barzegar"]
__license__ = "GPL-v3 https://www.gnu.org/licenses/gpl-3.0.en.html"
__version__ = "0.1.0"
__maintainer__ = "Pouya Abbassi"
__status__ = "Production"


def rashapay():
	import urllib                   # Used for sending request to rashapay webservice
	import json			# Used for parsing json object
	import random			# Used for generating random orderID

	consumer_key = "1234:5678"			# Copy the Ckey of your website from (http://rashapay.com//userpanel.php?action=listofsites)
	amount = "1000"					# Integer, Min 1000 (rials)
	email = "info@mail.com"				# Buyer Email (Bank may send an email to confirm payment)
	name = "Buyer"					# Buyer name
	orderid = random.randint(1,99999999999)		# Just a random integer as orderID
	callback = "http://localhost/callback"		# User will redirected here after payment
	mobile = "09120000000"				# Buyer phone number
	description = "Description"			# Max 200 characters

	data = urllib.urlencode({"consumer_key":consumer_key,"amount":amount,"email":email,"name":name,"orderid":orderid,"callback":callback,"mobile":mobile,"description":description})	# Generating data for creating the request.
	u = urllib.urlopen("http://rashapay.com/srv/rest/rpaypaymentrequest", data)	# Sending data to the webservice url.

	obj = u.read() # Reading received data
	parsed_json = json.loads(obj)	# Parsing json object

	if parsed_json['status'] == '11' :
		print ('مشخصات ارسالی نادرست است.')							# Incorrect variables
	elif parsed_json['status'] == '12' :
		print ('اتصال به وب‌سرویس ناموفق است.')						# Failed to connect to the WebService
	elif parsed_json['status'] == '13' :
		print ('IP سایت درخواست دهنده با IP ثبت شده در سیستم مطابقت ندارد.')			# Your IP is not the same as what is stored in our DataBase
	elif parsed_json['status'] == '14' : 
		print ('شماره‌ی سفارش ارسالی (order_id) تکراری است. لطفا دوباره امتحان کنید.')	# OrderID is not unique and was used before
	elif parsed_json['status'] == '15' :
		print ('فرمت مبلغ نامعتبر است.')								# Price format is invalid
	elif parsed_json['status'] == '16' :
		print ('فرمت ایمیل صحیح نیست.')								# Email format is invalid
	elif parsed_json['status'] == '17' :
		print ('آدرس callback تعریف نشده است.')							# No CallBack url was declared
	elif parsed_json['status'] == 'response':
		print ("http://rashapay.com/srv/gatewaychannel/requestpayment/" + parsed_json['token'])	# Everything is fine, Getting the "token" part of json data and appending it to the payment url
	else :
		print (parsed_json['status'])								# Contact us at http://rashapay.com//about.php?#contactus


if __name__ == "__main__" :
	rashapay()
