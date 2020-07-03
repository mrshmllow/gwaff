import gwaffutils
import datetime

new_users = gwaffutils.gethistory()
time = datetime.datetime.today()
print(f"{'~'*5}History{'~'*5}\n{new_users}")
gwaff = gwaffutils.makegwaff(new_users, time)
print(f"{'~'*5}gwaff{'~'*5}\n{gwaff}")
