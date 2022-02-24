## Seams Scraper - Scraping Dynamic Sites Faster

# Technologies: Python, Scrapy and Selenium Framework

Create virtual environment 
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#
```sh
pip install -r requirements.txt
```
Open the command prompt/terminal

```sh 
scrapy crawl sams
``` 
> The above command will output result on the command prompt/terminal.

To save the output result into a file (json or csv) then write the below command

```sh 
scrapy crawl sams -O your_file_name.json
scrapy crawl sams -O your_file_name.csv
```

> Note: If you do a capital O, It will overwrite the file completely but if you do a lowercase o, it will actually append it to your file into one file.


## Documents and References

| Name | Sources |
| ------ | ------ |
| Scrapy tutorial | [https://docs.atlas.mongodb.com/getting-started/][PlDb] |
| Selenium document | [https://selenium-python.readthedocs.io/][PlGh] |


   [PlDb]: <https://docs.scrapy.org/en/latest/intro/tutorial.html>
   [PlGh]: <https://selenium-python.readthedocs.io/>
