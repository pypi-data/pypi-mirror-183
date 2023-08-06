import playmanity

account = playmanity.account(nickname="X", password="x")
account.run()

prof = playmanity.get.profile(5)
print(account.token)