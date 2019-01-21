from credentials import production, staging
import credlib


srv, user, passwd = production.get(production)

print(srv, user, passwd)