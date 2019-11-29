import os
import pandas as pd


#    import tarfile
#    tf = tarfile.open("czech_corpus.tgz")
#    tf.extractall()
#    print("done")



#dir_name = "C:\Users\dawid.wojtas\Desktop\p\cz\czech_text_document_corpus_v20"
#test = os.listdir(dir_name)
dirpath = os.getcwd()

dir_name = dirpath+"\czech_text_document_corpus_v20"
test = os.listdir(dir_name)

#for item in test:
#    if item.endswith(".pos"):
#        os.remove(os.path.join(dir_name, item))

#print("done.")
df=[]

for item in test[:426]:
    if item.endswith(".tok"):
        #print(item)
        data = pd.read_csv(f'{dir_name}\{item}', sep=" ",header=None)
        df.append(data)
conDF = pd.concat(df, axis=1)
conDF = conDF.transpose()
conDF.columns = ["word"]

#print(conDF.head())

dups = conDF.pivot_table(index=["word"], aggfunc='size')
dupss = dups.sort_values(ascending=False)
print(dupss.head(100))