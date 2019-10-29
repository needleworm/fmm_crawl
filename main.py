import fmm_crawler as fc
import sys

argv = sys.argv

crawler = fc.crawler()

crawler.find_all_pathway(argv[1], argv[2], argv[3])