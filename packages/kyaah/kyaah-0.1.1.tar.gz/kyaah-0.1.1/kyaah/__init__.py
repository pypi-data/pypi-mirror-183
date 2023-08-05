
"""
    #    #   #   #    ##      ##    #    #
    #   #     # #    #  #    #  #   #    #
    ####       #    #    #  #    #  ######
    #  #       #    ######  ######  #    #
    #   #      #    #    #  #    #  #    #
    #    #     #    #    #  #    #  #    #

    Kyaah abstract away SMTP mail operations

    Simplify your email message with `kyaah`

    Usage at a glance:
    
        >>> import kyaah
        
        >>> sender = "my_email@gmail.com"
        >>> receiver = ["receiver_1@gmail.com", "receiver_2@gmail.com"]
        >>> passwd = "*********"

        >>> server = "gmail"
        >>> subj = f"Hellow world!"
        >>> body = "Lorem ipsum dolor sit amet adipisicing elit, rerum voluptate ipsum volupt."

        >>> kyaah.sendMail(
                from_usr=sender, to_usr=receiver, svr=server, subject=subj, body=body, mail_passwd=passwd)
"""


__title__ = "kyaah"
__author__ = "Usman Musa"
__author_email__ = "usmanmusa1920@gmail.com"
__author_website__ = "https://usmanmusa1920.github.io"
__copyright__ = "Copyright 2022 Usman Musa"


status = {
  # Information.
  200: ('success',),
  # Client Error.
  400: ('bad_request',),
  401: ('unauthorized',),
  404: ('not_found',),
  # Server Error.
  500: ('internal_server_error',),
  503: ('service_unavailable',),
}


def selector(env=None):
  """decide a class for `environment variable` for security purpose or not"""
  if env:
    cls = Vault
  else:
    cls = BaseMail
  return cls


from . base import BaseMail
from . vault import Vault

from . utils import Tokens
from . utils import Faker
from . server import Serve

from . api import (
  localMail, sendMail, sendImages, sendFiles, sendPage, fk, otp
  )
