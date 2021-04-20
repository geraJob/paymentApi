import pagarme,os,paypalrestsdk

pagarme.authentication_key(os.environ.get('api_key',"ak_test_K25D1A2mFSZ4sX6GatWv1ocF80hdCa"))
#paypal = paypalrestsdk.Api({
#    'mode':os.environ.get('paypal_mode','sandbox'),
#    'client_id':os.environ.get('paypal_client_id',"AaUAkwOv3dMunBPR7KleXCfEi1HoimA2tCpGuGiH_kuic-DzmgeDEios5P1fgWl5nAeEDIE83YF5SetV"),
#    'client_secret':os.environ.get('paypal_client_secret',"EMhI_C1VsLfek1GX4DEOtGzerKUh1Xnwol5OlyreSLCanPJgpMz5SNQ6KhmMIi4M25cPewdrrmSzs4WQ")
#})
gateway = pagarme