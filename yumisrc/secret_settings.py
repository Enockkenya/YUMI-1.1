import sys
import cloudinary
#---------------------------------------------------------------------------#
# Generic                                                                   #
#---------------------------------------------------------------------------#
SECRET_DEBUG = True
SECRET_KEY = '#i4$w=1u@0e2axijn04f@++z_&3zx1k+!lj2_lj2^(sgt8@$w='
# PASSWORD= 'Aggreyomondi90'
# USER= 'sean'


#---------------------------------------------------------------------------#
# Database                                                                  #
#---------------------------------------------------------------------------#



#---------------------------------------------------------------------------#
# Email                                                                     #
#---------------------------------------------------------------------------#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''


 
PAYPAL_RECEIVER_EMAIL = ''
PAYPAL_TEST = False  
PAYPAL_CLIENT_ID = ''
PAYPAL_CLIENT_SECRET = ''

UPLOADCARE = {
  # Don’t forget to set real keys when it gets real :)

  'pub_key': 'eb9da6d2caf0fa018118',
  'secret': '35fc8184bcfe7a3b5009',
}
cloudinary.config(
  cloud_name ='lada' ,
  api_key = '991846289858872',
  api_secret = 'PxriDvQELG9426d-3KZ1_OtbsVE',
  secure = True
)



