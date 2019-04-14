HOME   = $(shell cd; pwd)
PARENT = $(shell cd ../; pwd)
SRC    = /usr/local/src

.PHONY: all
all:
	cd $(CURDIR)
	$(shell echo '#!/bin/bash' > $(CURDIR)/pysync)
	$(shell echo 'export PATH=$$PATH:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin' >> $(CURDIR)/pysync)
	$(shell echo 'CURRENT=`pwd`' >> $(CURDIR)/pysync)
	$(shell echo 'python $(SRC)/PySync/PySync.py $$CURRENT $$1' >> $(CURDIR)/pysync)
	cp $(CURDIR)/pysync /usr/local/sbin/
	cp $(CURDIR)/pysync-default.json $(PARENT)/pysync.json
	mv $(PARENT)/PySync $(SRC)/
