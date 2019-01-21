# credlib

For retrieving stored credentials

So, basically you store your server, username and password in `credentials.py`:

```python
from credlib import credential
production = credential("p-sql-1", "sa-user", "pass")
```

In your application you then must import `credlib` and the set of credentials you need. Here we import `production`. You have have several sets of credentials stored.

```python
from credentials import production
import credlib

# Get server, username and password for `production`
srv, user, passwd = production.get(production)

print(srv, user, passwd)
```

Enjoy!