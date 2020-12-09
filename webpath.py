import timeit


 

start=timeit.timeit()

fp=open("wordlist.txt",'r')

data=fp.read().split()
 
 
data_=[]
user=input("Enter the url in this format  https://" )
for name in data:
      data=f"{user}/{data}"
      data_.append(data)

      
my_list=[]
import requests  
for urls in data_:
      url=requests.get(urls)
      if url.status_code==200:
            my_list.append(urls)
print(data_)
end=timeit.timeit()
print("total  = :",end-start)
 
