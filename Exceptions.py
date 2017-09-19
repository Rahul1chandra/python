import webbrowser
try:
    print int(2/0)
except Exception as e:
    err = str(e)
    err = "https://stackoverflow.com/search?q=" + "+".join(err.split(" "))
    webbrowser.open_new_tab(err)
    print "Error Code:",e