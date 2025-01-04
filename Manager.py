import pickle


class Manager:
    def __init__(self, username,  password='', admin=False):
        self.admin = admin
        self.username = username
        self.password = password
        if admin:
            self.all_usernames = set()
            self.all_usernames.add(self.username)
    
    @staticmethod
    def match(password,c_password):
        if password == c_password:
            return True
        print("Password does not match.\nPlease try again...")
        return False

    def change_password(self,password):
        if self.match(self.password, password):
            new_password = input("Enter the new Password:")
            c_password = input("Enter the confirm Password:")
            if self.match(new_password,c_password):
                self.password = c_password
                return True
        return False
    
    def __repr__(self):
        return f"Manager(username='{self.username}', password= '{self.password}')"
    
    def new_user(self, username, password, c_password, admin=False):
        if not self.admin:
            print("Adding new user requires a admin priviledge.")
            return False
        if username in self.all_usernames:
            print("Username already taken.\nPlease take another.")
            return False
        if self.match(password, c_password):
            c = Manager(username, password, admin)
            self.all_usernames.add(c.username)
        return True
    