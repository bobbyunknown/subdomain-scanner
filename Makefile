.PHONY: all clean package

PACKAGE_NAME = subdomain-scanner.tar.gz

FILES = scan_sub.py check_status.py

all: package

package:
	tar -czvf $(PACKAGE_NAME) $(FILES)

clean:
	rm -f $(PACKAGE_NAME)