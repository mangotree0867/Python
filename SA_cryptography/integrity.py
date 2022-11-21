from Crypto.Hash import MD5

m = MD5.new()

string_value = b'buy the stock at $2,500 a share'
spoofed_string_value = b'buy the stock at $3,500 a share'

m.update(string_value)
print( m.digest() )

m_hash_value = m.hexdigest()
print(m_hash_value)

###################################
#second one

n = MD5.new()
n.update(spoofed_string_value)
n_hash_value = n.hexdigest()
print(n_hash_value)
