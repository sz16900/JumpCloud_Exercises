import sys, ctypes, re, subprocess as sp

# checks if "Guest" exists by using subprocess and parsing the returned
# string with REGEX
def user_exists():
	theStr = str(sp.check_output('net user', shell=True))
	if (re.search(r'(?:^|\W)guest(?:$|\W)',theStr)):
		return True
	else:
		return False

# Checks if user has admin rights; then checks if it can elevate status
# if it can't elevate status it returns None. Else it elevates status and
# proceeds.
# In order for the shell to execute, the arguments and executable need to be in
# unicode.
# From https://stackoverflow.com/questions/19672352/how-to-run-python-script-
# with-elevated-privilege-on-windows
def check_admin_privilages():
	success = 32
	shell32 = ctypes.windll.shell32
	if shell32.IsUserAnAdmin():
	    return True
	else:
		argv = sys.argv
		if hasattr(sys, '_MEIPASS'):
		    # Support pyinstaller wrapped program.
		    arguments = map(unicode, argv[1:])
		else:
		    arguments = map(unicode, argv)
		argument_line = u' '.join(arguments)
		executable = unicode(sys.executable)
		ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line,
			None, 1)
		if int(ret) <= success:
		    return False
	return None


if __name__ == '__main__':
    if user_exists():
        ret = check_admin_privilages()
        if ret is True:
	    enable = str()
		    # Make sure user types correct input
            while not (enable == "yes" or enable == "no"):
                enable = raw_input('"Guest" enable: yes/no\n\r')
            sp.call('net user Guest /active:%s' % (enable), shell=True)
        else:
            print 'Error(ret=%d): cannot elevate privilages.' % (ret, )
