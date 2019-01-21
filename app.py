from credentials import production
import credlib


srv, user, passwd = production.get(production)

print(srv, user, passwd)