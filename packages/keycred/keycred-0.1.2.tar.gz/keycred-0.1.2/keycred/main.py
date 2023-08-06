import os
import getpass
import pycryptaes
from pykeepass import PyKeePass


'''
db.kbdx
pass1
'''


# base 64 encode and decode:
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# pykeepass:
# https://pypi.org/project/pykeepass/

class Credentials:
    """
    The credentials class takes care of handling Credentials in a safe way.
    - Generate credential entries
    - Get credential data
    """

    def __init__(self,
                 kdbx_path=os.path.join(os.environ['USERPROFILE'], "db.kdbx"),
                 user_path=os.path.join(os.environ['USERPROFILE'], ".user"),
                 pass_path=os.path.join(os.environ['USERPROFILE'], ".pass"),
                 key_path=os.path.join(os.environ['USERPROFILE'], ".key")):
        if not os.path.exists(kdbx_path):
            raise f"{kdbx_path} does not exist!"
        else:
            self.kdbx_path = kdbx_path
        self.user_path, self.pass_path, self.key_path = user_path, pass_path, key_path
        
    def prepare_kp(self):
        if not (os.path.exists(self.user_path) and os.path.exists(self.pass_path) and os.path.exists(self.key_path)):
            self.set_keepass_credentials(self.key_path, self.user_path, self.pass_path)
        self.co = self.get_keepass_credentials()
        self.kp = PyKeePass(self.kdbx_path, password=self.co.password)
        
    # LOGNAME, USER, LNAME, USERNAME
    def set_keepass_credentials(self):
        aes = pycryptaes.AES()
        aes.generate_key_user_pass(self.key_path, self.user_path, self.pass_path)
    
    def get_keepass_credentials(self):
        aes = pycryptaes.AES()
        co = aes.read_key_user_pass(self.key_path, self.user_path, self.pass_path)
        return co

    def keepass_credentials_set(self):
        return (os.path.exists(self.user_path) and os.path.exists(self.key_path) and os.path.exists(pass_path))
    
    def set_credentials(self, entry_name):
        """
        Persistently save credentials in KeePass.
        """
        if not hasattr(self, "kp"):
            self.prepare_kp()
        self.group = self.kp.add_group(self.kp.root_group, 'entries')
        self.kp.add_entry(
            self.group, 
            entry_name, 
            getpass.getpass(prompt="username: "),
            getpass.getpass(prompt="password: ")
        )
        self.kp.save()

    def get_credentials(self, entry_name):
        """
        Query for the credential by entry name. 
        The returned object can be used with: .password .username .
        """
        if not hasattr(self, "kp"):
            self.prepare_kp()
        return self.kp.find_entries(title=entry_name, first=True)

"""
cred = Credentials(
    kdbx_path = "c:\\Users\\kimgw1\\db.kdbx",
    user_path=os.path.join(os.environ['USERPROFILE'], "_test", ".key"),
    pass_path=os.path.join(os.environ['USERPROFILE'], "_test", ".user"),
    key_path=os.path.join(os.environ['USERPROFILE'], "_test", ".pass")
)
cred.set_keepass_credentials()
cred.set_credentials("test1")
"""
'''
reinintializing existing kbdx doesnt work yet - Credential error
ignored the keyfile and transformed_key parameters.

there should be also a delete_credentials() method

'''
