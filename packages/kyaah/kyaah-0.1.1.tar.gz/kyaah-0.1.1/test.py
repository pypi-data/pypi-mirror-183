import kyaah
from kyaah import fk, otp


subj = f"Hellow world! from kyaah"
body = "Lorem ipsum dolor sit amet consectetur adipisicing elit, rerum voluptate ipsum volupt."

mail_serve="gmail"
sender = "my_email@gmail.com"
passwd="**************" # mostly use app password
receiver = ["another_email@gmail.com", "my_email@gmail.com"]


"""
  NOTE: you can pass a keyword argument of `env=True` if you want to get your email app password from environment variable, as well as your email address too!. And instead of giving the value of `from_usr` your raw email address, give it the environment variable of your email, like wise the app password `mail_passwd` too!.
"""


"""local mail"""
# kyaah.localMail(from_usr=sender, to_usr=receiver, svr="local", subject=subj, body=body, mail_passwd=passwd)

"""plain mail"""
kyaah.sendMail(from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

"""mail with image"""
# images=['avater.jpg', 'image.jpg']
# kyaah.sendImages(images=images, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

"""mail with file"""
# files=['em.py', 'test.py', 'image.jpg']
# kyaah.sendFiles(files=files, from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

"""mail with page"""
# kyaah.sendPage(page='index.html', from_usr=sender, to_usr=receiver, svr=mail_serve, subject=subj, body=body, mail_passwd=passwd)

"""get a random email"""
# fk()

"""get an OTP code"""
# print(otp())
# print(otp(30)) # for specifying the range number
