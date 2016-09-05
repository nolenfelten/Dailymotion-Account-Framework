from selenium import webdriver


def firefox(tor, sock):
		
		# Create profile object
		profile = webdriver.FirefoxProfile()
		
		# Set Prefrences
		profile.set_preference("browser.cache.disk.capacity", 1000)
		profile.set_preference("browser.cache.disk.max_chunks_memory_usage", 1024)
		profile.set_preference("browser.cache.offline.capacity", 1200)
		profile.set_preference("browser.cache.memory.capacity", 4096)
		profile.set_preference("browser.cache.memory.enable", True)
		profile.set_preference("browser.cache.memory.max_entry_size", 924)
		profile.set_preference("browser.download.dir", "./cache")
		profile.set_preference("browser.download.folderList", 2)
		profile.set_preference("browser.download.manager.scanWhenDone", False)
		profile.set_preference("browser.download.manager.showAlertOnComplete", False)
		profile.set_preference("browser.download.manager.showWhenStarting", False)
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
		profile.set_preference("browser.newtabpage.rows", 0)
		profile.set_preference("browser.newtabpage.columns", 0)
		profile.set_preference("browser.link.open_newwindow", 3)
		profile.set_preference("browser.link.open_newwindow.restriction", 0)
		profile.set_preference("browser.preferences.instantApply", True)
		profile.set_preference("browser.preferences.animateFadeIn", False)
		profile.set_preference("browser.sessionhistory.max_entries", 4)
		profile.set_preference("browser.sessionhistory.max_total_viewers ", 0)
		profile.set_preference("browser.sessionstore.interval", 99999999)
		profile.set_preference("browser.sessionstore.enabled", False)
		profile.set_preference("browser.sessionstore.resume_from_crashuser", False)
		profile.set_preference("browser.showQuitWarning", False)
		profile.set_preference("browser.urlbar.maxRichResults", -1)
		profile.set_preference("config.trim_on_minimize", True)
		profile.set_preference("dom.disable_open_during_load", True)
		profile.set_preference("dom.max_script_run_time", 3000)
		profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
		profile.set_preference("javascript.options.gc_on_memory_pressure", False)
		profile.set_preference("layout.spellcheckDefault", 0)
		profile.set_preference("network.http.max-connections-per-server", 20)
		profile.set_preference("network.http.max-connections", 15)
		profile.set_preference("network.http.pipelining.maxrequests", 5)
		profile.set_preference("network.http.proxy.pipelining", True)
		profile.set_preference("network.http.pipelining", True)
		profile.set_preference("security.dialog_enable_delay", 0)
		
		if tor:
			profile.set_preference("network.proxy.type", 1)
			profile.set_preference("network.proxy.socks", "127.0.0.1")
			profile.set_preference("network.proxy.socks_port", int(socks))
		
		# Open Firefox with profile
		browser = webdriver.Firefox(profile)
		
		return browser