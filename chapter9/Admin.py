
import time
# from User import User
import User
#import User #你需要确保 User 是一个类而不是模块。
#类名和模块名要区分,确定想要调用的是类还是模块
#最好将类名和模块名区分
class Privileges():
    def __init__(self ):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print("Privileges:", self.privileges)

class Admin(User.User):#💯或者继承是选择类进行继承,而不是模块
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()


# admin1 = Admin("John", "Doe", 30)
# admin1.greets_user()
# admin1.describe()
# admin1.privileges.show_privileges()

# user1 = User("Amarsimos", "Gen", 25)
# print('greeted people')
# user1.greets_user()
# print('described people')
# user1.describe()

# print('login attempts')
# print(user1.login_attempts, 'attempts')
# user1.increment_login_attempts()
# time.sleep(1)
# user1.increment_login_attempts()
# time.sleep(1)
# user1.increment_login_attempts()
# time.sleep(1)
# user1.increment_login_attempts()
# time.sleep(1)
# user1.increment_login_attempts()
# time.sleep(1)

# print('reset')
# # user1.reset_login_attempts()