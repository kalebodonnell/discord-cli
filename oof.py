if c == curses.KEY_BACKSPACE:
	currStr = currStr[:-1]
	cmd_window.clear()
	cmd_window.refresh()
	cmd_window.addstr(currStr)
	