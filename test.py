import pyshopee2

shopid = "11392"
partnerid = "1001325"
partkey = "c4cbb3aca8cacfd35c7b1ba47c6bd6f2ae6d85d276d7bfa4583fc292f30a378b"
redirectUrl = "https://www.bajuhemat.com"
host = "https://partner.test-stable.shopeemobile.com/api/v2/shop/auth_partner"
client = pyshopee2.Client(shopid, partnerid, partkey, redirectUrl, True)
#print(client.shop_authorization("http://bajuhemat.com"))
#client.get_code()
#print(client.get_token())
reftok = "f91b6f27376eb54a97bcf18120ed99a3"
acctok = "0856cf6954d605cc60f284b94ea75895"
#print(client.get_access_token(shopid, partnerid, partkey, reftok))
#print(client.auth_url("/test")[0])

#client.set_access_token(acctok)

param= {
    "page_size" : 1,
    "page_no" : 1
}
print(client.public.get_shop_by_partner())