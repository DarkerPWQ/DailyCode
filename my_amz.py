# -*- coding: utf-8 -*-
import httplib2
import re

class searchKeyword(object):
    def __init__(self,asin):
        self.asin = asin
        self.product_name = ""
        self.related_list = []
        self.also_viewed_list = []
        self.all_list = []
        self.result_dict={}
        self.all_word_list=[]
        self.keyword = []
    def TestResult(self,result):
        if 'height' in result or 'Amazon ' in result:
            return False
        print "22"
        return True
    def get_page(self,url):
        headers = {
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Charset": "UTF-8;q=0.5",
          "Accept-Encoding": "gzip,deflate,sdch",
          "Accept-Language": "zh-CN,zh;q=0.8",
          "Cache-Control": "max-age=0",
          "Connection": "keep-alive",
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.91   Safari/534.30",
        }
        h = httplib2.Http()
        resp, content = h.request(url,headers=headers)
        return content

    #Customers Who Viewed This Item Also Viewed
    def also_view(self):
        url = 'http://www.amazon.com/gp/product/'+self.asin
        # print url
        content = self.get_page(url)
        pattern1 = re.compile('<div class="p13n-sc-truncate p13n-sc-line-clamp-4" aria-hidden="true" data-rows="4">(.*?)</div>',re.S)
        result1 = re.findall(pattern1,content)
        #print len(result1)
        for i in result1:
            self.also_viewed_list.append(i.replace("\n","").strip(" ").replace("\n",""))

    #Sponsored Products Related To This Item
    def Related(self):
        url = 'http://www.amazon.com/gp/product/'+self.asin
        # print url
        content = self.get_page(url)
        pattern1 = re.compile('<div data-rows="4" aria-hidden.*?>(.*?)<')
        result1 = re.findall(pattern1,content)
        for i in result1:
            self.related_list.append(i.replace("\n","").strip(" ").replace("\n",""))
            # yield i.replace("\n","").strip(" ").replace("\n","")
    def TestResult(self,result):
        #if 'height' and 'width' and 'Amazon' in result:
        if 'height' in result or 'Amazon ' in result:
            return False
        return True

    def get_product_name(self):
        url = 'http://www.amazon.com/gp/product/'+self.asin
        # print url
        print url
        content = self.get_page(url)
        pattern = re.compile('<img alt="(.*?)" src="',re.S)
        result = re.findall(pattern,content)
        print "  222"
        #print result
        for i in result:
            if len(i)!=0:
                print "name :" i
                i=i.replace("&#39;","'").replace("&amp;quot;",'"').replace("&quot;",'"').replace("&amp;","&")
                result=self.TestResult(i)
                if result:
                    self.product_name=i
                    break
    def get_all_list(self):

        self.all_list.append(self.product_name)
        for item in self.related_list:
            self.all_list.append(item)
        for item in self.also_viewed_list:
            self.all_list.append(item)

    def merge_list(self):
        self.get_product_name()
        print "get_name ..."
        self.Related()
        print "get_relate ..."
        self.also_view()
        print "get_view ..."
        self.get_all_list()

    def deal_word(self,word):
        if "&" in word:
            return False
        elif len(word)<3:
            return False
        elif word=="and" or word=="for":
            return False
        return True

    def get_result_dict(self):
        self.merge_list()
        for item in self.all_list:
            #item是每个商品名
            word_list = item.split(" ")
            for i in word_list:
                if self.deal_word(i):
                    if self.result_dict.has_key(i):
                        self.result_dict[i]+=1
                    else:
                        self.result_dict[i] = 1
    def get_keyword(self):
        self.get_result_dict()
        keyword_list = sorted(self.result_dict.items(),key=operator.itemgetter(1), reverse=True)
        keyword_list1 = keyword_list[0:5]
        print keyword_list1
        for i in range(5):
            for j in range(i+1,5):
                keyword = keyword_list1[i][0]+" "+keyword_list[j][0]
                print keyword
                if keyword.lower() in self.product_name.lower():
                    self.keyword.append(keyword)











import operator
asin = raw_input("please input asin ")
a=searchKeyword(asin)
a.get_keyword()
print a.keyword


