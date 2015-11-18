import scrapy
import csv

def parse_csv(file):
  daycare_center_urls = []
  with open(file) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        if row['County'].lower() not in ['new york', 'brooklyn', 'queens', 'bronx', 'staten island']:
          pass
        else:
          daycare_center_urls.append(row['Program Profile'])
  return daycare_center_urls


class KiddySpider(scrapy.Spider):
  name = 'kiddyspider'
  start_urls = parse_csv('../data/data.csv')

  def parse(self, response):
    main_div = len(response.css('#compliancehistoryDivImg > table:nth-of-type(2) tr'))
    print "NUM TR's is " + str(main_div)
