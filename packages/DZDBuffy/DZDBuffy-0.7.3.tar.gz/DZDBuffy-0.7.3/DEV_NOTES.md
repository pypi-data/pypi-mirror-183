
Versionized Caching Proxy for decoupling external responses
buffy

* Caching Proxy for external files and api calls
* versioning of files
* tagging of files (valid,failed)
	* Autofallback to valid files if current online file is tagged as "failed"
* stubborn downloader
	* But when threshold (timeout, n-times erros) is reached and old version is available server old version
* "Always use local cached version" option for certain files
* Server / Client Architecture


ToDo:

* Test and Transfer examples from blogpost to examples in docs
* Better server watchdog in buffy/buffyserver/main.py
* Add mkdoc build test to test job
* Docstrings for storage interface
* Auth
  1. Fully integrated in api
* API limitator to prevent DDOS

Server Ideas:

* Auth on buffyserver
* unpack compresses file in background so client has an even easier life
* Review response data writing at buffyserver.backend.register_response_data_writing in future when your are a better coder or have the time to read into the issue
* make content serving endpoint byte serving capaple. Clients will be able rejoin broken downloads https://github.com/rvflorian/byte-serving-php
* Proxy interface  https://stackoverflow.com/questions/8287628/proxies-with-python-requests-module

Client Ideas:
* cache local fallback downloads in tmp dir