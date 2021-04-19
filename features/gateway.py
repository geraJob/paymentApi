import pagarme,os

pagarme.authentication_key(os.environ.get('api_key',"ak_test_K25D1A2mFSZ4sX6GatWv1ocF80hdCa"))
gateway = pagarme