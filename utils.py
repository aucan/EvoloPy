#df = pd.read_csv('/content/drive/MyDrive/00dosyalar/pyhton/dostumhissedegiskenler.csv')
# data = pd.read_csv('/content/drive/MyDrive/00dosyalar/pyhton/dostumhissedegiskenler.csv', sep=";")   #on_bad_lines='skip'
# data.head()
# data_y=data.loc[:,"hkapanis"]
# data_y.head()
# data_x = data.drop(columns=data.columns[-1], axis=1)
# data_x = data.drop(columns=data.columns[0], axis=1)

# data_x.head()

# x = data[data['hisseadi'] == 'ARCLK']
# x.info()
import pandas as pd

def loaddata(hisseadi,dim):
    data = pd.read_csv('Y:\piton22\Evolopy\datas\dostumhissedegiskenler.csv', sep=";")
    data = data[data['hisseadi'] == hisseadi]
    data_y=data.loc[:,"hkapanis"]
    data_x = data.drop(columns=data.columns[-1], axis=1)
    data_x = data_x.drop(columns=data.columns[0], axis=1)
    
    data_x = data_x.to_numpy()
    data_y = data_y.to_numpy()
    degiskensayisi=3
    #1. ve 2. sütun kaç değişken kullanılacaksa o kadar değişken gönderiliyor
    data_x = data_x[:,0:dim]
    return data_x,data_y




