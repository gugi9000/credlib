class credential:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def get(self, *args):

        if len(args) == 1 and isinstance(args[0], credential):
            hostname = args[0].hostname
            username = args[0].username
            password = args[0].password
        elif len(args) == 3:
            hostname = args[0]
            username = args[1]
            password = args[2]
        else:
            raise ValueError('Invalid arguments')

        return(hostname, username, password)

# credentials.py should look like this
# at least two lines

# credentials.py:
# from credlib import credential
# production = credential("p-sql-1", "sa-user", "pass")
# staging = credential("s-sql-1", "sa-user", "pass")
# testing = credential("t-sql-1", "sa-user", "pass")