from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_url(id_from, id_to):
    query = "http://fmm.mbc.nctu.edu.tw/action.php?type=id"
    query += "&From=" + id_from.strip()
    query += "&To=" + id_to.strip()
    return query


class crawler():
    def __init__(self):
        self.options = Options()
        self.options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        print("Chromdriver is ready. Running as headless mode.")

    def kill(self):
        self.driver.quit()

    def check_pathway(self, query):
        self.driver.get(query)
        try:
            attribute = self.driver.find_element_by_tag_name("strong")
        except:
            print("Error occured during identification of elements\nFrom : " + id_from + "\nTo : " + id_to)
            return False

        if "Finding No Pathway" in attribute.text:
            return False
        else:
            return True

    def find_all_pathway(self, out_file_name, file_from, file_to):
        outfile = open(out_file_name, 'w')

        froms = []
        f_file = open(file_from)
        for line in f_file:
            strp = line.strip()
            if len(strp) > 3:
                froms.append(strp)
        f_file.close()

        t_file = open(file_to)
        tos = []
        for line in t_file:
            strp = line.strip()
            if len(strp) > 3:
                tos.append(strp)
        t_file.close()

        for from_id in froms:
            for to_id in tos:
                query = make_url(from_id, to_id)
                if self.check_pathway(query):
                    print("Pathways from " + from_id + " to " + to_id + " found!")
                    outfile.write(query + "\n")
                else:
                    print("no pathway from " + from_id + " to " + to_id )

        outfile.close()

