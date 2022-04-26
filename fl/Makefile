package:
	$(info "compressing csvs")
	tar -czvf ./csvs/tabula-reports.tar.gz ./csvs/*.csv

	$(info "compressing pdf reports")
	tar -cvf ./reports/reports.tar ./reports/*.pdf
	brotli -Z -f ./reports/reports.tar
	rm ./reports/reports.tar

unpackage:
	$(info "decompressing csvs")
	tar -xzvf ./csvs/tabula-reports.tar.gz

	$(info "decompressing pdfs")
	brotli -d ./reports/reports.tar.br
	tar -xvf ./reports/reports.tar -C reports/

clean:
	rm ./reports/*.pdf
	rm ./csvs/*.csv
